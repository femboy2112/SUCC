# Part IV — pure isometry obstruction to a normalizable critical-line observer

**Date:** 2026-10-13, zero-centered SUCC offshoot. **RH PROVED: no**. Complements [Part III](ZERO_CENTERED_ARCH_DILATION.md). No zero positions enter the construction.

## ZCR-P01: pure unilateral dilation theorem (PROVED LOCAL, classical operator-theory deduction)

On H=L²(0,1), extend f by zero outside its domain and define U_q f(x)=sqrt(q) f(qx), for any integer q>=2. From Part III, U_q* U_q=I. By induction,

  U_q^n f(x)=q^(n/2) f(q^n x),

and every vector in ran(U_q^n) vanishes on x>=q^(-n). A square-integrable function supported in (0,q^(-n)) for every n is zero. Hence

  intersection_(n>=1) ran(U_q^n)={0}.

Thus U_q is a **pure isometry** in the Wold sense, not a unitary onto H. This is a theorem about an explicitly defined Hilbert-space operator. There is no assertion about physical observers or quantum-gravity dynamics.

## ZCR-P02: no bounded unit-circle eigen-observer (PROVED LOCAL)

Suppose U_q* v=lambda v for a Hilbert vector v with |lambda|=1. Since U_q is isometric, its adjoint is a contraction, and

  ||U_q* v||=||v||  implies  U_q U_q* v=v,

because U_q U_q* is the orthogonal projection onto ran(U_q). Therefore v=lambda U_q v belongs to ran(U_q). Repeating yields v=lambda^n U_q^n v in every range. Purity forces v=0.

Consequently **U_q* admits no nonzero bounded Hilbert eigenvector of eigenvalue modulus one**.

The Mellin functional L_s(f)=int_0^1 f(x)x^(s-1)dx has the formal character L_s(U_q f)=q^(1/2-s)L_s(f). For Re(s)>1/2, L_s is bounded and the character lies in the open unit disk. At Re(s)=1/2 the character has unit modulus, but the Mellin functional is unbounded on H: these are *generalized boundary modes*, not Hilbert eigenvectors. This rigorously blocks the inference "unit-modulus clock -> physical/normalizable zeta-zero observer". The line is representation geometry, not a zero-location theorem.

## ZCR-P03: reciprocal-cell orthogonal projections (PROVED LOCAL, TESTED)

Identify H with ell²(N,w), w_k=1/[k(k+1)]. For j>=1, block B_j={qj,...,q(j+1)-1} has total weight w_j/q. The range of U_q consists of sequences vanishing at k<q and constant across each B_j. Its orthogonal projection P_q=U_q U_q* is

  (P_q f)(k)=0 if k<q, else
  (q/w_j) sum_(r=qj)^(q(j+1)-1) w_r f(r), j=floor(k/q).

This is an exact weighted conditional expectation onto lawful block observations. It is idempotent, self-adjoint and contractive. For every finitely supported sequence f, P_(q^n) f=0 once q^n exceeds the largest supported cell. Density of finite-support sequences plus ||P_(q^n)||<=1 yields P_(q^n) f->0 strongly for every f in H. In addition U_q^n f converges weakly to zero (support escapes toward x=0) while its norm stays constant, so it does not converge strongly to zero unless f=0.

Exact rational tests cover idempotency, weighted inner-product symmetry, norm contraction, low-cell omission and finite-support escape. These checks are not a substitute for the preceding infinite-dimensional proof.

## ZCR-P04: missing arithmetic/source coupling (UNVERIFIED)

The pure-isometry theorem is independent of the Möbius/zeta prime source and holds equally for fake integer dilations. It cannot exclude off-line zeros, establish RH or identify the completed Weil/Suzuki quadratic form. An authentic theorem must build a **zero-independent source-to-spectral intertwiner**, retain Gamma/pole/conductor structure, prove a global L² norm estimate or equivalent Weil positivity, and survive fake 6 / non-Euler controls.

**Relevant classical context:** Wold decomposition and pure isometries (classical); Nyman–Beurling and Báez-Duarte give the established connection to RH. We assert no novelty for pure-isometry spectral theory; the explicit reciprocal-cell realization is the SUCC instantiation.
