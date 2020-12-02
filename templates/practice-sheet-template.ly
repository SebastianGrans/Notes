\version "2.20.0"
#(set-default-paper-size "a4" 'landscape )
#(set-global-staff-size 28.5)
\paper {
    indent = #0
    oddHeaderMarkup = ##f
    evenHeaderMarkup = ##f
    oddFooterMarkup = ##f
    right-margin = #20 
    left-margin = #20 
}

upper =  {
    \clef treble
    \time 4/4

    <TREBLE_NOTES> % Insert 120 quarter notes here to fill a page.
}

upper_lyrics = \lyricmode {
    \override Lyrics.LyricText.font-shape = #'smallcaps
    \override Lyrics.LyricText.font-size = #-4
    <TREBLE_NOTES_STR>
}

lower =  {
    \clef bass
    \time 4/4


    <BASS_NOTES> % Insert 120 quarter notes here to fill a page.
}

lower_lyrics = \lyricmode {
    \override Lyrics.LyricText.font-shape = #'smallcaps
    \override Lyrics.LyricText.font-size = #-4
    <BASS_NOTES_STR>
}


\new Score \with 
{
    \remove Bar_number_engraver
}
{

    \new PianoStaff \with 
    { 
        \omit TimeSignature 
    }
        <<
            \new Staff = upper {
                \new Voice = "upper" \upper
            } 
            \new Lyrics \lyricsto "upper" {
                \upper_lyrics
            }
            \new Staff = lower 
            {
                \new Voice = "lower" \lower
            } 
            \new Lyrics \lyricsto "lower" {
                \lower_lyrics
            }
            
        >>
}
