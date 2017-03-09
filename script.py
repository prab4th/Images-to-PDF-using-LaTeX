import os
from os import listdir
from os.path import isfile, join

dir = str(os.path.realpath(__file__))[:-9]
onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]

for x in sorted(onlyfiles):
    print(x)

print(onlyfiles)
with open('1.tex', 'w',) as a:
    a.write("")    

with open('1.tex', 'a', encoding='utf-8') as w:
    w.writelines("""\\documentclass[a4paper]{slides}
\\usepackage{graphicx}
\\usepackage[margin=0.51cm]{geometry}
\\begin{document}
    \\title{BT4007}
    \\maketitle""")
    for item in onlyfiles:
        if item[-3:] == 'peg':
            w.writelines("""
        \\begin{slide}
            \\includegraphics[width=\\textwidth, height=\\textheight] {%s}
        \\end{slide}""" % item)

    w.write("""
\\end{document}""")
