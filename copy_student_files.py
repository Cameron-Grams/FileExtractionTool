import os
import shutil

"""
copies the most recent attempt assignment file from the student's directory to the 
output directory
"""

def copy_student_file(student, source_dir, output_dir):
    student_path = f"./{source_dir}/{student}"
    student_files = os.listdir(student_path)
    last_dir = max(student_files)

    # add generalized final folder for automated output
    automated_path = f"{student_path}/{last_dir}"
    automated_dir = os.listdir(automated_path)

    file_string = f"{automated_path}/{automated_dir[0]}"
    last_file = os.listdir(file_string)
    last_file = last_file[0]
    src = file_string + '/' + last_file
    dst = f"./{output_dir}/{student}_"
    shutil.copy(src, dst)
