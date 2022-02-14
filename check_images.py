import os
from glob import glob
from PIL import Image
import argparse

def check_images(input_dir, desired_width, desired_height, ext):
    in_files = glob(os.path.join(input_dir, f'*.{ext}'))
    for in_file in in_files:
        print(os.path.basename(in_file))
        img = Image.open(in_file)
        if img.width != desired_width or img.height != desired_height:
            print(f'Image {in_file} is wrong size (is: {img.width}x{img.height} required: {desired_width}x{desired_height}')
        # To check that the image is valid we will resize it
        (w, h) = (img.width // 2, img.height // 2)
        img.resize((w, h))


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Check if all images have the same size.')
    parser.add_argument('input_dir', help='The input directory')
    parser.add_argument('--width', dest='width', type=int, default=512, help='The width of the image')
    parser.add_argument('--height', dest='height', type=int, default=512, help='The height of the image')
    parser.add_argument('--ext', dest='ext', default='png', help='The image extension')
    args = parser.parse_args()
    check_images(args.input_dir, args.width, args.height, args.ext)
