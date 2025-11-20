# Blackandwhiteai<!--

 * @Author: SpenserCai

**Black & White AI** - Restore and colorize old black & white photos and videos using AI. * @Date: 2023-07-28 14:35:35

 * @version:

![example](examples/demo.jpeg) * @LastEditors: SpenserCai

 * @LastEditTime: 2023-08-28 01:05:53

## About * @Description: file content

-->

This application uses advanced AI technology to bring life back to old black and white photos and videos by automatically adding realistic colors. The tool provides an easy-to-use web interface for processing your media files.

<p align="center">

## Features  <a href="https://nonebot.dev/"><img src="./examples/logo.png" width="200" height="200" alt="nonebot"></a>

</p>

- 🖼️ **Image Processing** - Colorize black & white photos with adjustable render quality

- 🎬 **Video Processing** - Colorize entire videos frame by frame<div align="center">

- 🎨 **Artistic Mode** - Toggle between stable and artistic colorization styles

- ⚡ **Fast Processing** - Optimized for performance with GPU support# Black & White AI for Stable Diffusion WebUI

- 🌐 **Web Interface** - User-friendly Gradio-based web UI

<a href="https://discord.gg/rfU5FQATtv">

## Installation  <img src="https://discordapp.com/api/guilds/1138404797364580415/widget.png?style=shield" alt="Discord Server">

</a>

### Prerequisites  <a href="https://qun.qq.com/qqweb/qunpro/share?_wv=3&_wwv=128&appChannel=share&inviteCode=21gXfxbmZLJ&businessType=7&from=181074&biz=ka">

    <img src="https://img.shields.io/badge/QQ%E9%A2%91%E9%81%93-SD%20WEBUI%20DEOLDIFY-5492ff?style=flat-square" alt="QQ Channel">

- Python 3.8 or higher  </a>

- CUDA-compatible GPU (recommended for faster processing)

- FFmpeg (for video processing)This is an extension for StableDiffusion's [AUTOMATIC1111 web-ui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) that provides tools to restore and colorize old black & white photos and videos using AI. It is based on [DeOldify](https://github.com/jantic/DeOldify).



### Setup</div>



1. Clone this repository:![example](examples/demo.jpeg)

```bash

git clone https://github.com/Hrushi124/Blackandwhiteai.git<!--加粗字体：News-->

cd Blackandwhiteai

```## News



2. Install dependencies:### - 2023-08-12：The DeoldifyBot is open source, you can deploy it yourself.

```bash

python setup.py### - 2023-08-11：The DeoldifyBot is onlined.You can colorize old photo in [Discord](https://discord.gg/rfU5FQATtv).

```

### - 2023-08-07：Support video colorization.

3. Run the application:

```bash### - 2023-08-05：Support install from Extensions list.

python app_complete.py

```### - 2023-08-04：sd-webui-deoldify released.



4. Open your browser and navigate to the local URL shown in the terminal (typically `http://localhost:7860`)## Compatibility



## Usage### OS



### Image Colorization<!--制作一个表格显示操作系统的兼容性，Windows不确定，linux兼容-->



1. Navigate to the "Image — B&W AI" tab|     OS     | Compatibility |                      Remark                       |

2. Upload your black & white image| :--------: | :-----------: | :-----------------------------------------------: |

3. Adjust the render factor (1-50) - higher values give better quality but take longer| Windows 11 |      ✅       | Thank for [@w-e-w](https://github.com/w-e-w) test |

4. Toggle "Artistic Mode" if desired|   Linux    |      ✅       |                                                   |

5. Click "Process Image"

6. Download your colorized image### Pytorch



### Video Colorization<!--制作一个表格显示Pytorch版本的兼容性-->



1. Navigate to the "Video — B&W AI" tab|          Version          | Compatibility |                          Remark                          |

2. Upload your black & white video (supports MP4, AVI, MOV, MKV)| :-----------------------: | :-----------: | :------------------------------------------------------: |

3. Set the render factor (1-40)|      <=1.13.1+cu117       |      ✅       |                                                          |

4. Click "Process Video"| 2.1.0.dev20230711+rocm5.5 |      ✅       | Thanks for [@fgtm2023](https://github.com/fgtm2023) test |

5. Wait for processing to complete (this may take several minutes)|        2.0.1+cu118        |      ✅       |    Thank for [@w-e-w](https://github.com/w-e-w) test     |

6. Download your colorized video

### Other

## Configuration

If you have tested other systems or Pytorch during use, please submit a PR and attach a screenshot of the successful operation. Thank you

- **Render Factor**: Controls the quality of colorization

  - Lower values (1-10): Faster but less detailed## Installation

  - Medium values (15-25): Balanced quality and speed

  - Higher values (30-50): Best quality but slower processingIn web-ui, go to the "Extensions" tab and use this URL https://github.com/SpenserCai/sd-webui-deoldify in the "install from URL" tab.



- **Artistic Mode**: Provides more vibrant and creative colorization compared to the stable mode2023-08-05：Support install from Extensions list！！！



## System RequirementsIf your network is not good, you can download the extension from [![Hugging Face Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-blue)](https://huggingface.co/spensercai/DeOldify)



- **Minimum**: 8GB RAM, 4GB GPU VRAM## Usage

- **Recommended**: 16GB RAM, 8GB+ GPU VRAM

- **Storage**: At least 5GB free space for models1. In web-ui, go to the "Extra" tab and select "DeOldify" checkbox.



## Troubleshooting2. Upload the old photo you want to colorize.



### Common Issues## Application Scenario



1. **Out of Memory Error**: Reduce the render factor or process smaller images/videosCombining Upscale, GFPGAN, and Denoldify for old photo restoration effects

2. **Slow Processing**: Ensure you have a CUDA-compatible GPU and drivers installed

3. **Video Upload Issues**: Check that FFmpeg is properly installed and in your PATH|                            Before                            |                           After                            |

| :----------------------------------------------------------: | :--------------------------------------------------------: |

## Contributing| <img src="examples/before.jpeg" alt="before" align=center /> | <img src="examples/after.jpeg" alt="after" align=center /> |



Contributions are welcome! Please feel free to submit issues or pull requests.## Video Colorization



## License<img src="examples/video_demo.gif" alt="video_demo" align=center />



This project is licensed under the MIT License - see the LICENSE file for details.<hr/>



## Acknowledgments### Usage



- Based on DeOldify technology```bash

- Built with Gradio for the web interfacesudo apt install ffmpeg

- Uses PyTorch for deep learning inference```



## ContactIn "DeOldify" tab, upload the video you want to colorize,set "Render Factor" and click "Run".



For questions or support, please open an issue on GitHub.## DeOldifyBot



---### Usage



Made with ❤️ by the Black & White AI team#### 1.Add [Discord](https://discord.gg/rfU5FQATtv) Server.


![DeoldifyBot](examples/discord.gif)

#### 2.Build your own DeOldifyBot

```bash
# Instal golang
# https://golang.org/doc/install

# Enter bot directory
cd bot
# Create release directory
mkdir release
# Build
bash build.sh
# create config.json
cp ./config.example ./release/config.json
# Edit config.json
# Set your discord bot token
# Set your sd-webui address

# Run
release/DeOldifyBot
```

## TODO

- [x] Support video colorization
- [x] Improve video processing speed
- [ ] Support repair options
- [ ] Support for simultaneous generation of images with different Render Factor values and Artistic on/off like “X/Y/Z Script” [#2](https://github.com/SpenserCai/sd-webui-deoldify/issues/2)
- [x] Support need not to add `--disable-safe-unpickle` at startup [#5](https://github.com/SpenserCai/sd-webui-deoldify/issues/5)
