#!/usr/bin/env python3

import ssl
import urllib.request
import os

# Disable SSL verification as a workaround for certificate issues
ssl._create_default_https_context = ssl._create_unverified_context

# Download ResNet34 model manually
def download_resnet34():
    url = "https://download.pytorch.org/models/resnet34-b627a593.pth"
    cache_dir = os.path.expanduser("~/.cache/torch/hub/checkpoints")
    os.makedirs(cache_dir, exist_ok=True)
    
    model_path = os.path.join(cache_dir, "resnet34-b627a593.pth")
    
    if not os.path.exists(model_path):
        print("Downloading ResNet34 model...")
        try:
            urllib.request.urlretrieve(url, model_path)
            print("ResNet34 model downloaded successfully!")
        except Exception as e:
            print(f"Failed to download ResNet34 model: {e}")
    else:
        print("ResNet34 model already exists")

if __name__ == "__main__":
    download_resnet34()
