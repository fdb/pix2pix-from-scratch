import os
from glob import glob
from venv import create
from PIL import Image, ImageOps
import argparse

def ensure_directory(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != 17:
            raise e

def create_border(input_dir, output_dir, border_size=64, glob_pattern='*.jpg'):
    ensure_directory(output_dir)
    in_files = glob(os.path.join(input_dir, glob_pattern))
    for in_file in in_files:
        print(os.path.basename(in_file))
        new_img = Image.new('RGB', (1024, 512), (255, 255, 255))

        img = Image.open(in_file)
        # Crop the image to 512 x 512
        img = ImageOps.fit(img, (512, 512), Image.ANTIALIAS)
        #img.thumbnail((512, 512))
        new_img.paste(img, (0, 0))

        img = img.crop((border_size, border_size, 512-border_size, 512-border_size))
        new_img.paste(img, (512 + border_size, border_size))

        out_file = os.path.join(output_dir, os.path.basename(in_file))
        new_img.save(out_file)



if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Remove a border from the image')
    parser.add_argument('input_dir', help='The input directory')
    parser.add_argument('output_dir', help='The output directory')
    parser.add_argument('--size', dest='border_size', type=int, default=64, help='Size of the border')
    args = parser.parse_args()
    create_border(args.input_dir, args.output_dir, args.border_size)
