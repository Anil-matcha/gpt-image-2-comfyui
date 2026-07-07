# Seedream 5.0 API: Python Wrapper for ByteDance's AI Image Generator

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=seedream-5-api)

[![PyPI version](https://img.shields.io/pypi/v/seedream-5-api.svg)](https://pypi.org/project/seedream-5-api/)
[![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/Seedream-5-API.svg)](https://github.com/Anil-matcha/Seedream-5-API/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

The most comprehensive Python wrapper for the **Seedream 5.0 API** (developed by ByteDance), delivered via [muapi.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api). Generate stunning, high-fidelity **4K AI images** from text prompts with advanced visual reasoning and precise typography, or transform existing images using natural-language edits — all with a simple **Seedream 5.0 Python SDK**.

> ✅ **Seedream 5.0** (a.k.a. **Seedream 5 API**, **Seedream v5.0**) is ByteDance's next-generation text-to-image model — up to **4K resolution**, complex scene construction, consistent character generation, and real-time knowledge integration for accurate, contextually relevant visuals.
> - 🧪 Try **Seedream 5.0** now: [Text-to-Image Playground](https://muapi.ai/playground/bytedance-seedream-v5.0?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api) · [Edit Playground](https://muapi.ai/playground/bytedance-seedream-v5.0-edit?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api)
> - 🎨 This wrapper also supports **Seedream 4.5**, **Seedream v4**, and **Seedream v3** for teams that need version pinning.

> 🌊 **Also explore these top AI generation models:**
> - 🎬 [Seedance 2.0 API](https://github.com/Anil-matcha/Seedance-2-API) — ByteDance's video generation model, Text-to-Video & Image-to-Video
> - 🐎 [HappyHorse 1.0 API](https://github.com/Anil-matcha/HappyHorse-1.0-API) — Alibaba's #1 ranked video model (1392 Elo I2V)
> - 🎬 [Veo 4 API](https://github.com/Anil-matcha/Veo-4-API) — Google DeepMind's native 4K video model

## Related Projects

- [Seedance-2-API](https://github.com/Anil-matcha/Seedance-2-API) — Python wrapper for ByteDance's Seedance 2.0 video generation API
- [awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts) — Curated Seedance 2.5 API guide and prompts
- [Awesome-GPT-Image-2-API-Prompts](https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts) — Curated GPT-Image-2 prompts for the OpenAI API
- [gpt-image-2-comfyui](https://github.com/Anil-matcha/gpt-image-2-comfyui) — ComfyUI custom nodes for GPT-Image-2

## 🚀 Why Use Seedream 5.0 API?

Seedream 5.0 is ByteDance's flagship **text-to-image** and **image-editing** model, offering unparalleled fidelity, prompt adherence, and typography accuracy.

- **4K Resolution**: Generate ultra-high-fidelity images up to native 4K.
- **Advanced Visual Reasoning**: Handles complex, multi-subject scene construction with strong prompt adherence.
- **Precise Typography**: Renders legible, accurate text and logos inside generated images — ideal for posters, UI mockups, and product visuals.
- **Consistent Character Generation**: Maintain the same subject/character across multiple generations.
- **Natural-Language Image Editing**: Style transfer (Anime, Cyberpunk, Fantasy), background swaps, and object modification via `edit_image()` — no masking required.
- **Developer-First**: Fast processing via the MuAPI infrastructure with a simple Python SDK and MCP server.

## 🌟 Key Features of Seedream 5.0 API

- ✅ **Seedream 5.0 Text-to-Image**: Transform descriptive prompts into 4K AI images with `text_to_image()`.
- ✅ **Seedream 5.0 Edit**: Edit existing images using natural language with `edit_image()` — preserves lighting, color tones, and character consistency.
- ✅ **Multiple Aspect Ratios**: `1:1`, `16:9`, `9:16`, `4:3`, `3:4` and more.
- ✅ **Flexible Resolutions**: `1K`, `2K`, and `4K` output sizes.
- ✅ **Multi-Image Generation**: Generate up to 4 images per request with `num_images`.
- ✅ **Reproducible Seeds**: Pass a `seed` for deterministic, repeatable generations.
- ✅ **File Upload**: Directly upload local images using `upload_file()` for use in edit tasks.
- ✅ **Legacy Version Support**: Also wraps **Seedream 4.5**, **Seedream v4**, and **Seedream v3** for version-pinned pipelines.
- ✅ **MCP Server Included**: Use Seedream 5.0 as a Model Context Protocol server with Claude Desktop, Cursor, or any MCP client.

---

## 🛠 Installation

### Via Pip (Recommended)
```bash
pip install seedream-5-api
```

### From Source
```bash
# Clone the Seedream 5.0 API repository
git clone https://github.com/Anil-matcha/Seedream-5-API.git
cd Seedream-5-API

# Install required dependencies
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add your [MuAPI](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api) API key:
```env
MUAPI_API_KEY=your_muapi_api_key_here
```

---

## 🤖 Seedream 5.0 MCP Server

You can use Seedream 5.0 as an **MCP (Model Context Protocol)** server. This allows AI models (like Claude Desktop or Cursor) to directly invoke Seedream 5.0 image generation and editing tools.

### Running the MCP Server
1. Ensure `MUAPI_API_KEY` is set in your environment.
2. Run the server:
   ```bash
   python3 mcp_server.py
   ```
3. To test with the MCP Inspector:
   ```bash
   npx -y @modelcontextprotocol/inspector python3 mcp_server.py
   ```

---

## 💻 Quick Start with Seedream 5.0 API (Python)

```python
from seedream_api import SeedreamAPI

# Initialize the Seedream 5.0 client
api = SeedreamAPI()

# 1. Generate an image from text using Seedream 5.0 API
print("Generating AI image using Seedream 5.0...")
submission = api.text_to_image(
    prompt="A cinematic portrait of a cyberpunk samurai in a neon-lit Tokyo alley, 4k, hyperrealistic",
    aspect_ratio="16:9",
    size="4K",
)

# 2. Wait for completion
result = api.wait_for_completion(submission["request_id"])
print(f"Success! View your Seedream 5.0 image here: {result['outputs'][0]}")

# 3. Edit an existing image using natural language
edit_submission = api.edit_image(
    prompt="Change the outfit to samurai armor with gold trim, keep the face identical",
    image_urls=["https://example.com/portrait.jpg"],
    aspect_ratio="16:9",
)
edit_result = api.wait_for_completion(edit_submission["request_id"])
print(f"Edited image: {edit_result['outputs'][0]}")
```

---

## 📡 API Endpoints & Reference

### 1. Seedream 5.0 Text-to-Image
**Endpoint**: `POST https://api.muapi.ai/api/v1/bytedance-seedream-v5.0`

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/bytedance-seedream-v5.0" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A majestic eagle soaring over the snow-capped Himalayas, 4k, cinematic lighting",
      "aspect_ratio": "16:9",
      "size": "4K",
      "num_images": 1
  }'
```

### 2. Seedream 5.0 Edit (Image-to-Image)
**Endpoint**: `POST https://api.muapi.ai/api/v1/bytedance-seedream-v5.0-edit`

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/bytedance-seedream-v5.0-edit" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Turn the background into a cyberpunk cityscape at night, keep the subject unchanged",
      "image_urls": ["https://example.com/photo.jpg"],
      "aspect_ratio": "16:9",
      "size": "2K"
  }'
```

### 3. Seedream 4.5 Text-to-Image
**Endpoint**: `POST https://api.muapi.ai/api/v1/bytedance-seedream-v4.5`

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/bytedance-seedream-v4.5" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A surreal sci-fi cityscape floating above the clouds, photoreal, cinematic",
      "aspect_ratio": "1:1",
      "size": "2K"
  }'
```

### 4. Seedream 4.5 Edit
**Endpoint**: `POST https://api.muapi.ai/api/v1/bytedance-seedream-v4.5-edit`

**Python SDK:**
```python
result = api.edit_image_v4_5(
    prompt="Replace the sky with a dramatic sunset",
    image_urls=["https://example.com/landscape.jpg"],
)
```

### 5. Seedream v4 Text-to-Image
**Endpoint**: `POST https://api.muapi.ai/api/v1/bytedance-seedream-v4`

**Python SDK:**
```python
result = api.text_to_image_v4(prompt="A fantasy castle on a floating island, artstation quality")
```

### 6. Seedream v4 Edit
**Endpoint**: `POST https://api.muapi.ai/api/v1/bytedance-seedream-v4-edit`

**Python SDK:**
```python
result = api.edit_image_v4(
    prompt="Change the season from summer to winter",
    image_urls=["https://example.com/scene.jpg"],
)
```

### 7. Seedream v3 Text-to-Image
**Endpoint**: `POST https://api.muapi.ai/api/v1/bytedance-seedream-v3`

**Python SDK:**
```python
result = api.text_to_image_v3(prompt="An anime-style portrait of a warrior princess, vibrant colors")
```

---

## 📖 Documentation & Guides

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `text_to_image` | `prompt`, `aspect_ratio`, `size`, `num_images`, `seed` | Generate a 4K image from text using **Seedream 5.0**. |
| `edit_image` | `prompt`, `image_urls`, `aspect_ratio`, `size`, `seed` | Edit an existing image using natural language via **Seedream 5.0 Edit**. |
| `text_to_image_v4_5` | `prompt`, `aspect_ratio`, `size`, `num_images`, `seed` | Generate an image using **Seedream 4.5**. |
| `edit_image_v4_5` | `prompt`, `image_urls`, `aspect_ratio`, `size`, `seed` | Edit an image using **Seedream 4.5 Edit**. |
| `text_to_image_v4` | `prompt`, `aspect_ratio`, `size`, `num_images`, `seed` | Generate an image using **Seedream v4**. |
| `edit_image_v4` | `prompt`, `image_urls`, `aspect_ratio`, `size`, `seed` | Edit an image using **Seedream v4 Edit**. |
| `text_to_image_v3` | `prompt`, `aspect_ratio`, `size`, `num_images`, `seed` | Generate an image using **Seedream v3**. |
| `upload_file` | `file_path` | Upload a local image to MuAPI for use in edit tasks. |
| `get_result` | `request_id` | Check task status for a Seedream generation task. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper for Seedream generation tasks. |

---

## 🔗 Official Resources
- **Playground — Seedream 5.0**: [Text-to-Image](https://muapi.ai/playground/bytedance-seedream-v5.0?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api) · [Edit](https://muapi.ai/playground/bytedance-seedream-v5.0-edit?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api)
- **Playground — Seedream 4.5**: [Text-to-Image](https://muapi.ai/playground/bytedance-seedream-v4.5?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api) · [Edit](https://muapi.ai/playground/bytedance-seedream-v4.5-edit?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api)
- **Playground — Seedream v4**: [Text-to-Image](https://muapi.ai/playground/bytedance-seedream-v4?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api) · [Edit](https://muapi.ai/playground/bytedance-seedream-v4-edit?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedream-5-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: Seedream 5.0 API, Seedream 5 API, Seedream v5.0, Seedream v5, ByteDance Seedream, Seedream AI, Seedream Text-to-Image, Seedream Image Editing, Seedream Python SDK, Seedream API Python, Seedream 5.0 Python Wrapper, AI Image Generator, Text-to-Image API, Image-to-Image API, 4K AI Image Generation, Seedream 4.5 API, Seedream v4 API, Seedream v3 API, MuAPI, Image Generation API, AI Art Generator, ByteDance Image AI, Seedream API Documentation, Seedream Character Consistency, Seedream Typography, Python Image Generation API, Seedream 5.0 Tutorial, Seedream 5.0 Edit API.
