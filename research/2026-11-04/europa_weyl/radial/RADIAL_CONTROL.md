# A genuine zero-seeded 8N source with almost maximal real energy

**Paper theorem.** Let Z=U−Y be the authentic radial projection of the original, literal zero-seeded BBP path. Then log den(Z_N)=(8+o(1))N. For its forcing LCM M_N one also has log(M_N/den(Z_N))=O(N^(2/3)). The radial differences obey the same square-root mean logarithmic loss estimates in either time direction as the angular differences. The finite dyadic density operators have the same nonzero eigenvalues in the two sources at all sufficiently large epochs. Yet for integer q≥2 with q=o(A),
$$
 J_{A,q}(Z)=q-\frac{3\log 2-2}{16}\frac{q^2}{A}
                   +O(q^2/A^2).
$$
Thus the radial source fails the desired o(K_A) bound as strongly as the normalization permits to first order. It lives in the original two-dimensional Frobenius source module, with the same literal initial condition and event times for its top odd primes. Its character is trivial and its completed period is zero; the angular character is χ₋₄ and the angular period is π.

**Prefix sign proof.** The radial taps are w=(2,−2,−1,−2,−1/2,−1/2,1/4,0), fixed by all four prime actions. At block k≥0 write D_l=16 Z_k+Σ_(j≤l) w_j/(8k+j). The authentic inequality 0<Z_n<1/(32n+16) for n≥1 follows from PF-8b of [#497](https://github.com/femboy2112/SUCC/blob/4383bd31340af700e312f13d7ef28af090c152d5/research/2026-11-04/frobenius_prime_saturation/PROOFS.md). The l=1,2 prefixes are positive because 2/(8k+1)>2/(8k+2). For 3≤l≤5 the omitted tail to D_8 contains −1/[2(8k+6)]+1/[4(8k+7)]<0 and any other nonzero terms are negative. Thus D_l>Z_(k+1)>0. But
$$
 D_6=Z_{k+1}-\frac{1}{4(8k+7)}
       <\frac{1}{32k+48}-\frac{1}{32k+28}<0 .
$$
D_7=D_8=Z_(k+1)>0. None of these prefixes vanishes. This sign change matters: uniform positivity of the partial pulses would have rejected the genuine radial source for the wrong reason.

**Arithmetic and spectral consequences.** For s=8k+l with 1≤l≤8 the normalized prefix L_a(s) in the [prime-layer theorem](../primal/PRIME_LAYERS.md) equals 16^(−k−1)D_l in every prime class. Every indicator in the exponent formula equals one. Since all odd tap positions are occupied, the same short-prefix numerator bound gives the O(N^(2/3)) loss. On any long-prime pulse-free run the normalized simple residue advances by 16. The [two endpoint arguments](../energy/PAIR_SIEVE.md) for state-denominator loss therefore apply to Z word for word with its own conductor. The uniform top-prime argument uses exactly one surviving p-tap for 4t<p≤8t and the unit multiplier, also valid here. Consequently the eventual distinctness, the density spectrum, and the relative cyclotomic independence in [EW6–EW7](../weyl/WEYL_CONDUCTOR.md) hold for these radial states too. A rank-two transfer for Y was never a hypothesis of those prime bounds. The pure finite spectra may live in different carrier dimensions (different zero-eigenvalue multiplicities); their nonzero spectra coincide. At an inert prime the aligned signs are different. This theorem identifies precisely what the absolute denominator and spectrum arguments forget.

**Real calculation.** The upper bound on Z_n makes 0<Z_n<1/q throughout the epoch eventually. Since every circular difference is then an ordinary difference of distance <1/q, the entire tent is linear. Moreover Z_n=1/(32n)+O(n^(−2)) by PF-8 (or integrate the radial tail, whose kernel equals −4 at the right endpoint). Lipschitz continuity of absolute value gives the double mean
$$
 A^{-2}\sum_{n,t}|Z_n-Z_t|
   =\frac1{32A}\int_1^2\int_1^2|x^{-1}-y^{-1}|\,dx\,dy+O(A^{-2}).
$$
The integrand is Lipschitz on the compact square, so the normalized Riemann sum has O(1/A) error. The integral is 6 log 2−4 by integrating over x<y and doubling. Substituting into the tent proves the stated expansion uniformly along q=o(A). In particular |μ̂_Z(h)|→1 for each fixed h. The [finite receipt](RECEIPT.json) checks every signed partial prefix through 166 blocks independently against the two projected streams, tests a surviving inert sign and evaluates genuine dyadic-window-style intervals (the finite choices of A need not be powers of two).

**Verdict-changing test.** Any proposed sufficient estimate based only on the common 8N exponent, near-full pair denominators, nonzero finite signed sums or the nonzero density spectrum would also apply to Z and would contradict this expansion. A useful next inequality must respond to a feature that differs here: the signed character together with time-ordered, real centered numerators is one concrete candidate. Retaining the character alone still admits the exact prime-window tap mutants in the prime-layer note. The theorem concerns one genuine sibling source; it supplies no negative conclusion about the angular normality conjecture.
