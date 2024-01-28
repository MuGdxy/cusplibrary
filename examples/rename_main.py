# go through all the files in this directory
# rename `int main(void)` to `TEST_CASE("$FILENAME", "[$FOLDERNAME]")`
# remove `return 0;`

import os
import re

def process_file(path, file_name, folder):
    with open(path, 'r') as f:
        lines = f.readlines()
    
    need_include = True
    for line in lines:
        if line.startswith('#include <catch.hpp>'):
            need_include = False

    with open(path, 'w') as f:
        if need_include:
            f.write('#include <catch.hpp>\n')

        for line in lines:
            if line.startswith('int main(void)'):
                f.write('TEST_CASE("' + file_name + '", "[' + folder + ']")\n')
            elif line.find('return 0;') != -1:
                continue
            else:
                f.write(line)

#process_file("Algorithms/blas.cu", "blas", "Algorithms")

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".cu"):
            print(f"find path={os.path.join(root, file)}, file={file}, folder={root[2:]}")
            filename_no_ext = os.path.splitext(file)[0]
            print(f"filename_no_ext={filename_no_ext}")
            process_file(os.path.join(root, file), filename_no_ext, root[2:])