# Download the image from script
wget $(random_splash.py) -O ~/Pictures/current.jpg -q 

# Set the background using feh
feh --bg-fill ~/Pictures/current.jpg
