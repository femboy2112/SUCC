# Same-model hostile audit: Borwein L2 appendix §§1--4

**Verdict: PASS as a paper proof, within the stated static-probability scope.**
No mathematical defect was found in §§1--4 of
`history_scratch/BORWEIN_L2_OPTIONAL_APPENDIX.md`, using BI-1 and BI-2 from
`SUCC/research/2026-11-17/pro_pi_crucible/BORWEIN_INVERSE.md` as the declared
previously proved instrument. This is same-model review, not an independent
external referee or formal verification. The optional Erdős--Turán section
was not used and was not audited.

## Checks of the load-bearing steps

1. **Semiconcavity and derivative estimate.** The distributional formula
   `g''=(324/289)(1_hot*mu)dt-(288/289)tau mu` is correct because the Haar
   convolution of L'' is zero. Positivity and mass one imply
   `g''<=(324/289)dt`. For smooth g, integrating this upper second-derivative
   bound backward from a positive derivative p gives
   `g(x)-g(x-t)>=pt-Kt²/2`. For negative p, the forward version gives the
   same absolute derivative bound. These inequalities hold on the periodic
   lift for all t>=0; they do not require t<=1/2. At t=|p|/K they imply
   `A>=M²/(4K)` with no missing sign assumption.

2. **Circle tent geometry.** Mean zero is essential and is present. For
   M>0, g has a zero. A point of maximum absolute value lies within circle
   distance 1/2 of any selected zero, hence `A/M<=1/2`. The two tent halves
   of radius A/M therefore do not double count any positive-measure region
   of the circle. The reverse triangle inequality supplies
   `|g(x+t)|>=A-M|t|` regardless of whether the maximum is positive or
   negative. Integrating gives `V>=2A³/(3M)>=M^5/(96K³)`. If M=0, mean
   zero gives g=0 and BI-1 gives nu=0; no division by zero is used.

3. **Interval inverse.** Since P is convolution by a probability,
   `|(P nu)(I)|<=D_arc`. Evaluating BI-1 on an interval and bounding the
   derivative endpoint difference by 2M gives
   `(7/8)D_arc<=(289/288)2M`, hence `D_arc<=(289/126)M`. The supremum need
   not be attained: the inequality holds for each interval and then passes
   to the supremum.

4. **Atomic extension.** Positive smooth mollification preserves
   probability and semiconcavity. Jensen/Young contraction gives
   `||g*mollifier||_2<=||g||_2`, so the same right side controls every
   mollification. Weak convergence transfers the bound to intervals with
   nonatomic endpoints. For arbitrary endpoint conventions, enclose the
   interval from outside to bound positive discrepancy and from inside to
   bound negative discrepancy, choosing nonatomic endpoints and taking
   lengths to their target. This handles endpoint atoms; no unsupported
   continuity of discrepancy under weak convergence is assumed.

5. **Sharpness packet.** For 0<epsilon<=1,
   `mu_epsilon=m-1_I dt+epsilon delta_0` is a nonnegative probability.
   Its discrepancy is at most epsilon, and intervals shrinking around zero
   approach epsilon, so `D_arc=epsilon` as a supremum. The centered-interval
   Fourier transform and `1-sinc(t)=integral_0^1(1-cos(tu))du` yield the
   global bound `|nuhat(h)|<=min(2epsilon,pi²h²epsilon³/6)`. No random
   source interpretation is involved.

6. **Packet energy and optimal exponent.** With epsilon=1/H, the low
   frequencies contribute at most `729/167042 * epsilon^5`. The high
   frequencies contribute strictly less than
   `17496/(83521*pi^4)*epsilon^5 <216/83521*epsilon^5`. Their sum is
   `1161/167042 * epsilon^5`. Therefore beta>1/5 is impossible in a uniform
   `D_arc<=C V^beta` inequality. The exponent is sharp; the displayed
   constant is not claimed optimal. This distinction must remain explicit.

7. **Original-source specialization.** The positive small BBP tail gives
   the inherited uniform kernel-response error epsilon_B. On a circle of
   Haar mass one it also bounds the L2 difference. Minkowski gives
   `sqrt(Vtrue)<=sqrt(Vhat)+epsilon_B`. Any nonnegative rational q with
   `q²>=Vhat` therefore yields the stated fully rational fifth-power
   discrepancy certificate. This is a finite certificate and supplies no
   source-specific asymptotic upper bound on Vhat_B.

## Exact arithmetic receipt

One small Python/Fraction check was executed, with these exact equalities:

```
(289/126)^5 * 96 * (324/289)^3 = 144324288/16807,
2*(27/578)^2 = 729/167042,
17496/(83521*81) = 216/83521,
729/167042 + 216/83521 = 1161/167042.
```

The fifth root of the main constant is approximately
`6.1202596130802317530792983606054756849281238589744`.
The decimal coefficient 6.121 is a valid upward rounding; the exact test
`(6121/1000)^5 >= 144324288/16807` returned True. The rational fifth-power
bound remains the authoritative statement.

No broad tests, finite-pi sweep, new theorem import, or formal checker was
run for this audit. No repository edits were made.

## Boundary

The audited result is

`D_arc(mu)^5 <= (144324288/16807)||L*(mu-m)||_2^2`

for every Borel probability mu on the circle, with sharp exponent 1/5.
It is valid instrument mathematics. It does not show that the authentic
BBP shell energy decays, and it does not prove R0 or pi normality.
