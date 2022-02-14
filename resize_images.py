import os
from glob import glob
from PIL import Image
import argparse

def ensure_directory(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != 17:
            raise e
            
def resize_images(input_dir, output_dir, desired_width, desired_height, ext):
    ensure_directory(output_dir)
    in_files = glob(os.path.join(input_dir, f'*.{ext}'))
    for in_file in in_files:
        print(os.path.basename(in_file))
        img = Image.open(in_file)
        img.thumbnail((desired_width, desired_height))
        fname = os.path.splitext(os.path.basename(in_file))[0]
        img.save(os.path.join(output_dir, fname + '.jpg'))


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Check if all images have the same size.')
    parser.add_argument('input_dir', help='The input directory')
    parser.add_argument('output_dir', help='The output directory')
    parser.add_argument('--width', dest='width', type=int, default=512, help='The width of the image')
    parser.add_argument('--height', dest='height', type=int, default=512, help='The height of the image')
    parser.add_argument('--ext', dest='ext', default='png', help='The image extension')
    args = parser.parse_args()
    resize_images(args.input_dir, args.output_dir, args.width, args.height, args.ext)
