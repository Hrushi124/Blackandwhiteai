#!/usr/bin/env python3

import os
import urllib.request
from tqdm import tqdm
import subprocess
import sys

# Define model URLs
MODEL_URLS = {
    "stable_model": "https://huggingface.co/spensercai/DeOldify/resolve/main/ColorizeStable_gen.pth",
    "artistic_model": "https://huggingface.co/spensercai/DeOldify/resolve/main/ColorizeArtistic_gen.pth", 
    "video_model": "https://huggingface.co/spensercai/DeOldify/resolve/main/ColorizeVideo_gen.pth"
}

models_dir = "models/deoldify"

# Ensure models directory exists
os.makedirs(models_dir, exist_ok=True)

def download(url, path):
    """Download a file from a URL to a specific path, showing progress."""
    if os.path.exists(path):
        print(f"{os.path.basename(path)} already exists")
        return False  # File already exists, no need to download
    try:
        print(f"Downloading {os.path.basename(path)}...")
        with urllib.request.urlopen(url) as request, open(path, 'wb') as f, tqdm(
            desc=f"Downloading {os.path.basename(path)}",
            total=int(request.headers.get('Content-Length', 0)),
            unit='B',
            unit_scale=True,
            unit_divisor=1024
        ) as progress:
            for chunk in iter(lambda: request.read(4096), b""):
                f.write(chunk)
                progress.update(len(chunk))
        return True
    except Exception as e:
        print(f"Failed to download {os.path.basename(path)}: {e}")
        return False

def download_models():
    """Download all models if they don't exist locally."""
    print("Checking and downloading models...")
    models_already_downloaded = True
    for name, url in MODEL_URLS.items():
        path = os.path.join(models_dir, os.path.basename(url))
        if download(url, path):
            models_already_downloaded = False
    if models_already_downloaded:
        print("All models for DeOldify are already downloaded.")

def install_packages():
    """Install required packages"""
    packages = [
        'wandb',
        'fastai==1.0.60',
        'tensorboardX',
        'ffmpeg-python',
        'yt-dlp',
        'opencv-python',
        'Pillow',
        'io',
        'base64'
    ]
    
    print("Installing Python packages...")
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to install {package}: {e}")
        except Exception as e:
            print(f"Error installing {package}: {e}")

if __name__ == "__main__":
    print("Setting up DeOldify...")
    install_packages()
    download_models()
    print("Setup complete!")
