import sys
import argparse
import pathlib

from . import parsing
from . import processing

__version__ = "0.1.0"

def my_print(val):
    print(type(val), val, sep=": ")

def parse():
    parser = argparse.ArgumentParser(description='parsing text file and make data dump files')
    parser.add_argument('input_path', type=pathlib.Path,
                        help='file to read')
    parser.add_argument('pool_dump_path', type=pathlib.Path,
                        help='path to pool dump file')
    parser.add_argument('sentences_dump_path', type=pathlib.Path,
                        help='path to sentences dump file')
    parser.add_argument('-f', '--force', action="store_true",
                        help='allow this command to overwrite files')

    args = parser.parse_args()

    input_path = args.input_path
    pool_path = args.pool_dump_path
    sentences_path = args.sentences_dump_path
    force = args.force

    parsing.parse_text_and_dump_data(input_path, pool_path, sentences_path, force=force)

def process():
    parser = argparse.ArgumentParser(description='process word salads using specified dumpfile')

    parser.add_argument('pool_dump_path', type=pathlib.Path,
                        help='path of used pool dump file')
    parser.add_argument('sentences_dump_path', type=pathlib.Path,
                        help='path of used sentences dump file')

    args = parser.parse_args()

    pool_path = args.pool_dump_path
    sentences_path = args.sentences_dump_path

    for sentence in processing.process_sentences_from_dump(pool_path, sentences_path):
        print(sentence)
