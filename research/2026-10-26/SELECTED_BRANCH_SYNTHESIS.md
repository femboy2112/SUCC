# Selected inverse branches: a quantitative carry bridge and its limits

**Research conclusion, 2026-10-26.** The original BBP source now has a proved
all-horizon bound on the exceptional steps needed to replace inverse digits
and remainder bins by literal carries and arrival bins. The error vanishes
at every prescribed subquadratic resolution. At a particular quadratic
resolution every bin label changes, so that allowance is sharp in order.
This closes a representation-error obligation between PRs #311 and #312.
It does **not** prove that either conditional energy tends to zero. No new
sublinear selected Weyl bound, improved order of the established absolute
modulus loss, or π-normality theorem is claimed.

This is a dossier of proved advances and obstructions, not a proposal to
regard a commuting diagram as cancellation. The original source is always

$$r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_{n+1}=16U_n+r(n+1).$$

The exact unwrapped states, all four signs, source indices and literal
integer carries remain authoritative. Changed selectors appear only in
explicitly marked adversarial controls.

## 1. Lineage, classical inputs and mathematical authority

The worktree descends from the live PR #312 head
`0c306a889f425418c29cbea3193205fb80c0575e`, branch
`research/lambda-inside-out-source-branch-duality-2026-10-26`.
Sibling #311 was inspected at
`a34c4484059e667202b97d5ab4102560987b1406`; their merge base is #310
at `a8c7c85b7a1900d422090f1757c174e7aac69f44`. The sibling was not
merged or treated as an ancestor. Its carry-sensitive primitive mass and
absolute-loss argument were independently rederived where used. The live
main baseline was `6dd80730c3575d91f746546a25da5aedbd2e2737`; main
was not changed. See the [remote baseline](selected_branch_validation/remote_baseline.json).

The inherited source-map firewall of #306, primitive Oily packet and
Gaussian atom decompositions of #307–#310, and #312's conditional Fourier
identity are used with their original limitations. In particular:

- The [Seinfeld dossier](../2026-10-25/SEINFELD_SUCC_NOTHING_THEOREMS.md),
  SS-05/06, already proves odd-torsion inverse uniqueness and failure of a
  continuous circle extension. Those facts are **inherited/classical**.
- The selected conditional-energy identity and existence-of-a-slow-schedule
  equivalence belong to #312. Neither is a new arithmetic saving here.
- The coefficient $1/29$ in the logarithmic **absolute** loss belongs to
  #311's direct arithmetic proof. This round does not improve its order.
- The irrationality exponent two of
  $\xi=\sum_{k\ge0}16^{-2^k}$ is a classical input, with the primary
  publication and attribution in the [analytic dossier](SELECTED_BRANCH_ANALYTIC.md).

The new all-horizon estimates below have **PAPER-PROVED** authority. Exact
`Fraction` and evaluated cyclotomic calculations give **EXACT FINITE**
witnesses. Ten stated finite declarations have actual **LEAN KERNEL**
authority, with four paired positive/negative controls. The infinite
estimates, Diophantine inputs and normality implications are not Lean
formalizations. No independent scholarly-priority claim is made. Parallel
derivations and hostile review came from the same research team/model
family, not external peer review.

## 2. A noncircular exceptional set that the source actually controls

Write $x_n=\{U_n\}$, $j_n=\lfloor16x_n\rfloor$, $t_n=\{16x_n\}$ and
$c_{n+1}=\lfloor U_{n+1}\rfloor-16\lfloor U_n\rfloor$. The carry can
be 16; it is reduced only when evaluating a character. For an integer
scale $a\ge1$, define the genuine forcing spill

$$s_k^{(a)}=\left\lfloor\{16aU_{k-1}\}+a r(k)\right\rfloor\ge0,
\qquad K_{N,a}=\#\{2\le k\le N+1:s_k^{(a)}>0\}.$$

This classification uses source arithmetic, not the measured value of a
desired Fourier estimate. A positive spill places the new fractional
state below $a r(k)$. Positivity, monotonicity and the proved original
bound $r(k)<15/[64(k-1)^2]$ force the next

$$L_a(k)=\max\left(0,\left\lfloor\log_{16}
\frac{4(k-1)^2}{a}\right\rfloor\right)$$

scaled literal carries to be zero. Packing the spill indices gives, for
every $2\le R\le N+1$,

$$K_{N,a}\le B(N,a;R):=\min\left(N,R-2+
\left\lceil\frac{N+2-R}{L_a(R)+1}\right\rceil\right).$$

Prescribe $R=\max(2,1+\lfloor(aN^2)^{1/4}\rfloor)$, using the trivial
bound if $R>N+1$, and call the result $B(N,a)$. The
[arithmetic proof](SELECTED_BRANCH_ARITHMETIC.md) includes every rounding
cost and shows

$$K_{N,1}=O(N/\log N),\qquad B(N,a_N)=o(N)
\quad\text{for every prescribed }a_N=o(N^2).$$

This is a source-verified upper bound on a genuine exceptional timeline.
The local argument also holds for other initial states under this forcing,
and for other positive decreasing forcings satisfying the same upper
bound. It therefore cannot by itself select the π history or imply that
its ordinary carries balance.

### The critical source band cannot be erased

For every $N\ge1$ the unchanged authentic source satisfies

$$K_{N,8N^2}=N.$$

The four-pole rational expression gives $8N^2r(N+1)>1$. After writing
$m=N-1$, its numerator is exactly

$$448m^4+1976m^3+2904m^2+1478m+87>0.$$

Monotonicity proves the result at all earlier transitions. More strongly,
at $M=8N^2$ **every original remainder-bin label differs from its arrival-bin
label**. Here $1\le s_k^{(M)}<M$, since $r(k)\le r(2)=106/819<1/2$ and
$M\ge8$. The exact bin relation is addition of $s_k^{(M)}$ modulo $M$.
This proves failure of a universal vanishing record-change budget at the
critical scale. It does not assert that a relabeling changes the resulting
energy or that a Fourier coefficient has a lower bound.

## 3. The quantitative edge from actual carries to selected branch energy

Compare the two actual empirical records

$$R_n=(\lfloor Mt_n\rfloor,j_n),\qquad
\widetilde R_n=(\lfloor Mx_{n+1}\rfloor,c_{n+1}\bmod16).$$

Let $E_{N,M}(h),\Delta_{N,M}$ be #312's conditional quantities, and use
tildes for the second table. Changing any $K$ records, including both
their bin and digit, changes a conditional unit-character energy by at
most $4K/N$, and the full defect by at most $32K/N$. These universal
constants are sharp. The source bounds the changed records by
$K_{N,1}+K_{N,M}$. Hence

$$\boxed{\lvert E_{N,M}(h)-\widetilde E_{N,M}(h)\rvert
\le\min\left(1,\frac{4[B(N,1)+B(N,M)]}{N}\right),}$$

$$\boxed{\lvert\Delta_{N,M}-\widetilde\Delta_{N,M}\rvert
\le\min\left(15,\frac{32[B(N,1)+B(N,M)]}{N}\right).}$$

The [transport proof](SELECTED_BRANCH_TRANSPORT.md) treats empty bins and
simultaneous bin/label changes. Both errors vanish at every prescribed
$M_N=o(N^2)$, uniformly in $h$. The concrete schedule
$M_N=\max(2,\lfloor\log_2N\rfloor)$ has error $O(1/\log N)$.
There is no favorable-window selection from data.

For the #311 endpoint packet law, let $\Phi_b$ be its primitive mass
conditioned on the actual arrival bin. Its carry translation gives

$$\Phi_b=\frac49+\frac19\Pr(c_{n+1}\text{ odd}\mid b),\qquad
\boxed{\widetilde E_{N,M}(8)=
324\sum_b\widetilde p_b(\Phi_b-1/2)^2.}$$

Thus the missing parity estimate is now precisely a conditional variance
of the actual carry-translated primitive statistic, with the change of
observer paid for. Unconditioned primitive mass cannot replace it. The
quarter-turn identity

$$\widetilde E(4)=\widetilde E(12)=\frac{1+\widetilde E(8)}2
-4\sum_b\widetilde p_b(p_{b0}p_{b2}+p_{b1}p_{b3})$$

also exposes the extra opposite-pair correlation. Even perfect parity
balance does not force quarter-turn cancellation.

## 4. Why more exact conditioning can be the wrong objective

Let $Q_N=\operatorname{lcm}_{n\le N}\operatorname{den}(r(n))$. The
original four-pole cancellation makes $Q_N$ odd; it also equals the
minimal common denominator of the actual states. The inherited unique
odd inverse means each exact tail determines one digit, without any
assumption that different times have distinct tails. Therefore the new
[resolution theorem](SELECTED_BRANCH_OPERATOR.md) gives

$$\Delta_{N,M}\ge
\frac{16}{\min(16,\lceil Q_N/M\rceil)}-1.$$

In particular **the authentic orbit itself** satisfies
$E_{N,M}(h)=1$ and $\Delta_{N,M}=15$ whenever $M\ge Q_N$. Exact-tail
conditional energy cannot contract. On the corresponding common odd
carrier the authentic affine step is a permutation and its pullback is
unitary. The real-circle Haar transfer, with sixteen possible predecessors,
is a different operator. The source-selected singleton inclusion is
noncartesian; a signed missing-point indicator explicitly detects its
failure to preserve pushforward. No lambda/Yoneda identification preserving
all evaluations can discard that difference.

Weak limiting measures do not repair this for free: the odd inverse is
discontinuous, and exact-tail conditioning need not commute with a weak
limit. Under the **unproved normality premise**, the two iterated limits
of $\Delta$ would be zero and 15 in the two orders. This is an order-of-limits
obstruction, not a contradiction to normality.

## 5. A stronger hostile control against the proposed energy route

The [analytic dossier](SELECTED_BRANCH_ANALYTIC.md) constructs, for every
finite cutoff $H$, one **fixed changed real seed** obeying the complete
original forcing at every time. Choose $q=3^k$, $L=q/3>H$, $q\le9H$, and

$$\alpha=1/q+\sum_{j\ge0}16^{-2^j},\qquad
W_n=16^n\alpha-T_n,\qquad W_0=\alpha-\pi/16<0.$$

This control has:

- $A_N^W(h)=O_H(\log(N+1)/N)$ for every $0<|h|\le H$;
- $E_{N,M}^W(h)\to1$ and $\Delta_{N,M}^W\to15$, uniformly for every
  $M\ge q$, including arbitrary growing schedules;
- endpoint irrationality exponent two and the same donor-level $1/29$
  logarithmic absolute-loss bound at every fixed nonzero frequency;
- $A_N^W(L)\to e(1/3)\ne0$, so it is nonnormal.

The infinite future sparse digits and Green tail have explicit summable
budgets. A source-independent bad-time set has size $O_q(\log N)$ and
pays for the uniform conditional-energy conclusion. The control fails
the authentic zero seed and is **not** assigned its rational-state or
conductor passport. Only negativity and nonzeroness of this initial seed
are proved; its irrationality is not assumed. This does not refute the
all-mode normality equivalence or the possibility of an estimate genuinely
using the zero selector. It refutes combining finite-band cancellation,
finite Diophantine type, the complete forcing and logarithmic absolute
loss as though they already forced the conditional-energy estimate.

## 6. Preserve the cross-bin signs and state the remaining obligation

Let $\tau_b=(b+1/2)/M$ and retain the actual complex bin amplitudes:

$$\widetilde C_{N,M}(h)=\frac1N\sum_{n=1}^N
e\left(\frac{h(c_{n+1}+\tau_{\lfloor Mx_{n+1}\rfloor})}{16}\right).$$

The literal recurrence gives the exact continuous-character estimate

$$\left|A_N(h)-\widetilde C_{N,M}(h)\right|
\le\frac{\pi|h|}{16M}
+\frac{\pi|h|}{8N}\sum_{n=1}^N r(n+1).$$

There is no upper restriction on $M$ for this signed transport. All
cross-bin terms survive; taking conditional absolute squares would lose
them. Outward rational certificates evaluate this finite instrument with
the existing native Machin/Taylor engine. A bound at one horizon is finite
evidence only.

**Next narrow obligation, still OPEN.** At the preset
$M_N=\max(2,\lfloor\log_2N\rfloor)$, prove from the zero-selected source
either the carry-conditioned variance above tends to zero (first $h=8$,
then all required branch modes), or the weaker signed quantity
$\widetilde C_{N,M_N}(h)\to0$ for every fixed $h\ne0$. The latter suffices
by the displayed bound and the authenticated Green-to-π transport, but
merely defining it is not progress on that cancellation. The completed
work removes an independently bounded source discrepancy and proves
specific failure mechanisms for suggested replacements; the final signed
arithmetic estimate survives.

See the [scoped claim ledger](../../docs/CLAIM_SUPPLEMENT_SELECTED_BRANCH.md),
[validation receipt](SELECTED_BRANCH_VALIDATION.md), and
[next handoff](../../handoffs/SELECTED_BRANCH_NEXT_PI_2026-10-26.md).
