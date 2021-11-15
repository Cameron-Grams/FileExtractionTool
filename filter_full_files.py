import os
import shutil
import argparse

from output_dir import build_output_dir
from clean_file import clean_file

def filter_student_files(output_compare, base):
    student_files = os.listdir('./py_')

    for file in student_files:
        clean_file(output_compare, base, file)

    print("Filter complete")

    return None


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('base', help='First specify the name of the file to compare to')
    parser.add_argument('output_dir', help='Second name the output directory for filered files')

    args = parser.parse_args()

    build_output_dir(args.output_dir)
    filter_student_files(args.output_dir, args.base)
