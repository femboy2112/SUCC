# Gaussian causal Yoneda: source-anchored spectral observers

**Status:** additive research dossier (2026-11-19), based on Main XXVI
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`. No modifications to the
original BBP recurrence, initial seed, frozen history, import manifest, CI,
production defaults, other agents' branches, or main.

## The research question

Can an embedded finite observer's Gaussian representation retain enough
source-labeled causal phase information to distinguish actual motion from an
apparently locked co-moving chart, and can that information supply pi's
missing anti-lock inequality?

**Answer with theorems:** Gaussian smoothing is a faithful but unstable
encoding of complete circle measures; the properly anchored Gaussian L2
**displacement** is quantitatively equivalent to R0; Gaussian L2
**empirical-to-Haar discrepancy** is equivalent to all-mode Weyl normality;
and both have controlled finite-rational BBP source approximants. None gives
the required source-selected positive lower bound by itself. The unmodified
BBP forcing contributes positive but summably small local Gaussian energy,
including on an identically locked wrong-seed completion.

## What is actually proved

| Claim | Outcome | Scope |
|---|---|---|
| GYC-01 | Gaussian measure representation injective, inverse unstable | finite signed circle measures, full spectral readout |
| GYC-02 | `T_b* G_lambda = G_(b^2 lambda) T_b*` | integer multiplying circle maps; all measures |
| GYC-03 | `4 e^-lambda A_B <= E_B <= 2 S_lambda A_B` | any phase sequence; R0 iff Gaussian displacement noncollapse |
| GYC-04 | `V_B=sum_(h!=0) e^(-lambda h^2)|W_B(h)|^2` | all-mode Weyl iff Gaussian discrepancy to Haar vanishes |
| GYC-05 | mean-energy/energy-of-mean split | exact Hilbert variance identity |
| GYC-06 | rational BBP E and sqrt(V) errors O(B^-2) | original four poles, literal zero seed, positive BBP tail |
| GYC-07 | original forcing innovation energy ~ const*n^-4 | original r(n), any seed; no anti-lock inference |
| GYC-08 | complete late phase probes cannot recover 1/16 seed alias | all n>=1, even full Gaussian spectra |
| GYC-09 | Gaussian seed microscope demands sigma=O(16^-n) | declared seed-perturbation instrument; Hermite energy same for locked seed |
| GYC-10 | one oriented near-zero streak length O(log N) | original positive tail; excluded upper-fringe orientation remains |
| GYC-11 | independent signed Gaussian witness ⇒ R0 | conditional; crucial witness estimate UNVERIFIED |
| GYC-12 | causal square + dense Yoneda probes ⇒ target reconstruction | classical, explicitly limited to lawful observation class |
| GYC-13 | finite rational terminal cancels source forcing exactly | genuine BBP source, every finite horizon; local Gaussian position defect O(n^-2) |
| GYC-14 | terminal endpoint M=2B improves Gaussian error 64-fold | E/V source transfer O(1/(4096 B^2)); fixed rational M cannot be Haar |
| GYC-15 | source-labeled Gaussian cross-covariance recovers the signed five-channel Jacobian | exact affine family; output covariance alone has orthogonal gauge; seed needs anchor |

## Two different spectra, two different frontiers

Define `theta_n={16^n*pi/16}` and `K_theta(u)=K_lambda(u-theta)` for the
periodized heat Gaussian. Let `A_B` denote the shell mean of
`1-cos(2*pi*theta_n)`.

**R0: a source-anchored departure from zero phase**

```
E_B = (1/B) sum ||K_(theta_n)-K_0||_2^2
4 exp(-lambda) A_B <= E_B <= 2 S_lambda A_B.
```

**Full base-16 normality: the whole observed empirical distribution tends
Haar**

```
M_B = (1/B) sum K_(theta_n)
V_B = ||M_B-1||_2^2
    = sum_(h!=0) exp(-lambda*h^2)*|W_B(h)|^2.
```

The first is mean squared displacement. The second is squared displacement
of the mean *from Haar*, not from the anchor. Neither should be confused
with conserved Hermite L2 energy of a Gaussian seed ensemble. Keeping the
full complex phase and the original seed journal is mandatory.

## Strongest source-specific advance and strongest counterexample

For the exact BBP `U_n`, the inherited completed tail obeys
`0<T_n<1/(64*n^2)`. With `L_lambda=4*pi*sum_(h!=0)|h|e^(-lambda*h^2)`,

```
|E_B - Ehat_B| <= L_lambda/(64*B^2),
|sqrt(V_B)-sqrt(Vhat_B)| <= (2*pi*sqrt(S_lambda))/(64*B^2),
```

where hats use only **finite exact rational** states `U_n`. These are
all-shell rigorous analytic transport inequalities, not empirical fits.
One finite source-rational terminal endpoint `P_(2B)` improves both errors
from `1/(64*B^2)` to `1/(4096*B^2)` (GYC-14), while its compensated
finite trajectory commutes **exactly** with the radix-16 successor (GYC-13).
The signed source arithmetic needed to show a positive all-late-shell
rational terminal energy lower bound remains open.

The same exact original forcing and seed `-pi/16` produce `Y_n=0`
for all n. Yet the Gaussian energy of the nonzero innovations `r(n)` is
~`1.9181587589*n^-4` at lambda=1. Local causal activity, positivity,
Jacobian rank, and spectral energy conservation are not enough.

## Navigating this dossier

- [PROOFS.md](PROOFS.md): complete statements, derivations and failure cases.
- [NEXT.md](NEXT.md): preregistered source-sensitive signed-witness offensive.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md): precise claim authority and residual debt.
- [gaussian_causal.py](gaussian_causal.py): stdlib exact-rational BBP and
  Gaussian finite Fourier diagnostics.
- [test_gaussian_causal.py](test_gaussian_causal.py): 29 focused tests, exact
  rational identities, independent quadrature, tails, mutation-like controls.
- [VALIDATION.md](VALIDATION.md): actual executed tests and unexecuted gates.

**Test:** from this directory run `python -m unittest -v test_gaussian_causal`.

Everything is additive and draft-only. In particular **R0, pi normality,
source-selected signed cancellation, and RH remain OPEN**.
