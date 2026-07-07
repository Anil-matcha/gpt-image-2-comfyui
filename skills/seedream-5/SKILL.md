---
name: seedream-5
description: Generate 4K AI images from text prompts and edit existing images using natural language with Seedream 5.0 (by ByteDance).
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        - MUAPI_API_KEY
      bins:
        - python3.11
    emoji: 🎨
    homepage: https://muapi.ai
    os: ["macos", "linux"]
---

# Seedream 5.0

Seedream 5.0 is ByteDance's next-generation text-to-image model, delivering high-fidelity AI art with advanced visual reasoning and precise typography. This skill allows you to generate images from text and edit existing images using natural language commands.

## Prerequisites

- **MUAPI_API_KEY**: You must have an API key from [muapi.ai](https://muapi.ai). Set it as an environment variable.

## Usage Guide

You can use Seedream 5.0 to create images in various aspect ratios (1:1, 16:9, 9:16, 4:3, 3:4) and resolutions (1K, 2K, 4K).

### Text-to-Image
Generate an image from a descriptive text prompt.
```bash
python3.11 skills/seedream-5/seedream_cli.py t2i --prompt "A cinematic portrait of a cyberpunk samurai in a neon-lit Tokyo alley" --size 4K --wait
```

### Image Editing
Edit an existing image using natural language.
```bash
python3.11 skills/seedream-5/seedream_cli.py edit --images "https://example.com/photo.jpg" --prompt "Change the background to a cyberpunk cityscape at night" --wait
```

### Legacy Versions
Generate with earlier Seedream versions for version-pinned pipelines.
```bash
python3.11 skills/seedream-5/seedream_cli.py t2i-v4-5 --prompt "A surreal sci-fi cityscape floating above the clouds" --wait
python3.11 skills/seedream-5/seedream_cli.py t2i-v4 --prompt "A fantasy castle on a floating island" --wait
python3.11 skills/seedream-5/seedream_cli.py t2i-v3 --prompt "An anime-style portrait of a warrior princess" --wait
```

## Tips for Best Results

- **Be Descriptive**: Detailed prompts result in better image quality and more accurate scene construction.
- **Wait for Completion**: Use the `--wait` flag to receive the final image URL directly. Without it, you will receive a `request_id` which you can check later using the `status` command.
- **Aspect Ratios**: Use `1:1` for square, `16:9`/`9:16` for widescreen/vertical content.
- **Resolution**: Use `--size 4K` for maximum fidelity, `--size 1K` for fast drafts.
- **Reproducibility**: Pass `--seed` to get deterministic, repeatable generations.

## Commands Reference

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `t2i` | `--prompt`, `--aspect_ratio`, `--size`, `--num_images`, `--seed`, `--wait` | Text to Image (Seedream 5.0) |
| `edit` | `--images`, `--prompt`, `--aspect_ratio`, `--size`, `--seed`, `--wait` | Image Editing (Seedream 5.0 Edit) |
| `t2i-v4-5` | `--prompt`, `--aspect_ratio`, `--size`, `--num_images`, `--seed`, `--wait` | Text to Image (Seedream 4.5) |
| `edit-v4-5` | `--images`, `--prompt`, `--aspect_ratio`, `--size`, `--seed`, `--wait` | Image Editing (Seedream 4.5) |
| `t2i-v4` | `--prompt`, `--aspect_ratio`, `--size`, `--num_images`, `--seed`, `--wait` | Text to Image (Seedream v4) |
| `edit-v4` | `--images`, `--prompt`, `--aspect_ratio`, `--size`, `--seed`, `--wait` | Image Editing (Seedream v4) |
| `t2i-v3` | `--prompt`, `--aspect_ratio`, `--size`, `--num_images`, `--seed`, `--wait` | Text to Image (Seedream v3) |
| `status`| `--request_id` | Check Task Status |
