# The circle is a Fourier line and a positive analytic sheet — typed, exact, non-mystical

**Scope:** Classical Fourier/Bergman/Gram geometry instantiated on original BBP \(\pi\) orbit. No π normality or physical quantum claim. Complements the source Laplace line→convolution sheet LS-01/02 in PROOFS.md.

## Two geometrically distinct sheet constructions

**A. Analytic Γ sheet.** The line \(D(s)=\int e^{-st}\kappa(t)dt\) produces the two-variable positive sheet \(\kappa(u)\kappa(v)/16\). Diagonal fibers \(u+v=t\) yield \(Q_{\rm sheet}(t)=(\kappa*\kappa)(t)/16\). The *source-authentic* BBP kernel \(Q_{\rm BBP}(t)\) is now proved strictly pointwise dominated for all t>0. The defect \(W(s)>0\) is completely monotone at all real s>0. This is positivity in the CONTINUUM SOURCE scale, not a temporal signed Fourier bound.

**B. A circle boundary with a real two-dimensional disk observer.** For the completed authentic orbit \(x_n=\{16^n\pi/16\}\in\mathbb T\), write \(c_N(m)=N^{-1}\sum_{n<N}e(mx_n)\), \(e(t)=\exp(2\pi it)\). The usual Fejér pair energy is

\[
E_{N,H}=1+2\sum_{m=1}^H\left(1-\frac{m}{H+1}\right)|c_N(m)|^2.
\]

Construct the holomorphic polynomial on the genuine UNIT DISK \(\mathbb D\subset\mathbb C\):

\[
\boxed{G_{N,H}(z)=
\sqrt2\sum_{m=1}^H
\sqrt{(m+1)\left(1-\frac{m}{H+1}\right)}\ c_N(m)z^m.}
\]

Angular orthogonality and the exact elementary disk integral \(\frac1\pi\int_{\mathbb D}|z|^{2m}\,dA=1/(m+1)\) give a **perfect disk-area identity**

\[
\boxed{E_{N,H}-1=\frac1\pi\int_{|z|<1}|G_{N,H}(z)|^2\,dA(z).}
\tag{DISK-01}
\]

This is an exact classical weighted Bergman norm representation of the source-selected Fourier spectrum: a one-dimensional circle boundary generates a two-dimensional positive area-energy observable. It is a *chosen analytic representation*, not a new source-cancellation theorem or physical sheet attached to a photon.

**Equivalent finite Fourier-line/Gram representation (INHERITED SUCC #296).** Let \(v_H(x)=(1,e(x),\ldots,e(Hx))/\sqrt{H+1}\). Then

\[
F_H(x-y)=(H+1)|\langle v_H(x),v_H(y)\rangle|^2.
\]

The positive density matrix \(R_{N,H}=N^{-1}\sum_n v_H(x_n)v_H(x_n)^*\) obeys \(E_{N,H}=(H+1)\operatorname{tr}(R_{N,H}^2)\). This is exactly the earlier internal Fourier purity identity; we do not claim it as independently invented.

## Radix Ward dynamics creates a testable obstruction in the disk

For any fixed h≠0,

\[
|c_N(16^k h)-c_N(h)|\le 2k/N
\]

by an exact shift of the finite expanding-circle trajectory. If \(|c_N(h)|\ge\varepsilon>0\), \(K\le\varepsilon N/4\) and \(2|h|16^{K-1}\le H\), then \(K\) distinct monomials \(z^{|h|}, z^{16|h|},\ldots,z^{16^{K-1}|h|}\) in \(G_{N,H}\) each carry nonnegligible weighted energy. Therefore

\[
\boxed{E_{N,H}-1=\pi^{-1}\|G_{N,H}\|_{L^2(\mathbb D)}^2
\ge K\varepsilon^2/4.}
\tag{DISK-02}
\]

This geometrically explains why the **sublogarithmic** bound of LS-10 suffices. A persistent fixed Fourier harmonic would replicate through about \(\log_{16}H\) mutually orthogonal holomorphic disk monomials, forcing a logarithmic area-energy cost. A constant cap is stronger than needed.

A quantitative converse for the fixed source follows: if base-16 π normality fails, some fixed h has a positive limsup Weyl coefficient. The square-checkpoint interpolation preserves a positive limsup along infinitely many \(N=L^2\), and DISK-02 forces \(E_{L^2,L}\gtrsim_h \log L\). The Fejér→integer-mesh inequality and LS-11 then force *some* original-source dyadic epoch \(A\in[L,L^2]\) to satisfy \(\mathscr C_A\gtrsim_h\log A\). No assertion of such an epoch for actual π is made; this is the **CONTRAPOSITIVE** of the conditional sufficient criterion with an exact geometric diagnostic.

## No secret source transport between the two sheets

Both Γ-sheet and disk-sheet are positive 2D objects. But they live in DIFFERENT spaces and have different meanings:

- Γ sheet coordinates (u,v) are real positive CONTINUUM scale variables; its Laplace convolution has no selected chronological phase.
- Disk sheet coordinates (Re z, Im z) carry a holomorphic encoding of the actual chronological circle Fourier coefficients, which are precisely the unsolved signed observables.

**No canonical phase-preserving map from the first sheet to the second has been proved.** The previously developed source-specific finite Γ seam bounds make finite observations precise; they do not create missing real-circle cancellation. Similar geometry, positivity, and matching quadratic scalings are therefore meaningful mathematical structure but **not** proof of the remaining selected cofactor collision estimate.

Next mathematical lamp: construct an ORIGINAL-four-pole, original-zero-seed bound on the disk area norm via the exact simultaneous p-primary and p-free cofactor labels; a Galois-average area norm over many embeddings is NOT the disk area norm of the selected real embedding.
