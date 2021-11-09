import os
import shutil
import argparse

def build_output_dir(output_dir):
    try:
        os.mkdir(output_dir)
    except FileExistsError as exec:
        print("Choose another output file name")
        print(exec)


def copy_student_file(student, source_dir, output_dir):
    student_path = f"./{source_dir}/{student}"
    student_files = os.listdir(student_path)
    last_dir = max(student_files)
    file_string = f"{student_path}/{last_dir}/Msnj0"
    last_file = os.listdir(file_string)
    last_file = last_file[0]
    src = file_string + '/' + last_file
    dst = f"./{output_dir}/{student}_"
    shutil.copy(src, dst)


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
