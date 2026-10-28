# Two-bit source partitions: weighted obstruction and exact memory law

Audited commit: `91d908b775241df6a7f91e9de843c88e6774e0c9`. Read the complete dossier, handoff, script and tests from their git blobs. Read-only sibling; this proof extension is additive on the independent child branch. The finite coding claims check out. The new branch itself correctly leaves real cancellation OPEN.

## 1. Full and partial codes are different partitions

The full valid code `(A(x) mod q,sheet,pole,lift)` is a bijection from `x mod q` to exactly q valid states. Invalid syntactic combinations of the two bits are not extra states. Consequently its unweighted q-normalized collision energy and complete-period-Haar energy are exactly the ordinary time-residue energy E_q, for every N. Its empirical conditional energy agrees with E_q on complete periods and is asymptotically equivalent when q=o(N); it need not equal E_q on an incomplete period.

For the partial valid code `(A(x) mod q,sheet,pole)`, dropping lift creates genuine fibers. Put `b=89/240 modq`, `u=x-b`, `q=p^L`, and write `u^2=v`. For nonzero v of valuation 2s<L, each of the two canonical branches is

`x=b+p^s(±r+j p^(L−2s)) modq`, `0≤j<p^s`.

Thus each branch has p^s states. The critical fiber v=0 has one conventional sheet and `p^floor(L/2)` states.

The pole bit does not split any such branch: changing j changes x by a multiple of `p^(L−s)`, hence preserves x modulo p. The critical fiber also has constant x modulo p. Therefore `(A,sheet,pole)` and `(A,sheet)` induce exactly the same partition, although pole remains a valid source-authenticated check.

The canonical root is the Hensel lift of the unique root in `{1,…,(p−1)/2}` modulo p. Reversing this convention merely swaps the names of the two noncritical sheets at a fixed target; it does not change the partition. The critical sheet convention supplies one class, not two. No additional pole multiplicity should be counted.

One minor distinction matters across primes: the critical pole bit is not always zero. Direct evaluation gives `D(89/240)=−11²·29·31/6480000`, so it is one precisely at p=11,29,31 among primes p≥7. This changes no class counts. It is zero at 7 and 241.

The partial code need not have a well-defined autonomous successor after lift is forgotten. For example at p=7,L=2, x=6 and x=13 share the critical partial label, but their successors 7 and 14 have different numerator targets. The full code's exact successor conjugacy is unaffected, and the partition-energy theorem never assumes a quotient successor.

## 2. Exact partial-label counts

For each s with 2s<L there are `(p−1)p^(L−2s−1)/2` numerator targets, each with two partial classes of size p^s. Add one critical class of size `p^floor(L/2)`. Therefore

`k'_L=1+(p−1) sum_(s=0)^floor((L−1)/2) p^(L−2s−1)`

and

`k'_L/p^L → p/(p+1)`.

Equivalently, `k'_L=2k_L−1`, where k_L counts undecorated A-values. The exact ordered collision count is

`sum_classes m² = ceil(L/2)(p−1)p^(L−1)+p^(2floor(L/2))`.

Each noncritical valuation layer contributes `(p−1)p^(L−1)` independently of s. These formulas include L=1, when the partial code is already injective.

At p=7 the first five `(q,k',ordered pairs)` values are `(7,7,7)`, `(49,43,91)`, `(343,301,637)`, `(2401,2101,6517)`, `(16807,14707,45619)`.

## 3. General deterministic-partition theorem

The proper-Haar obstruction does not require that the partition arise from a quadratic polynomial. Let q_j=q(2^j)→∞ with q_j=o(2^j). At each j let a deterministic partition of the q_j time residues have k_j nonempty classes and suppose `k_j/q_j→κ>0`. Its conditional-average matrix P_j has blocks `J_m/m`, hence

`P_j²=P_j=P_j*`, `||P_j||_2=||P_j||_∞=1`, `P_j1=1`, `tr P_j=k_j`.

There is a single base-16 normal α with μ(α)≤4 such that, for every fixed nonzero h, the partition's Haar energy and empirical conditional energy have lower limit at least κ/4 along N_j=2^j. The same α can handle any fixed finite collection of such deterministic partitions, by taking the intersection of their good-word events. Existing truncated-K_S events for the stronger original unweighted A-energy can be retained in that intersection.

Proof details establishing that the extension is legitimate:

* For the uniform q-digit periodic word, its radix phases have covariance `(1−ε)I+εJ`, ε=16^(−q). Thus `R=q^(−1)w*Pw` has expectation `(1−ε)k/q+ε≥k/q`.
* Changing one digit changes the sum of phase-coordinate distances by at most `2π|h|`. Since P has maximum absolute row sum one, R changes by at most `4π|h|/q`; Efron–Stein gives `Var R≤8π²h²/q`.
* With `H=floor(q^(1/8))`, `δ=q^(−1/8)`, simultaneous concentration over `1≤h≤H` fails with probability `O(q^(−3/8))`. The old-prefix correlation against Pw has second moment at most `2Pstage²/q+εPstage²`; its simultaneous failure probability is at most `2q^(−5/8)+q^(3/8)16^(−q)`.
* These probabilities, the unchanged cyclic-frequency failure probability, and any fixed finite collection of such events still total o(1). Marker conditioning costs only a factor sixteen. The stage marker, q=o(N), and cyclic-frequency constraints therefore retain the same E7 proofs of all-prefix normality and μ(α)≤4.
* For ψ=Pw and N=2Pstage, the exact old/new phase error and the incomplete final period give `Re sum_(n≤N)z_n conjugate(ψ_n)≥Pstage R−δPstage−2q−4π|h|/15`.
* Weighted Cauchy–Schwarz over partition classes has second factor `sum_class m|ψ_class|²=||Pw||²=qR`. Hence

  `H_partition ≥ [R/2−δ/2−2q/N−4π|h|/(15N)]_+²/R`.

  Since R≥k/q−δ→κ from below, monotonicity in R gives the κ/4 lower limit.
* Every class count satisfies `m(N/q−1)≤c≤m(N/q+1)`. Therefore `H/(1+q/N)≤Qemp≤H/(1−q/N)` for N>q, proving the same lower limit for empirical energy.

No independence of the radix phase coordinates, nested partitions, or branch-compatible dynamics is used. The required determinism means the partition is fixed before selecting the auxiliary word. A partition chosen from those random phases would require a separate argument.

## 4. Consequences for the fresh code

For the partial sheet/pole code, κ=p/(p+1). Consequently the same construction gives

`liminf H_partial ≥ p/[4(p+1)]`, `liminf Qemp_partial ≥ p/[4(p+1)]`.

At p=7 the constant is **7/32**. Since the unweighted partial energy is at least its Haar energy, it too has a positive obstruction; no partial-energy lower constant 1/4 is claimed here.

For the full code κ=1 and H_full=E_q exactly, giving the familiar 1/4 lower bound. The original undecorated A partition has κ=p/[2(p+1)], hence constant p/[8(p+1)]. All three statements can hold for the same normal α with μ(α)≤4 by the finite intersection just described, while retaining the original C_A≥1/4 construction through its K_S event. This requires choosing α with the augmented conditions from the start; it is not a claim about every previously selected α.

Summable original BBP tails transfer H and Qemp with O_h(1/N) error, so these obstructions survive the identical four-pole forcing at the explicit changed selector `(α−π)/16`. They remain strictness results for prescribed growing energies, not a refutation of a sufficient bound at the authentic zero selector.

## 5. Exact validation and provenance

The unchanged sibling source probe and all **10 unchanged focused tests** passed in an isolated scratch namespace. This is not a native full-suite or CI claim about that sibling. An independent enumeration checked full-code bijectivity, exact partial fiber sizes, pole redundancy, label counts and ordered-pair counts for 14 cases totaling **81,254 residue states**: p=7 through L=5; p=11 through L=3; p=29,31 through L=2; p=241 through L=2. The extra 29/31 cases test critical pole contact directly.

Probe: `pi_two_bit_partition_audit.py`.

The reproduction script extracts the unmodified pinned git blobs into the explicitly supplied isolated output directory. Git blob IDs and SHA-256 values are recorded in `pi_two_bit_partition_receipt.json`; focused test output is preserved alongside it.

Machine receipt: `pi_two_bit_partition_receipt.json`.

Audited source-script SHA-256: `c487c393b06d9bf7bdb95cb62f4d9902ffed7956eca83da8f110ef110affef8e`.

Audited test-file SHA-256: `821a20a31de90c9136163abfb53820cb86483f36087f818710ca6155aafbe8c9`.

## 6. Autonomous quotients and the exact order-two output law

Let q=p^L with p≥7, and let B be any deterministic label on Z/q such that A is determined by B. If there is a deterministic successor F satisfying `B(x+1)=F(B(x))` for every x, then B is injective.

Proof: `B(x)=B(y)` implies both `A(x)=A(y)` and `A(x+1)=A(y+1)`. But

`[A(x+1)−A(y+1)]−[A(x)−A(y)]=240(x−y)`.

Since 240 is a unit modulo q, x=y. Thus no noninjective refinement of A can be an autonomous deterministic quotient of the time successor.

For the probabilistic statement, choose X uniformly in Z/q and define the stationary process `B_n=B(X+n)` for integer n. Two consecutive outputs determine the current residue x because

`A(x)−A(x−1)=240x−209`,

so `x=(A(x)−A(x−1)+209)/240 modq`. Therefore the next output is a deterministic function of `(B_(n−1),B_n)`, and the output process satisfies the order-two Markov property.

If a current label has m>1 residue states, all m occur with positive equal conditional probability. Their next A-values are pairwise distinct: for x≠y in this fiber,

`A(x+1)−A(y+1)=240(x−y)≠0 modq`.

Hence their next B-labels are also distinct. Given B_n alone the next-output law has m equally likely outcomes; given the realized pair `(B_(n−1),B_n)` it is a point mass. These conditional laws disagree on events of positive probability, so the stationary process is not first-order Markov. The distinction concerns first-order *stochastic* Markov behavior as well as deterministic autonomy.

Applied to the partial `(A,sheet,pole)` code: L=1 is injective and has a deterministic first-order successor. For every L≥2 its critical class has `p^floor(L/2)>1` states, so the stationary output process has exact Markov order two. All realized single-label and pair-label events used in this argument have positive Haar-time probability. This finite clock statement makes no real-phase independence or continuum minimal-memory claim.

The finite entropy calculation sharpens this distinction. Use natural logarithms, and set `a=floor(L/2)`. Since each current class of size m has m distinct equiprobable next outputs,

`H(B_(n+1)|B_n)=(1/q) sum_classes m log m`.

For the partial code, its class size at x is exactly `p^min(v_p(x−b),a)`, with v_p(0)=∞. Uniform x gives

`E min(v_p(x−b),a)=sum_(j=1)^a P(p^j|(x−b))=sum_(j=1)^a p^(−j)`.

Consequently

`H(B_(n+1)|B_n)=log(p)·(1−p^(−floor(L/2)))/(p−1)`.

For the original undecorated A-label, each noncritical class has twice the partial class size, while the critical class is unchanged. Its noncritical mass is `1−p^(−ceil(L/2))`, so

`H(A_(n+1)|A_n)=log(p)·(1−p^(−floor(L/2)))/(p−1)+log(2)·(1−p^(−ceil(L/2)))`.

For either label, the conditional entropy given two consecutive outputs is zero. Every output block of length at least two determines the original uniform residue, so its joint entropy is exactly log q; in particular the entropy rate is zero. Positive one-step conditional entropy here records information omitted by the current label, not independent innovations. These are exact finite Haar-time laws, not probability laws asserted for the selected real pi phase.
