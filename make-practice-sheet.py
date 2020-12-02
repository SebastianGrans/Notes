#!/usr/bin/python3
import os
import subprocess

import numpy as np

lilypond_template = 'templates/practice-sheet-template.ly'

folder = 'output/'

if not os.path.exists('output'):
    os.mkdir('output')

treble_set = ['a', 'b', \
            'c\'', 'd\'', 'e\'', 'f\'', 'g\'', 'a\'', 'b\'', \
            'c\'\'', 'd\'\'', 'e\'\'', 'f\'\'', 'g\'\'', 'a\'\'', 'b\'\'', \
            'c\'\'\'']

treble_set_str = ['A3', 'B3', \
            'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', \
            'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', \
            'C6']



bass_set = ['c,', 'd,', 'e,', 'f,', 'g,', 'a,', 'b,', \
            'c', 'd', 'e', 'f', 'g', 'a', 'b', \
            'c\'', 'd\'', 'e\'']
            
bass_set_str = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', \
            'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', \
            'C4', 'D4', 'E4']


def to_ly_string(s):
    '''
        Converts a note, e.g. 'c4' to

        \markup{C \hspace #-0.5 \sub{4}}
    '''
    template = '\\markup{{{:1s} \\hspace #-0.5 \\sub{{{:1s}}} }}' 
    return template.format(s[0], s[1])


treble_notes_idxs = np.random.choice(range(len(treble_set)), size=80)
treble_notes = [treble_set[i] for i in treble_notes_idxs]
treble_notes_str = [to_ly_string(treble_set_str[i]) for i in treble_notes_idxs]


bass_notes_idxs = np.random.choice(range(len(bass_set)), size=80)
bass_notes = [bass_set[i] for i in bass_notes_idxs]
bass_notes_str = [to_ly_string(bass_set_str[i]) for i in bass_notes_idxs]

f = open(lilypond_template, 'r')
ly_template_string = f.read()
f.close()

output_ly = None

# Inside the template, we replace the placeholder string with the new one
ns = ly_template_string.replace('<TREBLE_NOTES>', ' '.join(treble_notes))
ns = ns.replace('<TREBLE_NOTES_STR>', ' '.join(treble_notes_str))
ns = ns.replace('<BASS_NOTES>', ' '.join(bass_notes))
ns = ns.replace('<BASS_NOTES_STR>', ' '.join(bass_notes_str))

# Write to file.
file_name = folder + 'practice-sheet.ly'
f = open(file_name, 'w')
f.write(ns)
f.close()


#cmd = 'lilypond -o {:s} {:s}'.format(folder+note_s, file_name)
#s = subprocess.run(cmd, shell=True)


#os.system('cp practice-sheet.pdf ..')
print("\n\nOutput file is " + file_name + "\nNow safe to delete 'output' folder.")
