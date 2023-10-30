import ast
import os
import shutil
from task03 import task

# Task 03
print('****************  TASK 03 STARTED  *********************')

try:
    os.mkdir("tests/out/")
except:
    shutil.rmtree("tests/out/")
    os.mkdir("tests/out/")

all_files = []
for index in range(1, 6):
    file_name = "tests/in/test_" + str(index) + ".in"
    all_files.append(file_name)

index = 1
for file in all_files:
    with open(file) as f:
        lines = f.read()
    
    # convert to dictionary
    reg = ast.literal_eval(lines)
    result = task(reg)
    
    write_file = "tests/out/test_" + str(index) + ".out"
    g = open(write_file, "w+")
    g.write(str(result))
    g.close()

    index += 1

solved = 1
for test_case in range(1, 6):
    out_file = "tests/out/test_" + str(test_case) + ".out"
    ref_file = "tests/ref/test_" + str(test_case) + ".ref"

    out_content = open(out_file).readlines()
    ref_content = open(ref_file).readlines()

    if out_content == ref_content:
        print("TEST " + str(test_case) + " .............................. PASSED")
    else:
        solved = 0
        print("TEST " + str(test_case) + " .............................. FAILED")

if solved:
    print('**************** TASK 03 COMPLETED *********************')
else:
    print('******************* FAILED TESTS ***********************')

