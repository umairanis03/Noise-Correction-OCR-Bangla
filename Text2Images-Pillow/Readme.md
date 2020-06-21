# Images formation using Pillow ImageDraw

- Issue: Pillow doesn't renders bangla text correctly

### Solution 1
- Follow [this](https://github.com/python-pillow/Pillow/issues/3593) issue to setup the environment correctly 
### Summary
- `sudo apt-get install libfreetype6-dev libharfbuzz-dev libfribidi-dev gtk-doc-tools`
- `then clone pillow git and go depends folder`
- Run `chmod +x install_raqm.sh`
- Run `./install_raqm.sh`
- `Uninstall your previous pillow version and install,`
- `conda install pillow=6.0.0`

### Solution 2 - Using Docker Image
- Go to `ImgGen` folder in the same directory to get the docker
- Use `text2img.py` inside this environment for drawing bangla text over Images
