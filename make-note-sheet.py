#!/usr/bin/python3
import os
import subprocess
import time


latex_template    = 'templates/flashcards-template.tex'
lilypond_template = 'templates/note-template.ly'

folder = 'output/'
lilypond_output = folder + '{}.ly'
latex_output = folder + 'flashcards.tex'

if not os.path.exists('output'):
    os.mkdir('output')

# Treble
# notes_s = ['c4','d4', 'e4','f4', 'g4', 'a4', 'b4', \
#          'c5','d5', 'e5','f5', 'g5', 'a5']
# clef_ly = '\\clef treble'
# notes_ly = ['c\'','d\'', 'e\'','f\'', 'g\'', 'a\'', 'b\'', \
#          'c\'\'','d\'\'', 'e\'\'','f\'\'', 'g\'\'', 'a\'\'']

# Bass
notes_s = ['e2', 'f2', 'g2', 'a2', 'b2', 'c3', 'd3', 'e3', \
        'f3', 'g3', 'a3', 'b3', 'c4']
clef_ly = '\\clef bass'
notes_ly = ['e,', 'f,', 'g,', 'a,', 'b,', 'c','d', 'e', \
        'f', 'g', 'a', 'b', 'c\'']

f = open(lilypond_template, 'r')
ly_template_string = f.read()
f.close()

output_ly = None

# Generate all the .ly files

# This template defines the clef, if easy heads should be used and 
# which note to use.
add_line_template = '{:s} {:s} {:s}'
for note_s, note_ly  in zip(notes_s, notes_ly):

    # We generate the strings we wish to insert into the template
    # \clef bass \easyHeadsOn c' s1
    add_line = add_line_template.format(clef_ly, '', note_ly)
    add_line_answer = add_line_template.format(clef_ly, '\easyHeadsOn', note_ly)

    # Inside the template, we replace the placeholder string with the new one
    ns = ly_template_string.replace('<PLACEHOLDER>', add_line)
    ns_answer = ly_template_string.replace('<PLACEHOLDER>', add_line_answer)

    # Write to file.
    file_name = lilypond_output.format(note_s)
    f = open(file_name, 'w')
    f.write(ns)
    f.close()

    
    cmd = 'lilypond -o {:s} {:s}'.format(folder+note_s, file_name)
    s = subprocess.run(cmd, shell=True)
    
    # With easyHeads
    file_name = lilypond_output.format(note_s + '-ans')
    f = open(file_name, 'w')
    f.write(ns_answer)
    f.close()
    
    cmd = 'lilypond -o {:s} {:s}'.format(folder+note_s+'-ans', file_name)
    s = subprocess.run(cmd, shell=True)

    



# Compile to pdf using lilypond
# os.chdir('output/') # lilypond CLI seems to be broken.
# # os.system('lilypond *.ly')
# import subprocess 
# s = subprocess.run('lilypond *.ly', shell=True)
# os.chdir('..') 

# Now we simply have to add it to the latex template
lines = ""
add_line_template = '\\card{{ \\includegraphics[width=.20\\linewidth]{{{:s}}} }}{{ \\includegraphics[width=.20\\linewidth]{{{:s}}} }} \n'
for note_s  in notes_s:

    # We generate the strings we wish to insert into the template
    # \clef bass \easyHeadsOn c' s1
    add_line = add_line_template.format(note_s+ '.pdf', note_s+ '-ans.pdf')

    # Inside the template, we replace the placeholder string with the new one
    lines += add_line


f = open(latex_template, 'r')
latex_template_string = f.read()
f.close()

ns = latex_template_string.replace('<PLACEHOLDER>', lines)

# Write to file.
f = open(latex_output, 'w')
f.write(ns)
f.close()

os.chdir('output/') # lilypond CLI seems to be broken.
os.system('pdflatex flashcards.tex')
os.system('cp flashcards.pdf ..')
os.chdir('..') 
print("\n\nOutput file is 'flashcard.pdf'. \nNow safe to delete 'output' folder.")
