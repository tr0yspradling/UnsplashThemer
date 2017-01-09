import subprocess
import urllib.request
import shutil
import sys
import getopt

# Unsplash API Endpoints
unsplash = {}
unsplash['random'] = 'https://source.unsplash.com/random/{width}x{height}'

def unsplash_image():
    screen_resolution = get_screen_resolution()
    output_name = 'background.jpeg'
    url = unsplash['random'].format(height=screen_resolution[1], width=screen_resolution[0])
    with urllib.request.urlopen(url) as response, open(output_name, 'wb') as output_file:
        shutil.copyfileobj(response, output_file)
    apply_themer(output_name, 'main')

def apply_themer(background_image, theme_name):
    subprocess.call(['themer', '-a', 'generate', theme_name, background_image])

# Courtesy of Andrey Izman on StackOverflow
# http://stackoverflow.com/a/33713312/851230
def get_screen_resolution():
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[0].split(b'x')
    return (resolution[0].decode('UTF-8'), resolution[1].decode('UTF-8'))

unsplash_image()

