\version "2.22.1"

#(set-default-paper-size "a4")
#(set-global-staff-size 35)
\paper {
    % indent=10\mm
    % paper-width = 115\mm % Minimum width to fit c-flat key signature
    paper-height =65\mm
    % right-margin = 0 % Paper margin sometimes limits staff length.
    % left-margin = 0
    oddFooterMarkup=##f
    oddHeaderMarkup=##f
    % bookTitleMarkup = ##f
    % scoreTitleMarkup = ##f
    % top-system-spacing = #'((space . 4) (padding . 4) (stretchability . 1)) 
}

% \header {
%     % Do not display the default LilyPond footer for this book
%     tagline = ##f
% }

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
                    \relative {
                        \easyHeadsOn
                        a b c d e f g a b c d e f g a b
                    } 
                }
            } 

            \new Staff = lower 
            {
                \new Voice = "lower" {
                    \clef bass
                    \time 4/4
                    \relative {
                        \easyHeadsOn
                        c, d e f g a b c d e f g a b c d
                    } 
                }
            }  
        >>
}   
