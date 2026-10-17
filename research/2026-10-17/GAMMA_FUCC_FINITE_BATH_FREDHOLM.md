# Operation GAMMA-BATH: first-prime partial involution and effective OU Fredholm certificates

**Research date:** 2026-10-17. **Status:** PAPER DERIVED classical analysis on the exact source, stand-alone exact rational implementation, pending authentic installed-source CI for the gamma-clock sign crossing. **RH PROVED: NO.** The original first-window Suzuki Schur sign and all-support Weil positivity remain OPEN. This is a continuation of PR #158 (source jump spectral), #159 (source hidden-memory Schur), and #155 (piecewise source derivatives). No archived source changed or nontrivial zeta zero used.

## 1. Source, domain and sign conventions

Fixed genuine Q-zeta source: `observational_succ/source_weil_hierarchy.py` Git blob **`0cc8510b71d178fc79e8d410a86d8b6014cf9178`**, same as the frozen source in #137/#159. Let `a=1/2`, `I=(-a,a)`, `b=log 2`, `w=log2/sqrt2`, and `C=C_infty=gamma_E+pi/2+3 log2+log pi`. The true first-prime wavefront at this radius is **only `(2,2)`**, never an independent atom at 6. The original Gamma real-place rungs have `d_j=4j+1`, `alpha_j=d_j/2`, one true real Gamma factor, the original negative contact, and both completed polar channels. The true source formula on primitive `F=Vu`, extended by zero, is

\[
Q(F')=Q_\Gamma(F')-C\|F\|_2^2-2w\operatorname{Re}\langle F,T_bF\rangle
       +2|\langle F,c\rangle|^2-2|\langle F,s\rangle|^2,
\quad c(x)=\cosh(x/2),\ s(x)=\sinh(x/2).
\]

Initially `F in H^1_0(I)` and `u=F' in L²_0(I)`; the positive Gamma form is then closed on its stated completion. **No assertion about physical apparatus or positivity is imported from the Nature hidden-memory experiment.**

## GB-01 — exact finite-Gamma decomposition and Markovian auxiliary realization [PAPER PROVED]

For each true Gamma rung the whole-line positive Fourier multiplier is

\[
\frac{4\xi^2}{d_j(\xi^2+d_j^2/4)}
 =\frac4{d_j}-\frac{d_j}{\xi^2+d_j^2/4}.
\]

Let `E_alpha` be convolution on the zero extension of `F` by `exp(-alpha|x-y|)` restricted back to I. Its Fourier multiplier is `2alpha/(alpha²+xi²)`, so it is positive, compact and trace class. Its continuous positive kernel has trace `Tr E_alpha=2a=1`. Therefore the **genuine** `J`-rung Gamma source, without adding a positive bath, is

\[
Q_{\Gamma,J}(F')=c_J\|F\|^2-\langle F,K_JF\rangle,
\quad c_J=\sum_{j=0}^{J-1}\frac4{4j+1},\quad
K_J=\sum_{j=0}^{J-1}E_{(4j+1)/2}\succeq0,\quad\operatorname{Tr}K_J=J.
\]

Every individual rung `4/d_j I-E_alpha_j` is nonnegative by its exact multiplier; hence the genuine complete `Q_Gamma` is the increasing monotone form limit of the true finite-rung source, **not** a new bounded covariance model.

A useful hidden-degree-of-freedom realization is genuinely **local**: `v_j=E_alpha_j F` is exactly the weak solution of

\[
(-\partial_x^2+\alpha_j^2)v_j=2\alpha_j F,
\quad v_j'(-a)=\alpha_j v_j(-a),\quad v_j'(a)=-\alpha_jv_j(a).
\]

Those Robin traces come from the same full-line OU kernel, not an arbitrary reflective boundary. This is a *finite-J Markovian auxiliary field* for the true nonlocal Gamma source (classical Green-function construction). In the limit J grows, retaining the positive per-rung cancellation is mandatory. Distinguish this mathematical memory reconstruction from physical work extraction.

## GB-02 — first-prime `FUCC` is an exact partial involution [PAPER PROVED]

Let `T_b F(x)=F(x+b)` on the zero-extended source, and `A_b=1_I(T_b+T_{-b})1_I`. At the first-prime radius `a=1/2`, the genuine logarithm satisfies `a<b<2a` (indeed `1/2<log2<1`). There are three disjoint open regions

- Left `L=(-a,a-b)` and right `R=(-a+b,a)`, each of width `delta=2a-b`.
- Central `C_0=(a-b,b-a)` of length `2b-2a`.

`A_b` swaps L/R by literal translation and vanishes on the middle. Thus

\[
\boxed{A_b^3=A_b,\quad A_b^2=P_L+P_R,\quad \sigma(A_b)=\{-1,0,1\}.}
\]

All three spectral values have infinite multiplicity. This is exact at the **irrational authentic `log2`**, not an assumption that `log2` sits on an integer sampling grid. It holds throughout the single-p2-wavefront stage while `a<b`. At later radii with longer prime paths or additional true primes the polynomial relation changes; do not extrapolate it globally.

**Negative control:** compressing `A_b` to an N-cell observer projector generally destroys `A³=A`. The included rational source-shaped N=4, b=3/5 model proves the failure exactly. Consequently **never apply the cubic resolvent formula to a sampled `P_N A_b P_N` without verifying its actual algebra**.

## GB-03 — explicit source baseline inverse and three essential spectral bands [PAPER PROVED]

Define the exact **finite true Gamma source**, including authentic prime, contact and both poles,

\[
H_J=(c_J-C)I-wA_b-K_J+2|c\rangle\langle c|-2|s\rangle\langle s|.
\]

Set `gamma_J=c_J-C`, `B_J=gamma_J I-w A_b`. The genuine Gamma scalar prefix obeys the exact rational bound

\[
c_8=\frac{63349408}{10094175}>\frac{25}4,
\quad C<\frac{43}8,\quad 0<w<\frac12.
\]

Therefore, for all J≥8,

\[
\boxed{B_J\succ \frac38 I.}
\]

The inverse is **explicit** by the source cubic identity:

\[
\boxed{ B_J^{-1}=\frac1{\gamma_J}I
 +\frac{w}{\gamma_J^2-w^2}A_b
 +\frac{w^2}{\gamma_J(\gamma_J^2-w^2)}A_b^2. }
\]

The true compact K_J and rank-two completed pole terms cannot change the essential spectrum, so Weyl's theorem gives

\[
\boxed{\sigma_{\rm ess}(H_J)=\{\gamma_J-w,\gamma_J,\gamma_J+w\}\subset(3/8,\infty).}
\]

Every negative spectral mode of the **true J-rung truncated** source is therefore a *discrete, isolated, finite-multiplicity* eigenmode. This is not the essential spectrum of the **unbounded complete** Gamma operator; take J→∞ only through genuine monotone quadratic forms.

## GB-04 — compact Birman–Schwinger with authentic two-pole compensation [PAPER PROVED]

Let `B_J^+=B_J+2|c><c|` and `Q_J^-=K_J+2|s><s|>=0`. Then the original signed finite-Gamma source is **exactly** `H_J=B_J^+-Q_J^-`. The inverse of `B_J^+` is explicitly the Sherman–Morrison correction

\[
(B_J^+)^{-1}=B_J^{-1}
 -\frac{2\,B_J^{-1}|c\rangle\langle c|B_J^{-1}}{1+2\langle c,B_J^{-1}c\rangle}.
\]

The equivalence

\[
\boxed{H_J\succeq0\quad\Longleftrightarrow\quad
\left\|(B_J^+)^{-1/2}Q_J^-(B_J^+)^{-1/2}\right\|\le1}
\]

is the classical Birman–Schwinger principle, now **without any compact zero-shift inverse or unknown positive-jump projector**. The RHS is a **positive trace-class** operator with genuine original OU, prime and completed polar channels. The scalar source bound gives the negative index upper

\[
\boxed{n_-(H_8)<\frac{8+1/16}{c_8-C-w}<20;\quad n_-(H_8)\le19.}
\]

The final strict `<20` needs exact authenticated intervals for C,w (the standalone coarse 43/8,1/2 yield only `<21`, hence at most20). Dedicated actual-source CI rechecks it. The original complete source already has a stronger but different WB4 negative-index bound ≤4; GB-04 is an **independent finite-Gamma-prefix** bound rather than an improvement to RH.

## GB-05 — an exact finite analytic Fredholm PSD certificate from source OU cells [PAPER PROVED; incomplete source implementation]

Let `P_N` be projection onto N equal L²-normalized cell indicators of I. For the **actual** true OU kernel `E_alpha`, its full-line Fourier derivative multiplier is `2alpha|xi|/(alpha²+xi²)≤1`. The cellwise mean-zero Poincaré inequality gives

\[
\|(I-P_N)E_\alpha\|\le\frac1{\pi N};\qquad
\boxed{\|K_J-P_NK_JP_N\|\le\frac{2J}{\pi N}<\frac{2J}{3N}=:\epsilon_{J,N}.}
\]

No false derivative-after-*Legendre*-projection inequality is being used. This is a cellwise L² output smoothing estimate for the genuine OU kernel; it applies on **all** L² inputs.

The exact source cell Gram entry of `E_alpha` is, writing `h=1/N`, k=|i−j|,

\[
M_{\alpha,0}=\frac2\alpha-\frac{2(1-e^{-\alpha h})}{\alpha^2h},
\quad
M_{\alpha,k}=\frac{(1-e^{-\alpha h})^2e^{-\alpha(k-1)h}}{\alpha^2h}\quad(k\ge1).
\]

This formula is proved by directly integrating the exponential kernel on each cell pair; the code implements it with **outward exact Fraction exponential intervals**, including adjacent cells, and the source adapter replays the archive's own exp(-rational) intervals. Source true Gamma means precisely `d_j=4j+1` and **positive coefficients 1** in K_J; no fabricated bath atoms or mismatched Gamma normalization.

From the operator error:

\[
\boxed{H\succeq H_J\succeq
B_{J,N}+2|c\rangle\langle c|-P_NK_JP_N-2|s\rangle\langle s|,}
\quad B_{J,N}=(\gamma_J-\epsilon_{J,N})I-wA_b.
\]

At J=8,N=32, even the **coarse** original source bounds prove `B_(8,32)>5/24 I`. This is a genuine all-input lower operator, **not** a finite Galerkin PSD substitution.

Because `B_(J,N)` has the same explicit cubic inverse, define the finite feature map \(\Phi=[e_1,\ldots,e_N,c,s]\) and `D=diag(-[<e_i,K_J e_j>]_(i,j), 2, -2)`. The right side is exactly `B_(J,N)+Phi D Phi*`. Let `W=Phi* B_(J,N)^-1 Phi` (an exact finite Gram of source functions). Then

\[
\boxed{B_{J,N}+\Phi D\Phi^*\succeq0\ \Longleftrightarrow\ W+WDW\succeq0.}
\]

This has dimension **N+2**, with a **bounded and explicit positive reference inverse**; unlike the original four-mode zero-shift inverse, no unbounded compact inverse occurs. In principle every `W` entry is a finite integral of the polynomial in `A_b` against known cells and the two explicit hyperbolic functions, so it is computable to arbitrary rational precision (source log2 and exp intervals). The repository currently implements `K_J`'s genuine source cell intervals and the **exact finite rational surrogate** of this Fredholm algebra, but **not** the complete original `W+WDW` interval matrix for useful J,N, and therefore does not certify first-window positivity.

**Important hostile control:** at J=8 the *truncated* authentic source has an actual negative direction (GB-06), so no honest J=8 sufficient positive-source certificate can pass. This is expected and correctly refuses false positivity.

## GB-06 — a source-diagnostic hidden-Gamma clock sign transition [EXACT SOURCE GATE PENDING]

The first *original* low test `u(t)=P_1(2t)=2t`, `F(t)=t²−1/4`, gives an unusually clean witness to the importance of the hidden positive Gamma rungs. The numerical discovery (independent of the later source interval checker) is

\[
Q_{G_8}(u)\approx-0.000480574,\quad
Q_{G_{18}}(u)\approx-0.0000023333,\quad
Q_{G_{19}}(u)\approx+0.0000102530,\quad
Q_{G_{64}}(u)\approx+0.000112295.
\]

These four decimal calculations are **NUMERICAL DISCOVERY ONLY** until the installed authentic source `suzuki_legendre_source.authentic_full_low_entry(1,1,J)` strictly encloses them with rational signs. The new source adapter **refuses to pass unless** its exact original complete contact/poles/prime-2/Gamma interval calls prove `upper(G18)<0<lower(G19)`, and replay separately `G8<0<G64` and original blob bytes. Every new Gamma rung is positive; consequently, if the original source adapter passes, **J=19 is the exact first positive Gamma rung on this one specified source polynomial**, *not* a global positivity threshold and not evidence of a negative completed Weil witness. The complete Gamma source on P1 is positive by the retained positive tail and G19>0. This shows how missing hidden Archimedean degrees can reverse a finite-world signed diagnostic.

This is a mathematical realization of a **delayed-information** mechanism, not a claim about extracting thermodynamic work. Nature Physics (Muruga et al., 2026) is experimental context, not an imported SUCC proof premise.

## 7. False shortcuts and next required source gate

- An arbitrary positive finite Gamma covariance is **not** the signed Weil form. Our `E_alpha` is exactly the true rung and its source is pinned.
- Cubic `A³=A` holds on the **continuous true** first-prime shift; *not* on arbitrary compressed rational-grid matrices, which may lose a prime channel.
- Finite `G_J` can be negative even if full `G` is positive on the same polynomial; no inference from a truncated sign to the completed Weil sign.
- A finite *Galerkin compression* of `G_J` is not a whole-Hilbert certificate. GB-05 includes a rigorous all-input operator error and positive reference operator.
- The trace-class OU bath still has infinitely many eigenvalues; the label `J` counts OU **rungs**, not their spatial dimension. Do not call this a finite-dimensional ODE in the entire spatial phase space; it is J auxiliary **fields**.
- SUCC #159 dyadic Schur and #158 source spectral projectors remain independent available routes. New contribution is an explicitly invertible FUCC baseline and a finite computable compact Fredholm interface.
- If the full first-window source is **strictly** positive, monotone Gamma-form convergence plus compactness implies some genuine finite-J truncation and sufficiently fine N will admit a finite strict certificate. No uniform J/N/time bound is proved and zero-margin positivity need not terminate. The installed numerical capacities are deliberately bounded (J≤16/N≤10 for source adapter), so **effective total certification is not yet implemented**.
- To close the current first-window sign, build the complete source `W+WDW` interval packet at increasing J,N and certify its exact Loewner sign. A negative lower packet is **inconclusive**. A negative *upper evaluated actual completed source* test would require independent hostile review.

## Reproduction

```sh
python -m unittest discover -s tests -p 'test_finite_gamma_fucc_fredholm.py' -v
python scripts/finite_gamma_fucc_fredholm_probe.py --verify
python scripts/finite_gamma_fucc_fredholm_probe.py --source --verify
python scripts/verify_provenance.py
```

Dedicated GitHub PR exact-head two-interpreter checks must execute every original-source test **without skips**. The full repository suite is separate. No merge, release or archive rewrite without explicit authorization.

## GB-07 — four different clocks of positivity in the *same* authentic arithmetic source [EXACT SOURCE GATE]

Our source-independent numerical discovery found **different first positivity thresholds** for the four original low test directions, after the true signed contact, genuine prime2, and **both** completed polar channels had been included:

| Original unnormalized low SUCC mode `u=P_k(2x)` | Last predicted strictly negative Γ-rung prefix | First predicted strictly positive Γ-rung prefix | Numerical discovery values before / after (not sign proof) |
|---|---:|---:|---|
| k=1 (odd u, even primitive) | 18 | **19** | ~−2.33331e−6 / +1.02530e−5 |
| k=2 (even u, odd primitive) | 9 | **10** | ~−2.38705e−5 / +2.28078e−5 |
| k=3 (odd u, even primitive) | 19 | **20** | ~−3.10914e−6 / +1.00168e−6 |
| k=4 (even u, odd primitive) | 6 | **7** | ~−1.09366e−5 / +3.64272e−5 |

The new fail-closed `source_original_four_mode_gamma_clock()` evaluates the eight required **actual source interval inequalities**, `Q_(G_(J−1))(P_k)<0<Q_(G_J)(P_k)`, via `suzuki_legendre_source.authentic_full_low_entry(k,k,J)` and checks the original SHA/tape before admitting them as proved. Because each newly added Gamma rung is a PSD original-source operator (GB-01), the eight strict signs prove the **first** positive rung for each specific mode *without* enumerating all preceding Γ stages. This is a rigorous mathematical example of four source-locked observation channels having different finite-depth information-access thresholds; it is not a redefinition of Γ, not an artificial bath, and not a claim about a person's ability to harvest thermodynamic work.

**Evidence status:** Numerical discovery is not source proof. The previous exact GitHub head `e74c9bf...` did prove J18<0<J19 for P1 under Python3.10/3.13 and original archived source, with zero skips. The **new** expanded four-mode source gate must separately pass exact-head hosted CI before the other three crossings can be promoted. No individual diagonal positivity implies positivity of the joint four-mode Gram, let alone the original four-mode Schur complement or RH.

**Research interpretation:** The Archimedean Gamma tower is not simply a smooth positive background. Its finite, true OU rungs restore positive energy to source test directions at different depths, even with identical active prime2 source tape. That resembles delayed revelation of hidden degrees of freedom in the mathematical SUCC observer telescope, while all signed polar/prime contributions remain fixed. The time/rung number is a mathematical reconstruction index rather than physical elapsed time.

## GB-08 — an explicit *four-body*, source-true Gamma-rung positivity threshold [EXACT SOURCE GATE]

The same direct-original-source numerical discovery reveals that the **full four-mode low Suzuki/Weil Gram** `A_(4,J)` first becomes strictly positive definite at `J=64`. This is stronger than the GB-07 four individual diagonal tests and sharpens the historical WB4/CFS first low positivity at J=64 (previous work did not establish the **minimal** J). The numerical even-block smallest eigenvalues are approximately `−5.85970816e−8` at `J=63` and `+9.24760878e−8` at `J=64`; these decimals are **discovery only**, not proof.

The new `source_original_four_mode_PD_transition()` is a **fail-closed genuine-source certificate**. It calls the original `authentic_full_low_entry(i,j,a=1/2,J)` for the actual six same-parity Gram entries at both J=63 and J=64, retaining the **one real Gamma, contact, genuine p2 half-density, and both completed polar terms**, with the archive's outward rational source arithmetic.

At J=63 it tests the explicit **rational source vector**

\[
\boxed{u=24P_2(2t)-25P_4(2t),\quad
Q_{G_{63}}(u)=576A_{22}^{(63)}-1200A_{24}^{(63)}+625A_{44}^{(63)}<0.}
\]

The upper bound is formed conservatively as `576 A22.hi − 1200 A24.lo + 625 A44.hi` and must be *strictly* negative. At J=64, reflection parity makes `A_(4,64)` two Hermitian 2×2 blocks `(1,3)` and `(2,4)`. Each is **strictly positive** provided its two exact interval diagonal lower endpoints are positive and its exact determinant lower

\[
\boxed{\det_{\rm lo}=A_{ii}^{lo}A_{kk}^{lo}-\max(|A_{ik}^{lo}|,|A_{ik}^{hi}|)^2>0.}
\]

The arithmetic checker rejects missing source channels or failed determinant margins. Since each true added Gamma rung is nonnegative as a quadratic form (GB-01), `A_(4,J)` is Loewner nondecreasing in J. Thus the negative J=63 witness proves every earlier `1<=J<=63` fails PSD, and strict J=64 block positivity establishes **the first PD stage at exactly 64**. This needs only one exact negative rational combination at J=63 and a six-entry rational interval matrix at J=64, rather than 63 separate positive-definiteness computations.

**Boundary:** This statement is about the unshorted true **four-low** `A_4` after only J genuine Gamma rungs. It is **not** the signed completed all-test Weil form, not `S_4=A_4-R_4`, and not RH. Even a strict four-low Gram can hide a negative high response. The new source gate awaits exact-head GitHub CI; the earlier source ΓJ18/19 P1 gate was verified independently at the prior head. Once CI passes the four-body stage will be labeled SOURCE-VERIFIED with original SHA and no numerical sign inference.
