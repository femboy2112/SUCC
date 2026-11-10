# Equivalent carry-stream implementation

After the development receipts at `627f8644`, the first A22003 holdout run
was interrupted (exit130) before it emitted a source receipt or any phase
result. Its bottleneck was repeated division of the full exponentially
growing unwrapped numerator. No held-out result selected the change.

The replacement keeps that numerator and its exact hash, and computes its
remainder by the literal carry recurrence instead. If U=N/D=k+r/D, then

    N_next=16N+F,
    (c,r_next)=divmod(16r+F,D),
    k_next=16k+c.

Therefore divmod(N_next,D)=(k_next,r_next), exactly. The source, boundary,
unwrapped history and carry stream are unchanged. This is the same algebra
as the canonical integer carrier, with one common denominator fixed before
the run. No floating arithmetic or discarded carry is involved.

The complete source payloads at all three development selectors1103,2203,5501
were rebuilt with this implementation and compared as parsed JSON: every
phase interval, folded value, direct Weyl enclosure, principal-part check,
unwrapped hash and carry hash was identical to the committed receipts.
The pre-change direct reduced-Fraction review of A1103/2203 remains evidence
for those identical source payloads, while its old code hash stays historical.

The held-out run is restarted once with this equivalent implementation.
Its own result records the actual new code hashes. Historical development
receipt metadata is preserved; mathematical payload replay compares metadata
separately from numerical data.
