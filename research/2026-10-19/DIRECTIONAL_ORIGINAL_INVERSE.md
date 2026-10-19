# Genuine source inverse response and a finite auxiliary-family obstruction

**Status:** paper-proved operator inequalities and exact rational source certificates; original first-window S4 and RH remain OPEN. Global high coercivity is used only in the original **primitive K-Hilbert completion**, with the source interpretation and closure hypotheses made explicit. No nontrivial zero coordinate is an input.

## 1. Recovered state and source contract

This lane starts at PR179 `81684b4b8956f9f5da56c376ba7e4339277eb665`. It does not merge the sibling history of PR178. Original signed source blob: `0cc8510b71d178fc79e8d410a86d8b6014cf9178`. The unchanged PR177 continuum module has blob `f5dd37fa99a109ca614ae52dd6b67d2cadcb4f48` both at PR177 `f309d9104ba480c1999c962af1df7c50f19e1bfe` and at this baseline.

The selected PR178 material is read from exact commit `e42096ec0186228dd0f748767599e470f2ca2e1d`:

| Selected object | Exact provenance | Use |
|---|---|---|
| `scripts/institute_schur_probe.py::gamma_coefficients` | Git blob `1a09b58c0c5bdc4a86a756cad640f9f27511c73c` | Reimplemented IN-GAMMA-02 H¹/H² tail coefficients; no other script definitions imported |
| `scripts/institute_eta_probe.py::triangle_obstruction` and analysis §8 | Script blob `bb7cdf0dc00803280c526319d0101c852c576682` | Independently reconstructed fixed-data obstruction; no scalar parameter search repeated |
| `research/2026-10-18/INSTITUTE_GAMMA_ETA_SOURCE.json` | Git blob `468b91e2a6f9bbc37f97774954212b829638f1e7`, SHA256 `0a24144e8a22178296ad314e846ea13ab41a67efc291a42b6764f73d61e0d7aa` | Sealed J24,M192,P18 original source energy, parent coefficients and continuum residual Gram |

The exact PR178 witnesses show `T[e1]-M[e1]/kappa<0` in both parity blocks. Consequently scalar Young tuning and PSD error penalties on those fixed objects cannot repair positivity. PR179 independently found that retaining a more accurate Gamma tail can worsen the nominal continuum residual. The present route changes the **inverse estimate**, using actual extra source directions.

## 2. Correct coefficient and form domains

Let I=(-1/2,1/2), E=(polynomials of degree<=3)^perp in L²(I), and H be the genuine completed primitive source operator. Let d be the restriction of its closed form to E and D its associated operator. The inherited source Bessel theorem is

\[
D\ge\kappa I_E,\qquad
\kappa_{\mathrm{odd\ derivative}}=63/500,\quad
\kappa_{\mathrm{even\ derivative}}=153/500.
\]

The originating statement is `tate_weighted_bessel_four_schur.py::source_parity_split_four_moment_coercivity_certificate` (baseline Git blob `273260238ab1d345ab176329ade8231ac6e2ee26`), an all-four-moment source inequality. Its derivative version is D4>=kappa Q4 K Q4, with K=V*V. It is **not** a derivative-L² spectral gap. The PR174 bridge transfers it to E under the closed-source-form hypotheses. The coordinator's separate closed-form/core audit addresses that transfer; this executable receipt retains the inherited-source authority label rather than silently upgrading it to a kernel proof.

For low coordinates c in C^4 define F_i=V(P_i(2x)), A_ij=q(F_j,F_i), and B=Q_E H F. The map F:C^4→L²(I) is not an orthogonal identification with E^perp: F_3 and F_4 contain degree4 and degree5 primitive components. The relevant original-coordinate Schur form is nevertheless

\[
S[c]=\inf_{x\in\operatorname{Dom}(d)}q(Fc-x)
=c^*(A-B^*D^{-1}B)c.
\]

The low primitives lie in H¹_0(I), hence in Dom(H) by the original Gamma multiplier estimate m_Gamma<=5|xi| plus bounded contact, prime and polar channels. Thus B is an actual L² vector map. For any U:C^4→Dom(D), finite rank, put R=B-DU. Direct completion of the D-energy square proves

\[
\boxed{S=A-B^*U-U^*B+U^*DU-R^*D^{-1}R.}
\tag{DIR-1}
\]

This identity requires neither an orthogonal primitive low decomposition nor a finite compression masquerading as an infinite inverse.

## 3. Source-relative finite-rank inverse theorem

**Theorem DIR-2.** Let D be positive selfadjoint on E with D>=kappa I, kappa>0. Put C=D-kappa I. Let W:C^k→Dom(D) have finite rank and G=W*CW>0. Define Z=CW and K=kappa G+Z*Z. Then K>0 and

\[
\boxed{D^{-1}\le\kappa^{-1}I-\kappa^{-1}ZK^{-1}Z^*.}
\tag{DIR-2}
\]

**Proof.** For every x in Dom(C^(1/2)) and a in C^k,

\[
0\le\|C^{1/2}(x-Wa)\|^2
=q_C[x]-2\Re\langle Z^*x,a\rangle+a^*Ga.
\]

Minimizing the finite quadratic in a gives C>=ZG^-1Z* as forms. Therefore D>=kappa I+ZG^-1Z*. Positive resolvent order reverses the inequality; the finite-rank inverse identity yields (DIR-2). This argument is valid for unbounded C because W's columns lie in Dom(C), and only its closed form is used on general x. ∎

For a single auxiliary w this specializes to

\[
\langle r,D^{-1}r\rangle\le\frac{\|r\|^2}{\kappa}
-\frac{|\langle Cw,r\rangle|^2}
{\kappa\{\kappa\langle w,Cw\rangle+\|Cw\|^2\}}.
\]

The global source gap is essential. The exact positive matrix `D=[[2,9/5],[9/5,2]]` has the observed e1 energy2>1, yet `(D^-1)22>1`. A positive finite compression cannot justify the false global assertion D>=I.

## 4. Full-continuum enclosure of the directional correction

The chosen W has two high columns per parity,

\[
w_\ell=V(P_{m+2\ell}-P_{m+2\ell+2}),\qquad
m=5\ \text{or}\ 6,\quad \ell=1,2.
\]

Their derivative moments against the four original low modes vanish exactly, and w=w'=0 at both endpoints. They are source-valid H²_0 operator-domain vectors. The parent's fitted correction uses level0, so these are additional directions rather than a re-expression of that one fitted column.

Every action uses the original signed source: one real Gamma, contact, both opposite polar terms, and genuine prime2 with (log2)/sqrt2 half-density. The source action is a three-piece exact rational polynomial, with explicit finite approximation error and infinite-Gamma action error. The smaller of independently valid PR178 finite-tail and PR179 retained-tail error representations is selected for each auxiliary column. The residual columns retain the sealed parent's representation, allowing an exact parent-Gram equality check.

From ||z_i-z_hat_i||<=epsilon_i and ||r_j-r_hat_j||<=delta_j, the actual cross response V=Z*R has the rigorous entrywise enclosure

\[
|V_{ij}-\langle\widehat z_i,\widehat r_j\rangle|
\le\epsilon_i\|\widehat r_j\|+\delta_j\|\widehat z_i\|+\epsilon_i\delta_j.
\tag{DIR-3}
\]

The same formula encloses Z*Z. The original exponential/Legendre source integrator independently encloses G. Its **lower** uses the whole PSD order of the omitted Gamma tower; treating unknown off-diagonal tail entries independently would needlessly destroy that lower. For its **upper**, positive tail energy obeys q_tail(w)<=16 S_3(J)||w'||² and Cauchy controls mixed entries. Entrywise interval radii become a diagonal row-sum Loewner bound. These data give a true K_upper>=K.

For any rational X and actual V,

\[
V^*K^{-1}V\ge V^*K_{\mathrm{upper}}^{-1}V
\ge V^*X+X^*V-X^*K_{\mathrm{upper}}X.
\tag{DIR-4}
\]

The implementation chooses X=K_upper^-1 V_hat. Entrywise uncertainty in V is charged by a diagonal row-sum floor. This yields a whole signed lower for the inverse correction. It uses the entire matrix only when PSD; otherwise the independently valid zero correction is selected. No positive-part projection is applied to an indefinite lower.

## 5. A stronger finite-family impossibility test

**Theorem DIR-5.** Fix Hermitian T,M, positive K,kappa, and a coupling matrix V. For every response matrix X, every eta>0, and every PSD penalty P,

\[
L_{\eta,X,P}=T-\frac{1+\eta}{\kappa}M
+\frac{V^*X+X^*V-X^*KX}{\kappa}-P
\le T-\frac{M}{\kappa}+\frac{V^*K^{-1}V}{\kappa},
\tag{DIR-5}
\]

provided M>=0. Consequently a negative rational direction of the right side excludes **all** response coefficients X in this selected auxiliary family, all positive scalar Young parameters and all PSD error penalties.

**Proof.** Subtract the left side from the right side. The difference is

\[
\frac\eta\kappa M+\frac1\kappa(X-K^{-1}V)^*K(X-K^{-1}V)+P\ge0.
\]

This is an exact finite-family obstruction. Its right side is an optimistic upper envelope of sufficient certificates; a negative direction is **not** a negative direction of the genuine Weil form. ∎

For compact independent checking, the receipt rounds each retained T,M,K,V entry outward to rational intervals on a 10^-18 grid. The verifier first certifies M>=0 using its symmetric midpoint minus diagonal row-radius lower. It constructs K_lower by the same row-radius subtraction, uses K^-1<=K_lower^-1, and interval-bounds each rational witness direction. Thus its strictly negative upper is checked without floating eigenvalues or trusting a stored truth flag.

## 6. Results and limits

The sealed J24,M192 parent decomposition was reproduced exactly. The additional high family did not yield a PSD paid correction. Both parity blocks therefore retain the already valid parent lower. The stronger all-response cap, which is optimistic even before any error payment, has the following negative axial witnesses:

| Derivative parity | PR178 nominal-only obstruction e1 | New rank-2 family cap e1 | New cap e2 | Paid correction PSD? |
|---|---:|---:|---:|---|
| odd | -0.000507559990850513 | -0.000482157981535073 | -0.000179240261094445 | No |
| even | -0.000750855731462995 | -0.000458846398602338 | -0.000319774633018096 | No |

The table shows outward upper bounds for the new witnesses, computed by the independent compact interval verifier. The rank-2 inverse information improves the optimistic ceiling, particularly in the even sector, but **even that ceiling remains negative**. Thus DIR-5 excludes every response matrix X and every PSD error penalty using these retained T,M,K_upper,V_hat objects. This is stronger than a failed search for selected X, and is not merely another scalar-parameter obstruction.

The fresh coefficient combinations (1,1) and (1,-1) were also independently interval-checked. Their new cap upper bounds are approximately -0.001245342027326751 and -0.000077454457932267 in the odd sector, and -0.001547501982859394 and -0.000009740080381462 in the even sector. All eight tested directions are strictly negative as exact rational inequalities.

The actual paid rank-2 correction lower has diagonal entries approximately (-0.0002114608,-0.0001423009) in the odd sector and (-0.0002377042,-0.0002564052) in the even sector. These signed lower matrices are not substituted by their positive parts; the valid zero correction is selected. Mixed-action errors remain substantial relative to the actual observed couplings. The result supplies no negative original-source test and no positivity certificate.

`DIRECTIONAL_INVERSE_RECEIPT.json` contains the compact retained-data enclosures and exact rational obstruction witnesses. It is independently rechecked by `directional_source_inverse_probe.py --verify`. The complete unrounded raw run is archived separately at `receipts/directional-inverse-J24.json.gz`, with SHA256 recorded in the compact receipt, and is reproducible with the explicit source-replay command; its large generated fractions are separated from the reviewed interface.

The J12 preflight used parent-fitted residuals and the same fixed auxiliary levels1,2. Its mixed-action error radii exceeded several nominal couplings, so the interval correction was indefinite and was not used. That failure is retained as a resolution/domain-budget observation, not promoted to an intrinsic impossibility of directional inverse methods.

Fresh validation uses J5 and high levels3,4, absent from fitting and the retained auxiliary family. Full signed source pairings from the archived exponential integrator intersect the independent continuum action intervals in both parities. Changing the contact by1 produces disjoint source intervals. Exact finite controls recover D^-1 when W spans the full positive excess, check all sixteen corners of an interval response matrix, and exhibit the false-global-gap counterexample above.

## 7. Classical predecessor and exact remaining lemma

The general operator ingredients are classical form Cauchy–Schwarz, positive resolvent order, Schur/shorting and finite-rank inversion. Anderson and Trapp, *Shorted Operators. II*, SIAM J. Appl. Math. 28(1), 60–71 (1975), DOI [10.1137/0128007](https://doi.org/10.1137/0128007), supplies the relevant classical Hilbert-space shorting context; its publisher abstract was checked. We do not claim a new general inverse theorem. The contribution is a source-attested realization with paid continuum errors and a wider, explicitly bounded failed-certificate family.

The next missing lemma is a source-valid high family or decomposition for which the actual residual response captures enough inverse energy **and** the mixed action error is small enough to give a useful matrix correction. A more optimistic finite PSD block does not establish that lemma. Larger families, different localized boundary packets or tighter source mixed-response enclosures are legitimate next probes; repeating scalar Young tuning on these fixed retained matrices is excluded.

| Claim | Ledger status | Boundary |
|---|---|---|
| DIR-1 coefficient-space residual identity | PROVED / CLASSICAL | U maps into Dom(D), actual source B, positive high inverse |
| DIR-2 finite-rank high inverse upper | PROVED / CLASSICAL | Global D>=kappa I and W⊂Dom(D), not finite PSD alone |
| DIR-3–4 source matrix enclosure | PROVED + EXACT SOURCE MODEL | Authenticated original channels; inherited global source/closure authority |
| DIR-5 all-response finite-family obstruction | PROVED / CLASSICAL ALGEBRA | Fixed retained T,M,K,V and PSD payments |
| All-response rank-2 source-family obstruction | TESTED EXACT SOURCE DATA + PROVED UNIVERSAL FAMILY BOUND | J24,M192, declared high levels1/2; original sign still OPEN |
| General mathematical novelty | NOT CLAIMED | Source realization/obstruction is a scoped repository advance |
| RH | UNVERIFIED | No all-radius source positivity proof |

Reproduce with `python -m unittest tests.test_directional_source_inverse -q` and `python scripts/directional_source_inverse_probe.py --verify --source-holdouts --reconstruct-pr178`. A full original-source rerun is explicitly requested with `--run-source --output <receipt.json> --raw-gzip <raw.json.gz>`; it performs one J24 source calculation rather than one per trial coefficient.

Validation performed before commit: the 8-test prior Gamma suite passed before development; the new 8-test directional suite and prior suite passed together (16 tests). The compact exact verifier, fresh source holdouts and pinned PR178 reconstruction passed. No full-suite claim is made by this isolated lane; the coordinator owns integrated regression validation.

Hostile arithmetic audit found and repaired a generic checker-domain omission: DIR-5 needs M>=0, and the initial validator assumed the source Gram premise without enforcing it on arbitrary API input. The exact mutant T=-2I, M=-I, K=I, V=0, kappa=1 has a negative optimistic cap but becomes positive at eta=2, so it must be rejected. The checker now certifies M>=0 from the entire interval enclosure before claiming the universal obstruction. All actual retained source M enclosures pass this stronger check; no source result changed. The sealed-receipt path also verifies the recorded raw-gzip SHA256 and rejects missing or changed archives. This checks archive integrity, not identification with the canonical Weil source.
