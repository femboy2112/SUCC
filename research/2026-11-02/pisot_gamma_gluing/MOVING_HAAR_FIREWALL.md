# PG-10 — moving Pell frame can look Haar while retaining non-Haar original information

**Exact classical Fourier countermodel, specialized to the unimodular silver-Pisot carrier.** This is a probe/source-map firewall, NOT a counterexample to normality of the actual π orbit. It connects the user's "rotated Fourier observer" intuition to a rigorously typed limit-order issue.

Let the P_k from PG-01 be the primitive integer Pell coordinates (P_0=P_1=1, P_(k+2)=2P_(k+1)+P_k). Their consecutive pairs are coprime by the unimodular determinant, and P_(k+1)/P_k→λ=1+√2.

Consider the explicit NON-HAAR probability measure on the ordinary circle T=R/Z:
\[
d\mu(x)=(1+\cos(2\pi x))\,dx.
\]
It is nonnegative, total mass one, and its circle Fourier coefficients obey
\[
\widehat\mu(0)=1,\quad
\widehat\mu(\pm1)=\tfrac12,\quad
\widehat\mu(m)=0 \text{ for every integer }|m|\ge2.
\]
At each k define the two-coordinate rotating/Pell observer
\[
F_k:T\longrightarrow T^2,\qquad
F_k(x)=(P_kx,P_{k+1}x)\pmod1,\qquad
\nu_k=(F_k)_*\mu.
\]

**Theorem PG-10A (fixed-probe apparent Haar):**
For every FIXED integer pair (a,b)≠(0,0),
\[
\widehat\nu_k(a,b)
=\widehat\mu(aP_k+bP_{k+1})=0
\quad\text{for all sufficiently large }k.
\]
Proof: if b≠0, \((aP_k+bP_{k+1})/P_k\to a+bλ\ne0\) because λ irrational; if b=0 then a≠0 and |aP_k|→∞. Therefore the integer index eventually has modulus ≥2, and the source μ has exactly zero Fourier coefficient at that index. Classical character density then gives
\[
\boxed{\nu_k\Longrightarrow\mathrm{Haar}_{T^2}\quad(k\to\infty).}
\]
Each individual ν_k is supported on a 1D closed subgroup (with a nonuniform density); its weak limit is the full 2D Haar probability. This is genuine weak-* convergence, not total-variation or entropy convergence.

**Theorem PG-10B (selected moving inverse detects the hidden non-Haar mode):**
Let u_k,v_k be the exact Bézout coefficients, u_kP_k+v_kP_(k+1)=1. Then for EVERY k,
\[
\boxed{
\widehat\nu_k(u_k,v_k)
=\widehat\mu(1)=\tfrac12.
}
\]
The dual probe (u_k,v_k) is MOVING and grows exponentially. Thus the sequence of Haar-looking observers hides a persistent non-Haar Fourier harmonic inaccessible to every fixed observer frequency at large k. This is exactly the information-loss mechanism that SUCC's causal-response-rotation, entropy and rotated-Fourier firewalls warned about, now with an explicit **integral Pisot/Pell phase-space frame and exact inverse**.

**Critical scope:** μ is NOT ×16 invariant. Any non-Haar ×16-invariant measure cannot be Rajchman: \(\widehat\mu(16^j h)=\widehat\mu(h)\) for every fixed h, so Fourier decay at infinity would force Haar. Hence this constructed μ is a **universal inference countermodel**, not an original BBP dynamical countermodel. No conclusion about the true selected π orbit follows.

**Research consequence:** Never infer original selected Weyl cancellation solely from (a) weak 2D Haar of a moving Pisot observer, (b) cancellation of finitely many fixed high-frame Fourier tests, or (c) independently small Fourier marginals. An actual proof must retain the moving source-attested Bézout character or prove a separate, non-tautological arithmetic bound on its signed time average; that average is the original Weyl quantity. This theorem is a precise probe limitation, not a new saving.
