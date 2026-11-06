# From the unrounded reflected source to the signed beta arithmetic tape

**Status:** paper proof and finite checks. This calculation takes the source-reflection identity for the polynomial below as its input. It compares the unrounded finite coefficients with the signed *arithmetic* side of the beta explicit formula. No empirical BBP/Weyl orbit, Gamma term or zero sum occurs in the hypothesis.

Put `chi = chi_{-4}`, `c(n)=[x^(n-1)]Q_N(x)` for positive n, where

    Q_N(x) = (1 − 16^(−N)(1−x)^(8N))/(1+x²).

The numerator vanishes at ±i, so long division over the rationals is exact. Denote by * ordinary Dirichlet convolution. Since c(1)=1−16^(−N), its inverse under * exists. Here B_N(n) denotes the log-derivative coefficient at integer n, distinct from the Dirichlet polynomial in the beta note. Define B_N=(c log)*c^(-1), where (c log)(n)=c(n)log n. This definition uses the supplied rational coefficients even when they miss their nearest correct integer. For the infinite character coefficient sequence, the corresponding B is b(n)=chi(n)Λ(n) by the Euler product, or by the divisor identity b*chi=chi log. Thus b(p^k)=chi(p)^k log p including zero at p=2.

Let λ in (0,4) solve 8H(λ/8)=log 16 with natural logarithms. Set g=log((8−λ)/λ), r=e^(−g), and

    C = 1 / ((1+r²) sqrt(2πλ(1−λ/8))),
    D = C / (sqrt(λ)(1−r)).

For every fixed B>0, uniformly for positive integers L with |L−λN| ≤ B log N,

    Σ_(n≤L) |B_N(n)−chi(n)Λ(n)| / sqrt(n)
       = (D+o(1)) exp(g(L−1−λN)) log N / N.                (1)

Consequently the signed half-density arithmetic measures at positions log n converge in total variation on the expanding interval [0,log L] when L=λN+(log N−log log N)/g−ω(1) in this window. At offsets bounded from the displayed threshold the defect is bounded above and below by positive constants, and at +ω(1) it diverges. The sign convention in the explicit formula may multiply both measures by −1. Symmetrizing introduces the corresponding reflected copy. Formula (1) is a uniform statement about arithmetic tests of sup norm at most one; the completed signed Weil form carries extra terms and different test constraints.

**Proof.** Write l=n−1 and E_l=16^(−N) Σ_(j=0..floor(l/2)) (−1)^j binom(8N,l−2j). Expansion gives c(n)−chi(n)=(−1)^(l+1)E_l. For l≤4N the magnitudes decrease from the first summand, so E_l lies between 16^(−N)(binom(8N,l)−binom(8N,l−2)) and 16^(−N)binom(8N,l), taking binom(8N,k)=0 when k<0. For |l−λN| ≤ B' log N, the ratio binom(8N,l−2j)/binom(8N,l) tends to r^(2j) for each fixed j, uniformly over this window, and is bounded by t^(2j) for any fixed r<t<1 at all sufficiently large N. Dominated convergence on this series and uniform Stirling expansion of the binomial coefficient yield

    E_l=(C+o(1)) exp(g(l−λN)) / sqrt(N).                    (2)

In particular nearest-integer decoding first loses a coefficient at l=λN+(log N)/(2g)+O(1). More precisely, in this window the transition occurs as l crosses λN+[(log N)/2−log(2C)]/g, up to an o(1) displacement and integer rounding. This last language allows near-ties. For a fixed margin away from the entropy root, the upper bound proves correct decoding for the full initial prefix below it. The two-term lower bound gives failure at every l/N in compact subsets of (λ,4). At l=4N the lower bound loses only a polynomial factor and still implies failure.

For a uniform inverse check on m≤M=floor(L/2), all errors c(m)−chi(m) are O(e^(−ηN)) for some η>0 by the entropy upper bound. In the finite Dirichlet algebra obtained by discarding all indices above M, the norm Σ_{m≤M}|a(m)|m^(−2) is submultiplicative. The inverse of chi is the restriction of μchi, of norm at most ζ(2). A convergent geometric series around that inverse bounds the norm of c^(-1)−chi^(-1) by O(e^(−ηN)). The same norm estimate holds for (c−chi)log since Σ log(m)/m² is finite. Multiplication now bounds |B_N(d)−b(d)| by O(M²e^(−ηN)) for every d≤M.

For every n≤L, expand the coefficient equation B_N*c=c log. Its d=1 term vanishes since B_N(1)=0. For 1<d<n dividing n, both d and n/d belong to the safe range ≤M. Subtract the corresponding equation b*chi=chi log to obtain, uniformly,

    B_N(n)−b(n) = log(n)(c(n)−chi(n)) + O(e^(−η'N)),       (3)

for some η'>0. Indeed all proper-divisor products cost at most a polynomial times e^(−ηN), b(d) is at most log L, and dividing by c(1)=1−16^(−N) introduces an exponentially small extra error since sup_{n≤L}|c(n)| grows at most polynomially in the stated logarithmic window. This argument includes composite and prime-power rows.

For n=L−j with fixed j, insert (2) into (3), use log(n)/sqrt(n)~log(N)/sqrt(λN), and sum the geometric factors r^j. For domination on L/2<n≤L, the unsigned upper binomial bound relative to binom(8N,L−1) costs at most t^j, with any fixed t between r and one for large N. Terms n≤L/2 are exponentially small by the preceding inverse bound. This proves (1).

**Falsifiers and scope.** With l=n−1, changing the sign in the reflected numerator changes the observed constant-tap error. Omitting division by c(1) fails at n=2. Polynomial division from the highest coefficient checked every l≤4N exactly for N=23,73,199. An exact log-prime vector oracle verified the rounded arithmetic tape strictly before the first loss of unique rounding (22,66,177 recovered n rows respectively). The direct raw log-derivative probe also bounds the residual in (3) through rows 25, 69 and 180, using exact rational coefficients and log(p) ≤ p; conservative bounds are 2.30·10^−15, 1.42·10^−47 and 7.18·10^−131. The finite scaling receipt evaluates the leading coefficient term in (3); it does not evaluate the entire raw log derivative at the larger horizons. The proof, rather than those values, controls the divisor terms. The calculation bounds the half-density defect on a real logarithmic Euler test grid, not temporal phases e(hY_n). It supplies no estimate for the selected pair energy and no comparison to the empirical Gram.

**Reproduction.** Run `python referee_probe.py` beside this note with mpmath installed; its output is `REFEREE_RECEIPT.json`. The initial hypotheses and controls appear in `REFEREE_PREREG.md`. This is an independent derivation within the same model family, without a priority claim or external referee.
