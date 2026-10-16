# Authentic Schur response certificate — Arithmetic Resonance E

The authentic first-prime zero-shift bracket is improved on **both sides**.
The sign of the original short remains OPEN; RH is not proved. This is a
conditional paper proof with exact rational source-interval executions, not
an analytic theorem inferred from finite eigenvalues and not a Lean proof.

The worker started at `24d0f18a103fb2add32ee817fdfefb4ff401ed27` on
`research/arithmetic-wavefront-spectral-response-2026-10-16`. Only the assigned
new module, test, probe, this dossier and `arithmetic_resonance_receipts/resolvent*`
receipts are owned. No archives, prior modules or shared indexes are changed;
no commit, staging or push is performed. Other workers own concurrent files.

The protected source is `observational_succ/source_weil_hierarchy.py`, Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, SHA256
`183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`, from
`dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`. Both live and originating Git bytes
were checked. The founding 72-entry import manifest is a different lineage.
Read before edits: `AGENTS.md`, `docs/METHOD.md`, the manifest, Round II report,
handoff, source/compactness dossiers and hostile audit, and the actual source,
Legendre, shorting and residual modules. The conditional statements below use
OS-SOURCE-01/04, CG-02/03/05 and the inherited quotient/Douglas range theorem.
No new external source or zero-location data enters the construction.

**Definitions and inherited premises.** On I=(-1/2,1/2), H=L²₀(I;C), let G
be the original even signed Suzuki convolution compressed to H. Retain the
contact, both signed poles, the genuine prime-2 half density and one entire
real Gamma tower. Let l_k(t)=P_k(2t), P span l_1,...,l_4, Q=1-P,
A=PGP, b=QGP, D=QGQ. Let Vu(t)=integral from -1/2 to t of u(s)ds and K=V*V.
The inherited paper premises are

    D >= kappa QKQ,  kappa=20699/1000000,
    Ran b subset Ran D^(1/2),  ||g'||_1 < 11/40.

The probe replays the inherited exact scalar bounds supporting these premises;
it does not independently formalize the underlying Bessel, range or domain
proofs. Write R0=(D^(-1/2)b)*(D^(-1/2)b) and S0=A-R0. The coordinate metric is

    W=diag(1/3,1/5,1/7,1/9).

Every displayed finite matrix is a FORM in this metric. Reflection splits odd
indices (1,3) and even indices (2,4). All inequalities cover complex coefficients;
source matrices are real Hermitian. No bounded inverse of D at zero is assumed.

**E-01 — certified positive-shift residual error (conditional paper proof).**
For lambda>0, an arbitrary finite-column U:P H -> span(l_5,...,l_N) and
v=P-U, set

    R_lambda=b*(D+lambda)^(-1)b,
    L_lambda=U*b+b*U-U*(D+lambda)U,
    r_lambda=b-(D+lambda)U=QGv-lambda U.

Expanding the square with the bounded inverse of D+lambda proves exactly

    R_lambda-L_lambda = r_lambda*(D+lambda)^(-1)r_lambda,
    0 <= R_lambda-L_lambda <= r_lambda*r_lambda/lambda.       (E.1)

No exact Galerkin equation is required: rounding or a shifted/midpoint solve
merely changes the admissible U. This identity accounts for its actual residual.
For M>=N let z_q=<l_q,Gv>-lambda<l_q,U>, q=5,...,M. Parseval gives

    r_lambda*r_lambda
       = sum_{q=5}^M (2q+1) z_q* z_q
         + [(1-P_M)Gv]*[(1-P_M)Gv].                         (E.2)

The second term is orthogonal to the finite residual, so no artificial
factor two is needed. From the weighted Legendre inequality in CG-03,

    ||(1-P_M)Gf||² <= ||g'||_1²/[4(M+1)(M+2)] ||f||².

It follows that (E.2) is at most C_M, the finite residual Gram upper plus

    [121/(6400(M+1)(M+2))] v*v.                              (E.3)

All finite z_q entries include the entire Gamma source through entry intervals.
For midpoint matrices with symmetric interval error, the maximum absolute
row sum of radii is an operator-norm error. Apply it separately in each parity
sector to enclose the finite Gram. This proves a rational C_M without any
sample-only quadrature. Combining (E.1) with H_lambda=v*Gv+lambda U*U gives

    H_lambda-C_M/lambda <= S_lambda=A-R_lambda <= H_lambda.  (E.4)

The probe executes lambda=1/100 and 1/1000, M=20 on a frozen degree-16 shifted
trial and records every matrix and both generalized error caps. These are
bounds for positive shift only. S_lambda decreases to S0, but the lower side
of (E.4) is NOT a lower bound for S0. No regularization rate is asserted.

The inherited exact hidden-mode control D=K=diag(j^-2), b_m=e_m/m, A=1/2
has R0=1 but R_lambda=1/(1+lambda m²). Its negative S0=-1/2 is compatible with
positive S_lambda at large m. This is a synthetic changing-cross-source
counterexample to a missing uniform gap estimate, not a Suzuki negative vector
and not a failure of fixed-source Galerkin convergence. The receipt labels it
accordingly. The new genuine lower bound below uses a different argument.

**E-02 — exact source calculation and degree-20 upper (paper proof + exact
computation).** The finite-J source matrix uses the existing authenticated
prime/contact/pole primitives. For the Gamma pairs a second integration
representation is used: form the exact polynomial

    rho_ij(t)=integral[-1/2,1/2-t]
              [l_i(y+t)l_j(y)+l_j(y+t)l_i(y)]dy,  0<=t<=1.

Then the OU pair is integral_0^1 rho_ij(t) exp(-alpha t)dt. For monomial t^k
its value is A_k+B_k exp(-alpha), with

    A_0=1/alpha, B_0=-1/alpha,
    A_k=k A_(k-1)/alpha, B_k=(k B_(k-1)-1)/alpha.

Thus every algebraic coefficient is rational. For alpha<=256 reuse the
inherited directed Taylor exponential; above 256, 0<exp(-alpha)<2^-floor(alpha)
suffices, including either sign of B. Exact controls agree with the independent
inherited two-variable antiderivative coefficients for low and higher degrees
and small/large alpha. Both representations share the same source provenance.

The genuine omitted Gamma operator on mean-zero inputs is positive and obeys

    0 <= G-G_J <= tau_J I,
    tau_J=2/(4J+1)²+16/(4J+1)³.

Consequently, if H_J=v*G_J v and V=v*v,

    H_J^- <= H_U=v*Gv <= H_J^+ + tau_J V.                   (E.5)

This Loewner propagation avoids unnecessary independent-entry inflation of the
positive tail. It does not add an invented positive source channel. Selection
uses exact rational midpoint solves at J=64 in two parity sectors, checks each
solve equation exactly, and rounds U to denominator 10^10. All candidates
(degrees 12,16,20, and degree16 at shift1/100) are saved and hashed **before**
J=512 certificate evaluation. Candidate selection is not proof. There is no
spatial quadrature in these source pairings.

The best frozen degree-20 trial gives the exact operator upper caps

    S0_odd  <= (300761/1073741824) I_odd,
    S0_even <= (11742983/8589934592) I_even.

These are about 0.000280105509 and 0.001367063145, improving the inherited
1939731/4294967296 and 3654297/2147483648 respectively. For each sector the
receipt contains the exact 2x2 form H+, metric W_p, and PSD slack c W_p-H+_p.
The acceptance tests use both diagonals and determinant, not floating eigenvalues.
The exact source order is S0<=H_U<=H+. A positive upper does not prove S0>=0.

The unshifted degree12/16 caps were also certified and retained. The degree16
candidate selected at lambda=1/100 has a worse zero-shift upper; it is retained
for its positive-shift response experiment, not silently declared an improvement.

**E-03 — genuine improved zero-shift lower at U=0 (conditional paper proof
with exact full-source integration bounds).** This additional direction was
suggested by the principal. The quotient residual identity and D>=kappa K_Q
imply for x in PH

    <x,R0 x> <= kappa^-1 ||Pi_M (Gx)'||²
              <= kappa^-1 ||(Gx)'||²,
    M={f: integral t^j f(t)dt=0, j=0,...,3}.                 (E.6)

No questionable derivative of Q is inserted: Pi_M is the actual quotient
projection, used only through its contraction. Define T_J x=(G_J x)'. For
k=1,...,4, |P_k(t)|<=1 on [-1,1]. This can be checked directly from the four
polynomials: their interior extrema have absolute values at most 1/2 for P2,
1/sqrt(5) for P3, and 3/8 or 3/7 for P4. The inherited measure bound

    total variation(g_J'') <= V_J=16+8 sum_{j<J} 1/(4j+1)

therefore makes each (G_J l_k)' Lipschitz with constant V_J. There are no
uncontrolled prime-threshold gaps: the finite measure includes the actual
prime atoms, contact and signed source channels.

On a cell of width h centered at x_i, a rigorous point interval gives
m_i=max(|lo_i|,|hi_i|). For every point of the entire cell,

    |(G_J l_k)'(x)| <= m_i+V_J|x-x_i|.

Integrating the square exactly gives the cell upper

    h m_i² + m_i V_J h²/2 + V_J² h³/12.                    (E.7)

The implementation uses J=20 and 512 equal cells, with exact reflection reuse
of the positive half. It records the point intervals, midpoint contribution,
linear and quadratic between-cell errors separately. Every point enclosure
uses the original derivative primitive; no floating fitting enters this bound.

For sector p with normalized basis e_k=sqrt(2k+1)l_k, let

    t_p=sum_{k in p} (2k+1) E_(k,J),

where E_(k,J) is the whole-interval sum of (E.7). The Hilbert-Schmidt inequality
bounds ||T_J|p||<=sqrt(t_p). The ENTIRE omitted differentiated Gamma ladder has
whole-line L1 norm at most

    eta_J=2/(4J+1)+8/(4J+1)².

Young's inequality bounds the tail OPERATOR norm by eta_J, so no extra sector
rank factor is necessary. Minkowski now gives

    ||T_full|p|| <= sqrt(t_p)+eta_J,
    R0|p <= c_p I_p,
    c_p=(s_p+eta_J)²/kappa,  s_p²>=t_p.                    (E.8)

s_p is a directed rational square-root upper on denominator10^12, computed
with integer square root and an exact final comparison. Reflection maps input
parities to opposite derivative parities, hence the two ranges are orthogonal
and the sector bounds combine without cross-sector terms.

The actual exact caps c_p are stored in the packet; decimal displays are

    c_odd  ~= 0.454907537727 < 455/1000,
    c_even ~= 0.848146850190 < 849/1000.

Both strictly improve the inherited common 75625/20699 ~= 3.653558142905.
Let A^- be the exact interval lower of the finite-J=512 low source block.
Since the missing Gamma is positive, A^-<=A_J<=A. The new fully rational
zero-shift bracket is

    A^- - diag(c_odd/3,c_even/5,c_odd/7,c_even/9)
           <= S0 <= H+.                                  (E.9)

The packet fields `exactlower` and `exactupper` give these complete matrices,
not decimal summaries. The lower is still negative and does not resolve the
sign. The entire Gamma derivative tail is closed for this U=0 bound. The
relative residual of a useful higher-degree response and a shift-to-zero rate
remain separate unresolved obligations.

**E-04 — retained unsuccessful routes and source-interface defect.** The
finite-family attempt allowed every complex coefficient in
l_2+span(l_6,l_8,...,l_N), for N=12 and16. The quotient residual was bounded
below by the variational restriction to l_6,l_8,...,l_20 with its exact K Gram.
Thus G_trial-kappa^-1 C*K_probe^-1 C is an upper form for the sufficient lower
criterion. At J=512 its interval row-radius majorants (about .00144355 and
.00199110) did not certify negative definiteness. Results are UNRESOLVED,
not an all-family no-go, not evidence of source negativity, and not a repeated
degree-eight experiment. No larger budget was spent on this failed route.

The hostile auditor found a real defect in the initial `shifted_certificate`:
an optional external upper certificate was accepted after checking only its
candidate hash and J. Forged H=1000 W and V=U=0 could then acquire source status.
The exploit was executed and is preserved in
`resolvent-auditor-failed-regression.json`. The API now has **no external upper
parameter** and regenerates the full source upper internally. A regression
rejects the previously accepted call. This fix does not rely on hash validation
of caller-supplied mathematical claims.

A first live-runtime guard mistakenly treated a compiled module-level generator
expression as a named function binding and rejected the healthy source. The
independent auditor retained that initial failure. The correction checks named
bindings and original interval methods against compiled pinned bytes, plus
SCALE, Fraction and prime tape. Cold and warm healthy calls pass, while changed
runtime source functions or constants are rejected even on cached entries and
parity-zero calls. This is a runtime integrity check, not a sandbox against
arbitrary hostile mutation of Python itself. Byte pinning alone is never called
an external-source correctness theorem.

**Packet, tests and replay.** `scripts/arithmetic_resolvent_probe.py` requires
`--output PATH`, creates its parent, and writes an execution receipt plus adjacent
`-candidates.json` and `-packet.json`. There is no implicit default write target.
The packet is deterministic, without timestamps, wall time, machine paths or
interpreter-specific metadata. Its source identity, radius, W metric, exact
lower/upper forms, separated error budgets and incomplete-gap/debt fields are
explicit. Execution metadata and raw focused-test logs belong to the receipt.
Before/after hashes cover source dependencies and all four owned files. A packet
is accepted by the probe only if all source/stability/test/improvement gates pass.

The focused suite has 26 tests covering the alternate OU integration identity,
true-source primitive overlap, whole-Gamma enclosures, exact solves, frozen
candidate integrity, parity, all corners of an interval-majorant control, W
metrics, independent 2x2 cap slack, nonorthonormal residual completion, zero-shift
counterexamples, Lipschitz integration, directed square roots, lower-tail
propagation, runtime mutation and forged-certificate rejection. These are exact
finite controls, not a kernel proof or independent source lineage.

Run serially, with no compiler or heavy worker spawned:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
 /tmp/succ-proof-teeth-py313/bin/python -B scripts/arithmetic_resolvent_probe.py \
 --output research/2026-10-16/arithmetic_resonance_receipts/resolvent-final-py313.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
 /tmp/succ-proof-teeth-py310/bin/python -B scripts/arithmetic_resolvent_probe.py \
 --output research/2026-10-16/arithmetic_resonance_receipts/resolvent-final-py310.json
```

Full suites, CI, integration, commits and publication belong to the principal.
Initial candidate, upper, lower, failed-family and failure receipts remain intact.
Final execution counts and exact bytes are authoritative in the final receipts;
no historical successful run is attributed to subsequently edited code.

The next useful discriminator is an authenticated relative-residual bound for
an improved high trial, or actual adjoint/fractional source-range information
from the other lane. Neither the improved bracket nor a positive-shift estimate
settles those questions. The source, analytic premises and computational trust
base remain separated in the packet and in each claim above.
