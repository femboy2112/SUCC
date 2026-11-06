# Countermodel discrimination

| Model | RC1 / RC3 transport | Final fixed-radius lower-bound gate | Reason |
|---|---|---|---|
| Original literal zero | Applies | OPEN | No new selected arithmetic estimate |
| Same-source coherent seed `-pi/16` | Applies | Fails: limit `log(1-r)<0` | All completed phases converge to zero |
| Nearby periodic completions | Applies | Fails: strictly negative weighted Fourier energy | Finite periodic empirical measure is non-Haar |
| Rational seed `1/5` | Applies | Same verdict as zero | All pair changes `(16^j-16^i)/5` are integers |
| Unforced zero | Applies | Fails: limit `log(1-r)` | Exact full collisions; sharp linear cut profile |
| One-pole coefficient mutant `4->3` | Applies | OPEN; finite positives are not a proof | Different source numerator, no assumed normality |
| Half-circle grids | Applies when encoded as a source | Fails | Nonzero first Fourier coefficient |
| Biased invariant Bernoulli measure | Applies when encoded as a source | Fails | Non-Haar measure has a nonzero Fourier coefficient |
| Equidistributed sequence with sparse exact collisions | Applies | Passes, although singular Gate C fails | Density-zero edits preserve Weyl; smooth kernel remains finite |
| Normal wrong seed failing the critical ratchet | Applies | Passes if normality is established | Fixed-radius gate does not impose critical high-frequency rate |
| Radial-only zero-period nonnormal field | Applies | Fails when its non-Haar empirical limit exists | Only distribution, not radial source geometry, enters the gate |
| Odd-cyclotomic non-Haar sphere encoding | Requires lawful circle transport | Fails after source-correct circle transport | Odd conductor alone does not cancel the selected character |
| Smooth-window cancellation with sharp-window coherence | No window substitution is allowed | Undetermined until actual epoch is used | RC formulas use the declared sharp epoch throughout |

The universal bounds deliberately admit every listed source and boundary.
They do **not** identify the authentic seed. The open final inequality would
exclude coherent/periodic completions quantitatively; no literal-zero
arithmetic hypothesis sufficient to prove it has been discovered here.

The fixed-radius lower-bound gate is exactly distributional, so it need not
exclude every wrong source: normal source mutants legitimately pass it.
Passing such a gate cannot be used to authenticate source identity.
