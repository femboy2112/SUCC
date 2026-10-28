# Operation π, round 2: source reconstruction and the conditional-energy obstruction

**Verdict: new paper theorems and decisive obstructions; π normality remains OPEN.**
The original source and zero seed are unchanged. No stronger bound for the
authentic real Weyl sum is claimed. The results below were derived and checked
by separate internal lanes, then audited adversarially. This is not external
peer review, a Lean formalization, or a claim of priority in the literature.

## 1. The strongest new obstruction

Fix a prime p≥7. Write q=p^L, A(x)=120x²−89x+16, and let m_a be the number
of time residues modulo q having A-value a. For phases z_n, 1≤n≤N, put

$$S_a=\sum_{\substack{1\le n\le N\\A(n)\equiv a\pmod q}}z_n,
\qquad c_a=\#\{1\le n\le N:A(n)\equiv a\pmod q\}.$$

Three distinct energies matter:

$$C_A=\frac q{N^2}\sum_a|S_a|^2,\qquad
H_A=\frac q{N^2}\sum_{m_a>0}\frac{|S_a|^2}{m_a},\qquad
Q_A=\frac1N\sum_{c_a>0}\frac{|S_a|^2}{c_a}.$$

C_A is the proposed unweighted numerator-fiber gate. H_A uses the actual
pushforward Haar weights m_a/q. Q_A is exactly the squared norm of the
empirical conditional expectation of z given A(n) modulo q. In particular,
normalizing by the number of occupied labels is not the Haar normalization.

**Theorem R2.1.** For every prescribed schedule q(N)=p^{L(N)}→∞ with
q(N)=o(N), there exists one base-16 normal real α with irrationality exponent
at most four, such that, for z_n=e(h16^{n−1}α), simultaneously for every
fixed nonzero integer h,

$$\liminf_{j\to\infty}C_A(2^j,q(2^j),h)\ge\frac14,$$
$$\liminf_{j\to\infty}H_A(2^j,q(2^j),h)\ge\frac{p}{8(p+1)},
\qquad
\liminf_{j\to\infty}Q_A(2^j,q(2^j),h)\ge\frac{p}{8(p+1)}.$$

At p=7 the latter constant is 7/64. The quantifiers allow a different α for
each prime and prescribed schedule, including nonmonotone schedules. The
same α handles every fixed h; no uniform bound over growing h is asserted
beyond the explicit finite-stage range in the proof. The lower limits are
dyadic, not asserted at every N. The construction uses the augmented word
conditions for all three energies; an earlier lexicographic selection is
not silently assumed to satisfy new constraints.

[Full proof](PI_QUADRATIC_FIBER_ENERGY_OBSTRUCTION.md). The new step beyond
#327 is a bounded-fiber truncation that makes the quadratic coarse gate
controllable, followed by the genuine fiber-average projection for H_A and
Q_A. It is not an application of monotonicity from fine to coarse energy:
that monotonicity is false. Exact cyclic-word second moments and
independent-digit variance estimates replace a false independence assumption
between radix phases. Marker conditioning, all-prefix normality and rational
separation preserve the irrationality-exponent bound for this same α.

All three conclusions transfer to

$$V_n=16^{n-1}\alpha-T_n,\qquad V_0=(\alpha-\pi)/16,$$

with the **unchanged original four-pole forcing**. These are changed real
selectors, generally irrational states. They are not assigned authentic
2-adic U-states and are not counterexamples to a theorem specifically using
U_0=0. The theorem shows that neither generic normality, finite irrationality
type, nor correcting the conditional weights supplies the proposed moving
energy estimate.

## 2. Positive arithmetic: the full source reconstructs its input

Use the projective source R(x)=[A(x):D(x)] on affine time residues, retaining
all poles, and its consecutive code F_d(x)=(R(x),…,R(x+d−1)). The ordered
collision counts at every depth L≥1 are:

| Prime | One source sample | Two consecutive samples | Three consecutive samples |
|---|---|---|---|
| 7 | (12L+7)7^{L−1} | 7^L+2 | 7^L |
| 11 | (10L+17)11^{L−1} | 11^L+2 | 11^L |
| 241 | (240L+257)241^{L−1} | 241^L | 241^L |

At 7, three is the minimum number of consecutive full-source values that
recover time at every depth. Two samples have one persistent exceptional
unordered pair; its first lifts are {2,3}, {24,30}, {220,324}. The proof uses
integral local Taylor expansions, a proved quadratic Morse coordinate and a
nonsingular two-variable Hensel intersection. It is not extrapolated from
finite counts. At 241 the fresh depth-two holdout gives
(177617,58081,58081).

[Proof and finite certificates](PI_FULL_SOURCE_DELAY_RECONSTRUCTION.md).
The one-sample full-source collision slope at 7 is twice the numerator's
slope; denominator information does not automatically lower collision counts.
With arbitrary unit-bounded phases and q=7^L or 11^L,

$$G_2(N,q)=E(N,q)+\frac{2q}{N^2}\Re(Z_{a_L}\overline{Z_{b_L}}),
\qquad |G_2-E|\le\frac2q(1+q/N)^2.$$

Three samples give G_3=E exactly; at 241 already G_2=E. Thus full-source
delay conditioning reconstructs the old time partition and inherits its
prescribed-schedule obstruction. Reconstruction is a positive arithmetic
theorem, not a real cancellation theorem.

A second exact resolution uses the pair (A,D):

$$3375D=120A^2+2746A-3781-8x(930A-1243),$$
$$D(x)-D(89/120-x)=-\frac{(240x-89)(930A(x)-1243)}{50625}.$$

The complete collision classification exposes observation-specific primes
31,109,251, distinct from bad reduction at 2,3,5 and numerator-root
ramification at 241. At generic p≥7 the count is q or q+2 according to the
quadratic character of 27359/31; p=31 is injective. At p=109 or 251 it is q
for L=1, and q+(p−1)p^{L−1} for L≥2. Also, two numerator samples separated
by a shift s have exactly

$$q+\min(v_p(s),L)(p-1)p^{L-1}$$

collisions, with v_p(0)=∞. Every unit shift resolves the numerator branch.
[Proof](PI_JOINT_SOURCE_OBSERVATION.md). This separates Gaussian splitting,
source reduction, and the ramification of a chosen observation map.

## 3. Modular signed cancellation is real mathematics, but a different character

For q=7^L, L≥2 and 7∤a, the actual rational source satisfies

$$\left|\sum_{x\bmod q,\ 7\nmid D(x)}
 e_q\bigl(a[r(x)]_q\bigr)\right|\le2\sqrt q.$$

The two nondegenerate critical disks each contribute a quadratic Gauss sum
of magnitude √q; the remaining regular disk contributes zero. The regular
numerator-mirror difference has exactly zero complete character sum. Both
claims have short elementary proofs, including every conductor and excluded
pole disk.

Yet for the periodic modular observable
w_x=1_{7∤D(x)}e_q(a[r(x)]_q), its C_A energy on any complete number of periods
is **exactly 2/7**, even when N=q². This is a triangular modular family with
zero weights on four pole disks, not a fixed radix carrier.
[Proof](PI_PRIME7_MODULAR_REAL_BRIDGE.md).

The missing real factor is explicit. If u=A/B with 7∤B, R=[AB^{-1}]_q and
K=(BR−A)/q, then

$$e(hu/q)=e_q(hR)e_B(-hK),\qquad e(hu)=e_B(-hqK).$$

The complementary character cannot be dropped; in the unscaled real
character the integer residue R disappears. The authentic real source echo
e(h(U_n−16U_{n−1}))=e(hr(n)) tends to 1. Thus the same authentic rational
function exhibits modular oscillation and real echo coherence. No changed
seed is needed for that distinction. Four of the seven time disks are poles
for the modular finite chart, a positive-density omission, not a negligible
exceptional set.

## 4. The Gaussian lift has an exact descent boundary

For λ=1+i and the inherited source lift Ψ, conjugation equivariance and
isometry prove Ψ(Z₂)=Z₂ and Ψ^{-1}(Z₂)=Z₂. If Ψ(a+bi)=c+di, then
v₂(d)=v₂(b), and d/b≡−1 mod4 for b≠0. At depth λ^m, the successor has
2^{floor(m/2)} cycles, each of length 2^{ceil(m/2)}. Natural time visits
exactly the rational cycle. At m=8k it occupies 16^k of 16^{2k} states.

Finite conjugation-fixed states equal rational states at odd depths; at even
depths there is one extra fixed cycle, with no conjugation-fixed lift at the
next odd depth. The false finite descent is already refuted by i modulo 2.

More sharply, for every nonzero integer h, every m≥1 and every complex-valued
function g on the finite Gaussian quotient,

$$\sup_{n\ge0}|e(hU_n)-g(U_n\bmod\lambda^m)|>
\frac{47}{39168}.$$

There is no continuous extension of this real Fourier phase to the rational
or Gaussian completed state. [Proof](PI_GAUSSIAN_DESCENT_PHASE_OBSTRUCTION.md).
This is an obstruction in the uniform norm, not in density or empirical L².
It holds regardless of whether π is normal. It does not establish a
selection advantage of the zero seed: the phase-pair argument also applies
to changed real selectors when time-clock labels are supplied externally.
The inherited zero theorem identifies the authentic arithmetic orbit; it
does not supply the missing real decorrelation.

## 5. Falsifiable attempts and their verdicts

| Attempt and precise predicted inequality | Assumptions tested | Receipt / hostile family | Verdict |
|---|---|---|---|
| Numerator mirror forces C_A−E≤0 | Actual four poles, U_0=0, all finite N | Certified h=2,p=7 positive values; h=1 negative value | REFUTED |
| Two full source samples are injective at all 7-adic depths | Projective values, all poles included | One Hensel-lifted pair at every depth | REFUTED; three samples suffice |
| Normality and finite type imply prescribed C_A→0 | Fixed p≥7, any prescribed q→∞, q=o(N) | One normal α with μ(α)≤4 and dyadic liminf≥1/4 | REFUTED |
| Correcting Haar/empirical weights restores that necessity | Same schedule and normal finite type | Same augmented α, liminf H_A,Q_A≥p/[8(p+1)] | REFUTED |
| Modular source cancellation gives a decaying C_A | Complete regular source character at depth L≥2 | Scalar O(q^{-1/2}); C_A=2/7 exactly | REFUTED |
| Gaussian finite clocks approximate the real phase uniformly | Arbitrary depth and arbitrary observable g | Explicit universal error >47/39168 | REFUTED |
| A-fiber energy decreases when refining p-adic depth | Fixed N, arbitrary complex weights | Exact nonnegative child-difference identity | Opposite inequality PROVED |
| Ignore mixed valuation pairs beyond the prime level | q=7² or 7³ | All 12 tested authentic cases have nonzero omitted contribution | REFUTED |

The nonnormal #320 source remains a mandatory control: its summably small
tail makes C_A asymptotic to 1+L(1−1/p), while H_A and Q_A tend to 1. The
same-forcing future-selected V_n=−T_n behaves likewise. None is quietly
identified with the actual rational zero-selected trajectory.

The exact refinement statement, for every N≥1, is

$$C_{L+1}-C_L=\frac{p^L}{N^2}\sum_{a\bmod p^L}
 \sum_{0\le i<j<p}|S_{L+1,a+ip^L}-S_{L+1,a+jp^L}|^2\ge0.$$

It sharpens the endpoint-qualified comparison in #327. It also holds for
ordinary time-residue energies at nested moduli. It must not be transplanted
to a joint label with a different number of children but unchanged prefactor;
the joint (A,D) energy supplies an explicit contrary control.

## 6. What would change the verdict

The final live check found a new sibling at
`91d908b775241df6a7f91e9de843c88e6774e0c9`, announced on #325. Its complete
sheet/pole/target/lift code is faithful and has exactly q valid states. Its
unweighted and Haar energies equal E; empirical energy agrees on complete
periods and differs asymptotically by o(1) when q=o(N).

The partial code B=(A,sheet,pole), with the lifting index omitted, has

$$k'_L=1+(p-1)\sum_{s=0}^{\lfloor(L-1)/2\rfloor}p^{L-2s-1},
\qquad k'_L/p^L\longrightarrow p/(p+1).$$

The pole bit is redundant within each partial fiber, though it remains an
authentic source check. The projection proof extends to **any deterministic
partition** of q residues with k_q/q→κ>0: one normal finite-type α has
proper Haar and empirical energy lower limits at least κ/4. Any fixed
finite collection of such partitions can be handled simultaneously. Thus
the partial two-bit code has the stronger lower constant p/[4(p+1)], or
**7/32 at prime 7**. Its original A-partition and complete code can be
included in the same augmented construction.

There is also an exact source-memory theorem. Any autonomous deterministic
quotient of the successor which retains A must be injective, because

$$[A(x+1)-A(y+1)]-[A(x)-A(y)]=240(x-y).$$

Under uniform finite time, the partial code for L≥2 has exact Markov order
two. Its one-step conditional entropy is

$$H(B_{n+1}\mid B_n)=\frac{\log p}{p-1}
 (1-p^{-\lfloor L/2\rfloor}),\qquad
H(B_{n+1}\mid B_{n-1},B_n)=0.$$

Two outputs reconstruct the residue, so every output block of length at
least two has entropy log q and the entropy rate is zero. Positive
one-step uncertainty therefore cannot be treated as independent branch
innovations. These are the correct finite Haar-time laws, not a claimed
probability law for π. [Complete extension and audit](PI_TWO_BIT_PARTITION_MEMORY_OBSTRUCTION.md).
All ten unchanged sibling focused tests and an independent 81,254-state
enumeration passed in an isolated namespace. No sibling code was merged.

The new result cuts off four proposed routes: generic finite type plus a
prescribed energy schedule; normalization repair; extra Gaussian states as
extra observations; and modular character cancellation without its real
cofactor. None bounds the authentic zero-selected Weyl sum by o(N).

A verdict-changing proof must establish a **signed estimate coupling the
real complementary phase to the authentic arithmetic data, using U_0=0 in
a way that fails at the same-forcing changed selectors**. For example, an
arithmetic Fourier expansion on an explicitly specified period Q_N would
need a proved tail L¹ error o(N), explicit coefficient ℓ¹ norm B_N, and
selected sums bounded uniformly by ε_N N with B_N ε_N→0. Merely applying
modular stationary phase to a substituted character does not establish
any of these three obligations. Each frequency range and conductor must be
quantified; a fixed finite band is excluded by #324/#327 countermodels.

The weakest energy assertion still sufficient for normality is a proved
authentic C_A→0, or Q_A→0, along some admissible schedule for every fixed h.
Existence of a sufficiently slow schedule is equivalent to normality and
is **not itself an advance**. A prescribed schedule asks for more, as R2.1
now proves for both normalizations. No source-selected conditional
decorrelation or martingale premise has been assumed.

The earlier real-boundary result from #327 remains O(N/log N) at the fifteen
nonzero hexadecimal cuts; the zero cut remains unresolved for π. Smooth
lag-observer saturation, the E−16 echo target 1, and the finite-mode
counterexample remain unchanged. This round earns no new selected-boundary
estimate or improvement to #319's authentic real Fourier coercivity.

## 7. Literature and provenance

Bailey–Crandall's [Hypothesis A](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf)
is a conjecture for proper rational forcing and the zero initial condition.
Its π instance already implies the desired normality; labeling that instance
a new source condition would hide the target. Their changed-seed discussion
also underscores why the selector cannot be omitted.

Lagarias's [Theorems 3.1 and 3.3, and §4](https://arxiv.org/pdf/math/0101055)
separate general orbit shadowing, finite limit sets, dense-orbit hypotheses
and uniform-distribution hypotheses. Shadowing with decaying real errors
does not give cancellation. The new source-delay and Gaussian theorems do
not cross that gap.

The modular proof is self-contained. Its literature crosscheck is
[Bag–Baier–Haldar, Theorem 1](https://arxiv.org/pdf/2311.17706), with the
denominator-unit domain enforced. [Milićević's equation (4) and Definition 1](https://arxiv.org/pdf/1407.4100)
treat specified periodic p-adic phases, not a free replacement of the real
SUCC phase. [Silverman, AWS §6](https://swc-math.github.io/aws/2010/2010SilvermanNotes.pdf)
supplies the good-reduction scope; iteration of a rational map is distinct
from evaluating this forcing at consecutive integers. All were inspected
directly in this round; no unavailable publisher theorem is used.

| Reference | Pinned head / scope |
|---|---|
| #324 | fca58d3e0289e57596dd8ca74bace325a450df31; inherited dossier and handoff |
| #325 | 95ee2f1fab851afe1517d8ec5a0589885842426f; source Gaussian lift and prime-7 mirror, read-only sibling |
| #326 | 681f79cc1f045bef7cf2aa9e2b20ba1e9f7f27b2; Claude integration audit, read-only sibling |
| #327 | 76f3799658fde8a2eff649b0bd4926a2173918d0; actual parent, E7 and phase primitives |
| Two-bit sibling | 91d908b775241df6a7f91e9de843c88e6774e0c9; fresh #325 comment, full dossier/handoff/code/tests read and audited |
| main | 6dd80730c3575d91f746546a25da5aedbd2e2737; observed only |

Branch: `research/pi-prime7-mirror-source-descent-2026-10-27`, child of #327.
The earlier #315,#316,#319–#323 dependency reading is recorded in the parent
dossier. The complete #325 proof, probe and handoff, plus #326 integration
handoff, were inspected afresh. AGENTS.md and provenance were rechecked.
No sibling source was merged and no preserved original was rewritten.

## 8. Reproduction

See [validation and commands](PI_PRIME7_ROUND2_VALIDATION.md),
[the claim ledger](../../docs/CLAIM_SUPPLEMENT_PRIME7_ROUND2.md), and
[handoff](../../handoffs/CODEX_PI_PRIME7_ROUND2_2026-10-27.md).

The real-phase receipt contains 144 rows: 36 authentic and 108 controls.
All phases are reduced modulo one as exact rationals before trigonometric
enclosure. Maximum reported energy-interval width is 1/549755813888.
The exact modular receipt covers first-depth failure controls, cyclotomic
vanishing, incomplete-N refinement, and bounded-fiber kernels. Separate
projective and Gaussian probes include fresh 241² and odd-depth holdouts.
Finite computations corroborate the paper arguments; they do not certify
any asymptotic property of π.
