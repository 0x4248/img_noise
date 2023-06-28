# Img noise
# A python script to add noise to images.
# Github: https://www.github.com/aweomelewis2007/img_noise
# Licence: GNU General Public License v3.0
# By: Lewis Evans

import argparse
import imgnoise
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Add noise to a image')
    parser.add_argument('--input', '-i', help='input file')
    parser.add_argument('--output', '-o', help='output file')
    parser.add_argument('--noise', '-n', help='noise type (brightness or colour)')
    args = parser.parse_args()

    if args.input is None:
        print('Please specify an input file')
        exit()

    if args.output is None:
        print('Please specify an output file')
        exit()
    
    if os.path.isfile(args.input) is False:
        print('Input file does not exist')
        exit()
    
    if args.noise == 'brightness':
        imgnoise.brightness(args.input, args.output)
    elif args.noise == 'colour':
        imgnoise.colour(args.input, args.output)
    else:
        imgnoise.colour(args.input, args.output)