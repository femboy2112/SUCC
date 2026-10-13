# E37 — Archimedean Gamma boundary

## 1. Original question

Can a recorded factorial SUCC ladder legitimately yield Gamma through a
Mellin limit, and what additional identification is needed before calling
that limit an arithmetic completion? The faithful reading preserves finite
events and their boundary defect. It does not replace a finite transcript
with an already completed source. **RH PROVED: no.** This is an independent
first-generation dossier at SUCC parent
5eb09e7cba36ec01b8f9d6834b78b5766fd93935, branch
research/swm-e37-2026-10-13.

## 2. Existing mathematical context

The anchors are classical: [Gamma's Mellin integral and meromorphic
continuation](https://dlmf.nist.gov/5.2), [Euler's product
limit](https://dlmf.nist.gov/5.8.E1), [Beta's integral, for both real parts
positive](https://dlmf.nist.gov/5.12.E1), and [Gamma
recurrence](https://dlmf.nist.gov/5.5.E1). None is academic novelty.
The frozen SUCC_GAMMA_PRIME_PATH_GERMS.md already records the finite
recurrence defect and periodic-gauge ambiguity; FINITE_SUCC_HASSE_THETA_SEAM.md
records completion and trivial-zero jets. Their exact originating commit is
ba075348b7bcc66d938b3e0ca96c26e95bba340a in femboy2112/FuckingRH.
The receipt verifies six relevant manifest entries against that commit.
These archived documents and migrated modules share one provenance family;
agreement between them is not independent mathematical evidence.

## 3. Proposed SUCC objects

For each integer \(N\ge1\), retain the ordered events \(1,\ldots,N\), their
running products, and endpoint \(N!\). Define

\[
f_N(t)=(1-t/N)^N\mathbf1_{[0,N]}(t),\qquad
G_N(z)=\frac{N!N^z}{\prod_{j=0}^N(z+j)}.
\]

Use \(N^z=\exp(z\log N)\), with real logarithm. For measurable \(f\), define

\[
\mathcal M f(z)=\int_0^\infty t^{z-1}f(t)\,dt,
\quad t^{z-1}=\exp((z-1)\log t).
\]

The transcript-to-endpoint map forgets order; the endpoint-to-\(f_N\) map is
an explicitly chosen classical analytic realization. A physical observer
executing an infinite ladder is not a hypothesis or conclusion.

## 4. Candidate theorem

**CLASSICAL, with proof below.** For every \(N\ge1\) and every
\(z\in H=\{\Re z>0\}\), \(\mathcal Mf_N(z)=G_N(z)\).
For every compact \(K\subset H\) and every integer \(r\ge0\),

\[
\sup_{z\in K}|G_N^{(r)}(z)-\Gamma^{(r)}(z)|\longrightarrow0.
\]

Moreover \(G_N(z+1)/G_N(z)=Nz/(N+z+1)\), wherever both sides are defined;
it is a meromorphic identity after cancellation. The same approximants
converge locally uniformly on
\(\mathbb C\setminus\{0,-1,-2,\ldots\}\). This asserts compact convergence,
not uniformity on an entire unbounded half-plane or near moving poles.

## 5. Proof attempt

Substitute \(t=Nx\). Repeated integration by parts in
\(\int_0^1x^{z-1}(1-x)^Ndx\), including the terminal integral
\(\int_0^1x^{z+N-1}dx\), gives
\(N!/[z(z+1)\cdots(z+N)]\). The endpoint terms vanish for \(\Re z>0\).
Thus the transform equals \(G_N\), without using a Gamma quotient to prove
the identity it will later approximate.

For fixed \(t>0\), \(f_N(t)\to e^{-t}\), and
\(0\le f_N(t)\le e^{-t}\), since \(\log(1-u)\le-u\).
If \(a=\min_K\Re z>0\) and \(b=\max_K\Re z\), the difference of the
\(r\)-th transform derivatives has absolute integral bounded by

\[
\int_0^\infty(t^{a-1}+t^{b-1})|\log t|^r
                  |f_N(t)-e^{-t}|\,dt\longrightarrow0.
\]

The corresponding exponential majorant is integrable at both endpoints.
Dominated convergence proves the displayed supremum bound; local
domination also justifies holomorphy and differentiation under the
integral. For Gamma, integration by parts gives
\(\mathcal M(te^{-t})(z)=z\mathcal M(e^{-t})(z)\) on \(H\).
Cancelling finite products instead gives the finite defective ratio.

For compact \(K\) avoiding the nonpositive integers, choose one integer
\(k\) with \(K+k\subset H\). Exactly,

\[
G_N(z)=G_N(z+k)\prod_{j=0}^{k-1}\frac{N+z+j+1}{N(z+j)}.
\]

The finite correction converges uniformly on \(K\) to
\(\prod_j(z+j)^{-1}\). This proves continuation and local uniformity;
overlapping charts agree by recurrence. Residues follow by integration
around fixed small circles avoiding neighboring poles. No assertion about
analytic continuation follows from finite sampled equality alone.

For \(q\ge1\) integral, \(G_N(q)=(q-1)!\prod_{j=1}^q(1+j/N)^{-1}\).
Writing each factor as \(1-\delta_j\), with
\(\delta_j=j/(N+j)\), gives the rigorous finite bound
\[
0<(q-1)!-G_N(q)\le(q-1)!\frac{q(q+1)}{2N},
\]
because \(1-\prod_j(1-\delta_j)\le\sum_j\delta_j\).
At each fixed \(m\ge0\), for every \(N\ge\max(1,m)\), direct cancellation
gives
\(\operatorname{Res}_{z=-m}G_N=(-1)^m\binom NmN^{-m}\).
Its limit is \((-1)^m/m!\). Neither statement supplies arithmetic zeros.

## 6. Crucible

**REFUTED: every finite cutoff already obeys Gamma recurrence.** At
\(N=2,z=1\), \(G_2(1)=2/3\), \(G_2(2)=1/3\), and the ratio is \(1/2\).
For every positive integer \(q\), the exact deficit is
\(q(q+1)/(N+q+1)>0\). Independently expanding \(f_N\) as a polynomial and
integrating each monomial gives rational positive controls in the probe.

**REFUTED: factorial values and recurrence identify Gamma.** For any
nonzero real \(\epsilon\),
\(\Gamma_\epsilon(z)=\Gamma(z)e^{\epsilon\sin(2\pi z)}\) has the same
recurrence and positive-integer values, but
\(\Gamma_\epsilon(1/4)=e^\epsilon\Gamma(1/4)\). Positive-real
log-convexity is an additional selector in
[Bohr–Mollerup](https://dlmf.nist.gov/5.5.iv).

**REFUTED: sampled functional equations identify completion or zeros.**
For any finite sample set \(S\), the nonzero symmetric polynomial

\[
P_S(s)=[s(s-1)]^2\prod_{a\in S}[(s-a)(s-(1-a))]^2
\]

vanishes with its first derivative at all samples and reflected samples.
Thus \(\xi+\epsilon P_S\) preserves those values, jets, normalization at
0 and 1, and even global reflection symmetry. Separately
\((s-1/4)(s-3/4)\) is entire and symmetric with off-line roots inside the
critical strip. These are countermodels to the stated implication, not
arithmetic zeta functions. Higher finite jet orders merely require higher
powers. No nontrivial zeta zero is a construction input.

**CLASSICAL cancellation boundary.** For each \(m\ge1\), take a disk
about \(-2m\) of radius less than 1. Classical zeta reflection
and nonvanishing of \(\zeta(2m+1)\) give a simple zero there:
the sine factor has order one while the other factors are analytic and
nonzero at the center. \(\Gamma(s/2)\) has a simple pole with leading term
\(2(-1)^m/[m!(s+2m)]\). Consequently \(\Gamma(s/2)\zeta(s)\)
extends holomorphically with value
\(2(-1)^m\zeta'(-2m)/m!\).
[The functional equation](https://dlmf.nist.gov/25.4.E2) supplies the
arithmetic order; the Gamma residue alone does not.

## 7. Verdict

**SURVIVES, CLASSICAL:** a fully specified Mellin realization, compact
convergence with all fixed derivative orders, and lawful continuation.
**FAILS, REFUTED:** finite recurrence perfection, Gamma identification
from factorials alone, and completion/zero identification from sampled
symmetry. **TESTED MODEL:** the bounded exact-rational implementation,
with its raw witnesses in the receipt. The proof and code share this
investigator; computation checks algebra, rather than independently
certifying the universal analytic theorem.

The predictive comparison is qualitative: integer values and recurrence
leave canonical Gamma and periodic gauges indistinguishable; evaluation
at \(1/4\) separates the displayed pair. Finite samples leave the symmetric
perturbation indistinguishable; a fresh \(1/4\) value separates the chosen
polynomial. Here κ is exact symbolic contact, φ is scoped identification,
σ retains source lineage, and ρ supplies no evidentiary weight. No
probabilities or phasor phases are assigned.

## 8. Remaining obstruction

Gamma is compatible with many arithmetic sources. For the matched
non-Euler control \(D(s)=\zeta(s)+6^{-s}\), \(a(6)=2\) while all other
coefficients remain 1. Its connected coefficient at 6 is
\(a(6)-a(2)a(3)=1\), compared with 0 for zeta. Completing with zeta's
Gamma leaves at \(-2m\) an extra nonzero residue
\(2(-1)^m6^{2m}\pi^m/m!\). A counterfeit composite Euler base 6 likewise
passes the same Gamma calculation but fails this source test.
This is a necessary identification control, not an arithmetic bridge.

## 9. Cross-domain connection with actual maps

For locally absolutely continuous \(f\), suppose on every compact
substrip \(a<\alpha\le\beta<b\) that
\((t^{\alpha-1}+t^{\beta-1})(|f|+t|f'|)\) is integrable and
\(t^\sigma f(t)\to0\) at both endpoints for every \(a<\sigma<b\).
Then \(\mathcal M(-tf')(z)=z\mathcal Mf(z)\) on that strip. Multiplication
by \(t\) instead gives \(\mathcal M(tf)(z)=\mathcal Mf(z+1)\) wherever
both transforms converge. For \(f=e^{-t}\), the differential equation
\(-f'=f\) identifies these arrows. This is a concrete differential-to-
successor transport, not a generic SUCC law.

There is also an actual test-space limit. Write
**Quotient premise made explicit after independent review:** Gamma has no zeros ([DLMF §5.2](https://dlmf.nist.gov/5.2)); alternatively Hurwitz applied to the zero-free G_N on Re(z)>0 and Gamma(1)=1 proves this here. Compact-uniform derivative convergence therefore implies G_N′/G_N → Gamma′/Gamma on this half-plane.

\(\psi_N(z)=G'_N/G_N=\log N-\sum_{j=0}^N(z+j)^{-1}\).
For each fixed \(\sigma>0\), uniformly in \(N\ge1,t\in\mathbb R\),
\[
|\psi_N(\sigma+it)|\le C_\sigma+\log(2+|t|).
\]
Indeed \(\log N-H_N\) is bounded; in
\(\psi_N=\log N-H_N-1/z+\sum_{j=1}^Nz/[j(z+j)]\),
split at \(j=|z|\). The first part is bounded by a harmonic sum because
\(|z+j|\ge|z|\); the tail is bounded by \(|z|\sum_{j>|z|}j^{-2}\).
Pointwise derivative convergence and this majorant imply, for every
\(h\in\mathcal S(\mathbb R)\), convergence of the integral of
\(\psi_N(\sigma+it)h(t)\) to that with \(\psi\).
This **CLASSICAL** distributional limit is only the Archimedean term.

## 10. Deliverables

New E37 dossier, standalone standard-library exact probe, and JSON receipt;
no imported path changes. The smallest remaining bridge lemma is a
source-derived identification on a declared common Mellin test core,
including the pole subtraction, conductor, half-density and phase, with
uniform form bounds and fake/non-Euler controls. Concretely, an
independently constructed pairing must equal the completed Weil pairing
on \(C_c^\infty(\mathbb R)\) in logarithmic coordinates; no such pairing
is constructed here. Positive completed-Weil
identification remains **CONJECTURE**. No RH advance, completed-source
certificate, infinite physical execution, or floating-point proof is claimed.
