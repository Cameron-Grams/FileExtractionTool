import argparse
import re


def clean_file(output_compare, base, student_file):
    output = []

    regex_pattern = r"(\S+).py"
    student_object = re.match(regex_pattern, student_file)
    student_title = student_object[1] 

    with open(base, "r") as file_1:
        base_lines = file_1.readlines()

    with open(f"./py_/{student_file}", "r") as file_2:
        student_lines = file_2.readlines()

    for line_ in student_lines:
        if line_ not in base_lines:
            output.append(line_)

    with open(f"./{output_compare}/{student_title}.py", 'w') as out_file:
        for out_line in output:
            out_file.write(out_line)

    return out_file

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('base_file', help='First file is the original')
    parser.add_argument('student_file', help='Second file is the student work')

    args = parser.parse_args()

    clean_file(args.base_file, args.student_file)
