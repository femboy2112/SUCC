# Six-frame Omega-Haar -> exact signed Weyl observer (Basel-calibrated)

**Research: 2026-11-10.** Parent: Main XXIII draft #584 at `50481e49592af00d87c602f671a28f3503709de0`. Additive research; no frozen source, original seed, inherited code, main or historical proof changes. **Status:** algebraically proved identities, calibrated local finite tests, **NOT** a normality/RH proof or independently externally reviewed theorem.

## 1. Exact six-frame geometry

On `H = l2(N>=1)`, let `S e_n=e_(n+1)`, and let `B2` average each pair `(2m,2m+1)` and `B3` each triple `(3m,3m+1,3m+2)` for `m>=1`; both vanish on the initial incomplete boundary. The skew-adjoint real operator `C=[B2,B3]` is the intrinsic chronological Omega4/Omega5 coarse-graining commutator of #583, whose six-cell bulk blocks match #582.

For all `n>=6`, the **directed nearest-neighbor** matrix coefficient is

```math
c_n:=\langle e_n, C e_{n+1}\rangle=
\begin{cases}
1/6,&n\equiv1\pmod6,\\
-1/6,&n\equiv3\pmod6,\\
0,&\mathrm{otherwise}.
\end{cases}
```

Single-frame sampling loses four residue classes out of six. For `t=0,...,5`, define the bounded directed weighted shifts

```math
A_t=\sum_{n\ge t+6}c_{n-t}|n\rangle\langle n+1|,
```

obtained from the shifted commutator `S^t C S^{*t}` by retaining its successor edges. For **every** integer `n>=11`, precisely two of `c_n,c_(n-1),...,c_(n-5)` are nonzero, with squared magnitude `1/36`. Therefore

```math
\boxed{18\sum_{t=0}^{5}|\langle e_n,A_t e_{n+1}\rangle|^2=1.}
\tag{SIX-FRAME}
```

This is an exact partition-of-unity **on the chronological successor edges**, not a direct CRT conditional expectation theorem. The signs change under reversed projection order; the squared weights do not.

## 2. Source-selected phase transport theorem

Keep precisely the four-pole BBP source, in zero-based indexing from #582/#583:

```math
R(j)=\frac4{8j+1}-\frac2{8j+4}-\frac1{8j+5}-\frac1{8j+6},\quad
P_L=\sum_{j=0}^{L-1}16^{-j-1}R(j),\quad P_\infty=\pi/16.
```

This is identical to the one-based `r(n)=R(n-1)` in the maintained pi-normality frontier. For real initial seed `s`, the *completed real lift* is `Y_n(s)=16^n(s+P_infty)`. Thus `Y_(n+1)=16Y_n`, with `s=0` the authentic carrier and `s*=-pi/16` a mathematically coherent (not rational p-adic) wrong seed yielding `Y_n=0`.

For any nonzero integer `h`, define the diagonal unitary `D_(h,s)` via

```math
D_{h,s}e_n=\exp\!\left(2\pi i\,\frac h{15}Y_n(s)\right)e_n.
```

**The factor `h/15` is necessary and source-type sensitive:**

```math
\frac h{15}(Y_{n+1}-Y_n)=hY_n.
```

The divided difference is defined using **real lifts and integer windings**. Forming it after separately reducing the inputs mod 1 generally gives the wrong phase. For `A>=11` and `P_A=sum_(n=A)^(2A-1) |n><n|`, exact finite trace algebra yields

```math
\boxed{\frac{18}{A}\sum_{t=0}^{5}
\operatorname{Tr}(P_A A_tD_{h,s}A_t^*D_{h,s}^*)
=\frac1A\sum_{n=A}^{2A-1}e^{2\pi i hY_n(s)}=:c_A(h;s).}
\tag{OMEGA-WEYL}
```

**Proof:** the `n`-diagonal element is `|c_(n-t)|^2 exp(2pi i(h/15)(Y_(n+1)-Y_n))`. The source-selected real-lift law turns its phase into `exp(2pi ihY_n)`. Summing the six squared coefficients gives 1 by SIX-FRAME. The finite projection makes the trace unproblematic. No cancellation has been assumed or derived. QED.

**Verdict:** this is an *exact carrier-level realization* of the original signed Weyl obstruction using six translated Omega-Haar frames. It does **not** advance the analytic estimate `c_A(h;0)->0`. The original-zero seed and all real carries remain load-bearing.

## 3. The actual Basel -> signed Weyl operator interface

Let `H0 e_n=(log n)e_n`, so `rho2=zeta(2)^(-1) exp(-2 H0)` has diagonal `1/(zeta(2)n^2)` and trace 1. Let

```math
W_A=\sum_{n=A}^{2A-1}n^{-2},\quad
\rho_{2,A}=W_A^{-1}P_Ae^{-2H_0}P_A,\quad Ne_n=ne_n.
```

The reciprocal-square Gibbs operator now gives an **exact weighted signed observer**:

```math
\boxed{18\sum_{t=0}^5\operatorname{Tr}
(\rho_{2,A}A_tD_{h,s}A_t^*D_{h,s}^*)
=\frac{1}{W_A}\sum_{n=A}^{2A-1}\frac{e^{2\pi ihY_n(s)}}{n^2}.}
\tag{BASEL-WEYL}
```

The raw Gibbs observable has a different measure from the uniform epoch statistic needed for normality. But the *retained Archimedean integer height* exactly corrects it:

```math
\boxed{\frac{18W_A}{A}\sum_{t=0}^{5}
\operatorname{Tr}(N^2\rho_{2,A}A_tD_{h,s}A_t^*D_{h,s}^*)=c_A(h;s).}
\tag{HEIGHT-COMPENSATED}
```

Here `N^2 rho_(2,A)=P_A/W_A` is finite rank, even though `N^2` on the whole Hilbert space is unbounded. This shows precisely why reciprocal-square normalization and the Archimedean height cannot be conflated with an all-local 2/3-adic observable. It is an algebraic reconstruction, not an unexplained analytic estimate.

## 4. Exact finite-source phase budget and wrong-seed crucible

The same four-pole source has its positive moment representation

```math
R(j)=\int_0^1x^{8j}(1-x)M(x)\,dx,\quad
M(x)=(x^2+2)(x^2+2x+2),\quad 0<M(x)<15\ (x<1).
```

Therefore geometric comparison gives, for `L>=0`,

```math
0<P_\infty-P_L<\frac{16^{-L}}{(8L+1)(8L+2)}.
```

For `Y_n^(L)(s)=16^n(s+P_L)`, the exact Weyl mean computed at common finite horizon `L>=2A` obeys

```math
\boxed{|c_A(h;s)-c_A^{(L)}(h;s)|
\le\frac{2\pi|h|16^{2A-1-L}}{(8L+1)(8L+2)}.}
\tag{PHASE-BUDGET}
```

To obtain a rational bound, use `2pi<44/7`; certify the finite complex exponential separately with rational interval arithmetic. The exact six-frame identity introduces no additional theoretical phase error. A naive numerical cosine evaluation is *not* a finite rigorous certificate.

**Controls:** The coherent fixed `s*=-pi/16` gives `c_A(h;s*)=1` for all A,h. In a finite common-horizon test, `s_L=-P_L` is rational and yields `c_A^(L)(h;s_L)=1`; do not treat `s_L` as a fixed infinite p-integral control. The adversarial epoch-dependent rational p-integral control PPP-08 from #572 is a different, stronger test. Arbitrary source/seed choices leave the unphased Basel graph trace unchanged. A positive extra-pole moment mutant from #583 may match finite source samples while changing completion. All source-blind deductions of normality are thereby rejected, while the phase-sensitive reconstruction survives as an exact identity.

## 5. Claim ledger and next falsifier

| Claim | Status | Probe/failure mode |
|---|---|---|
| Classical Basel, Euler factorization, CRT cycle-graph trace, Gamma-jet | DISCLOSED within stated classical domain; see `PROOFS.md` | Drop remaining-prime factor or Archimedean height: reconstruction fails |
| SIX-FRAME and OMEGA-WEYL for each A>=11, real seed and integer h | DISCLOSED by exact matrix proof; finite independent tests | Skip any translated frame: residue holes; discard carries: wrong phase |
| BASEL-WEYL and HEIGHT-COMPENSATED | DISCLOSED finite trace identities | Remove `N^2`: Gibbs-weighted mean, not uniform mean |
| PHASE-BUDGET | DISCLOSED elementary tail estimate | Corrupt original four-pole endpoint factor: bound need not survive |
| Original-zero `c_A(8k;0)->0` for odd k | OPEN; not proved by these identities | Try fresh odd h=8, signed lag/Weyl holdouts; test PPP-08 and non-normal seeds |
| Pi base-16 normality, RH, quantum advantage | OPEN / unclaimed | Requires separate asymptotic/source/sign or completed Weil bridge |

**Verdict-changing next result:** A source-selected signed estimate on `c_A(8k;0)` (or an equivalent source-locked six-frame trace), for all large A with all genuine integer carries and real-tail boundary payments, must exclude the coherent wrong-seed and p-integral PPP-08 control. Finite calibration and a positive energy only verify the instrument. Retain the full CRT complement and prime-power history; do not confuse mod-6 arithmetic frequencies with digits of pi.

## 6. Provenance and validation boundary

- `docs/PI_NORMALITY_FRONTIER.md` and `observational_succ/duck_bbp.py` source contract; inherited Main XXIII candidate #584.
- #583: `research/2026-11-10/omega_bbp_operational_completion/intrinsic_carrier/PROOFS.md` for `H0,B2,B3`.
- #582: `research/2026-11-10/omega_bbp_operational_completion/OMEGA_HAAR_WAVELET.md` for the six-cell chronological commutator.
- `PROOFS.md` is the accompanying independent Basel/2-3 CRT/Gamma/mixed-Gibbs dossier.
- `test_phase_weyl.py`: nine focused tests, exact Fraction arithmetic and a bounded floating smoke comparison. `test_basel_omega.py`: nine independent earlier SymPy/MPMath Basel and mixed-trace checks.
- **Not run:** ~13k repository-wide native tests, hosted CI completion, Lean, external blind review. No main merge/tag/release. Scoped to research branch.
