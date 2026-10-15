# ATOM V — Finite-adèle quotient reconstruction and the real–profinite adelic solenoid

**Date:** October 15, 2026. Source branch: research/observer-tate-bijective-descent-2026-10-15, parent Phoenix II main 03db4420. This is a CLASSICAL additive-adele theorem with an exact finite-SUCC source constructor; it is NOT analytic Poisson or RH and is NOT a novel academic-priority assertion. **RH PROVED: NO.**

## 1. The genuinely global finite arithmetic object

Let
\[
\mathbb A_f=\prod_p'(\mathbb Q_p,\mathbb Z_p),\qquad
\widehat{\mathbb Z}=\prod_p\mathbb Z_p
\]
be respectively the restricted finite adeles and the compact-open integral adeles. An adele a=(a_p)_p has a_p∈Z_p for all but finitely many genuine primes. At a nonintegral place p there exists k>=1 and a unique p-primary fractional coset
\[
[a_p]\in\mathbb Q_p/\mathbb Z_p
=\left[\frac{u_p}{p^k}\right]+\mathbb Z_p,\quad 0\le u_p<p^k.
\]
(Here a smaller denominator due to cancellation is permitted; its class is unchanged.) Consequently,
\[
\mathbb A_f/\widehat{\mathbb Z}
\cong\bigoplus_p(\mathbb Q_p/\mathbb Z_p).
\]
The sum is DIRECT because an adele has only finitely many nonintegral coordinates. Each finite p-primary group Q_p/Z_p is a Prüfer p-group, and together the direct sum is canonically Q/Z.

## 2. EXACT additive strong approximation with a finite SUCC witness

Given the finite source local fractional cosets u_p/p^k, construct the RATIONAL number
\[
\boxed{q=\sum_{p\in S}\frac{u_p}{p^{k_p}}\in\mathbb Q.}\tag{ATOM-V-LIFT}
\]
At a selected prime p, the difference
\[
q-\frac{u_p}{p^{k_p}}
=\sum_{q'\in S,\ q'\ne p}\frac{u_{q'}}{q'^{k_{q'}}}
\]
is an element of Z_p, because all other denominators are units at p. At an unselected prime, q is also integral at p. Thus the diagonal rational q represents the prescribed finite adelic coset, proving
\[
\boxed{\mathbb A_f=\mathbb Q+\widehat{\mathbb Z}.}\tag{ATOM-V-STRONG}
\]
This is additive strong approximation for the rational number field. It uses the original p-primary finite fraction residues and no limiting computation or nontrivial zeta-zero data. It is stronger than merely producing the profinite compact carrier.

**Exact intersection:** a rational q lying in Z_p for EVERY finite prime p has no prime divisor in its reduced denominator, hence is an integer. Therefore
\[
\boxed{\mathbb Q\cap\widehat{\mathbb Z}=\mathbb Z.}
\]
By the first isomorphism theorem, the finite-adele quotient is
\[
\boxed{
0\to\widehat{\mathbb Z}\to\mathbb A_f
\to\mathbb Q/\mathbb Z\to0.
}\tag{ATOM-V-SEQ}
\]
The quotient Q/Z here inherits the DISCRETE quotient topology from A_f/Zhat because Zhat is open in A_f. It is NOT the usual subspace topology from R/Z, where Q/Z is dense. This distinction is a load-bearing source/topology contract.

**Examples:** p=2 local fraction 1/2 and p=3 fraction 2/3 construct q=7/6, representing the Q/Z class 1/6. At p=2 and p=3, the p-adic fractional parts of 7/6 are exactly 1/2 and 2/3. Re-encoding the same 2-local coset as 2/4 does not change the result. Local source addition with carries (1/2+1/2=1∈Z_2) becomes the same Q/Z addition.

The exact implementation uses genuine prime and prime-power residue checks, rational arithmetic, the previously proved diagonal finite-to-real additive character reconstruction, and different source paths for quotient addition. No floating character values, extra composite Euler place, or source interpolation from RH zeros are involved.

## 3. The connected real place enters by a different, lawful gluing construction

Let \(\mathbb A_\mathbb Q=\mathbb R\times\mathbb A_f\), with diagonal embedding \(q\mapsto(q,q)\). The natural inclusion R×Zhat↪A induces a continuous map
\[
\Phi:(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z
\longrightarrow \mathbb A_\mathbb Q/\mathbb Q.
\]
This is a topological group ISOMORPHISM.

**Proof of surjectivity:** given (t,a_f)∈A, choose q∈Q by the above constructive strong approximation with a_f−q∈Zhat. Then (t−q,a_f−q)∈R×Zhat represents the same class modulo diagonal Q.

**Proof of injectivity:** a pair (t,z)∈R×Zhat maps to zero in A/Q iff (t,z)=(q,q) for some rational q. The finite membership q∈Zhat forces q∈Z, so the kernel is EXACTLY diagonal Z.

**Topology:** the map is continuous and open in the quotient group topology; alternatively, the source is compact (every class admits representative in [0,1]×Zhat), the target is Hausdorff (diagonal Q is closed/discrete), hence a continuous bijection is a homeomorphism. Diagonal Q is discrete since
\[
\mathbb Q\cap((-1/2,1/2)\times\widehat{\mathbb Z})=\{0\}.
\]
It is also closed as a discrete subgroup of this locally compact abelian adelic group. The quotient is the classical **real–profinite solenoid**, compact and capable of having connected directions although Zhat itself is totally disconnected. This is a lawful repair of the prior no-go: real R is NOT a pure inverse limit of finite discrete carriers, but it CAN be coupled to a profinite carrier by a discrete-lattice quotient.

\[
\boxed{
(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z
\ \cong\ 
\mathbb A_\mathbb Q/\mathbb Q.
}\tag{ATOM-V-SOLENOID}
\]

**Why this matters to Tate:** the RHS is precisely the compact quotient on which adelic Fourier analysis and diagonal Poisson summation are formulated. Source-canonical finite residue reconstruction (ATOM-I), two-axis local Q_p Schwartz charts (ATOM-II), global additive character product on Q (ATOM-IV), and this exact real–profinite quotient are now one coherent arithmetic construction **at the additive/topological object level**.

## 4. Remaining Tate/Weil/RH obligations

This classical additive strong approximation and solenoid object do NOT construct the global Schwartz–Bruhat test topology with its full restricted tensor Fourier on all functions, or prove diagonal Poisson summation and multiplicative Tate zeta integrals with all Hecke conductors/epsilon factors. For a complete SUCC derivation of Tate, those analytic laws require independent source-consistent proofs and convergence estimates. Nor does the existence of a compact quotient imply Weil positivity: compact abelian geometry supports plenty of signed, indefinite quadratic forms.

A future fundamental route might try to derive the ORIGINAL positive Weil form from a source-identified cohomology or intersection pairing on this adelic quotient. Such an object and its positivity are not built here. The original signed Suzuki low/high zero-shift Schur criterion at a=1/2 and all-a sign remain RH-strength UNVERIFIED gates.

**Status:** exact finite↔adelic quotient and real–profinite carrier representation CLASSICAL/PROVED; global Tate Poisson, original signed Weil positivity and RH UNVERIFIED. Academic novelty UNVERIFIED.
