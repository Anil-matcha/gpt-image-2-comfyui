"""
MuAPI GPT-Image-2 ComfyUI Nodes
================================
ComfyUI nodes for GPT-Image-2 image generation via muapi.ai.

  GPTImage2TextToImage     — POST /api/v1/gpt-image-2-text-to-image
  GPTImage2ImageToImage    — POST /api/v1/gpt-image-2-image-to-image

Auth:     x-api-key header
Polling:  GET /api/v1/predictions/{request_id}/result
Upload:   POST /api/v1/upload_file
"""

import io
import os
import time

import numpy as np
import requests
import torch
from PIL import Image

BASE_URL = "https://api.muapi.ai/api/v1"
POLL_INTERVAL = 5
MAX_WAIT = 600


# ── Helpers ────────────────────────────────────────────────────────────────────

def _load_api_key(api_key_input):
    if api_key_input and api_key_input.strip():
        return api_key_input.strip()
    config_path = os.path.expanduser("~/.muapi/config.json")
    if os.path.isfile(config_path):
        try:
            import json as _json
            with open(config_path) as f:
                key = _json.load(f).get("api_key", "")
            if key:
                return key
        except Exception:
            pass
    raise RuntimeError(
        "No API key found. Either paste your key into the api_key field, "
        "or run `muapi auth configure --api-key YOUR_KEY` in a terminal."
    )


def _upload_image(api_key, image_tensor):
    if image_tensor.dim() == 4:
        image_tensor = image_tensor[0]
    arr = (image_tensor.cpu().numpy() * 255).astype("uint8")
    buf = io.BytesIO()
    Image.fromarray(arr, "RGB").save(buf, format="JPEG", quality=95)
    buf.seek(0)
    resp = requests.post(
        f"{BASE_URL}/upload_file",
        headers={"x-api-key": api_key},
        files={"file": ("image.jpg", buf, "image/jpeg")},
        timeout=120,
    )
    _check(resp)
    return _url(resp.json())


def _url(data):
    u = data.get("url") or data.get("file_url") or data.get("output")
    if not u:
        raise RuntimeError(f"Upload missing URL: {data}")
    return str(u)


def _submit(api_key, endpoint, payload):
    resp = requests.post(
        f"{BASE_URL}/{endpoint}",
        headers={"x-api-key": api_key, "Content-Type": "application/json"},
        json=payload,
        timeout=60,
    )
    _check(resp)
    rid = resp.json().get("request_id")
    if not rid:
        raise RuntimeError(f"No request_id in response: {resp.json()}")
    return rid


def _poll(api_key, request_id):
    deadline = time.time() + MAX_WAIT
    while time.time() < deadline:
        resp = requests.get(
            f"{BASE_URL}/predictions/{request_id}/result",
            headers={"x-api-key": api_key},
            timeout=30,
        )
        _check(resp)
        data = resp.json()
        status = data.get("status")
        print(f"[GPTImage2] {status}  {request_id}")
        if status == "completed":
            return data
        if status == "failed":
            raise RuntimeError(f"Generation failed: {data.get('error', 'unknown')}")
        time.sleep(POLL_INTERVAL)
    raise RuntimeError(f"Timeout waiting for result: {request_id}")


def _output_image_url(result):
    out = result.get("outputs") or result.get("output") or []
    if isinstance(out, list) and out:
        return str(out[0])
    if isinstance(out, str):
        return out
    for k in ("image_url", "url"):
        if result.get(k):
            return str(result[k])
    raise RuntimeError(f"No output image URL in result: {result}")


def _download_image(url):
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    img = Image.open(io.BytesIO(r.content)).convert("RGB")
    arr = np.array(img).astype(np.float32) / 255.0
    return torch.from_numpy(arr).unsqueeze(0)


def _check(resp):
    if resp.status_code == 401:
        raise RuntimeError("Auth failed — check your API key.")
    if resp.status_code == 402:
        raise RuntimeError("Insufficient credits — top up at muapi.ai.")
    if resp.status_code == 429:
        raise RuntimeError("Rate limited — please retry later.")
    if not resp.ok:
        print(f"[GPTImage2] API ERROR {resp.status_code}: {resp.text[:500]}")
        try:
            err = resp.json()
            raise RuntimeError(f"API {resp.status_code}: {err}")
        except Exception:
            raise RuntimeError(f"API {resp.status_code}: {resp.text[:300]}")


# ── Nodes ──────────────────────────────────────────────────────────────────────

class GPTImage2ApiKey:
    """
    Store your MuAPI API key once and wire it to any GPT-Image-2 node.
    Alternatively, leave all api_key fields empty — nodes auto-read from
    ~/.muapi/config.json (set via `muapi auth configure --api-key YOUR_KEY`).
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": (
                    "STRING",
                    {
                        "multiline": False,
                        "default": "",
                        "tooltip": "Your muapi.ai API key. Get one at muapi.ai → Dashboard → API Keys",
                    },
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("api_key",)
    FUNCTION = "run"
    CATEGORY = "🖼️ GPT-Image-2"

    def run(self, api_key):
        return (_load_api_key(api_key),)


class GPTImage2TextToImage:
    """
    GPT-Image-2 Text-to-Image
    --------------------------
    Generate a high-quality image from a text prompt using GPT-Image-2.

    Endpoint: POST /api/v1/gpt-image-2-text-to-image
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "A photorealistic image of a red fox sitting in a snowy forest at dusk.",
                    },
                ),
            },
            "optional": {
                "api_key": ("STRING", {"multiline": False, "default": ""}),
            },
        }

    RETURN_TYPES = ("IMAGE", "STRING", "STRING")
    RETURN_NAMES = ("image", "image_url", "request_id")
    FUNCTION = "run"
    CATEGORY = "🖼️ GPT-Image-2"

    def run(self, prompt, api_key=""):
        api_key = _load_api_key(api_key)
        payload = {"prompt": prompt}
        print("[GPTImage2 T2I] Submitting...")
        rid = _submit(api_key, "gpt-image-2-text-to-image", payload)
        result = _poll(api_key, rid)
        url = _output_image_url(result)
        print(f"[GPTImage2 T2I] Done → {url}")
        image = _download_image(url)
        return (image, url, rid)


class GPTImage2ImageToImage:
    """
    GPT-Image-2 Image-to-Image
    ---------------------------
    Transform or edit up to 9 reference images guided by a text prompt.
    Common uses: style transfer, product shots, scene editing.

    Endpoint: POST /api/v1/gpt-image-2-image-to-image

    Example prompt:
        "Transform this product image into a premium e-commerce poster style."
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Transform this product image into a premium e-commerce poster style.",
                    },
                ),
            },
            "optional": {
                "api_key": ("STRING", {"multiline": False, "default": ""}),
                "image_1": ("IMAGE",),
                "image_2": ("IMAGE",),
                "image_3": ("IMAGE",),
                "image_4": ("IMAGE",),
                "image_5": ("IMAGE",),
                "image_6": ("IMAGE",),
                "image_7": ("IMAGE",),
                "image_8": ("IMAGE",),
                "image_9": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE", "STRING", "STRING")
    RETURN_NAMES = ("image", "image_url", "request_id")
    FUNCTION = "run"
    CATEGORY = "🖼️ GPT-Image-2"

    def run(
        self,
        prompt,
        api_key="",
        image_1=None,
        image_2=None,
        image_3=None,
        image_4=None,
        image_5=None,
        image_6=None,
        image_7=None,
        image_8=None,
        image_9=None,
    ):
        api_key = _load_api_key(api_key)
        tensors = [image_1, image_2, image_3, image_4, image_5,
                   image_6, image_7, image_8, image_9]
        images_list = []
        for i, img in enumerate(tensors, 1):
            if img is not None:
                print(f"[GPTImage2 I2I] Uploading image {i}...")
                images_list.append(_upload_image(api_key, img))
        if not images_list:
            raise ValueError("At least one input image is required.")

        payload = {"prompt": prompt, "images_list": images_list}
        print(f"[GPTImage2 I2I] Submitting ({len(images_list)} image(s))...")
        rid = _submit(api_key, "gpt-image-2-image-to-image", payload)
        result = _poll(api_key, rid)
        url = _output_image_url(result)
        print(f"[GPTImage2 I2I] Done → {url}")
        image = _download_image(url)
        return (image, url, rid)


NODE_CLASS_MAPPINGS = {
    "GPTImage2ApiKey":        GPTImage2ApiKey,
    "GPTImage2TextToImage":   GPTImage2TextToImage,
    "GPTImage2ImageToImage":  GPTImage2ImageToImage,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GPTImage2ApiKey":        "🔑 GPT-Image-2 API Key",
    "GPTImage2TextToImage":   "🖼️ GPT-Image-2 Text to Image",
    "GPTImage2ImageToImage":  "🖼️ GPT-Image-2 Image to Image",
}
