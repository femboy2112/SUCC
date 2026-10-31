# Principal review, shared provenance and final theorem scope

This is a same-model principal reconstruction of the three fronts, not an
external referee report or a Lean proof. The root read all final dossiers,
the PR411 dossier/code/tests/receipts/manifest, parent407, sibling410/409
criteria, PR408 signed-fabric theorem, and relevant COUNT-OUT/Noether/double
triangle records at their pinned commits. Front manifests record their
additional prior sources. No sibling implementation was silently merged.

Final dossiers reviewed:

* kernel/KERNEL_TRANSPORT.md:
  `58003553e965fce21c56f1bb8a89d662103560f76972d72ebd1295395bc557ea`
* cylinders/CYLINDERS_AND_STONEHAM.md:
  `a2c18866434bd3055f404ee733a19220b09f166092d049398476a5d7f4f2162c`
* arithmetic/ARITHMETIC_THEOREMS.md:
  `08fb418d338659c38f994a5f8e9e25121e69f8a63bd4bdc36b29ea02fc4f74eb`

## Kernel and sharpness reconstruction

The finite feature norm is sqrt(H), and its derivative norm squared is
`(2pi)^2 H(H²-1)/6`. Fejer nonnegativity improves the global feature-difference
cap to sqrt(2H), not2sqrt(H). With `T_n<1/(64n²)`, integrating the decreasing
minimum gives exactly `C²=pi/(8sqrt3)`. Applying reverse triangle inequality
before squaring is the important stronger step. All seams are periodic.

For sharpness, n on the sqrt(H) scale gives the sinc-square profile. Its tail
is bounded by a multiple of x^-4 and its small-x segment has vanishing length;
these justify the improper Riemann-sum limit. The cross-term identity leaves
a vector-square error O(H²/N²), which after normalization is
O(sqrt(H)/N). The stated joint limit N/sqrt(H)→infinity is sufficient.

An alternative evaluation of the Mellin integral avoids treating an
oscillatory integral as absolutely convergent: represent t^-3/2 as a Laplace
integral, use the nonnegative integrand1-cos(at), and integrate t first.
This reduces the result to
`(2 sqrt(a)/sqrt(pi)) integral_0^infinity v^-1/2/(1+v²) dv`
`=sqrt(2pi a)` by Euler's Beta integral. Applying the triangular sinc-square
representation gives pi/15. This confirms the constant and source scaling.
Its source-only character is a boundary, not an omitted zero-seed assumption.

## Low-slip and grid reconstruction

The centers j/15 are fixed by multiplication16. The strict17epsilon<1 gate
forces adjacent good centers to agree. The center0 has two circle sides,
giving digits0 and15; their sides remain fixed on consecutive good visits.
A constant three-digit block suffices for one low-slip position, giving the
two terminal exceptions in K<=2C+2. Period01 has distance1/17 in every lag,
yet only two completed states, so its high collision energy is exact.

For Stoneham, the stage grid size is c^(p-1), multiplicity c(c-1), and complete
stage lengths sum to c^(P+1)-c<cN. Nonnegative kernel domination permits the
partial final stage to be completed. The finite grid Fourier sum is at most
q+H. The future impulse budget is less than1/[15(c-1)], producing precisely
the displayed error. This is a bound for the entire paired real phase of a
different, provably normal source. It is not imported as BBP arithmetic.

## Quadrature reconstruction and prior-result correction

The original Green measure has mass1/64 and positive density on a support
containing open intervals. All polynomial moments and prefix forcing targets
are rational. The rational evaluation cone is full dimensional. A supporting
functional vanishing at the target would be a nonnegative rational function
with zero integral, hence vanish on an open interval and identically. The
target is therefore interior, allowing finite rational nodes and positive
rational weights; minimal conic support has at mostD=M+J+1 independent columns.

For the new lower bound, polynomial elimination gives derivative rows of
F_n. In the determinant-of-integrals expansion, the increasing x Vandermonde
and decreasing exp(-x) Vandermonde have fixed signs. Derivative row signs
leave net sign `(-1)^(m(J+1))`, so every leading Wronskian is nonzero.
Division by the first nonvanishing basis function, differentiation and Rolle
give the zero-count theorem. A nonzero combination of the first2s+1 functions
with double zeros at s nodes is nonnegative up to sign everywhere, contradicting
positive-density integration if2s<D. Thus s>=ceil(D/2). No claim that the
rational upper boundD is optimal is made.

The original mass and support bound alone give the unchanged Green estimates
and total budget17/648. For infinite moment identification, positivity and
monotone convergence first give every rival the same finite exponential
moment; analyticity is therefore derived, not assumed for the rival.

The earlier cylinder review covered arithmetic hash
`a3fca923e38ea38807ece8c88a63704c68e8dbd78695cdabd87ff2eb7d3b0d3a`.
The principal reviewed the later additions: explicit PR408 credit, unchanged
tail budgets, rival exponential-moment justification, fixed-frequency mutant
coherence and the Chebyshev atom bound. Earlier review receipts retain their
actual hash; they are not presented as having checked these later additions.

Reading PR408 exposed that its SF02--04 already proves positive zero-seed
arbitrary prefix/jet spoofing, with relative closeness and dyadic control.
That broad result was initially treated as a new obstruction during discovery;
the final dossier and root summary correct the scope. Our separate cubature
and atom complexity results survive; no academic novelty claim is made.

## Evidence dependence and remaining gap

Root intervals are built from positive BBP sums; their separate oracle uses
four-pole exact rational phases. The kernel front additionally uses a combined
fraction, Laplace integration and Gamma identities. Cylinder words have a
separate Machin check. Arithmetic witnesses have symbolic and rational checks.
All researchers are the same model family and share task history; external
independent proof authority is absent. The six prime windows overlap and do
not create independent data families or a coverage theorem.

No review found a new all-horizon selected Fourier upper bound. Source
identification, finite intervals and transport comparisons must not be promoted
to that missing result. No physical/category-carrier interpretation, pi
normality, RH or new Lean authority is certified by this round.
