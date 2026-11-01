# Clipped four-pole transport and the doubled logarithmic clock

**Status: paper proof, original source retained. This is transport, not selected
signed cancellation.** Parent: PR #434 at `030ee84b8b7f655fcf433375bfc0b347e0483c89`.
The clipping technique already occurs for the one-step ladder in
`observational_succ/ladder_shift_audit.py` and
`research/2026-10-26/OILY_MACARONI_SOURCE_BRIDGE.md`. The increment here is its
all-lag application and the triangularly weighted doubled-clock consequence;
no claim of literature novelty is made.

Let the four original signed poles define r, let U_0=s be a declared real seed,
and put U_(n+1)=16U_n+r(n+1). The authentic source has exactly s=0. Write
C_k=sum_(n=1)^(N-k)e(h(U_(n+k)-U_n)), D_k=sum_(n=1)^(N-k)e(h(16^k-1)U_n).
All statements below hold for every integer N>k>=1 and h!=0.

The original source bound r(n+j)<15/(64 n²), for n,j>=1, gives

    0 < F_(n,k) = sum_(j=1)^k 16^(k-j)r(n+j)
                < (16^k-1)/(64 n²).

Using both chord bounds, not just the Lipschitz bound, and pi<22/7,

    |e(h(U_(n+k)-U_n))-e(h(16^k-1)U_n)|
      <= min(2, 2 pi |h| F_(n,k))
      <= min(2, a_k/n²),    a_k=11|h|(16^k-1)/112.

The function f(x)=min(2,a/x²), with f(0)=2, is decreasing. Thus
sum_(n>=1) f(n)<=integral_0^infinity f(x)dx=2 sqrt(2a). Consequently

    |C_k-D_k| <= sqrt(11 |h| (16^k-1)/14).                 (T1)

One may take the minimum of this, 2(N-k), and the parent bound
11|h|(16^k-1)/56. The executable instrument rounds the square root UP on a
2^32 rational grid and retains all three majorants. No floating arithmetic
enters a certificate. It does not take an absolute value of the signed score.

For any 1<=K<=N define E* by weighting these valid per-lag majorants with
2(K-k)/(K²N). The original signed VdC inequality is therefore strengthened to

    |S_N(h)/N|² <= (1+(K-1)/N) [1/K + L_(N,K)(h) + E*].   (T2)

For an analytic closed form let B_h=ceil(sqrt(11|h|/14)). Since T1<=B_h 4^k
and sum_(j>=1) j/4^j=4/9,

    E* <= (2 B_h/(K²N)) sum_(k=1)^(K-1)(K-k)4^k
        <= (8 B_h/9) 4^K/(K²N).                          (T3)

Here the implemented rational grid ceiling also stays <=B_h 4^k, so the
same inequality applies to its returned E*. The K=1 error is exactly zero.
At K=floor(log_4 N), for N>=4,

    E* <= 8 B_h/(9 K²) -> 0.                             (T4)

This doubles the leading logarithmic depth permitted by the parent
Lipschitz-only estimate. At the original K=floor(log_16 N) it yields
O_h(1/(sqrt(N) K²)). The parent itself also admits a triangular-weight
improvement to O_h(1/K²) at its original clock; neither observation is
arithmetic cancellation. The necessary and sufficient criterion at both
clocks is proved in BOUNDARY.md.

**Scope audit.** T1-T4 hold for arbitrary real s. They must hold for the
coherent changed seed and both shadow families. They cannot distinguish
s=0, cannot prove limsup L<=0, and cannot satisfy the source-selected
fireworks criterion by themselves. The signed upper estimate remains OPEN.

# Independent exact measurement instrument

`interval_oracle.py` evaluates the same finite signed statistic without
importing the parent oracle. It uses the combined identity

    r(n)=(120n²-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)]

and a circle-reduced recurrence, independently checked against the parent's
unwrapped four-pole fractions. It obtains pi from the original BBP sum:

    p_d=16 sum_(j=1)^d 16^-j r(j),
    p_d < pi < p_d + 16^(1-d)/(64d²).

The tail bound follows from r(d+j)<15/(64d²) and sum_(j>=1)16^-j=1/15.
The default d=28 is fixed before fresh measurements. This pi enclosure has
different construction from the parent's Machin/arctangent enclosure;
both represent the same classical pi and are not independent source families.

For a rational circle phase x in [-1/2,1/2], first enclose x in its exact
outward dyadic cell of width 2^-96. Multiply the full cell interval by the
above pi interval to enclose y=2 pi x/2^44. No phase rounding is discarded.
This avoids cubing the enormous original source denominator. If |y|<=Y, then

    1-Y²/2 <= cos y <= 1,
    y_low-Y³/6 <= sin y <= y_high+Y³/6.

These inequalities follow from Taylor's bounded-derivative remainder.
Apply cos(2y)=cos²y-sin²y and sin(2y)=2 sin y cos y exactly 44 times.
Each product is a full interval product, outward rounded on a 2^120 grid;
each true sine/cosine remains in [-1,1], allowing sound clipping there.
Finally round outward to 10^-12. This is separate code, pi construction,
range reduction, and angle evaluation from the parent's direct 17-term
Taylor polynomial. Both rely on classical trigonometric identities and
rational arithmetic; they are implementation bearings, not two proofs of
normality. A display decimal is never used as a certificate.

Falsifiers: an original source mismatch, exact-root interval exclusion,
disjoint independently computed intervals, or failure of the summed clipped
budget would invalidate the instrument or bound. None can be excused by
numerical agreement elsewhere.
