\version "2.20.0"
\paper {
    indent=0\mm 
    paper-width = 50\mm % Make output pdf smaller
    paper-height = 45\mm 
    oddFooterMarkup=##f % Remove "Made with lilypond footer"
}
\layout {
    #(layout-set-staff-size 50) % Increase the staff size
}
{   
    % Increase space between clef and first note.
    \once \override NoteColumn.X-offset = 3 
    \omit Staff.TimeSignature % Remove the TimeSignature
    c'
}