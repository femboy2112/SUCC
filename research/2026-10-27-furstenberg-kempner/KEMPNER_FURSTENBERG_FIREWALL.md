# Furstenberg ×2×3 reality check: a decisive Kempner firewall

**2026-10-27. Corrective draft child of PR #334.** This is additive research. Do not alter main, the original four signed BBP poles, zero initial condition, or historical contracts. π normality and the Furstenberg measure conjecture remain OPEN.

## FK-1. The free-entropy lemma R4 in PR #334 is false

The parent document PRIME_LADDER_REDUCTION_THEOREM.md asserts that π's transcendence implies positive topological entropy of its base-16 orbit closure. Non-eventual-periodicity does **not** imply positive topological entropy. And even positive topological entropy of an orbit closure does not imply positive **measure-theoretic** entropy for every weak-* limit of one orbit. Its resulting R5 equivalence between vanishing ×3 defects and π normality remains unjustified.

**A very strong exact countermodel:** the Kempner number

$$
\kappa=\sum_{j=0}^{\infty}2^{-2^j}
=0.1101000100000001\ldots{}_2
$$

is transcendental and has irrationality exponent **2** (minimum possible for an irrational). Primary peer-reviewed reference: A. N. W. Hone and J. L. Varona, *Continued fractions and irrationality exponents for modified Engel and Pierce series*, Monatshefte für Mathematik 190 (2019), Section 4, https://doi.org/10.1007/s00605-018-1244-1 , citing Bugeaud–Han–Wen–Yao (2016).

Its binary digit is 1 exactly at positions 2^j, otherwise 0. Put ν_N=N^(-1)Σ_{n<N}δ_{{2^nκ}}. For fixed L, at most L(1+floor(log₂(N+L))) of the first N shifts have a 1 among the first L digits. All other shifts lie in [0,2^(-L)]. Let N→∞ then L→∞ to prove

$$
\boxed{\nu_N\Longrightarrow\delta_0.}
$$

Yet δ₀ is invariant under both ×2 and ×3, so for every integer h,

$$
\frac1N\sum_{n<N}\left[e(3h2^n\kappa)-e(h2^n\kappa)\right]\longrightarrow0,
$$

while κ is **not** base-2 or base-16 normal. The binary orbit closure also has zero topological entropy: any length-L factor starting beyond 2L contains at most one 1, while the first 2L starting positions account for at most 2L additional factors; therefore the word complexity is O(L), and entropy is zero.

**REFUTED in general:** transcendence + finite irrationality exponent (even 2) + ×2/×3 invariance of all rank-one weak limits implies normality. This does not refute a hypothetical theorem genuinely exploiting π's entire original zero-seeded four-pole forcing.

## FK-2. The corrected theorem

For real α let ν_N^α=N^(-1)Σ_{n<N}δ_{{2^nα}}. Assume:

(A) For all fixed integers h≠0,

$$
D_{N,h}(\alpha)=\int_{\mathbb T}[e(3hx)-e(hx)]\,d\nu_N^\alpha(x)\longrightarrow0.
$$

(B) Uniform asymptotic anti-concentration:

$$
\lim_{\epsilon\downarrow0}\limsup_{N\to\infty}
\sup_{x\in\mathbb T}\nu_N^\alpha(B_\epsilon(x))=0.
$$

**PROVED conditional theorem:** If Furstenberg's ×2×3 measure-rigidity conjecture is true, then (A)+(B) imply α is base-2 and base-16 normal.

**Proof.** Let μ be any weak-* limit of the ν_N^α. The exact telescoping of the rank-one binary orbit implies T₂*μ=μ. Condition (A) plus Fourier uniqueness implies T₃*μ=μ. If μ has an atom of mass c at x, Portmanteau on every open ball Bε(x) implies limsup_N sup_y ν_N^α(Bε(y))≥c, contradicting (B). Thus μ has no atoms. The conjectural full Furstenberg measure theorem forces μ=Haar. As every weak-* limit equals Haar, the orbit measures converge to Haar and α is base-2/16 normal. ∎

**Unconditional alternative:** prove (A) and show every joint-ergodic component of every such limit has positive measure-theoretic T₂ or T₃ entropy. Rudolph–Johnson then gives Haar. A positive entropy claim based merely on transcendence or topological orbit complexity is insufficient.

## FK-3. Actual universal Furstenberg obstruction

For any jointly invariant μ, let a_h=∫e(hx)dμ(x). Invariance forces a_h=a_{2h}=a_{3h}. This positive-definite Fourier system still allows rational atomic periodic orbits. The unresolved conjectural counterexample is a **jointly invariant, jointly ergodic, non-atomic, zero-entropy measure**. Source-specific BBP work can attack π's selected orbit, but cannot by itself solve this *universal* classification.

References: Rudolph (1990), https://doi.org/10.1017/S0143385700005629 ; Burton–Panangaden (2026), https://doi.org/10.1007/s43034-026-00512-1 . Furstenberg's topological orbit-density theorem already applies to every irrational α; density does not imply Haar genericity.

## Next verdict-changing probe

1. Independently derive selected π's **unaveraged** ×3 Fourier defects (A) from its true original four-pole U₀=0 source, rather than averaging a rank-two rectangle.
2. Prove a genuinely source-specific uniform anti-concentration bound (B), or a metric entropy property of **every** relevant invariant component. Test the Kempner and SUCC PR #320 nonnormal mutants.
3. For the universal Furstenberg conjecture, study the zero-entropy digit carry constraint on all jointly invariant measures. Do not infer joint measure independence from commutative rank-two squares.
4. Mark PR #334 R4 and its claimed R5 equivalence as **REFUTED general bridge / UNVERIFIED for π**, not PROVED.

Five focused independent Python controls were run locally: **5 PASS**, checking Kempner's exact sparse binary digits, finite word counts, next-L-digit exceptional sets and dyadic shifts. The mathematical universal assertions above rest on the paper proof and cited reference, not finite testing. No hosted CI/Lean/full-native run claimed. No main merge, release or publication authorized.


## FK-5. Additional logical defect: a trivial O(1) bound does not imply ×3 invariance

PR #334's A2/R3 discussion invokes \(|D_{N,h}^{(3)}(\alpha)|\le2\) for all α and N and then describes vanishing ×3 defects as non-discriminating or automatic. The bound **does not entail** \(D_{N,h}^{(3)}\to0\). A fixed rational example refutes any such inference:

Take α=1/5 and the hexadecimal orbit \(x_n=\{16^n/5\}=1/5\) (since 16≡1 mod5). For h=1 and **every** N,

$$
D_{N,1}^{(3)}(1/5)=e(3/5)-e(1/5)\ne0,
\qquad |D_{N,1}^{(3)}(1/5)|=2\sin(2\pi/5)>0.
$$

Thus the genuine ×3-invariance hypothesis is nontrivial; it can fail spectacularly even when ×16-invariance of the empirical measure is exact. At the same time, the Kempner example FK-1 shows that **even when ×3 invariance succeeds**, it need not imply Haar because atomic limits are permitted. These are logically separate obstructions. For a base-2 orbit replace 16 by 2; the corresponding ×2-invariant rational periodic orbit also need not be ×3-invariant.

The correct hierarchy is (i) ×2 invariance of binary orbit weak limits: automatic by telescoping; (ii) ×3 invariance: independent and UNVERIFIED for π; (iii) atomlessness or appropriate entropy in *every* component: independent and UNVERIFIED for π; (iv) full Furstenberg measure conjecture itself: OPEN.
