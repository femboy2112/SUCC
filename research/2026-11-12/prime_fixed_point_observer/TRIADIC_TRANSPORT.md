# Three relations, shared frames, and arithmetic transport

**Date:** 2026-11-12. **Companion:** [Borwein ratchet](BORWEIN_RATCHET.md). **Verdict:** three has a precise role as the minimum length of a simple graph cycle and as a comparison between direct and composed transport. It is not a universal origin of linear algebra or dynamics. The constructions below are classical specializations or explicitly derived local identities; academic novelty is not claimed.

## 1. The useful content of the proposed hierarchy

The sequence “source, consistency, duality, motion” can organize a design:

| Role | Operational interpretation | Necessary qualification |
| --- | --- | --- |
| 0: source | Declare the carrier, inputs, and types | A source is not mathematically identical to the numeral zero. |
| 1: consistency | Choose an identity, reference, or unit | A reference alone does not determine every relation. |
| 2: duality | Compare two states or specify forward/reverse transport | Two-state systems already support motion and period-two dynamics. |
| 3: composition check | Compare a direct relation with a two-step route | A triangle is minimal only under the graph assumptions below. |

This is an interpretation, not a theorem about the integers 0–3. Linear algebra exists in dimensions zero, one, two, and higher. Its defining ingredients are vector addition and a compatible scalar action over a field. A triangle can expose a linear dependence; it does not create linearity.

The shared-framework intuition is productive when made explicit. Values must use declared units or coordinates, and transformations must have compatible domains before composition is meaningful. A scalar field supplies common algebraic operations; a physical scale convention is additional. An order, measure, or inner product is also additional structure, not a requirement of every category or vector space. In particular, the complex field used below is not an ordered field. Analogies to governance or theology can concern a shared criterion of consistency; these equations establish no corresponding institutional or theological necessity.

## 2. A triangle is the first simple loop

**TRI-01 — PROVED LOCAL within a simple undirected loop-free graph.** A closed walk of length one would require a loop. A closed walk of length two must traverse its sole edge and immediately reverse it. Thus the smallest nonbacktracking cycle has length three, attained by a triangle. The qualification matters: directed graphs, parallel labelled arrows, and self-loops permit other minimal cycles.

Give every oriented edge \(i\to j\) a transport \(u_{ij}\in U(1)\), with \(u_{ji}=u_{ij}^{-1}\). An immediate backtrack has transport one. For the oriented triangle \(0\to1\to2\to0\), its holonomy is

\[
H=u_{20}u_{12}u_{01}.
\]

This is an operational phase: multiply the three declared complex transports in their common one-dimensional fiber. It may differ from one. A triangle does not force that difference, and assigning transports from vertex potentials makes every loop trivial.

These are standard connection notions. Kenyon, *Spanning forests and the vector bundle Laplacian*, §3.1, defines inverse-edge transport, gauge equivalence, and loop monodromy; §3.2 explicitly uses \(K_3\) as an example ([primary paper](https://arxiv.org/pdf/1001.4028)). The construction here specializes that framework rather than claiming a new triangle mechanism.

## 3. Linearizing the consistency question

**TRI-02 — CLASSICAL specialization with explicit derivation.** Use vertex coordinates \((0,1,2)\) and edge coordinates \((01,12,20)\). The transported boundary matrix is

\[
B=\begin{pmatrix}
-1&0&u_{20}\\
u_{01}&-1&0\\
0&u_{12}&-1
\end{pmatrix},\qquad
\boxed{\det B=H-1.}
\]

The determinant follows by expansion in the first row. A fixed two-by-two minor equals one, so \(\operatorname{rank}B=2\) when \(H=1\), and it is three otherwise. When \(H=1\),

\[
\ker B=\operatorname{span}\{(1,u_{01},u_{12}u_{01})\}.
\]

For the ordinary incidence matrix, all transports equal one and this becomes \(\operatorname{span}\{(1,1,1)\}\): the three oriented boundary columns sum to zero. Strang's *ZoomNotes for Linear Algebra*, §3.6, treats incidence matrices, dependent cycles, and loop currents ([official MIT source](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/4d876a9159e32543eb0d73b4d4382f4c_MIT18_06S10ZoomNotes.pdf)). His ordinary incidence convention is edge-by-vertex; our ordinary \(B\) is its transpose.

Choose the standard Hermitian inner products and set \(L=B^*B\). Then

\[
z^*Lz=\|Bz\|^2\ge0,\qquad
\boxed{\det L=|H-1|^2.}
\]

Here \(L\) acts on edge coefficients. The vertex connection Laplacian is \(BB^*\); in this square example they have the same eigenvalues. The smallest eigenvalue tends to zero as \(H\to1\). This should not be confused with the first *nonzero* eigenvalue at \(H=1\), which equals three.

The finite probe also uses the vertex-value convention

\[
A_{\mathrm{inc}}=\begin{pmatrix}
u_{01}&-1&0\\0&u_{12}&-1\\-1&0&u_{20}
\end{pmatrix}
=-\operatorname{diag}(u_{01},u_{12},u_{20})B^*.
\]

For unitary phases this has the same singular values and determinant \(H-1\); its vertex Laplacian is \(A_{\mathrm{inc}}^*A_{\mathrm{inc}}=BB^*\). The convention change is explicit: edge currents and vertex values remain different typed objects even when their coordinate dimensions coincide.

For an explicit gauge convention, let coordinates change by \(z_i'=g_i z_i\), with \(|g_i|=1\). Then

\[
u_{ij}'=g_j u_{ij}g_i^{-1},\qquad H'=H.
\]

Writing \(G=\operatorname{diag}(g_0,g_1,g_2)\) on vertices and \(D=\operatorname{diag}(g_0,g_1,g_2)\) on edges, indexed by their tails, gives \(B'=GBD^{-1}\) and \(L'=DLD^{-1}\). Thus the nullity and spectrum do not depend on those coordinate choices. No curvature or empirical phase has been inferred without specified transports.

## 4. The prime-edge carrier has squares before triangles

**TRI-03 — PROVED LOCAL.** On positive integers, join \(n\) to \(pn\) for every genuine prime \(p\). Each edge changes \(\Omega(n)\), the number of prime factors counted with multiplicity, by one. Its parity is therefore a bipartition, ruling out every odd cycle. Distinct primes \(p,q\) give the first possible simple cycle:

\[
n\to pn\to pqn\to qn\to n.
\]

With only one prime generator there are no such squares. Adding a composite chord \(n\to pqn\) permits a triangle, but it also introduces a composition relation. On \(\ell^2(\mathbb N_{>0})\), let \(V_d e_n=e_{dn}\). Then

\[
V_qV_p=V_{pq},\qquad (V_{pq})^*V_qV_p=I.
\]

The triangle is flat for these authentic operators because the two routes agree. Assigning the chord a different independent phase changes the connection; it is not newly discovered arithmetic curvature. Also, \(V_d^*\) is a partial inverse: \(V_d^*V_d=I\), whereas \(V_dV_d^*\) projects onto multiples of \(d\).

## 5. Mixed additive/multiplicative loops anchor the unit

**TRI-04 — PROVED LOCAL on the full positive-integer Hilbert carrier.** Let \(Se_n=e_{n+1}\), and for every integer \(d\ge2\) define

\[
A_d=V_d^*S^{d-1},\qquad
A_de_n=\begin{cases}
e_{1+(n-1)/d},&n\equiv1\pmod d,\\
0,&\text{otherwise}.
\end{cases}
\]

For \(d=3\), this is the triangle \(1\xrightarrow S2\xrightarrow S3\xrightarrow{V_3^*}1\). Its basis path closes only at source one: solving \(1+(n-1)/d=n\) gives \(n=1\). The same anchor exists for every \(d\ge2\), including composite \(d\).

Moreover,

\[
\boxed{A_dA_e=A_{de}=A_eA_d,\quad\text{hence }A_2A_3=A_6.}
\]

Both sides keep exactly those indices \(n\equiv1\pmod{de}\) and send them to \(1+(n-1)/(de)\). The operators compare real source arithmetic, not just a three-vertex picture.

Writing \(E_{11}\) for projection onto the unit, iteration gives

\[
\|(A_d^r-E_{11})x\|^2
=\sum_{k\ge1}|x_{1+d^rk}|^2\longrightarrow0.
\]

Thus \(A_d^r\to E_{11}\) strongly and \(\operatorname{Fix}(A_d)=\mathbb Ce_1\). The convergence is not in operator norm: \(x=e_{1+d^r}\) gives \(\|(A_d^r-E_{11})x\|=1\) for every \(r\). A finite prefix cannot substitute for this tail argument.

Already \(A_2=V_2^*S\) compares two differently labelled arrows from one to two. In the underlying simple graph that looks like backtracking, but \(V_2\) and \(S\) are distinct operators. Consequently three is not even the minimum comparison length in the full labelled arithmetic action. Nor does the unit anchor constitute a prime detector or supply the directional clock established in the [Borwein construction](BORWEIN_RATCHET.md).

## 6. The strongest probe checks shared source composition

**TRI-05 — PROVED LOCAL countermodel.** Local anchors and even their strong limits do not authenticate the arithmetic source. Let \(f\) swap 5 and 7 and fix every other positive integer, let \(F e_n=e_{f(n)}\), and replace dilation by

\[
\widetilde V_d=FV_dF^{-1},\qquad
C_d=\widetilde V_d^*S^{d-1}.
\]

Keep the authentic successor \(S\). For \(d=2,3\),

\[
C_d^*e_m=e_{df(m)-d+1}.
\]

Indeed, \(df(m)\) cannot equal 5 or 7, so the outer permutation does nothing. This index map is injective, fixes one, and strictly increases every \(m\ge2\), including \(m=7\), whose smallest image is nine. Iteration therefore gives \(C_d^r\to E_{11}\) strongly, by the same square-summable-tail argument. Its fixed space is also exactly \(\mathbb Ce_1\). The counterfeit passes both these substantial anchor tests.

It fails the source braid at the concrete source label four:

\[
\boxed{\widetilde V_2Se_4=e_{14},\qquad
S^2\widetilde V_2e_4=e_{10}.}
\]

A genuine three-relation comparison also separates it:

\[
C_3^*C_2^*e_3=e_{19},\qquad C_6^*e_3=e_{13},
\]

so \(C_2C_3\ne C_6\). These are algebraic receipts, not a conjectured numerical effect. The swap even preserves \(\Omega\), since both swapped labels are prime. Degree information alone therefore misses this source-coupling defect.

The useful “third” is the additional comparison constraint: the direct route must agree with the composed route under a declared source frame. A geometric triangle alone is insufficient. This supplies a discriminating probe for the existing [prime-wave carrier](PRIME_WAVES.md), while leaving its source-specific prime-pair estimates open.

## 7. Claim ledger and executable boundary

**TRI-06 — research interpretation and validation boundary.** The shared-framework account organizes a testable model; its extension to other domains remains an analogy unless separately formalized.

| Claim | Scope and status | Failure control |
| --- | --- | --- |
| TRI-01 | Minimum nonbacktracking cycle is a triangle in a simple loop-free undirected graph: PROVED LOCAL | Parallel labelled arrows and directed two-cycles change the scope. |
| TRI-02 | Twisted triangle determinant, gauge invariance, and positive Laplacian: CLASSICAL specialization / PROVED LOCAL | Flat transports give ordinary nullity; altered holonomy changes the determinant. |
| TRI-03 | Prime-edge graph is bipartite; composite chord closes flatly: PROVED LOCAL | A triangle requires additional edges or changed generators. |
| TRI-04 | All-\(d\) unit anchor, composition, and strong but non-norm convergence: PROVED LOCAL | Applies to composites too; no privilege of three follows. |
| TRI-05 | Counterfeit preserves local anchors but breaks shared source composition: PROVED LOCAL | Explicit 14/10 and 19/13 output discrepancies. |
| TRI-06 | Shared frames provide a useful design interpretation: INTERPRETATION | No universal numeral hierarchy, physical mechanism, or prime theorem is established. |

The designated finite probe is `triadic_probe.py`; actual execution status belongs in [VALIDATION.md](VALIDATION.md). Expected controls are flat and twisted triangle determinants, gauge changes, ordinary cycle nullity, genuine source composition, and the two counterfeit discrepancies. Finite checks support implementation fidelity; the displayed proofs establish the quantified claims. The next verdict-changing arithmetic result would require a source-sensitive estimate beyond these composition identities.
