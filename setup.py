from setuptools import setup

setup(
    name="seedream-5-api",
    version="0.1.0",
    author="Anil Matcha",
    description="Python wrapper for ByteDance's Seedream 5.0 API — 4K text-to-image generation, natural-language image editing, precise typography, and consistent character generation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["seedream_api", "mcp_server"],
    install_requires=[
        "requests",
        "python-dotenv",
        "mcp[cli]"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
