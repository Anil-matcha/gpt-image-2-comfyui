# GPT-Image-2 ComfyUI Nodes

> **ComfyUI custom nodes for GPT-Image-2** — OpenAI's latest image generation model.
> Generate and edit stunning AI images directly inside ComfyUI using the [muapi.ai](https://muapi.ai) API.
> If you wish to check the API documentation check this [GPT-Image-2 API](https://muapi.ai/docs).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Node-blue)](https://github.com/comfyanonymous/ComfyUI)
[![GPT-Image-2](https://img.shields.io/badge/Model-GPT--Image--2-green)](https://muapi.ai)

---

## What is GPT-Image-2?

GPT-Image-2 is OpenAI's latest image generation model with native image editing support. It supports:

- **Text-to-Image** — generate high-quality images from a text description
- **Image-to-Image** — edit or transform up to 9 reference images guided by a prompt

---

## Nodes

| Node | Description |
|------|-------------|
| 🔑 GPT-Image-2 API Key | Set your key once — wire to all nodes |
| 🖼️ GPT-Image-2 Text to Image | Generate an image from a text prompt |
| 🖼️ GPT-Image-2 Image to Image | Edit or transform up to 9 reference images |

---

## Installation

### Via ComfyUI Manager (recommended)
1. Open **ComfyUI Manager** → **Install via Git URL**
2. Paste: `https://github.com/Anil-matcha/gpt-image-2-comfyui`
3. Restart ComfyUI

### Manual
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Anil-matcha/gpt-image-2-comfyui
pip install -r gpt-image-2-comfyui/requirements.txt
```

---

## Quick Start

1. Sign up at [muapi.ai](https://muapi.ai) and go to **Dashboard → API Keys → Create Key**
2. Right-click the ComfyUI canvas → **Add Node** → **🖼️ GPT-Image-2**
3. Add a **🔑 GPT-Image-2 API Key** node, paste your key, and wire its output to any generation node
4. Write a prompt and hit **Queue Prompt**

> **Tip:** If you use the [MuAPI CLI](https://github.com/SamurAIGPT/muapi-cli), run `muapi auth configure --api-key YOUR_KEY` once and all nodes will pick it up automatically — no need to paste the key anywhere.

---

## Node Reference

### 🔑 GPT-Image-2 API Key

Set your muapi.ai API key once and wire the output to all generation nodes. Alternatively, leave every `api_key` field blank — nodes automatically read from `~/.muapi/config.json` if you've authenticated via the CLI.

| Field | Description |
|-------|-------------|
| `api_key` | Your muapi.ai API key |

**Output:** `api_key` string (wire to generation nodes)

---

### 🖼️ GPT-Image-2 Text to Image

Generate a high-quality image from a text prompt.

| Field | Description |
|-------|-------------|
| `prompt` | Describe the image you want to generate |
| `api_key` | *(optional)* API key — wire from the API Key node or leave blank |

**Outputs:**

| Output | Type | Description |
|--------|------|-------------|
| `image` | IMAGE | Generated image as a ComfyUI tensor |
| `image_url` | STRING | CDN URL of the generated image |
| `request_id` | STRING | Generation request ID |

**Example prompt:**
```
A photorealistic image of a red fox sitting in a snowy forest at dusk.
```

---

### 🖼️ GPT-Image-2 Image to Image

Edit or transform up to 9 reference images guided by a text prompt.

| Field | Description |
|-------|-------------|
| `prompt` | Describe the desired transformation or style |
| `image_1` … `image_9` | *(optional)* Reference images to edit |
| `api_key` | *(optional)* API key — wire from the API Key node or leave blank |

**Outputs:**

| Output | Type | Description |
|--------|------|-------------|
| `image` | IMAGE | Generated image as a ComfyUI tensor |
| `image_url` | STRING | CDN URL of the generated image |
| `request_id` | STRING | Generation request ID |

**Example prompt:**
```
Transform this product image into a premium e-commerce poster style.
```

---

## API

All requests go through the [muapi.ai](https://muapi.ai) API. Get your API key from the dashboard.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/gpt-image-2-text-to-image` | POST | Submit a text-to-image request |
| `/api/v1/gpt-image-2-image-to-image` | POST | Submit an image-to-image request |
| `/api/v1/predictions/{request_id}/result` | GET | Poll for result |

---

## License

MIT — see [LICENSE](LICENSE).
