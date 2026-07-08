import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SeedreamAPI:
    def __init__(self, api_key=None):
        """
        Initialize the Seedream 5.0 Pro API client.
        :param api_key: Your MuAPI.ai API key. Defaults to MUAPI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("MUAPI_API_KEY")
        if not self.api_key:
            raise ValueError("API Key is required. Set MUAPI_API_KEY in .env or pass it to the constructor.")

        self.base_url = "https://api.muapi.ai/api/v1"
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def text_to_image(self, prompt, aspect_ratio="1:1", size="2K", num_images=1, seed=None):
        """
        Submits a Seedream 5.0 Pro Text-to-Image generation task.

        Seedream 5.0 Pro is ByteDance's flagship text-to-image model, delivering
        maximum-fidelity AI art with advanced visual reasoning and precise typography.
        Supports up to 4K resolution, complex scene construction, and consistent
        character generation.

        :param prompt: Descriptive text prompt for the image to generate.
        :param aspect_ratio: Image aspect ratio (e.g. '1:1', '16:9', '9:16', '4:3', '3:4').
        :param size: Output resolution — '1K', '2K', or '4K'.
        :param num_images: Number of images to generate (1-4).
        :param seed: Optional seed for reproducible generations.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/bytedance-seedream-v5.0-pro"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "size": size,
            "num_images": num_images,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def edit_image(self, prompt, image_urls, aspect_ratio="1:1", size="2K", seed=None):
        """
        Submits a Seedream 5.0 Pro Edit (image-to-image) generation task.

        Seedream 5.0 Pro Edit enables precise, controllable edits using natural language —
        high-fidelity style transfer (Anime, Cyberpunk, Fantasy), background swaps,
        and object modification while preserving lighting, color tones, and character
        consistency.

        :param prompt: Natural-language instruction describing the desired edit.
        :param image_urls: List of source image URLs to edit (reference with @image1, @image2, ...).
        :param aspect_ratio: Output aspect ratio.
        :param size: Output resolution — '1K', '2K', or '4K'.
        :param seed: Optional seed for reproducible generations.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/bytedance-seedream-v5.0-pro-edit"
        payload = {
            "prompt": prompt,
            "image_urls": image_urls,
            "aspect_ratio": aspect_ratio,
            "size": size,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def text_to_image_v5(self, prompt, aspect_ratio="1:1", size="2K", num_images=1, seed=None):
        """
        Submits a Seedream 5.0 (base, non-Pro) Text-to-Image generation task.

        :param prompt: Descriptive text prompt for the image to generate.
        :param aspect_ratio: Image aspect ratio.
        :param size: Output resolution — '1K', '2K', or '4K'.
        :param num_images: Number of images to generate (1-4).
        :param seed: Optional seed for reproducible generations.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/bytedance-seedream-v5.0"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "size": size,
            "num_images": num_images,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def edit_image_v5(self, prompt, image_urls, aspect_ratio="1:1", size="2K", seed=None):
        """
        Submits a Seedream 5.0 (base, non-Pro) Edit (image-to-image) generation task.

        :param prompt: Natural-language instruction describing the desired edit.
        :param image_urls: List of source image URLs to edit.
        :param aspect_ratio: Output aspect ratio.
        :param size: Output resolution — '1K', '2K', or '4K'.
        :param seed: Optional seed for reproducible generations.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/bytedance-seedream-v5.0-edit"
        payload = {
            "prompt": prompt,
            "image_urls": image_urls,
            "aspect_ratio": aspect_ratio,
            "size": size,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def text_to_image_v4_5(self, prompt, aspect_ratio="1:1", size="2K", num_images=1, seed=None):
        """
        Submits a Seedream 4.5 Text-to-Image generation task.

        Seedream 4.5 is ByteDance's advanced text-to-image diffusion model for
        high-detail, high-contrast, cinematic and stylized images — surreal fantasy,
        sci-fi worlds, product visuals, and photoreal scenes.

        :param prompt: Descriptive text prompt.
        :param aspect_ratio: Image aspect ratio.
        :param size: Output resolution — '1K', '2K', or '4K'.
        :param num_images: Number of images to generate.
        :param seed: Optional seed.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/bytedance-seedream-v4.5"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "size": size,
            "num_images": num_images,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def edit_image_v4_5(self, prompt, image_urls, aspect_ratio="1:1", size="2K", seed=None):
        """
        Submits a Seedream 4.5 Edit (image-to-image) generation task.

        :param prompt: Natural-language instruction describing the desired edit.
        :param image_urls: List of source image URLs to edit.
        :param aspect_ratio: Output aspect ratio.
        :param size: Output resolution — '1K', '2K', or '4K'.
        :param seed: Optional seed.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/bytedance-seedream-v4.5-edit"
        payload = {
            "prompt": prompt,
            "image_urls": image_urls,
            "aspect_ratio": aspect_ratio,
            "size": size,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def text_to_image_v4(self, prompt, aspect_ratio="1:1", size="2K", num_images=1, seed=None):
        """
        Submits a Seedream v4 Text-to-Image generation task — high-fidelity images
        with strong support for realism, fantasy, and artistic styles.

        :param prompt: Descriptive text prompt.
        :param aspect_ratio: Image aspect ratio.
        :param size: Output resolution — '1K' or '2K'.
        :param num_images: Number of images to generate.
        :param seed: Optional seed.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/bytedance-seedream-v4"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "size": size,
            "num_images": num_images,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def edit_image_v4(self, prompt, image_urls, aspect_ratio="1:1", size="2K", seed=None):
        """
        Submits a Seedream v4 Edit (image-to-image) generation task.

        :param prompt: Natural-language instruction describing the desired edit.
        :param image_urls: List of source image URLs to edit.
        :param aspect_ratio: Output aspect ratio.
        :param size: Output resolution.
        :param seed: Optional seed.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/bytedance-seedream-v4-edit"
        payload = {
            "prompt": prompt,
            "image_urls": image_urls,
            "aspect_ratio": aspect_ratio,
            "size": size,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def text_to_image_v3(self, prompt, aspect_ratio="1:1", size="1K", num_images=1, seed=None):
        """
        Submits a Seedream v3 Text-to-Image generation task — visually rich and
        artistic images, ideal for fantasy, anime, surrealism, and vibrant color
        compositions.

        :param prompt: Descriptive text prompt.
        :param aspect_ratio: Image aspect ratio.
        :param size: Output resolution.
        :param num_images: Number of images to generate.
        :param seed: Optional seed.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/bytedance-seedream-v3"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "size": size,
            "num_images": num_images,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def _post_request(self, endpoint, payload):
        response = requests.post(endpoint, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def upload_file(self, file_path):
        """
        Uploads a local file (image) to MuAPI for use in generation tasks.

        :param file_path: Path to the local file to upload.
        :return: JSON response from the MuAPI containing the URL of the uploaded file.
        """
        endpoint = f"{self.base_url}/upload_file"

        # Omit Content-Type to let requests set the multipart boundary automatically
        headers = {
            "x-api-key": self.api_key
        }

        with open(file_path, "rb") as file_data:
            files = {"file": file_data}
            response = requests.post(endpoint, headers=headers, files=files)

        response.raise_for_status()
        return response.json()

    def get_result(self, request_id):
        """
        Polls for the result of a generation task.
        """
        endpoint = f"{self.base_url}/predictions/{request_id}/result"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def wait_for_completion(self, request_id, poll_interval=5, timeout=300):
        """
        Waits for the image generation to complete and returns the result.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = self.get_result(request_id)
            status = result.get("status")

            if status == "completed":
                return result
            elif status == "failed":
                raise Exception(f"Image generation failed: {result.get('error')}")

            print(f"Status: {status}. Waiting {poll_interval} seconds...")
            time.sleep(poll_interval)

        raise TimeoutError("Timed out waiting for image generation to complete.")

if __name__ == "__main__":
    # Example usage for Text-to-Image
    try:
        api = SeedreamAPI()
        prompt = "A cinematic portrait of a cyberpunk samurai in a neon-lit Tokyo alley, 4k, hyperrealistic"

        print(f"Submitting Seedream 5.0 Pro Text-to-Image task with prompt: {prompt}")
        submission = api.text_to_image(prompt=prompt, aspect_ratio="16:9", size="2K")
        request_id = submission.get("request_id")
        print(f"Task submitted. Request ID: {request_id}")

        print("Waiting for completion...")
        result = api.wait_for_completion(request_id)
        print(f"Generation completed! Image URL: {result.get('outputs', [result.get('url')])[0]}")

    except Exception as e:
        print(f"Error: {e}")
