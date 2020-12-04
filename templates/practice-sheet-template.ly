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

%%
% No heads sheet.
% 

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
                \new Voice = "upper" {
                    \clef treble
                    \time 4/4
                    \repeat unfold 40 { \hideNotes a c'''}
                }
            } 
            \new Lyrics \lyricsto "upper" {
                \lyricmode {
                    \override Lyrics.LyricText.font-shape = #'smallcaps
                    \override Lyrics.LyricText.font-size = #-4
                    <TREBLE_NOTES_STR>
                }
            }
            \new Staff = lower 
            {
                \new Voice = "lower" {
                    \clef bass
                    \time 4/4
                    \repeat unfold 40 { \hideNotes c, e' }
                }
            } 
            \new Lyrics \lyricsto "lower" {
                \lyricmode {
                    \override Lyrics.LyricText.font-shape = #'smallcaps
                    \override Lyrics.LyricText.font-size = #-4
                    <BASS_NOTES_STR>
                }
            }
            
        >>
}

%% 
% No names sheet
% 
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
                \new Voice = "upper" {
                    \clef treble
                    \time 4/4
                    <TREBLE_NOTES>
                }
            } 
            \new Lyrics \lyricsto "upper" {
                \lyricmode {
                    \override Lyrics.LyricText.font-shape = #'smallcaps
                    \override Lyrics.LyricText.font-size = #-4
                    % Hack to make them all the staff groups equally high of content.
                    \repeat unfold 80 { \markup{ \with-color #(x11-color 'white) "A" \sub{ \with-color #(x11-color 'white) 2}}}
                }
            }
            \new Staff = lower 
            {
                \new Voice = "lower" {
                    \clef bass
                    \time 4/4
                    <BASS_NOTES>
                }
            } 
            \new Lyrics \lyricsto "lower" {
                \lyricmode {
                    \override Lyrics.LyricText.font-shape = #'smallcaps
                    \override Lyrics.LyricText.font-size = #-4
                    \repeat unfold 80 { \markup{ \with-color #(x11-color 'white) "A" \sub{ \with-color #(x11-color 'white) 2}}}
                }
            }
            
        >>
}


%%
% Answer sheet
%

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
                \new Voice = "upper" {
                    \clef treble
                    \time 4/4
                    <TREBLE_NOTES>
                }
            } 
            \new Lyrics \lyricsto "upper" {
                \lyricmode {
                    \override Lyrics.LyricText.font-shape = #'smallcaps
                    \override Lyrics.LyricText.font-size = #-4
                    <TREBLE_NOTES_STR>
                }
            }
            \new Staff = lower 
            {
                \new Voice = "lower" {
                    \clef bass
                    \time 4/4
                    <BASS_NOTES>
                }
            } 
            \new Lyrics \lyricsto "lower" {
                \lyricmode {
                    \override Lyrics.LyricText.font-shape = #'smallcaps
                    \override Lyrics.LyricText.font-size = #-4
                    <BASS_NOTES_STR>
                }
            }
            
        >>
}