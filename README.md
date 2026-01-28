# icon_banner_generator
Adds banners to app icon
Original icon should be 512x512 pixels.

1. save the icon without a banner as assets/icons/icon.png (or change the code to point to your preffered location)
2. run `python3 icon_banner_generator.py`
3. the new icons will be generated in assets/icons.


Original image: 

<img src="assets/icons/icon.png" alt="Original image" width="100" />

Generated images:  

<img src="assets/icons/dev_icon.png" alt="Original image" width="100" /><img src="assets/icons/prod_icon.png" alt="Original image" width="100" /><img src="assets/icons/stg_icon.png" alt="Original image" width="100" />

## Get the project running
```bash
brew install python
python3 -m venv ~/icon_banner_env 
source ~/icon_banner_env/bin/activate
pip install pillow 
python3 icon_banner_generator.py    
```
