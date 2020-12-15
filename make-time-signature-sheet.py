#!/usr/bin/python3
import os
import subprocess

## Settings
# Treble or bass clef
TREBLE = True
# If this is set to true, you flip the card up or down (⇅) to see the answer. 
# This felt more natural to me.
FLIP_UP = True


## Only edit settings below if you now what you're doing, 
# or if you wanna play :) 

latex_template    = 'templates/flashcards-template.tex'
lilypond_template = 'templates/time-signature-template.ly'

tmp_folder = 'tmp_output/'
lilypond_output = tmp_folder + '{}.ly'
latex_output = tmp_folder + 'flashcards.tex'

pdf_output = ('treble' if TREBLE else 'bass') \
            + '-key-sign-sheet-' \
            + ('flipud' if FLIP_UP else 'fliplr') \
            + '.pdf'

if not os.path.exists(tmp_folder):
    os.mkdir(tmp_folder)

## Key signatures 

## With sharp
# Major  | Minor key  |# of flats  |  Sharp notes
#   C    |  A         |   0        |  
#   G    |  E         |   1        |  F♯
#   D    |  B         |   2        |  F♯, C♯
#   A    |  F♯        |   3        |  F♯, C♯, G♯
#   E    |  C♯        |   4        |  F♯, C♯, G♯, D♯
#   B    |  G♯        |   5        |  F♯, C♯, G♯, D♯, A♯
#   F♯   |  D♯        |   6        |  F♯, C♯, G♯, D♯, A♯, E♯
#   C♯   |  A♯        |   7        |  F♯, C♯, G♯, D♯, A♯, E♯, B♯

l_sharp = [ # (major, minor, # of accidentals)
    ('c',   'a',   0), # We can probably skip c major and a minor..
    ('g', 'e',  1),
    ('d', 'b',  2),
    ('a', 'fis', 3),
    ('e', 'cis', 4),
    ('b', 'gis', 5),
    ('fis', 'dis', 6),
    ('cis', 'ais', 7),
]

## With flat
# Major  | Minor key  |# of flats  |  Flat notes
#   C    |  A         |   0        |  
#   F    |  D         |   1        |  B♭
#   B♭   |  G         |   2        |  B♭, E♭
#   E♭   |  C         |   3        |  B♭, E♭, A♭
#   A♭   |  F         |   4        |  B♭, E♭, A♭, D♭
#   D♭   |  B♭        |   5        |  B♭, E♭, A♭, D♭, G♭
#   G♭   |  E♭        |   6        |  B♭, E♭, A♭, D♭, G♭, C♭
#   C♭   |  A♭        |   7        |  B♭, E♭, A♭, D♭, G♭, C♭, F♭

l_flat = [ # (major, as_string, minor, as_string, # of accidentals)
    ('c',   'a',   0),
    ('f',   'd',  1),
    ('bes',  'g',  2),
    ('ees',  'c',  3),
    ('aes',  'f',  4),
    ('des',  'bes', 5),
    ('ges',  'ees', 6),
    ('ces',  'aes', 7),
]

width = {
    0: 3,
    1: 3,
    2: 4,
    3: 4,
    4: 4,
    5: 5,
    6: 5,
    7: 6
}

f = open(lilypond_template, 'r')
template_string = f.read()
f.close()
clef = ('treble' if TREBLE else 'bass')

for el in l_flat + l_sharp:
    major_key, minor_key, n_of_accidentals = el
    w = width[n_of_accidentals]

    key_string = major_key + ' \\major'
    
    template_string = template_string.replace('<CLEF_PLACEHOLDER>', clef)
    major_string = template_string.replace('<KEY_PLACEHOLDER>', key_string)
    major_string = major_string.replace('<WIDTH_PLACEHOLDER>', str(w))
    

    # key_string = minor_key + ' \\minor'
    # minor_string = template_string.replace('<KEY_PLACEHOLDER>', key_string)
    # minor_string = minor_string.replace('<WIDTH_PLACEHOLDER>', str(w))

    major_file_name = lilypond_output.format(major_key+'-major')
    # minor_file_name = lilypond_output.format(major_key+'-minor')

    f = open(major_file_name, 'w')
    f.write(major_string)
    f.close()

    cmd = 'lilypond -o {:s} {:s}'.format(tmp_folder+major_key+'-major', major_file_name)
    s = subprocess.run(cmd, shell=True)

    # f = open(minor_file_name, 'w')
    # f.write(minor_string)
    # f.close()

    # cmd = 'lilypond -o {:s} {:s}'.format(folder+minor_key+'-minor', minor_file_name)
    # s = subprocess.run(cmd, shell=True)

print("Done writing lilypond files.")

## Example output
# front: pdf
# back: note, sharp/flat, major/minor
# note, sharp, flat, major/minor
# pdf
if FLIP_UP:
    latex_template_string = '\\card{{ \
\\includegraphics[width=.25\\linewidth]{{{:s}}}}}{{ \
\\Large \\bf {:s} {:s} {:s} / \
{:s} {:s} {:s} \\\\ \
\\rotatebox[origin=c]{{180}}{{ \\includegraphics[width=.25\linewidth]{{{:s}}} }} \
}} \n'
else:
    latex_template_string = '\\card{{ \
\\includegraphics[width=.25\\linewidth]{{{:s}}}}}{{ \
\\Large \\bf {:s} {:s} {:s} / \
{:s} {:s} {:s} \\\\ \
\\includegraphics[width=.25\linewidth]{{{:s}}} \
}} \n'

def decode_note(note):
    if len(note) == 1:
        return (note.upper(), ' ')
    else:
        if note[-2:] == 'is':
            return (note[0].upper(), '\\hspace{-0.5em} $\\sharp$')
        elif note[-2:] == 'es':
            return (note[0].upper(), '\\hspace{-0.5em} $\\flat$')
    
    return "ERROR"

lines = ""
for el in l_flat + l_sharp:

    major, minor, _ = el
    file_name = major+'-major.pdf'
    maj_note, maj_accidental = decode_note(major)
    min_note, min_accidental = decode_note(minor)

    add_line = latex_template_string.format(
        file_name,
        maj_note, maj_accidental, 'major',
        min_note, min_accidental, 'minor',
        file_name
    )
    # Inside the template, we replace the placeholder string with the new one
    lines += add_line

f = open(latex_template, 'r')
template_string = f.read()
f.close()

output_string = template_string.replace('<PLACEHOLDER>', lines)

f = open(latex_output, 'w')
f.write(output_string)
f.close()

os.chdir(tmp_folder) # lilypond CLI seems to be broken.
os.system('pdflatex flashcards.tex')
os.system('cp flashcards.pdf ../' + pdf_output)
os.chdir('..') 
print("\n\nOutput file is {:s}. \nNow safe to delete {:s} folder.".format(pdf_output, tmp_folder))