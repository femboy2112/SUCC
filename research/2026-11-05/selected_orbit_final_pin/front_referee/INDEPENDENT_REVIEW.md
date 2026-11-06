# Independent hostile review of candidate claims

This is a separate agent's mathematical derivation and countermodel audit,
with shared model family and inherited repository source. It is not a Lean
proof, external scholarly referee report, or a proof of either moonshot.
No new front was read before the initial entropy/countermodel derivation.

**Review policy:** no defect found is not automatic certification. Where no
counterexample or proof error was found, the final promotion verdict remains
**UNVERIFIED pending independent certification**. The explicitly written
second derivations below are paper evidence, with their precise scope.

## #518 pressure criterion

Reviewed `research/2026-11-05/yoneda_circle/PROOFS.md` at parent749931f0.
The cell-constant Cauchy-Schwarz proof handles boundary atoms without silently
assuming weak convergence of half-open cell masses. It takes the time limit
at fixed depth before increasing depth. Its invariant L1 density argument is
valid by the Fourier identity mu_hat(h)=mu_hat(16^j h) and Riemann-Lebesgue.
The criterion is conditional and equivalent to normality under invariance;
none of these checks pays its arithmetic premise. R1–R3 in this front give an
independently derived weaker growth-envelope version.

## Alpha macro-carry bound

Reviewed `front_alpha/PROOFS.md`, SHA256
`95e7391e0c8c931738fad2c0b0e1b4e6495ab0b901da49ef8456d1ee944b8a6c`.
With B=16^m and q=C(B-1)/(15(A+1)^2), a correction gives
x_(n+m)<R_m(n)<=q. The kth subsequent macro transition has positive unwrapped
upper comparison q(1+B+...+B^k)=C(B^(k+1)-1)/(15(A+1)^2).
For1<=k<=L-1 this is <1. Hence successive corrections in a residue class are
at least L macro steps apart. Packing at most ceil(A/m) starts yields exactly
m ceil(A/(mL)). The floor and the strict inequality at threshold are correct.
For label histograms, max coordinate difference<=E/A and sum(p+q)=2 give
pressure difference<=2BE/A. This is useful finite transport at fixed m.

The coherent completion has W=K=B-1 and no corrections for all large n.
The same statement holds for nonintegral odd-denominator periodic completions
by their positive distance from radix boundaries. They have pressure>=B/p.
These countermodels PROVE that the proposed inference from rare/absent
corrections to bounded cell pressure is false. The auxiliary inequality itself
is seed-uniform, not a source-selected normality advance. The zero-seed count
of accumulated carries remains unpaid.

## Delta regularized cut

Reviewed `front_delta/PROOFS.md`, SHA256
`5f5080736bd3cb6fd308a6b0fe42b5ac3985e2590657c1ff0efa975298c75324`.
For g_r=log|1-r e(t)|^2, the mean is zero and the primitive is
−sum r^h sin(2pi h t)/(pi h^2). A cross interval Q=16^b−delta leaves the
NEGATIVE short interval [alpha−delta,alpha], not a positive one.
Its normalized absolute contribution is at most
(16B_r/15)16^(-a-b). Summing a>=1,b>=0 gives256B_r/3375.
The past-pair count is t(t−1)/2; the unforced center value is2log(1−r),
so the stated linear-cut limit c^2 log(1−r) and error constants follow.
The bound sum q_ij16^-2A<A/15, together with mean distance length/2,
gives the exact Lipschitz error LIP_r/(30A).

Independently expanding sum_(i<j)cos gives (|sum e|^2−A)/2, hence
E=−sum_(h>=1)(r^h/h)|c_A(h)|^2−log(1−r)/A. Absolute summability makes one
fixed r sufficient and equivalent to fixed-h Weyl. This is strictly less
singular than GateC and removes infinite seed resolution. It is an exact
representation relative to GateA; the selected-source lower bound is OPEN.

The interval implementation was read, not fully rerun here. Its midpoint
remainder uses sup|g_r''|<=8pi^2 r/(1−r)^2 and the correct1/(24 panels^2)
normalized quadrature factor. Its Green remainder also has an independent
integral proof: write r(n)=integral_0^1 t^(8n−8)g(t)dt with
`g(t)=(1-t)(4+4t+4t^2+2t^3+t^4)`; since the bracket<=15 and16−t^8>=15,
`T_n=integral t^(8n)g(t)/(16−t^8)dt <=1/[(8n+1)(8n+2)]`.
This supports the analytic enclosure design, not a formal verification of
mpmath or an independent execution of the entire receipt.

## Separate RH local Volterra estimate

Reviewed `prime_jet_volterra/PROOFS.md`, SHA256
`095a7695cec393573a3adc4483ad21b1cc645e6f0bcc8670cb5842f3a3f14a60`.
A derivation from the coordinator's formula preceded reading this proof file.
For f in H1_0(0,D), D=a+delta, define p(s)=f'(s), q(t)=−f'(D−t).
Fubini on s<=x<=delta−t gives the kernel(delta−s−t)+ with the
conjugation exactly as stated. Its squared HS norm isdelta^4/12.
The endpoint derivative intervals are disjoint because delta<a, so
2||p||||q||<=||f'||^2. The single-shift coefficient1/sqrt12 is valid.

For two widths u<=v, direct integration gives
integral_0^u z(u−z)(v−z)dz=u^3(2v−u)/12. Summing weighted kernels therefore
gives the claimed joint coefficient; all original prime-power weights remain
in the formula. For D<2log2 every active endpoint interval has width<D/2.
The estimate is source-blind as an analytic inequality. The prime-weight
specialization and completed Gamma/pole form must remain separately typed.

The modulation f_R=e^(iRx)phi independently refutes uniform absorption of an
H1 derivative norm into Gamma+pole: the derivative cost grows quadratically;
the translated Fourier mass sees logarithmic digamma growth; compact smooth
support makes the two pole transforms rapidly decreasing. This defeats that
coercivity proof route, not RH or Weil positivity. No claim of improving the
published completed-form positivity range is justified by this local estimate.

## Promotion boundary

The countermodel no-go claims have explicit receipts. The candidate analytic
lemmas have written first and second derivations but no kernel or external
certification. None supplies a new zero-selected signed/unsigned asymptotic
inequality. The remaining claims BBP normality, selected pressure growth zero,
selected regularized energy nonnegativity, and completed Weil positivity are
OPEN/UNVERIFIED.
