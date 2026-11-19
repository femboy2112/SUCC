# Source-clock transport, causal memory, and the remaining real-phase estimate

Research date: 2026-11-18, America/New_York. Base: Main XXVI,
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`.

This synthesis joins the explicit [Fibonacci construction](FIBONACCI_LOCAL_BRIDGE.md),
the [mixed-place shadow theorem](CAUSAL_SHADOWS.md), and the
[Collatz/RH translation](COLLATZ_RH_TRANSLATION.md). Paper proofs and finite
implementation checks have different authority. R0, pi normality, Collatz and RH
remain OPEN. No claim of academic priority or physical measurement is made.

## 1. Source and causal contract

Retain, for every integer n>=1,

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Write x=pi/16, P_n=sum_(j=1)^n 16^(-j)r(j) and
T_n=sum_(j>=1)16^(-j)r(n+j). The inherited BBP identity gives

\[
U_n+T_n=16^n x,\qquad 0<T_n<r(n+1)/15.
\]

Here T_n denotes the scalar Green tail; the bold matrix \(\mathbf T\) below
denotes the five-channel Fibonacci successor. They are unrelated types.
All four signs, the literal zero boundary, chronological integer winding and
actual carries remain part of the source contract.

An embedded observer has a present state (n, memory, model, permitted probes).
Its legal source transition increases n. A computation that estimates a previous
state is performed now; it is not a legal backward source transition. A repeated
local report may therefore be a cycle in a quotient while the causal state is
different. The internal model must retain the distinctions needed for its task;
the forward arrow alone does not require unbounded memory for every task.

For moving linear readouts P_n and proposed internal updates B_n, the prediction
defect is the inherited nonstationary expression

\[
D_n=P_{n+1}K_n-B_nP_n.
\]

Nothing about changing coordinates alone supplies a signed arithmetic bound.
The explicit map below is useful because it satisfies its forward square and
identifies its exact loss of information.

## 2. C235-04: a compatible source-to-Fibonacci observer

Let \(C(n)=120n^2-89n+16\). The inherited source-clock theorems state:

* \(\Phi_a(n)=[U_n]_{2^a}\) is a compatible bijection of time classes modulo
  2^a; identifying its infinite-past interpolation with U_n uses the original
  zero-boundary theorem.
* \(C_b(n)=[C(n)]_{3^b}\) is a compatible bijection of time classes modulo
  3^b. This is the cleared **forcing numerator**, not a reduction of U_n in Z_3.

Fix a,b>=1 and M=2^a3^b. Invert these two maps and use ordinary CRT to define

\[
\tau=\operatorname{CRT}(\Phi_a^{-1}(u),C_b^{-1}(v))\pmod M.
\]

Put \(\mathbf T=\operatorname{Sym}^4(A^2)\), A=[[1,1],[1,0]], and e0=(1,0,0,0,0).
The proved orders in the Fibonacci note are

\[
u_a=3\,2^{\max(a-3,0)},\qquad v_b=2\,3^{b-1}.
\]

Both divide M. Thus

\[
\mathcal J_{a,b}(u,v)=
(\mathbf T^\tau e_0\bmod2^a,\ \mathbf T^\tau e_0\bmod3^b)
\]

is independent of the representative of tau. When the actual BBP clock advances,
tau becomes tau+1 modulo M, and

\[
\mathcal J_{a,b}(\Phi_a(n+1),C_b(n+1))
=\mathbf T\,\mathcal J_{a,b}(\Phi_a(n),C_b(n)).
\]

For smaller a',b', compatible source inverses reduce tau modulo 2^(a')3^(b').
The corresponding matrix orders divide that smaller modulus, so reduction of
the finer observer agrees with the coarser observer. This proves the entire
compatible family, not merely a coincidence at one modulus.

**Exact compression.** For a>=4,b>=2, the joint e0-orbit period is

\[
L=\operatorname{lcm}(u_a,v_b)=2^{a-3}3^{b-1}=M/24.
\]

Every one of its L reports therefore has exactly 24 preimages among the M source
clock labels. This number is an information-loss certificate for this map; it is
not an identification with any other occurrence of 24 in SUCC.

**Scope.** This is a forward observer factor through the recovered clock. It
does not conjugate the BBP rational recurrence to Fibonacci dynamics and does not
retain the real phase. One BBP clock tick drives two Fibonacci ticks by the
declared observer rule. This convention is explicit, not a discovery that the
native carrier laws are identical. A fifth-prime report requires the additional
retained time residue modulo 5^c.

`clock_bridge.py` implements the map using the existing source codecs. Their
finite implementation caps are a<=32,b<=15; the mathematical construction is
all-depth. Independent tests compare the output with literal Fraction source
states and with quartics of the fast-doubled Fibonacci pair.

## 3. C235-05: actual zero-source real phase cannot descend to a fixed local clock

This is a joint binary/ternary extension of inherited HBR-04 in
`research/2026-11-02/carrier_hbar_bridge/PROOFS.md`, not a newly discovered
expanding-circle principle.

**Classical gap lemma.** For every irrational beta and integer B>=2,

\[
\limsup_{n\to\infty}\|B^n\beta\|_{\mathbb R/\mathbb Z}\ge\frac1{B+1}.
\]

Proof: if the limsup were smaller, choose c strictly between it and 1/(B+1).
For all late n, choose nearest integers m_n and errors eps_n=B^n beta-m_n
with |eps_n|<c. The integer m_(n+1)-B m_n has absolute value at most
|B eps_n|+|eps_(n+1)|<(B+1)c<1, hence is zero. Thus eps_(n+1)=B eps_n
forever, and boundedness forces eps_n=0, contradicting irrationality. The
argument is universal; finite numerical checking is not its proof.

Let \(\ell_{a,b}(n)=(\Phi_a(n),C_b(n))\), h a fixed nonzero integer, and
M=2^a3^b. This label is exactly M-periodic. But for the **original zero seed**,

\[
h(U_{n+M}-U_n)=16^n\beta+h(T_n-T_{n+M}),\qquad
\beta=h(16^M-1)\pi/16.
\]

Beta is irrational by the classical irrationality of pi, and the tail difference
tends to zero. Apply the lemma with B=16 and use
|exp(2pi i t)-1|=2 sin(pi ||t||_T). It follows that

\[
\boxed{\limsup_n|e(hU_{n+M})-e(hU_n)|\ge2\sin(\pi/17).}
\]

Consequently, for **every fixed function** f on the finite label set,

\[
\boxed{\limsup_n|e(hU_n)-f(\ell_{a,b}(n))|\ge\sin(\pi/17).}
\]

Proof: f takes the same value at n and n+M; the sum of the two prediction errors
bounds their target separation. Taking limsups gives the displayed bound. The
same result holds for a fixed finite window of these periodic reports.

**Finite internal-state extension.** Any deterministic observer with a finite
internal state set, time-homogeneous update/output, and only these fixed-resolution
periodic labels as external input has eventually periodic output. Augment its
state by n modulo M; this is a finite deterministic system, so an eventual cycle
exists. Apply the same gap argument to its positive eventual output period L.
Its limsup phase error is again at least sin(pi/17).

The exclusions matter: an unbounded retained clock, increasing local precision,
an explicitly time-varying model, or exact current rational forcing r(n) is not
such a finite periodic input model. In particular r(n) is strictly decreasing
on positive integers and exact knowledge of it can distinguish the clock.
The theorem concerns fixed finite compression, not impossibility of computing pi.

**What is gained toward pi.** This is an actual selected-zero-source real-phase
separation theorem, without changing its seed. It guarantees infinitely repeated
separation and a quantitative failure of fixed local descent. It supplies no
positive density of separated positions and therefore does not prove R0.

### 3.1 A countermodel to the missing density inference

The distinction has a concrete receipt. Let

\[
\beta_* = \sum_{j\ge1}16^{-j!},\qquad B_k=2k!\quad(k\ge4).
\]

The base-16 expansion has ones at distinct factorial positions and zeros
elsewhere. Its unbounded zero runs and infinitely many ones prevent eventual
periodicity, so beta_* is irrational. For B_k<=n<2B_k, the terms with j<=k
in 16^n beta_* are integers, and the remaining positive tail satisfies

\[
0<\{16^n\beta_*\}
\le\sum_{m=(k+1)!}^{\infty}16^{n-m}
\le\frac1{15}16^{-(k-3)k!}.
\]

The bound is less than one and justifies the fractional-part equality. Since
1-cos(2pi t)<=2pi^2 t^2,

\[
0\le1-\Re\left(\frac1{B_k}\sum_{B_k\le n<2B_k}e(16^n\beta_*)\right)
\le\frac{2\pi^2}{225}\,16^{-2(k-3)k!}\longrightarrow0.
\]

Thus this irrational fails an eventual uniform R0 margin. Yet at
n=(k+1)!-1 its fractional part tends to 1/16, giving infinitely recurring
separation even stronger than the general 1/17 lemma. This is an exact
countermodel to upgrading a limsup separation to positive shell density.
It is not pi and makes no claim about the authentic zero-selected BBP orbit.

## 4. C235-06: finite-history controls can also match both genuine local places

The complete construction and proof are in [CAUSAL_SHADOWS.md](CAUSAL_SHADOWS.md).
For every finite carry-residue word of length N, a>=2 and b>=1, a rational
changed seed s with denominator prime to 6 satisfies, for every n>=0,

\[
v_2(U_n(s)-U_n(0))\ge a+4n,\qquad
v_3(U_n(s)-U_n(0))\ge b,
\]

while realizing exactly the prescribed values of floor(U_n(s)) modulo 4 for
1<=n<=N. The rational seed is constructed from P_(N+1), with no numerical pi
oracle, and has height at most 256(2^a3^b)16^N+1.

The adaptive version preserves every finite transcript driven by such local
queries, including the actual 3-adic polar parts. It preserves source-only
windows and the derived clock observer at the specified resolutions. It fails
the exact-zero predicate, as it must. It is not a counterexample to the fixed
source theorem in section 3 or to the original pi-normality problem.

If a proposed seed-uniform count inequality is delta*N minus a boundary debt,
the zero-word control forces that debt to be at least delta*N on these seeds.
An estimate cannot discard this cost merely because both local histories agree.
Height-qualified state reconstruction remains available: the inherited bound
2^a3^b>2H^2 distinguishes rationals of height at most H, with polar parts retained
when necessary. Recovery of a finite state and distribution of an infinite
selected orbit are still different claims.

## 5. The precise pi-normality hole

For \(W_B(h)=B^{-1}\sum_{B\le n<2B}e(h16^n\pi/16)\), R0 asks

\[
\exists\eta>0,B_0\quad\forall B\ge B_0:
\Re W_B(1)\le1-\eta.
\]

Full base-16 normality requires W_B(h)->0 for every fixed nonzero integer h.
The five-channel construction, local compatibility, source norm and shadow
results do not establish either quantifier.

The weakest selected-source edge this dossier actually closes is section 3's
infinite real-phase separation. The missing upgrade is a **uniform positive
lower shell density** (or equivalent signed estimate), with authenticated zero
ancestry and complete rational winding retained. Requiring all conditional
local classes to escape is a stronger sufficient hypothesis, not a proved fact
or a demonstrably easier theorem.

The existing carry implementation supplies a specific rational target. Let
L_n=lcm(1,3,...,8n-1), b_n=L_n/L_(n-1), R_n=L_n r(n), and

\[
A_0=0,\quad A_n=[16b_n A_{n-1}+R_n]_{4L_n}.
\]

Then floor(U_n) mod4 is floor(A_n/L_n). A uniform positive lower bound on
the fraction of A_n in [L_n,3L_n) on every late shell is a sufficient stronger
route to R0, inherited from Main XXVI. This is a target, not an estimate.

### Prospective probe contract

Before another source-count experiment, fix a candidate source/height-sensitive
inequality, its constants, and the declared state variables. It must:

1. follow actual zero-seeded chronological source transitions;
2. survive the constructed mixed-place shadow test by correctly exposing a
   seed-height or exact-boundary discriminator;
3. keep the real carry or phase unweighted when conditioning on local labels;
4. pay approximation, latency and changing-resolution errors;
5. make a prediction on an untouched source interval beyond the already used
   index 131072.

A finite failure refutes the proposed finite bound. A finite pass does not
establish its all-late-shell extension. No new statistical prediction was fitted
or tested on such a holdout in this dossier. The source energy intervals through
512 are explicitly replays/calibrations of the instrument.

**Novelty tax.** The five-channel clock and mixed shadow extension are proved
local constructions. The selected-phase separation is a direct extension of an
inherited gap lemma. The terminal carry gate is an inherited sufficient reduction;
reexpressing it through the new observer alone would not advance its truth state.
