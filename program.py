import subprocess
import urllib.request
import shutil
import sys

# Downloads a random image from source.unsplash.com and returns the filename.
def unsplash_image(category='random'):
    screen_resolution = get_screen_resolution()
    url = 'https://source.unsplash.com/{category}/{width}x{height}'.format(category=category, width=screen_resolution[0], height=screen_resolution[1])
    output_name = 'background.jpeg'
    with urllib.request.urlopen(url) as response, open(output_name, 'wb') as output_file:
        shutil.copyfileobj(response, output_file)
    return output_name

# Use feh to apply our wallpaper
def set_background(file_name):
    subprocess.call(['feh', '--bg-scale', file_name])

# Use themer to apply an appropriate theme
def apply_themer(background_image, theme_name):
    subprocess.call(['themer', '-a', 'generate', theme_name, background_image])

# Get our screen resolution from xrandr
def get_screen_resolution():
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[0].split(b'x')
    return (resolution[0].decode('UTF-8'), resolution[1].decode('UTF-8'))

def main(argv):
    if len(argv) > 0:
        print('Categories: building, food, nature, people, technology, objects')
        set_background(unsplash_image('category/{0}'.format(argv[0])))
    else:
        set_background(unsplash_image())

if __name__ == '__main__':
    main(sys.argv[1:])
