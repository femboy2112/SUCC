# Independent audit of the root complement-budget certificate

**Verdict: SURVIVES within the finite declared dictionary. No unresolved defect
found in the reviewed proof and execution. Pi normality remains OPEN.**

The source-code and result hashes actually reviewed are pinned in
[ROOT_REVIEW.json](ROOT_REVIEW.json). This review does not certify subsequent
unseen edits. The reviewer is a separate agent in the same model family and
workspace, not an external mathematical referee.

## Proof audit

For `<u,v>=mean conjugate(u)v`, `W=<r,B>`, and `u=B-Wr`, the root's
orthogonality and identity `<u,B>=E-|W|^2` are correct. The triangle estimate
uses `|u|<=1+|W|` and `|<u,phi>|<=(M+|W|)w`. Hence the stated lower bound
on `rho+weighted_nonresonant_cost` holds even for an unrestricted complex
retained resonance R. It is a method-cost bound, not a lower bound on W.

The outward scalar certificate uses E's lower endpoint and upper endpoints
for |W| and M. These substitutions decrease the nonnegative quotient, so the
rounding direction is valid. For the tested monomial menu, the degree1 slope
`-h` is exactly the omitted resonant atom. Degree2/3 with nonzero coefficient
has reduced degree2/3 after adding hX because d<m. The zero monomial atom is
retained once. No claim about all mixed-coefficient polynomials follows.

The complex Fourier sign is correct: scattering B at `x^d` and taking the
negative-sign DFT produces `<phi_(d,t),B>`. Multiplication by the local prime
phase gives the direct full source W, and the sampled resonant DFT value is
its expected orientation.

## FFT error audit

A butterfly's error decomposition `w(b-bc)+(w-wc)bc` pays `2R` for the first
term and `T|bc|_1` for the second. Adding the other input's radius gives3R;
two downward coordinate roundings cost less than2 integer units. Thus no
missing product-error cross term is needed in that particular decomposition.
The general product bound separately includes `R_A R_B`. Inverse scaling
rounds each coordinate and rounds the radius upward. Bluestein's signed
chirp identity and both placements of the difference kernel were checked
algebraically; N>=2p-1 prevents wrap aliasing. All computations are integer,
and the recorded common radius stays conservative rather than relying on
ambient floating precision.

## Executed independent bearing

`review_root.py` reconstructs the complete source intervals for A1103 and A2203 using
`SelectedOrbit`: a reduced Fraction at every time. The root instead uses one
global common denominator, unwrapped states, and streamed hashes. Both use
the same canonical four-pole source. The reviewer rebuilt3,290 source states,
3,290 folded values across h1/3, and four direct Weyl means; all matched the
root intervals.

Twelve complete FFT spectra were replayed and their hashes/radii matched. This
replay is repeatability, not algorithmic independence. For78 independently
summed coefficients, including every reported maximizing slope and the fixed
slopes0,1,7,p//2,p-1,-h, the **entire** direct interval rectangle fit inside
the FFT's L1 error ball. These sums bypass FFT, chirps, and convolution, but
reuse the outward phase primitive. All twelve final dual lower bounds were
recomputed with rational arithmetic. The command exited0:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
/tmp/succ-learning-yoneda-venv/bin/python \
  research/2026-11-08/complement_budget/resonance/review_root.py \
  --epochs 1103 2203 \
  --output research/2026-11-08/complement_budget/resonance/ROOT_REVIEW.json
```

The reviewer inspected the full transform error induction; sampled direct
coefficients alone would not certify every unmeasured coefficient. No fresh
asymptotic hypothesis or independent provenance of pi is inferred from this
same-source audit.
