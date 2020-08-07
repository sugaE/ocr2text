import os
from glob import glob
# from images2pdf import folder_output

folder_output = "txt"


# filenames = ['file1.txt', 'file2.txt', ...]
filenames = sorted(glob(os.path.join(folder_output, '*')))
print("reading txt:")
print(filenames)

with open(os.path.join(folder_output, 'combine.txt'), 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            # for line in infile:
            #     outfile.write(line)
            outfile.write(infile.read())
        outfile.write('\n\n\n')
