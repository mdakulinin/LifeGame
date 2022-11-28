import sys
import argparse

def Parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-g', '--genome_size', default='16')

    return parser
