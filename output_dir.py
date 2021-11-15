import os



def build_output_dir(output_dir):
    try:
        os.mkdir(output_dir)
    except FileExistsError as exec:
        print("Choose another output file name")
        print(exec)



