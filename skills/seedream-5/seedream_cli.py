import sys
import os
import argparse
import json

# Add the parent directory to the path so we can import the existing SeedreamAPI
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from seedream_api import SeedreamAPI

def main():
    parser = argparse.ArgumentParser(description="Seedream 5.0 CLI Wrapper for OpenClaw Skill")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    def add_t2i_parser(name, help_text, default_size="2K"):
        p = subparsers.add_parser(name, help=help_text)
        p.add_argument("--prompt", required=True, help="Text prompt")
        p.add_argument("--aspect_ratio", default="1:1", help="Aspect ratio (1:1, 16:9, 9:16, etc.)")
        p.add_argument("--size", default=default_size, choices=["1K", "2K", "4K"], help="Output resolution")
        p.add_argument("--num_images", type=int, default=1, help="Number of images to generate")
        p.add_argument("--seed", type=int, default=None, help="Optional seed for reproducibility")
        p.add_argument("--wait", action="store_true", help="Wait for completion")
        return p

    def add_edit_parser(name, help_text):
        p = subparsers.add_parser(name, help=help_text)
        p.add_argument("--prompt", required=True, help="Edit instruction")
        p.add_argument("--images", required=True, nargs="+", help="List of source image URLs")
        p.add_argument("--aspect_ratio", default="1:1", help="Aspect ratio")
        p.add_argument("--size", default="2K", choices=["1K", "2K", "4K"], help="Output resolution")
        p.add_argument("--seed", type=int, default=None, help="Optional seed for reproducibility")
        p.add_argument("--wait", action="store_true", help="Wait for completion")
        return p

    # Seedream 5.0
    add_t2i_parser("t2i", "Generate image from text (Seedream 5.0)", default_size="2K")
    add_edit_parser("edit", "Edit an existing image (Seedream 5.0 Edit)")

    # Seedream 4.5
    add_t2i_parser("t2i-v4-5", "Generate image from text (Seedream 4.5)")
    add_edit_parser("edit-v4-5", "Edit an existing image (Seedream 4.5 Edit)")

    # Seedream v4
    add_t2i_parser("t2i-v4", "Generate image from text (Seedream v4)")
    add_edit_parser("edit-v4", "Edit an existing image (Seedream v4 Edit)")

    # Seedream v3
    add_t2i_parser("t2i-v3", "Generate image from text (Seedream v3)", default_size="1K")

    # Upload
    upload = subparsers.add_parser("upload", help="Upload a local image file")
    upload.add_argument("--file_path", required=True, help="Path to local file")

    # Status
    status = subparsers.add_parser("status", help="Get task status")
    status.add_argument("--request_id", required=True, help="Request ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        api = SeedreamAPI()

        if args.command == "t2i":
            res = api.text_to_image(args.prompt, args.aspect_ratio, args.size, args.num_images, args.seed)
        elif args.command == "edit":
            res = api.edit_image(args.prompt, args.images, args.aspect_ratio, args.size, args.seed)
        elif args.command == "t2i-v4-5":
            res = api.text_to_image_v4_5(args.prompt, args.aspect_ratio, args.size, args.num_images, args.seed)
        elif args.command == "edit-v4-5":
            res = api.edit_image_v4_5(args.prompt, args.images, args.aspect_ratio, args.size, args.seed)
        elif args.command == "t2i-v4":
            res = api.text_to_image_v4(args.prompt, args.aspect_ratio, args.size, args.num_images, args.seed)
        elif args.command == "edit-v4":
            res = api.edit_image_v4(args.prompt, args.images, args.aspect_ratio, args.size, args.seed)
        elif args.command == "t2i-v3":
            res = api.text_to_image_v3(args.prompt, args.aspect_ratio, args.size, args.num_images, args.seed)
        elif args.command == "upload":
            res = api.upload_file(args.file_path)
            print(json.dumps(res, indent=2))
            return
        elif args.command == "status":
            res = api.get_result(args.request_id)
            print(json.dumps(res, indent=2))
            return

        request_id = res.get("request_id")

        if args.wait and request_id:
            print(f"Task submitted: {request_id}. Waiting for completion...")
            result = api.wait_for_completion(request_id)
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(res, indent=2))

    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=2))
        sys.exit(1)

if __name__ == "__main__":
    main()
