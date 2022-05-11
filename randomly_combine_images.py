from PIL import Image
import os
from glob import glob
import argparse
from random import choice

def ensure_directory(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != 17:
            raise e


def combine_images(input_dir_first, input_dir_second, output_dir, amount, ext='jpg'):
    ensure_directory(output_dir)
    first_images = glob(os.path.join(input_dir_first, f'*.{ext}'))
    second_images = glob(os.path.join(input_dir_second, f'*.{ext}'))
    for i in range(amount):
        print(i)
        first_image = choice(first_images)
        second_image = choice(second_images)
        img_first = Image.open(first_image)
        img_second = Image.open(second_image)
        img_first.thumbnail((512, 512))
        img_second.thumbnail((512, 512))
        output_image = Image.new('RGB', (1024, 512))
        output_image.paste(img_first, (0, 0))
        output_image.paste(img_second, (512, 0))
        output_image_file = os.path.join(output_dir, f'{i:05}.jpg')
        output_image.save(output_image_file)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Check if all images have the same size.')
    parser.add_argument('input_dir_first', help='The first input directory')
    parser.add_argument('input_dir_second', help='The second input directory')
    parser.add_argument('output_dir', help='The output directory')
    parser.add_argument('--amount', help='The amount of random images to generate', type=int, default=5000)
    #parser.add_argument('--width', dest='width', type=int, default=512, help='The width of the image')
    ##parser.add_argument('--height', dest='height', type=int, default=512, help='The height of the image')
    #parser.add_argument('--ext', dest='ext', default='png', help='The image extension')
    args = parser.parse_args()
    combine_images(args.input_dir_first, args.input_dir_second, args.output_dir, args.amount)
