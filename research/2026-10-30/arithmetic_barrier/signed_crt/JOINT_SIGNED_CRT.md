# Joint signed CRT: sharp restoration obstruction and a tested one-lag target

**Status:** paper proofs of elementary algebra and quantitative obstructions; certified finite
original-source measurements; one unproved source-selected interaction target. No fixed-frequency
unbounded-horizon cancellation theorem is claimed. No π-normality or RH status changes.

**Source and lineage.** Parent PR #398, commit `1a1524de28b155139d8fe84ea90fc2f117fbb9f3`.
All authentic calculations use `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)` and `U_0=0`.
Write `e(x)=exp(2*pi*i*x)`. Preserve the index convention
`U_n=16^(n-1)*pi-T_n`, `0<T_n<(8n+1)^(-2)`.
The earlier all-odd-primary dyadic-seed obstruction is already proved in integrated
`research/2026-10-24/PI_LAG_ADVERSARIAL_REVIEW.md`, section 2, and implemented in
`observational_succ/pi_carry_prefix_control.py` (PRs #259/#266 lineage). Its replay below is
credited reproduction, not a novelty claim. Classical character orthogonality and Gauss sums
are also not new mathematics.

## SC-01. Exact coprime cancellation is impossible; arbitrary close restoration is sharp

Let `P>1`, `D>=1`, `gcd(P,D)=1`, and `a` an integer modulo P. The nearest complementary mark is

```
m = nearest_integer(D*a/P),  b = -m mod D,
z = a/P - m/D.
```

Then `a/P+b/D == z mod 1` and `|z|<=1/(2D)`. If `a!=0 mod P`, exact cancellation is impossible:
`aD+bP == 0 mod PD` would imply `a==0 mod P`. Indeed

```
min_(b mod D) ||a/P+b/D|| = ||D*a/P||/D >= 1/(P*D).
```

For odd P the upper bound sharp over a is `(P-1)/(2PD)`. Multiplication by D permutes residues
mod P, so choose `Da == (P-1)/2 mod P` for equality. This corrects the over-literal reading of
parent RESEARCH section 4's arbitrary-cofiber exact cancellation sentence: **an unrestricted
complex weight can cancel exactly; a genuine complementary conductor coprime to a nonzero
primary conductor can approach coherence arbitrarily closely, but cannot cancel exactly.**
Archived parent wording is not rewritten here.

For any finite list `a_j` and the above choices at one common D,

```
Re sum_j e(a_j/P+b_j/D) >= L*cos(pi/D),
```

because all phase lifts lie in `[-1/(2D),1/(2D)]`. Hence the full modulus can approach L while
the complete primary list, and thus every primary marginal and every joint primary statistic,
remains exactly fixed. For squarefree `P=product p`, adding `b_j/D` leaves every p-primary
component unchanged. This is a **joint multi-prime** obstruction, with no independence assumption.
It holds for any finite P, not only one prime. It changes the cofiber; it does not claim that
these selected marks are the actual BBP cofiber or even form one causal source trajectory.

The finite receipt uses the actual p=97 first-birth primary orbit (L=12). At D=2^20 the restored
full modulus is in `[11.999999999977,11.999999999978]`. The original list has not changed in
F_97. This is a sharp quantitative failure of every cofiber-free loss uniformly separated
from L.

## SC-02. The actual zero-seed source already defeats a simple marginal transport

For `p>=13`, `p==1 mod4`, define the inherited first birth `b_p` and `L=ord_p(16)`:

```
b_p=(p+7)/8 (p=1 mod8),  b_p=(p+3)/8 (p=5 mod8).
a_j = c_p*16^j mod p, c_p=4 or -1, 0<=j<L.
U_(b_p+j) == a_j/p + v_j mod 1.
```

The first birth window contains this complete orbit and no later p-pole collision. Define
`S_p(h)=sum e(h U_(b_p+j))`, `P_p(h)=sum e_p(h a_j)`. The tempting rule
`|S_p(h)|<=|P_p(h)|+1` is false **on the authentic zero seed**, not just a synthetic control.

At p=13, h=1, j=0,1,2, exact rational/trigonometric certificates give

```
1.987669132363 <= |S_13(1)| <= 1.987669132364,
0.834999618124 <= |P_13(1)| <= 0.834999618125.
```

Thus the proposed inequality fails strictly. At h=3 the actual modulus is about 2.7767314,
while the primary modulus is again about 0.8349996. These refute this specific rule; they do
not refute every possible weighted or asymptotic joint estimate.

## SC-03. Weighted Gauss completion works algebraically and fails as a useful bound here

Let `f_j=e_p(hc_p16^j)`, `w_j=e(hv_j)`, h not divisible by p, and

```
what_l = (1/L) sum_j w_j e(-l*j/L),
F_l = sum_j f_j e(l*j/L).
S_p(h) = sum_l what_l F_l.
```

Every character of the subgroup `<16>` extends to F_p^*. If its index is m, its indicator
expansion averages the m extensions. The complete Gauss sum of a nontrivial multiplicative
character has modulus sqrt(p), while the trivial character has sum -1 at a nonzero additive
frequency. Hence `|F_l|<=sqrt(p)` for all l, including the trivial subgroup character. Therefore

```
|S_p(h)| <= sqrt(p) * sum_l |what_l|.                  (SC-3a)
```

No independence of f and w is used. A source-derived bound
`sum |what_l|=o(L/sqrt(p))` would be sufficient for o(L) cancellation by this route.
This is sufficient, not logically necessary; cancellation between the summands in SC-3a
can be much stronger than their absolute sum.

For incomplete periods, the normalized discrete Fourier coefficients of a length-t interval
have l1 norm at most `2+log L` (use `sin(pi*l/L)>=2*min(l,L-l)/L` and the harmonic-series
bound). Thus primary partial sums are at most
`B=min(L,sqrt(p)*(2+log L))`. Summation by parts gives the joint bound

```
|S_p(h)| <= B * (1 + V),
V = sum_(j<L-1) |w_(j+1)-w_j|.                        (SC-3b)
```

This requires small variation of the **actual** cofiber. It cannot be inferred from
`r(n)=O(n^-2)`: modulo one, `v_(j+1)==16 v_j+r(b+j+1)`, so the expanding factor remains.
Already at p=29, h=1 the certified V exceeds 7.62689780598; the concrete trial V<=4 fails.
The raw receipt shows the measured cofiber Fourier l1 norms and partial-summation bounds.
On the fresh selected periods these triangle-inequality bounds are larger than L. The
Fourier reconstruction is correct; it has delivered **no nontrivial fixed-mode bound**.

Why standard Burgess/Weil/subgroup results cannot simply be applied: w_j is a changing-
conductor rational exponential determined by the complete previous source history. We have
not shown it is a bounded-degree rational-function additive character over F_p, a single
multiplicative character, or a short interval weight of controlled Fourier norm. That missing
structural hypothesis is retained. Contemporary examples of genuinely structured character
sums include [Chang--Shparlinski, arXiv:1401.6611](https://arxiv.org/abs/1401.6611) and
[Gong, arXiv:1401.4618](https://arxiv.org/abs/1401.4618); their stated sums are different from
this actual w_j. No theorem from those papers is silently transferred.

## SC-04. A full signed energy identity survives the cofiber, but only after frequency averaging

Let `D=lcm(denominator(v_j):j<L)`; gcd(D,p)=1. For every integer h,

```
(1/p) sum_(t=0)^(p-1) |S_p(h+tD)|^2 = L.              (SC-4)
```

**Proof.** Expand the square. For i,j, the t-dependent factor is
`e(tD(U_i-U_j))=e_p(tD(a_i-a_j))`, because D kills both complementary denominators.
The sum over t is p when a_i=a_j and zero otherwise. The primary residues are distinct on
one complete order period, so only the L diagonal terms remain, each of modulus one.
The full complementary phases have been retained exactly. QED.

Cauchy--Schwarz gives `(1/p)sum_t |S_p(h+tD)|<=sqrt(L)`. For every K>0, at most p/K^2 of these
p frequencies have modulus larger than K sqrt(L). With repeated primary residues the exact
right hand side becomes
`sum_r |sum_(j:a_j=r) e(h U_j)|^2`, so discarding collisions would be wrong.
The same proof works with a product of prime-power conductors P and injective joint primary
vectors; it does not factor an empirical joint law into its marginals.

**Authority and limitation.** This is classical character orthogonality applied to a
source-proved injective residue window. It is a useful full-phase finite calibration and
a legitimate frequency-average constraint. The step D is enormous and increases with the
window. The theorem does not control h fixed, a contiguous low-frequency range, nor the
real-circle frequencies needed for normality. It is classified as a **non-improvement of
the selected fixed-frequency barrier**, not a new normality mechanism.

## SC-05. Same forcing and every odd-primary component still admit finite coherence

For arbitrary integers `1<=A<=B`, choose `M=B+K`, K>=1, and the exact rational BBP partial sum

```
q_M = sum_(n=1)^M r(n)/16^n,
s_M = -floor(16^M q_M)/16^M.
```

Since `q_M < pi/16 < q_M+16^-M/(8M+1)^2`, the positive number
`delta=s_M+pi/16` satisfies
`0<delta<16^-M*(1+(8M+1)^-2)`. For A<=n<=B, the changed pure phase has the real lift
`16^n delta < 16^-K*(1+(8M+1)^-2)`, while the changed rational U_n has lift

```
-T_A < -T_n+16^n delta < 16^-K*(1+(8M+1)^-2).
```

Their characters are therefore arbitrarily coherent as A,K grow, regardless of the chosen
length B-A. Yet `U_n(s_M)-U_n(0)=16^n s_M` is dyadic for **every** n. Thus every odd-prime-power
primary component agrees at every time, even beyond the observation window. For n>=M this
difference is an integer and the circle phases coincide exactly.

The receipt with A=80,B=120,K=8 has a 41-term full modulus greater than
40.999999999877, with every odd-primary mark preserved; aliasing begins at n=128.
The stronger historical #259/#266 construction additionally preserves a prescribed finite
literal-carry prefix and odd-lift divisibility. We do not claim to improve that theorem.
The point here is its concrete joint-CRT and signed-energy calibration.

**Typed boundary:** s_M is nonzero. This is not a counterexample to authenticated U_0=0.
Each fixed rational translated constant has the same normality status as pi, and these
trajectories even become exact circle aliases. No asymptotic failure of a rational seed is
claimed. Exact aliases and constant twists (e.g. s=1/15) must survive magnitude readouts.

## SC-06. A smaller source-selected interaction theorem, attacked but still open

The following is a more limited signed-window target; no logical implication from normality
to this uniform local statement is asserted. It would give a nontrivial unbounded selected
signed result. For each fixed nonzero integer h, seek a constant eta_h>0 such that,
for every sufficiently large eligible prime with `L=ord_p(16)>=sqrt(p)`,

```
E_p(h) = (1/(L-1)) sum_(j=0)^(L-2)
    [1 - Re(e_p(h*(a_(j+1)-a_j)) * e(h*(v_(j+1)-v_j)))] >= eta_h.       (SC-6)
```

The actual forcing gives the exact summand phase
`h*(U_(n+1)-U_n)=h*(15 U_n+r(n+1))`. Both complementary and primary terms remain signed.
This is one specific joint lag-one anti-compensation obligation. It is not claimed to be
the logically weakest possible additional condition. It does not assume independent primes,
independent marginals, or a reset cofiber.

**Consequence, proved independently of the conjecture.** Set z_j=e(hU_(b+j)) and
mu=(1/L)sum z_j. The elementary path inequality yields

```
2(L-1)E_p(h) = sum |z_(j+1)-z_j|^2
 <= 4 sum |z_j-mu|^2 = 4*(L-|S_p(h)|^2/L),
|S_p(h)|/L <= sqrt(1 - ((L-1)/(2L))*E_p(h)).             (SC-6b)
```

Thus eta_h=1/4 would force a limiting bound at most sqrt(7/8)<1 on those authentic windows.
This alone does **not** imply normality: prime-window coverage, all horizons, all h, and a
vanishing normalized bound are separate obligations. We assert no density result for the
eligible large-order primes here.

**Actual attack and outcome.** The preregistered threshold E>=1/4 was checked at fresh primes
521,541,569,577,601,613,617,641,653,673 and h=1,3. Of the 20 cases, 16 have L>=sqrt(p);
all 16 certified the threshold. The other 4 were retained as short-order controls. The
independent oracle reconstructed 206 distinct phases by a different integer common-
denominator algorithm and checked all 144 reported interval quantities with 90-digit
mpmath. The latter is calibration, not the authority behind the intervals.

A uniform proof attempt using weighted Gauss completion reduces to the cofiber norm in
SC-3; its measured bounds are vacuous. Summation by parts likewise fails because V is large.
The exact dyadic same-forcing control has E<10^-12 on its coherent window, proving that
odd-primary information alone cannot supply SC-6. The zero boundary and full complementary
source history must enter a new arithmetic step. **SC-6 remains OPEN after these attempts.**

## Validation and dependence

`test_signed_crt.py`: 12 exact tests; `run_probe.py`: 36 period/frequency rows, rational
interval certificates, primary-restoration and dyadic controls, six exact twist-energy
certificates; `independent_oracle.py`: 206 independently reconstructed source phases and
144 90-digit interval cross-checks. Raw outputs are included. No Lean proof is asserted.
The paper proof and production of these scripts share one reasoner; the integer oracle has
independent implementation/representation, not independent mathematical peer review.

All code lives in this new research directory. Authentic/archived source files and historical
contracts remain untouched. The author's Harmonic Numbers / Golden Ratio / Euler--Mascheroni
triangle and Oily--Macaroni provenance are neither renamed nor used as premises for a signed
bound. These arithmetic CRT phases are ordinary classical characters, not physical quantum
amplitudes or probabilities of truth.
