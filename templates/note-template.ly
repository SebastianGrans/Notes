\version "2.20.0"
\paper {
    indent=0\mm
    paper-width = 50\mm
    paper-height = 45\mm
    oddFooterMarkup=##f
    oddHeaderMarkup=##f
    bookTitleMarkup = ##f
    scoreTitleMarkup = ##f
}

\score {
    \layout {
        #(layout-set-staff-size 50)
    }
    {   
        \omit Score.BarLine
        \omit Staff.TimeSignature 
        \once \override NoteColumn.X-offset = 3
        <PLACEHOLDER> s1
    }
}
