import os
import shutil
import argparse

from output_dir import build_output_dir
from copy_student_files import copy_student_file

def main(args_source_dir, args_output_dir):
    files = os.listdir(args_source_dir)
    for file in files:
        copy_student_file(file, args_source_dir, args_output_dir)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('source_dir', help='First specify the source directory for files')
    parser.add_argument('output_dir', help='Second name the output directory which has not been created')

    args = parser.parse_args()

    build_output_dir(args.output_dir)
    main(args.source_dir, args.output_dir)
