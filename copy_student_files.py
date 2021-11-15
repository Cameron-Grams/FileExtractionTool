import os
import shutil

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
