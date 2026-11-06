# Alpha carry arithmetic preregistration

Pinned parent: `749931f0f357c60ef4e21879d96b0306999f428f` (#518).
Written before running this front's experiments. All inherited samples are developmental.

**Candidate AC-01:** positivity and the exact four-pole bound `0<r(n)<1/n^2`
for `n>=2` force a logarithmic exclusion interval after each forcing-induced
macro-carry correction. For fixed macro length m, this bounds the number of
corrections in `[A,2A)` by `m ceil(A/(m L))`, where
`L=floor(log_(16^m)(15(A+1)^2))>=1`. This is proposed for *every real seed*,
so it is explicitly not a class-A source-selection estimate.

**Candidate AC-02:** the actual cell label and accumulated literal m-step
carry (reduced modulo `16^m`) disagree at precisely the correction times;
their empirical pressures differ by at most `2*16^m*E/A`. This is an exact
transport with vanishing fixed-m error, not a simpler normality obligation.

**Candidate falsifier AC-F:** `E=0` or `E=o(A)` might force bounded pressure.
Coherent and nearby periodic same-forcing completions are predicted to kill
this implication. It is not our positive conjecture.

Fresh exact epochs: A=125,257,521; observer depths m=1,2,3. A=521 is larger
than this parent front's A=384. These are not claimed fresh relative to every
uninspected historical SUCC file, only this preregistered round. Additional
mechanism-favoring sample: A=37,m=3; the bound may be inapplicable and must
return DARK rather than silently extending its domain.

Controls: original zero seed; same source rational seed 1/5; coherent source
completion `-T_n`; nearest p=11 periodic completion; unforced zero; an exact
source mutation `r_mut(n)=2*r(n)` with literal zero seed. Controls using T_n
must be certified with exact rational tail intervals, not approximate pi.
Expected result: original and mutant pressure are finite diagnostics, coherent
pressure is exactly `16^m`, periodic pressure stays large despite eventually
zero corrections. Reject any asymptotic promotion from these samples.

Independent implementations: four signed Fraction poles/unwrapped recurrence
versus reduced rational polynomial and modulo-one recurrence. Preserve literal
carry and state hashes. Verify all actual macro transitions against the direct
unwrapped difference. No thousands-of-states sweep beyond n=1045; no full suite.
