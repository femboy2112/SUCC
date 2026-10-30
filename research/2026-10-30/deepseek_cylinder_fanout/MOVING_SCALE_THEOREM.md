# One moving-depth cylinder-collision certificate — exact finite theorem

**Status:** locally derived from classical Shannon/KL, Rényi-2 and Pinsker inequalities. It holds for any deterministic digit stream; it proves **nothing** yet about the actual collision energy of the authentic pi orbit. All logarithms are natural; empirical words use N starting times and may extend beyond the final starting time.

## MS-01. Finite-N collision-to-short-block bound (PROVED LOCAL)

Let b>=2 and let d_0,d_1,... be a deterministic digit sequence in {0,...,b-1}. Define the empirical length-m block frequencies
`p_(m,N)(w)=N^-1 # {0<=n<N: d_n...d_(n+m-1)=w}`,
`Q_(m,N)=b^m sum_(|w|=m) p_(m,N)(w)^2>=1`.
For every N>=1 and m>=k>=1 put q=floor(m/k). Then

```
||p_(k,N)-uniform_(b^k)||_1
  <= sqrt( 2 log(Q_(m,N)) / q ) + 2m/N.          (MS-01)
```

**Full proof:** Draw a uniformly random starting position I from {0,...,N-1}. Split the first qk coordinates of its m-block into q consecutive DISJOINT k-blocks V_j, j=0,...,q-1. The reference uniform law on b^m words is a product across these blocks. Chain rule for KL divergence, data processing and nonnegativity of dependence give

`D(p_(m,N)||uniform_(b^m)) >= sum_(j=0)^(q-1) D(law(V_j)||uniform_(b^k)).`

The Rényi-2 inequality H_1>=H_2 implies
`D(p_(m,N)||uniform_(b^m)) <= log(Q_(m,N))`.
At least one j therefore has k-block KL at most log(Q)/q. Pinsker with the FULL L1 norm gives its marginal L1 distance to uniform <=sqrt(2log(Q)/q). But the starts for V_j are jk through N+jk-1, whereas p_(k,N) uses 0 through N-1. Replacing at most jk observations in each end gives L1 discrepancy <=2jk/N<=2m/N. Triangle inequality completes the proof. No independence of time samples and no source law is assumed. QED.

## MS-02. Single-moving-depth criterion (PROVED LOCAL, classical mechanism)

For any deterministic infinite base-b digit stream, the following are equivalent:

(A) The stream is base-b normal.

(B) **There exists** a sequence of integer depths m_N->infinity with
`log Q_(m_N,N) = o(m_N)`.

**B=>A.** Diagonal self-collisions give `Q_(m,N)>=b^m/N`; so
`m_N log b <= log N+log Q_(m_N,N)`, which together with (B) implies `m_N=O(log N)` and `m_N/N->0`. Apply MS-01 for each fixed k: q=floor(m_N/k)->infinity and both upper-bound terms go to zero. Thus every fixed k-block frequency tends to b^-k.

**A=>B.** For every fixed m, normality implies Q_(m,N)->1. Choose thresholds N_m increasing so that for all N>=N_m, Q_(m,N)<=exp(sqrt(m)). Let m_N=m on [N_m,N_(m+1)). Then m_N->infinity and `log Q_(m_N,N)<=sqrt(m_N)=o(m_N)`. QED.

This avoids the original PR407 two ordered limits, but does not prove the required bound for the selected pi digits.

## MS-03. Concrete SOURCE-DIRECTED sufficient target (OPEN)

Use the exact original BBP source `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`,
`U_0=0`, `U_n=16U_(n-1)+r(n)`, `y_n={U_n+T_n}={16^(n-1)pi}`.

For N sufficiently large define `m_N=floor(log_16(N)/3)>=2`. Let
`Kcal_(ell,N)(x)=(1/N²)sum_(i,j<=N) ell^-1(1-||x_i-x_j||/ell)_+`
be the smoothed, two-time tent pair-collision observable. Inherited PR407 theorems CTC-05, CTC-05b imply

```
Q_(m_N,N)(y)
 <= (256/15) * [
   Kcal_(16^(-(m_N-1)),N)({U_1},...,{U_N})
   + 16^(2(m_N-1))/(16*N)
 ].
```

The second term is O(N^-1/3). Therefore **the following source-selected estimate, if proved, would prove base-16 normality of pi**:

```
log Kcal_(16^(-(m_N-1)),N)({U_n(0)}_(1<=n<=N))
             = o(m_N) as N->infinity.            (MS-03 OPEN)
```

The kernel has Fourier transform `sinc(pi h ell)^2`, so Kcal is nonnegative with a positive constant Fourier mode and `Kcal>=1`. Its logarithm is thus nonnegative. Under MS-03, the inherited hard/soft inequality gives `log Q_(m_N,N)(y)=o(m_N)`; MS-02 finishes. Any `m_N=floor(c log_16 N)` with 0<c<1/2 has a similar safe source-transfer error.

**This is a reduction—not an unconditional pi normality theorem, a spectral gap, or a new estimate on the actual selected orbit.** A proof must bound the full positive Fourier sum through original source/carry and zero-boundary arithmetic, not merely expand it into selected Weyl coefficients or use prime-only marginals.

## MS-04. Sample-size firewall

For every stream, `Q_(m,N)>=max(1,b^m/N)`. Consequently m greatly exceeding log_b(N) leads to huge collision scores even for Haar-random digits. A finite test must report N/b^m and actual sample scarcity; the first 256 pi positions at depth3 are particularly under-sampled. Periodic de Bruijn order m has Q_m=1 but is still nonnormal, so *fixed m* alone never certifies the infinite stream.

**Next probe:** prove MS-03 or a strictly stronger authentic source-selected two-time correlation inequality. The coherent same-forcing seed and zero-seed seven-pole null source must be killed by a correctly stated arithmetic hypothesis, not by assuming their absence.