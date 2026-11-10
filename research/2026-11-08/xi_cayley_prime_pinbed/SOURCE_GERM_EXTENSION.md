# Original-source germ crosses the Euler horodisk: an inherited Li theorem in Cayley geometry

**2026-11-08 · Exact corollary, no new RH positivity.**
SUCC base: \`main@43a607818907120d4cdab73d240f5b4d7700b63f\`.
This is a source-anchored consequence of **existing** [Euler–Mascheroni / completed Li source work](../../../handoffs/rh/2026-10-24-euler-mascheroni-completed-li.md) and the Cayley transformation in [PROOFS.md](PROOFS.md). The inherited source-germ estimate must be audited in its originating proof before promoting its external authority. **RH PROVED: NO.**

## SG-1 — transferable source-germ zero exclusion (conditional elementary theorem)

Let \(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\) be the **actual** completed zeta function, and
\[
G(s)=\zeta(s)-\frac1{s-1}.
\]
Suppose on the closed analytic disk \(|u|\le\delta<1\) one has a *genuinely source-certified* bound
\[
|G(1+u)|\le M,\qquad \delta M<1.
\]
Since \(\zeta(1+u)=u^{-1}+G(1+u)\) and the pole is removable in the completion,
\[
\xi(1+u)
=\frac12(1+u)\pi^{-(1+u)/2}
\Gamma((1+u)/2)\,[1+uG(1+u)].
\]
All factors are nonzero for \(|u|\le\delta\): \(|1+u|\ge1-\delta>0\), \(\Gamma((1+u)/2)\) has no zero or pole in the right half-plane, and
\[
|1+uG(1+u)|\ge1-\delta M>0.
\]
Therefore **the original completed xi is zero-free on the entire closed source disk** \(|s-1|\le\delta\).

Under the Cayley map \(s=1/(1-w)\), \(|s-1|=|w/(1-w)|\le r/(1-r)\) for \(|w|\le r<1\). Consequently,
\[
\boxed{r\le\frac{\delta}{1+\delta}\quad\Longrightarrow\quad
2\xi(1/(1-w))\ne0\ \text{for every }|w|\le r.}
\]
This is a true *source-derived* zero-free pin-bed certificate, but it is local. It does not certify the whole unit disk.

## SG-2 — instantiate the existing SUCC finite-cell arithmetic bound

SUCC's [2026-10-24 handoff](../../../handoffs/rh/2026-10-24-euler-mascheroni-completed-li.md) records a **paper proof** that the actual regularized \(G\) obeys
\[
|G(1+u)|\le5/3,\qquad |u|\le1/4.
\]
(The same estimate is calibrated against the centered/uncentered original integer Dirichlet-source cell cutoffs; it is not assumed for synthetic shifted Euler factors.)

Here \(\delta=1/4,\ M=5/3\), hence \(\delta M=5/12<1\) and
\[
\boxed{F(w)=2\xi(1/(1-w))\ne0\quad\text{for all }|w|\le1/5.}
\]

This disk is **not contained** in the unshifted Euler-product horodisk \(H_1=\{|w-1/2|<1/2\}\): for instance \(w=-1/5\) corresponds to \(s=5/6<1\), outside the absolutely convergent Euler product. The exact source-germ continuation crosses the earlier finite-access boundary without assuming RH. The Jensen defect satisfies \(J_\xi(r)=0\) for every \(0<r\le1/5\) by classical Jensen and the previous nonvanishing theorem.

**Status:** Proven local *corollary of an existing SUCC paper theorem*, not a newly proved prime zero-free region. The originating bound is independently referenced rather than rederived inside this branch. Any new all-radius RH claim needs an **actual extension of the source-certified bound**, not reuse of the same disk with new terminology.

## Next discriminatory probe

Use the source-faithful analytic Stieltjes/Gamma enclosure near \(s=1\) and a rigorously controlled Euler-prime/Gamma log on the original convergence horodisk, then build an overlapping atlas of nonvanishing neighborhoods. To enlarge the *circular* zero-free disk beyond \(r=1/5\), new overlapping source bounds or a certified Jensen integral upper estimate must actually pay for the additional region. Repeated finite disk images or unchanged \(\delta M=5/12\) do not constitute a new theorem. A hypothetical fake completed polynomial with zeros at \(s=1/4,3/4\) is not a counterexample to the inherited bound, because it does not match the actual regularized source \(G\).

**RH OPEN; original Euler product unchanged; half-density shifted products remain hostile controls only.**
