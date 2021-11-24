#!/bin/sh

# include the student files directory as second argument
python extract_files.py $2 output

mkdir py_

cd output
jupyter nbconvert * --to script

mv *.py ../py_

cd ..

# include the first argument as the base file for comparision
COMPARISON_FILES=student_comparison_$2
python filter_full_files.py $1 "$COMPARISON_FILES"

rm -rf output
rm -rf py_

mv moss ./$COMPARISON_FILES

cd $COMPARISON_FILES 

./moss -l python *.py

mv moss .. && cd ..
