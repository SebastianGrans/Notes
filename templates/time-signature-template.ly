

\version "2.20.0"
\paper {
    indent=0\mm
    paper-width = 65\mm % Minimum width to fit c-flat key signature
    paper-height = 45\mm
    right-margin = 0 % Paper margin sometimes limits staff length.
    left-margin = 0
    oddFooterMarkup=##f
    oddHeaderMarkup=##f
    bookTitleMarkup = ##f
    scoreTitleMarkup = ##f
    top-system-spacing = #'((space . 4) (padding . 4) (stretchability . 1)) 
}

\markup { % For centering
  \fill-line { % For centering 
    \score {
      {
        \clef bass
        \key <KEY_PLACEHOLDER>
        \repeat unfold 1 { s1 * <WIDTH_PLACEHOLDER> \break }
        % bes'
      }
      \layout {
        #(layout-set-staff-size 50)
        indent = 0\in
        \context {
          \Staff
          \remove "Time_signature_engraver"
          \remove "Bar_engraver"
          \override Clef.space-alist.key-signature = #'(minimum-space . 9)
        }
        \context {
          \Score
          \remove "Bar_number_engraver"
        }
      }
    }
  }
}