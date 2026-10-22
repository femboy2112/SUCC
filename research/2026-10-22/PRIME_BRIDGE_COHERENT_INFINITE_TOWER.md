# PRIME BRIDGE II — A coherent infinite arithmetic/analytic/EPR/three-ray code tower

**Date:** 2026-10-22. **Research parent:** \`research/prime-bridge-one-shot-2026-10-22@b74a202bbbb016094cf603251fbc625cdc6c3c27\`, in turn based on reviewed \`main@b116841f12b41aaf7600da39bbb40577f25b6295\`. **Branch:** \`research/prime-bridge-coherent-tower-2026-10-22\`. Non-main, no merge/release authorization. **Claim status:** explicit paper derivations plus exact finite checks, **not Lean-kernel certified**. Academic novelty **UNVERIFIED**. No Einstein–Rosen bridge, gravitational spacetime, p-adic CFT, signed completed-Weil positivity, or RH proof is claimed.

## Abstract and honest result

The earlier sparse source chart \`{1,2,4}\` has an affine-braid defect under *intermediate* projection. We repair that obstruction with complete integer prefixes \`F_k={1,...,3^k}\`. Their compressed **entire positive affine action** remains an exact representation at every stage. On each chart, encode the arithmetic basis in base three using the **standard** \`[[3,1,2]]_3\` erasure code, placing each successive three-qutrit layer at matched depths on three explicit rays of the genuine \`PGL_2(Q_2)\` Bruhat–Tits tree. The code is compatible with prefix inclusion. The inductive limit provides an isometry of the *full* source \`ell^2(N_{>=1})\` into an incomplete infinite tensor product of physical triple sites. Every bounded arithmetic observable, in particular both additive \`S\` and prime-multiplication \`V_p\`, has explicit **two-ray-local finite reconstructions converging strongly on the coded source**, and the original Hardy–Dirichlet representation and full arithmetic thermofield double are transported coherently.

This is a **synthetic, algebraic infinite-dimensional encoding**, which is precisely the scope allowed by the motivating question. It is **not an independent p-adic holographic duality**: the three rays, base-three digits, and qutrit alphabet are choices. The recovery operators are nonlocal in the unbounded-depth direction; source embeddings do not strictly intertwine finite compressed operators at their cutoff exits, and operator-norm reconstruction cannot replace strong convergence.

## 1. A complete positive-affine semigroup with exact finite SUCC coherence

Let \`A^+={(a,b): a in N_{>=1}, b in N_{>=0}}\` with multiplication

\[
(a,b)(c,d)=(ac,ad+b).
\]

On \`H=ell^2(N_{>=1})\` define the isometries

\[
U_{a,b}|n\rangle=|an+b\rangle.
\]

They form a genuine semigroup representation, since \`n -> an+b\` is injective, and \`U_{a,b}U_{c,d}=U_{ac,ad+b}\`. Ordinary additive SUCC is \`S=U_{1,1}\` and multiplication is \`V_p=U_{p,0}\`. In particular,

\[
V_pS=S^pV_p,\quad V_pV_q=V_qV_p,\quad S^rS^s=S^{r+s}.
\]

**AEPB2-01 (all-prefix representation, PROVED PAPER).** For each \`N>=1\` let \`P_N\` project onto \`span{|1>,...,|N>}\` and \`U^{(N)}_{a,b}=P_N U_{a,b} P_N\`, restricted to that range. Then

\[
\boxed{U^{(N)}_{a,b}U^{(N)}_{c,d}=U^{(N)}_{ac,ad+b}\quad\text{for ALL }a,c\ge1,b,d\ge0.}
\]

**Proof.** Every positive affine map \`f(n)=an+b\` satisfies \`f(n)>=n\`. For any basis \`|n>\` inside the prefix, if the composite endpoint \`f(g(n))<=N\`, then both intermediate address \`g(n)\` and the final address lie inside the prefix, so both projected and unprojected paths return the same basis vector. If the composite endpoint exceeds \`N\`, both products vanish: once an increasing affine path exits an initial segment, no later positive-affine transformation can reenter. Equality holds on a basis, hence as operators. This holds at **every** finite \`N\`, not merely in the limit. No primality assumption is needed for the larger affine monoid; a declared prime jet must still have an authenticated genuine prime label. QED.

This is stronger than the single braid and repairs the exact defect caused by a **non-prefix** finite chart. The code's finite stage therefore represents the full causal positive-affine SUCC monoid, not an arbitrarily fitted list of operations.

**AEPB2-02 (strict-inclusion obstruction and exact exit term, PROVED PAPER).** Put \`N_k=3^k\`, \`J_k:H_{N_k}->H_{N_{k+1}}\` the ordinary prefix inclusion, and \`Q_k=J_k^*\`. Then

\[
Q_k U^{(N_{k+1})}_{a,b}J_k=U^{(N_k)}_{a,b},
\]

but the strong embedding square is **not** generally strictly commuting:

\[
E_{k,a,b}:=U^{(N_{k+1})}_{a,b}J_k-J_k U^{(N_k)}_{a,b}
=\sum_{\substack{1\le n\le N_k\\N_k<an+b\le3N_k}}|an+b\rangle\langle n|.
\]

The nonzero columns are orthonormal, hence \`||E||=1\` when this exit set is nonempty, \`0\` otherwise. For \`S\`, the witness \`n=N_k\` gives \`||E_{k,1,1}||=1\` at **every** stage. The correct inter-stage structure is exact compression with a separately conserved **exit defect**, not fictitious strict intertwiners. Meanwhile \`P_{N_k}U_{a,b}P_{N_k}->U_{a,b}\` **strongly** on \`H\` by density plus uniform norm \`<=1\`. For \`S\` the convergence is **not** in operator norm, since on \`|N_k>\` the compressed operator gives zero while the full successor gives \`|N_k+1>\`.

## 2. Reversible Dirichlet analysis at every stage, and globally

Define \`B:H -> \\mathscr H^2\` by the coefficient-norm Hardy–Dirichlet transform

\[
\mathcal B\left(\sum_{n\ge1}a_n|n\rangle\right)(s)=\sum_{n\ge1}a_n n^{-s},\qquad
\|\mathcal Ba\|^2_{\mathscr H^2}=\sum|a_n|^2.
\]

As defined, \`B\` is unitary onto its coefficient-norm image; each point evaluation for \`Re s>1/2\` is bounded. For any fixed \`sigma>1/2\`, the Fourier/Bohr means

\[
a_n=\lim_{T\to\infty}\frac1{2T}\int_{-T}^{T}n^{\sigma+it}F(\sigma+it)\,dt
\]

recover coefficients. Proof: Cauchy–Schwarz gives \`sum |a_m|m^{-sigma}<infty\`; expand the sum, apply the Cesàro mean to \`exp(it log(n/m))\`, and justify dominated convergence.

On \`H_{N_k}\` the Dirichlet polynomial \`F_k(s)=sum_{n<=N_k}a_n n^{-s}\` is recovered **exactly** from the \`N_k\` samples \`F_k(1),...,F_k(N_k)\`. This is the rational Vandermonde matrix \`x_n^r\`, with \`x_n=1/n\`, \`r=1,...,N_k\`: its determinant is \`(prod_n x_n) prod_{i<j}(x_j-x_i)\` up to orientation, hence is nonzero. All tested inverse calculations use exact \`Fraction\` arithmetic, with a separate Gaussian-elimination oracle. Prefix zero extension preserves old samples and supplies a coherent restriction map; a finite list of samples **does not** reconstruct a general unbounded-support Dirichlet series.

Full operators transport exactly as \`B U_{a,b} B^{-1}\` and therefore preserve the semigroup relations. These operators need not be simple multipliers in \`s\`: for example \`B V_p B^{-1}\` multiplies by \`p^{-s}\`, whereas \`B S B^{-1}\` shifts the **source coefficients**, not the analytic variable itself.

## 3. The chosen, genuine 2-adic geometric addresses

Let \`L_0=Z_2^2\`. For three primitive integer normals

\[
v_0=(1,0),\quad v_1=(0,1),\quad v_2=(1,1),
\]

specify rays of lattice homothety classes, for integer \`r>=1\`, by

\[
L_{j,r}=\{(x,y)\in Z_2^2: v_j\cdot(x,y)\equiv0\pmod {2^r}\}.
\]

Each quotient \`L_0/L_{j,r}\` is cyclic of order \`2^r\`, \`L_{j,r+1}\` is an index-two sublattice of \`L_{j,r}\`, and the three initial lines \`L_{j,1}/2L_0\` are the three distinct one-dimensional subspaces of \`F_2^2\`. These are actual vertices, with successive vertices adjacent, in the usual \`PGL_2(Q_2)\` Bruhat–Tits tree. They form three pairwise disjoint rays after the root. The graph distance between sites \`(j,r)\` and \`(l,s)\` is \`|r-s|\` for \`j=l\`, or \`r+s\` for distinct initial branches.

Assign **one physical qutrit** to each \`(j,r)\`. This is a **declared embedding**, not a consequence of \`Q_2\` being a field of characteristic zero: the quantum alphabet \`F_3\`, the site-to-digit association and these three chosen rays are extra structure. It uses genuine geometry but does not derive physics from it.

**Noncanonicity counterexample.** The alternative ray \`L'_{0,r}={x+2y≡0 mod 2^r}\` agrees with \`L_{0,1}={x even}\` at \`r=1\`, but differs from \`L_{0,2}\` (e.g. \`(2,1)\` lies in \`L'_{0,2}\` and not \`L_{0,2}\`). Thus the first-shell geometry alone does not canonically select continuation rays. This kills automatic source-free geometry from the finite code.

## 4. Compatible quantum code and infinite Hilbert realization

Let the single-site **classical** three-qutrit perfect code be

\[
W|i\rangle=\frac1{\sqrt3}\sum_{j\in F_3}|j,j+i,j+2i\rangle,
\qquad i\in F_3.
\]

For \`n=1,...,N_k\`, write \`n-1=sum_{r=0}^{k-1} d_r 3^r\` (least significant digit first). Set \`W_k\` to the reordered tensor product of the individual \`W|d_r>\`; it is an isometry \`H_{N_k} -> B_{0,k}\\otimes B_{1,k}\\otimes B_{2,k}\`, with \`B_{j,k}=(C^3)^{\\otimes k}\` placed at sites \`(j,1),...,(j,k)\`. Let \`K_k\` append the **encoded logical-zero** state \`|\\varphi_0>=W|0>\` across the three new sites, *not* a product \`|000>\`.

**AEPB2-03 (strict code naturality and infinite isometry, PAPER PROVED).**

\[
\boxed{W_{k+1}J_k=K_kW_k.}
\]

Proof: appending a zero **most significant** base-three digit to \`n-1\` leaves the original integer index unchanged. The local code on the appended digit is exactly \`W|0>\`. Tensor product of isometries preserves inner products; the inter-stage square commutes on every basis vector. QED.

Let the physical Hilbert carrier be the **von Neumann incomplete infinite tensor product**

\[
\mathcal K=\bigotimes_{r=1}^\infty{}^{\varphi_0}
[(\mathbb C^3)_{0,r}\otimes(\mathbb C^3)_{1,r}\otimes(\mathbb C^3)_{2,r}],
\]

completed from finite modifications of the **entangled** three-site reference \`\\varphi_0\`. The induced code vectors

\[
W_\infty|n\rangle=
\bigotimes_{r\ge1}W|d_{r-1}(n-1)\rangle
\]

are well-defined: all high digits eventually vanish, so every code basis vector differs from the reference in only finitely many factors. They are pairwise orthonormal, and extend uniquely to an isometry \`W_inf:H->K\`.

**Important infinite-subsystem boundary:** Because the reference vector is entangled across the three rays at each level, do *not* silently identify \`K\` with the tensor product of three independent pure-reference incomplete ray Hilbert spaces. Define the separate ray/region observable **algebras via their finite-site local operators**; all infinite claims below use those algebras and the encoded subspace. The full infinite-ray partial trace need not be a normal trace-class density matrix in this representation.

## 5. Exact finite erasure decoder and two-ray arithmetic reconstruction

For any visible two-ray subset \`A={x,y}\` (chosen in increasing order) and missing ray \`z\`, use the two-qutrit **basis permutation**

\[
D_{xy}:|u,v\rangle\longmapsto|i,k\rangle,
\qquad i=(v-u)(y-x)^{-1}\pmod3,
\quad k=u+i(z-x)\pmod3.
\]

For the single-site code,

\[
(D_{xy}\otimes I_z)W|i\rangle=
|i\rangle\otimes|\Phi_3\rangle_{\mathrm{anc},z},
\quad |\Phi_3\rangle=3^{-1/2}\sum_{k=0}^2|k,k\rangle.
\]

This identity is checked by substituting \`u=j+xi,v=j+yi\`. Iterating it gives \`D_{A,k}W_k|\\psi>=|\\psi>\\otimes|\\Phi_3>^{\\otimes k}\` with the logical factors decoded into the two visible rays and the spectator maximally entangled with the erased ray.

**AEPB2-04 (full finite bounded-operator representation, PROVED PAPER).** For arbitrary \`T\\in B(H_{N_k})\`, define the actual **two-ray-supported** operator

\[
B_{A,k}(T)=D_{A,k}^\dagger(T\otimes I_{\mathrm{anc}})D_{A,k},
\]

acting on the two visible rays and as the identity on the third. Then

\[
\boxed{(B_{A,k}(T)\otimes I_{A^c})W_k=W_kT.}
\]

Moreover \`T->B_{A,k}(T)\` is a unital faithful *-representation, so **all positive-affine SUCC relations remain exactly valid as operators on either two-ray boundary region**, even outside the code subspace. Arbitrary complex superpositions are covered by linearity; this is not a purely classical label decoder.

This is the standard code-theoretic reconstruction algebra, now populated by authenticated arithmetic operators rather than manufactured geometric laws.

## 6. Strong infinite reconstruction; exact source-truncation error budget

Fix one of the three two-ray regions \`A\`. For any **bounded** source operator \`T\\in B(H)\` define the finite compression \`T_k=P_{3^k}TP_{3^k}\` on \`H_{N_k}\` and the two-ray local physical approximant \`B_{A,k}(T_k)\` (extended as identity to every site of depth \`>k\`). This map is norm bounded by \`||T||\` and, after acting on codewords, preserves the code subspace. For every fixed basis \`|n>\`, if \`3^k>=n\`, then

\[
B_{A,k}(T_k)W_\infty|n\rangle=W_\infty P_{3^k}T|n\rangle.
\]

Since \`P_{3^k}->I\` strongly and \`||B_{A,k}(T_k)||<=||T||\`, density of finite-support source vectors gives

**AEPB2-05 (all bounded operators reconstructible on each pair, PROVED PAPER):**

\[
\boxed{\operatorname*{s-lim}_{k\to\infty}
 B_{A,k}(T_k)W_\infty=W_\infty T}\quad
\text{in }B(H,\mathcal K)\text{ strong topology}.
\]

The three choices of \`A\` give the same limiting action on \`W_inf H\`, although the physical boundary representatives on the full \`K\` differ. This is true for **both** \`S\` and each \`V_p\`. For any source vector \`\\psi\`, the result is a genuine **norm** limit of the resulting vectors; the family of physical operators is not asserted to converge in operator norm on \`K\`.

For a positive-affine operator \`U_{a,b}\`, a stronger explicit finite-support bound holds. Let \`M>=1\` and \`3^k>=aM+b\`. All basis vectors \`|n>\` with \`1<=n<=M\` then pass through the finite code **exactly**. Using both maps' operator norms \`<=1\`,

\[
\|B_{A,k}(U^{(3^k)}_{a,b})W_\infty\psi
 -W_\infty U_{a,b}\psi\|
\le2\|(I-P_M)\psi\|.
\]

Thus the **source tail** rather than a guessed geometry parameter gives an explicit reconstruction-error budget. In particular, compactly supported source vectors stabilize exactly after finite depth. For the analytic representation \`\\mathcal B\`, the same limit transports through the reversible Dirichlet map:

\[
\operatorname*{s-lim}_k B_{A,k}(U^{(3^k)}_{a,b})
 W_\infty\mathcal B^{-1}F
 =W_\infty\mathcal B^{-1}
 (\mathcal B U_{a,b}\mathcal B^{-1})F,
\quad F\in\mathscr H^2.
\]

This is a **lawful infinite arithmetic ⇄ analytic ⇄ boundary-observable coherence diagram**, not merely coincident numerical spectra.

### AEPB2-08: no bounded-depth exact successor operator; no operator-norm convergence

Consider a local physical operator \`O\` acting on **any fixed finite collection of depth levels** (even granting access to all three rays at those levels). Choose \`r\` deeper than its entire support and input \`n=3^r\`. The encoded source \`W_inf|n>\` has logical digit zero at level \`r+1\`, whereas \`W_inf S|n>=W_inf|3^r+1>\` has digit one at that level. These two local code-state factors are orthogonal; \`O\` cannot change the untouched deep factor. Hence

\[
\boxed{\|OW_\infty|3^r\rangle-W_\infty S|3^r\rangle\|\ge1.}
\]

So **no uniformly finite-depth/quasi-local norm-approximable physical operator** can implement full \`S\` on this code, although increasing-depth finite operators implement it **strongly** on the code. The same kind of deep-digit argument applies to every nontrivial prime multiplier. This is a locality obstruction of this particular encoding, **not** a physical no-go theorem for spacetime holography.

## 7. Exact finite and full infinite EPR transport

For any \`beta>1\`, let \`Z_k(beta)=sum_{n<=3^k}n^{-beta}\` and

\[
\Omega_{\beta,k}=Z_k(\beta)^{-1/2}\sum_{n=1}^{3^k}
 n^{-\beta/2}|n,n\rangle,
\qquad
\Omega_\beta=\zeta(\beta)^{-1/2}\sum_{n\ge1}n^{-\beta/2}|n,n\rangle.
\]

**AEPB2-06 (finite EPR mirror on all nine two-ray region pairs, PROVED PAPER).** At every \`k\` and every rational prime \`p\`, the *compressed* operators obey the **exact**, not approximate, finite mirror relation

\[
(U^{(N_k)}_{p,0}\otimes I)\Omega_{\beta,k}
=p^{\beta/2}(I\otimes U^{(N_k)\dagger}_{p,0})\Omega_{\beta,k}.
\]

The left sum retains terms \`n<=N_k/p\`; the right sum retains precisely \`m=pn<=N_k\` with coefficient \`p^{beta/2}(pn)^{-beta/2}=n^{-beta/2}\`. Applying \`W_k\` to both factors, then using the operator-reconstruction identity for **any** two-ray subset on each side, preserves this equality for all nine left/right choices. The executable exact oracle independently checks every choice at \`k=1,2\`, primes \`2,3,5\`, and even \`beta=2,4\` with rational numerator amplitudes.

The encoded finite states converge in Hilbert-space norm to \`(W_inf⊗W_inf)Omega_beta\`, because

\[
\|\Omega_{\beta,k}-\Omega_\beta\|^2
=2\big(1-\sqrt{Z_k(\beta)/\zeta(\beta)}\big)
\le\frac{2(3^k)^{1-\beta}}{(\beta-1)\zeta(\beta)}.
\]

This is a true source-derived finite error budget. **Do not conflate** the exact finite *compressed* mirror with the **nonzero ambient** truncation residual when \`V_p\` is left uncompressed:

\[
\varepsilon_{N,p}^2=
\frac{\sum_{\lfloor N/p\rfloor<n\le N}n^{-\beta}}
{\sum_{n\le N}n^{-\beta}}.
\]

By strong convergence of two-ray code operators on the encoded state, the global arithmetic mirror identity passes to the encoded limit in norm **on this particular state**. Neither the finite nor infinite mirror enables signaling.

### AEPB2-07: exact renormalized two-ray entropy

For any **finite** logical density operator \`rho_k\` on \`H_{N_k}\`, the two-ray reduced state, after local decoder, equals \`rho_k⊗I_{3^k}/3^k\`. Therefore

\[
S(AB)_{W_k\rho_k W_k^\dagger}=k\log3+S(\rho_k).
\]

For the finite thermal \`rho_{beta,k}\`, this gives the **finite** identity and the well-defined subtracted limit

\[
\lim_{k\to\infty}(S(AB)_{k}-k\log3)
=\log\zeta(\beta)-\beta\frac{\zeta'(\beta)}{\zeta(\beta)},
\quad\beta>1.
\]

Proof: \`sum_{n>=1}n^{-beta}log n<infty\` in this domain, and \`Z_k->zeta\`. This is a **code-theoretic entropy subtraction**. The unrenormalized area term grows linearly with depth, and there is no claim of a normal global infinite-ray entropy or of a gravitational Ryu–Takayanagi/QES law.

## 8. Hostile controls, provenance, and academic boundary

### Countercontrols with exact receipts

- Non-prefix chart \`{1,2,4}\` breaks affine braid through intermediate projection; the complete-prefix theorem repairs it.
- Full finite positive-affine monoid checked independently on \`3,9,27,81\` dimensional charts, including compositions that end beyond the cutoff.
- Finite embeddings do **not** intertwine all operators: the explicit exit projector has unit norm for \`S\` at every cutoff.
- The \`3\` selected lattice rays are exact \`2\`-adic congruence-lattice classes, not arbitrary drawing coordinates; their infinite continuation is **noncanonical**.
- The wrong qutrit encoding \`|j,j+i,j+i>\` fails to protect the logical state against erasure of the first leg.
- Quantum entanglement transport persists under legitimate two-ray reconstruction, not under mutation of source Schmidt coefficients; inherited finite tests retain counterfeit controls.
- No uniform finite-depth implementation of \`S\`; exactly identified strong versus operator-norm convergence obstruction.
- Finite depth has **three** logical digits per local source qutrit, and \`N_k=3^k\` source dimensions: **do not identify** the arithmetic base 3 with the local tree prime \`p=2\`.
- The dedicated finite code does **not** generate p-adic CFT correlators, an Einstein equation, or a backreacting horizon; geometric dependence is by chosen site placement.
- Thermal exact code-level mirror and uncompressed-ambient mirror residual are different typed statements.

### Reproduction

From repository root:

    python -Werror -m unittest discover -s tests -p 'test_arithmetic_epr_star.py' -v
    python -Werror -m unittest discover -s tests -p 'test_coherent_prime_tower.py' -v
    PYTHONPATH=. python scripts/coherent_prime_tower_probe.py

Run inherited repository checks before claiming repository-wide green. Dedicated CI on Python 3.10 and 3.13 should enforce the exact receipt; no Lean kernel proof is claimed without an actual pinned build. The probe hashes the tested module and tests. Preserve \`AGENTS.md\` and historical import archives untouched.

**Status ledger:** AEPB2-01/02/03/04/05/06/07 are **PAPER-PROVED with exact finite controls** (classical tools; synthesis new to SUCC; independent academic priority not established). AEPB2-08 and noncanonicity are **PROVED obstruction/counterexample**. Any claim of Einstein/ER geometry, genuine p-adic conformal-field-theory equivalence, full adelic source gluing or signed Weil positivity remains **UNVERIFIED**.

### Next theorem that would truly change the verdict

Find an **intrinsic** bulk dynamical/metric construction—preferably via authentic Bruhat–Tits network transfer rules or p-adic correlation functions—such that the arithmetic source operator algebra is intertwined by a source-derived map, compatible with nontrivial local geometry, with quantified continuum error and holographic entropy/recovery laws. A theorem forcing or obstructing locality under prime arithmetic would be especially decisive. The present strong-limit secret-sharing representation establishes the **synthetic coherence bridge** but precisely exposes the missing **geometric naturality and locality**.

## References (classical imported inputs)

1. Hedenmalm, Lindqvist, Seip (1997), *A Hilbert space of Dirichlet series and systems of dilated functions*, Duke Mathematical Journal; https://arxiv.org/abs/math/9512211.
2. Pastawski, Yoshida, Harlow, Preskill (2015), *Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence*, https://arxiv.org/abs/1503.06237 (the classical three-qutrit code).
3. Bhattacharyya, Hung, Lei, Li (2018), *Tensor network and (p-adic) AdS/CFT*, https://arxiv.org/abs/1703.05445.
4. Hung, Li, Melby-Thompson (2019), *p-adic CFT is a holographic tensor network*, https://arxiv.org/abs/1902.01411 (genuine holographic target, not a conclusion here).
5. Maldacena, Susskind (2013), *Cool horizons for entangled black holes*, https://arxiv.org/abs/1306.0533 (ER=EPR motivation, not an asserted mathematical equivalence to this code).
