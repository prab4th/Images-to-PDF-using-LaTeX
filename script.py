import os
from os import listdir
from os.path import isfile, join

dir = str(os.path.realpath(__file__))[:-9]
onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]


import re

n = 0
pic_files = list()

for f in onlyfiles:
    if '_' in f:
        pic_files.append(f)

sorted_files = sorted(pic_files, key = lambda k: int(k.split('_')[1].split('.')[0]))

with open('1.tex', 'w',) as a:
    a.write("")    

with open('1.tex', 'a', encoding='utf-8') as w:
    w.writelines("""\\documentclass[a4paper]{slides}
\\usepackage{graphicx}
\\usepackage[margin=0.51cm]{geometry}
\\begin{document}
    \\title{BT4007}
    \\maketitle""")
    for item in sorted_files:
        if item[-3:] == 'peg' or item[-3:] == 'jpg':
            w.writelines("""
        \\begin{slide}
            \\includegraphics[width=\\textwidth, height=\\textheight] {%s}
        \\end{slide}""" % item)

    w.write("""
\\end{document}""")
