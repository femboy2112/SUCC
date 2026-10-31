# Retained initial oracle failure

The first `independent_oracle.py` run exited 1 at its denominator positivity
assertion. It incorrectly required **all** polynomial coefficients to be
strictly positive. The exact denominator contains a power of `a`, hence
has zero trailing coefficients while remaining strictly positive for a>0.

The assertion was corrected to every coefficient nonnegative and at least
one coefficient positive. The separate numerator test remains strictly
positive coefficients. This was an overly strict implementation assertion,
not a failure of the source derivative sign theorem. The original failed
execution was observed before the corrected replay, and is not counted as
a pass.
