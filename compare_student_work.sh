#!/bin/sh

python extract_files.py student_files output

mkdir py_

cd output
jupyter nbconvert * --to script

mv *.py ../py_

cd ..

python filter_full_files.py base.py student_comparison

rm -rf output
rm -rf py_

mv moss ./student_comparison

cd student_comparison

./moss -l python *.py

mv moss .. && cd ..
