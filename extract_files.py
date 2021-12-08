import os
import shutil
import argparse

from create_dir import create_dir
from copy_student_files import copy_student_file

def main(args_source_dir, args_output_dir):
    files = os.listdir(args_source_dir)
    # build student profiles will need the full list of students in order to manage the collective record
    # will need class number and assignment number as arguments
    for file in files:
        copy_student_file(file, args_source_dir, args_output_dir)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    # add class number
    # add assignment number
    parser.add_argument('source_dir', help='First specify the source directory for files')
    parser.add_argument('output_dir', help='Second name the output directory which has not been created')

    args = parser.parse_args()

# output dir is an internal directory for managing converstion from notebook to .py
    create_dir(args.output_dir)
    main(args.source_dir, args.output_dir)
