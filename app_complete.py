'''
Black & White AI - Image & Video Colorization Application
Description: Restore and colorize old black & white photos and videos using AI
'''

# Fix SSL certificate issues on macOS
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from deoldify import device
from deoldify.device_id import DeviceId
from PIL import Image
import gradio as gr
import base64
from io import BytesIO
from pathlib import Path
import tempfile
import os
#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)

from deoldify.visualize import *

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()
MODELS_DIR = SCRIPT_DIR / "models"

import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
warnings.filterwarnings("ignore", category=UserWarning, message="The parameter 'pretrained' is deprecated since 0.13 and may be removed in the future, please use 'weights' instead.")
warnings.filterwarnings("ignore", category=FutureWarning, message="Arguments other than a weight enum or `None`.*?")

# Image conversion functions
def image_to_base64(image_path):
    with open(image_path, 'rb') as f:
        image = f.read()
    image_b64 = base64.b64encode(image).decode()
    return image_b64

def ColorizeImage(base64str, render_factor=50, artistic=False):
    vis = get_image_colorizer(root_folder=MODELS_DIR, render_factor=render_factor, artistic=artistic)
    # Convert base64 to PIL Image
    img = Image.open(BytesIO(base64.b64decode(base64str)))
    outImg = vis.get_transformed_image_from_image(img, render_factor=render_factor)
    return outImg

def ColorizeVideo(video_path, render_factor=21, progress=gr.Progress()):
    """Colorize a video file"""
    print(f"ColorizeVideo called with video_path: {video_path}, render_factor: {render_factor}")
    
    if video_path is None:
        print("❌ No video file provided - video_path is None")
        return None
    
    if not os.path.exists(video_path):
        print(f"❌ Video file does not exist at path: {video_path}")
        return None
    
    # Check file size
    file_size_mb = os.path.getsize(video_path) / (1024*1024)
    print(f"✅ Video file found: {video_path}")
    print(f"📦 File size: {file_size_mb:.2f} MB")
    
    if file_size_mb > 500:
        print(f"⚠️ WARNING: Large file ({file_size_mb:.2f} MB) - this may take a very long time!")
    
    try:
        print(f"🎬 Starting video colorization for: {video_path}")
        print(f"⚙️ Render factor: {render_factor}")
        
        # Create a temporary work folder
        work_folder = SCRIPT_DIR / "video_work"
        work_folder.mkdir(exist_ok=True)
        print(f"Work folder created at: {work_folder}")
        
        # Get video colorizer with correct model path
        print(f"Loading video colorizer with models from: {MODELS_DIR}")
        video_colorizer = get_stable_video_colorizer(
            root_folder=MODELS_DIR,
            render_factor=render_factor, 
            workfolder=str(work_folder)
        )
        print("Video colorizer loaded successfully")
        
        # Copy video to source folder
        source_folder = work_folder / "source"
        source_folder.mkdir(exist_ok=True)
        
        video_filename = Path(video_path).name
        source_path = source_folder / video_filename
        
        # Copy the uploaded file to our source directory
        import shutil
        print(f"Copying video to: {source_path}")
        shutil.copy2(video_path, source_path)
        print("Video copied successfully")
        
        # Colorize the video
        print(f"Starting colorization of: {video_filename}")
        result_path = video_colorizer.colorize_from_file_name(
            video_filename, 
            render_factor=render_factor, 
            post_process=True,
            g_process_bar=progress
        )
        
        print(f"Video colorization completed! Result: {result_path}")
        return str(result_path)
        
    except Exception as e:
        print(f"❌ Error processing video: {e}")
        import traceback
        traceback.print_exc()
        return None

# Create the Gradio interface
with gr.Blocks(analytics_enabled=False, title="Black & White AI - Image & Video Processing") as ai_app_interface:
    
    gr.Markdown("# 🖤 Black & White AI — Image & Video Processing")
    gr.Markdown("Restore, colorize, and enhance old black & white photos and videos using AI.")
    
    with gr.Tabs():
        # Image Tab
        with gr.TabItem("🖼️ Image — B&W AI"):
            def DeOldifyImage(image, render_factor=35, artistic=False):
                if isinstance(image, str):
                    image = image_to_base64(image)
                outImg = ColorizeImage(image, render_factor, artistic)
                return outImg
                
            with gr.Row():
                with gr.Column():
                    image_input = gr.Image(label="Original Image", type="filepath")
                    image_render_factor = gr.Slider(minimum=1, maximum=50, step=1, label="Render Factor", value=35)
                    image_artistic = gr.Checkbox(label="Artistic Mode", value=False)
                    image_button = gr.Button("Process Image", variant="primary")
                with gr.Column():
                    image_output = gr.Image(label="Colorized Image", type="pil")
            
            image_button.click(
                fn=DeOldifyImage,
                inputs=[image_input, image_render_factor, image_artistic],
                outputs=[image_output]
            )
        
    # Video Tab
    with gr.TabItem("🎬 Video — B&W AI"):
            gr.Markdown("### Upload and colorize your black & white videos")
            with gr.Row():
                with gr.Column():
                    video_input = gr.Video(label="Upload Original Video", sources=["upload"])
                    video_render_factor = gr.Slider(minimum=1, maximum=40, step=1, label="Render Factor", value=21)
                    gr.Markdown("""
                    ⚠️ **Important Notes:**
                    - Video processing can take **several minutes** depending on length and quality
                    - Lower render factor = faster processing (recommended: 10-21)
                    - Supported formats: MP4, AVI, MOV, MKV
                    - Please be patient - do not refresh the page during processing
                    """)
                    video_button = gr.Button("Process Video", variant="primary")
                with gr.Column():
                    video_output = gr.Video(label="Processed Video")
                    gr.Markdown("The processed video will appear here when processing is complete.")
            
            video_button.click(
                fn=ColorizeVideo,
                inputs=[video_input, video_render_factor],
                outputs=[video_output]
            )
    
    # Instructions
    with gr.Accordion("📋 Instructions", open=False):
        gr.Markdown("""
        ### How to Use:
        
    **For Images:**
    1. Upload a black & white or old photo
    2. Adjust the render factor (higher = more detailed but slower)
    3. Toggle artistic mode for more creative results
    4. Click "Process Image"
        
    **For Videos:**
    1. Upload a black & white video (MP4, AVI, MOV, etc.)
    2. Adjust the render factor (lower recommended for videos)
    3. Click "Process Video" and wait for processing
        
        ### Tips:
        - **Render Factor:** 10-20 for videos, 30-50 for images
        - **Artistic Mode:** More creative but less realistic colors
        - **Video Processing:** Can take 5-30 minutes depending on length
        
        ### ⚠️ Important for Video Upload:
        - **Use LOCAL URL (http://127.0.0.1:7860) for faster uploads!**
        - Public URL is much slower for video uploads
        - Recommended video size: Under 100MB for best results
        - For larger files, consider reducing video resolution first
        """)

# Launch the app with increased file size limit
print("\n" + "="*60)
print("🚀 Black & White AI Application Starting...")
print("="*60)
print("\n⚡ IMPORTANT: For video uploads, use the LOCAL URL for much faster uploads!")
print("   Local URL will be shown below (e.g., http://127.0.0.1:7860)")
print("\n" + "="*60 + "\n")

ai_app_interface.launch(
    share=True,
    server_name="0.0.0.0",
    server_port=7860,
    show_error=True
)
