# Real near pairs and interval returns below the quadratic scale

**Scope.** Paper derivations, no formal kernel or priority claim. They apply to the actual zero-seeded BBP circle points $x_n=\{U_n\}$, and uniformly to every other seed with precisely the same chronological four-pole forcing. All constants are absolute unless subscripted. Let $A$ be any sufficiently large integer and $D=\lfloor\log_{16}A\rfloor$. Write $N_A(w)$ for the ordered pair count on the integer epoch $[A,2A)$ at circle distance at most $w$, including the diagonal. The results quantify dispersion at fine resolution. The problem's logarithmic mesh is far coarser.

**F5.** Uniformly for $0\le w\le A^{-2}$,
\[
 N_A(w)/A^2\ll A^2w+1/\log A .
\]
In particular $w_A=o(A^{-2})$ implies $N_A(w_A)=o(A^2)$. For fixed $\delta>0$, $w_A\le A^{-2-\delta}$ gives $N_A(w_A)\ll_\delta A^2/\log A$.

**Proof.** For $A\le s<2A$ the beta moment bound of F1 gives $1/(512A^3)\le r(s)-r(s+1)\le 2/A^3$ for large $A$. Put $\Delta_n=U_{n+d}-U_n$ for $1\le d<A$. If all four times $n,n+j,n+d,n+j+d$ belong to the epoch, iteration gives the exact unwrapped law
\[
 \Delta_{n+j}=16^j\Delta_n-B,\qquad
 B=\sum_{i=1}^j 16^{j-i}[r(n+i)-r(n+d+i)].
\]
By telescoping the source differences, $16^{j-1}d/(512A^3)\le B\le2\cdot16^j d/(15A^3)$. Suppose $d>16384 A^3w$ and $\|\Delta_n\|\le w$. Modulo one use a centered representative $z$ for the *input only*, $|z|\le w$. Then $B-16^jz>w$ since $B>2\cdot16^j w$ (if $w=0$, $B>0$ directly). For $1\le j\le D$ we have $B+16^jw\le (1+2/15)/A<1/2$. Hence $\|\Delta_{n+j}\|>w$. Two hits of such a lag are separated by more than $D$ time steps. At most $1+A/D$ hits occur per large positive lag. The other positive lags number at most $16384A^3w$ and contribute at most $A$ each. Doubling and adding the diagonal proves F5.

**F5b. Fourier cross-check.** For fixed $0<\delta\le1$ and $w=A^{-2-\delta}$ there is another derivation, using F1's finite Gram sieve. Set $H=\lfloor\log A\rfloor$ and take the common depths $A^2\le16^j\le A^{2+\delta}/(4H)$, whose number $d\asymp_\delta\log A$. The nonnegative Fejér kernel $F_H(y)=H^{-1}|\sum_{m=0}^{H-1}e(my)|^2$ is at least $4H/\pi^2$ for $\|y\|\le1/(4H)$ by the elementary sine bounds. Every close pair therefore contributes at least that much to $F_H(16^j(x_n-x_t))$ at each depth. On the other hand the average over all epoch pairs equals $1+2\sum_{h=1}^{H-1}(1-h/H)|c_A(16^j h)|^2$ by the finite Fourier polynomial. Summing over $j$ and invoking F1 with $L=1$ bounds the result by $d+O(H)$: $h16^j$ belongs to its band for all the chosen $h,j$. Hence $N_A(w)/A^2\ll1/H+1/d$, as claimed. The two arguments share the original forcing and its beta moment inequalities. They differ at the proof step: one excludes a deterministic temporal revisit, the other sums nonnegative tests using near orthogonality.

**F6. Uniform occupancy.** For any circle arc $I$ of width $0\le w\le A^{-2}$ and any integer $1\le D'\le D$,
\[
 \#\{A\le n<2A:x_n\in I\}
 \le \lceil A/D'\rceil+C D'(1+A^3w).
\]
Consequently for fixed $\delta>0$ and $w\le A^{-2-\delta}$ the uniform cap is $O_\delta(A/\log A)$. In particular no single microscopic interval of such width can capture a fixed positive fraction of the actual phase cloud.

**Proof.** Lift $I$ to $[\theta,\theta+w]$. If $x_n,x_{n+j}\in I$ then
\[
 (16^j-1)\theta+R_j(n)\in \mathbb Z+[-16^j w,w],\qquad
 R_j(n)=\sum_{i=1}^j16^{j-i}r(n+i).
\]
This inclusion uses integer lifts of both visits, so also covers arcs wrapping through zero. For fixed $1\le j\le D'$, $R_j$ is decreasing and its total range is $\ll16^j/A^2\le C/A$, by $r(s)\ll A^{-2}$. Its adjacent decrement is at least $16^{j-1}/(512 A^3)$ by the $i=1$ term. The enlarged range of the left side has length $O(1/A)$, so at most a bounded number of integer translates of that short window are relevant. Each occupies at most $1+C A^3w$ possible integer times by the minimum decrement. Thus each lag $j\le D'$ has $O(1+A^3w)$ pairs of visits. Partition the epoch into disjoint consecutive blocks of at most $D'$ times. Every visit after the first in a block contributes a distinct ordered short-return pair with the preceding visit in that block. Summing those pairs plus one initial visit per block gives F6. In particular one can also choose $D'$ tending to infinity sufficiently slowly whenever $A^2w\to0$; all such widths have uniform occupancy $o(A)$.

**Sharp obstruction in scale.** On the fixed coherent counterseed $-\pi/16$, every point of the epoch is $-T_n$ with $0<T_n<1/(64A^2)$. Thus $N_A(1/(64A^2))=A^2$ and one arc of that width contains the entire epoch. #492's AS-02 source-native rational family likewise clusters within width $1/(32A^2)$ eventually. F5 and F6 cannot be extended to give an $o(1)$ proportion at every fixed positive multiple of $A^{-2}$ from seed-blind bounds. For the null forcing $r=0$, the zero-seeded orbit is constant: both fine-scale estimates fail, verifying that positive chronological shear does work. It is still possible that the original zero-seeded source admits much coarser dispersion.

**Relation to prior art.** #492 AV-01 gives one-step signed shear and SHARP_SHEAR.md controls its total budget; AV-07 pays for eventual resolution of distinct rational gaps. F5 gives an actual density estimate from *many-step* one-sided shear on shrinking arcs, and F6 bounds each interval's returns. Neither estimate reaches $w=1/q_A\asymp1/\log A$. For the fixed $h$ problem F4 instead identifies the signed cancellation improvement over sharp coherent controls that crossing this boundary costs.

**F7. Squared-logarithm bound for actual near pairs.** For every fixed $\delta>0$,
\[
 N_A(A^{-2-\delta})\ll_\delta A^2/(\log A)^2.
\]
This improves F5 at the polynomial scale. It also proves that **a union of a polynomial number of shrinking bins** has few visits. Let $\varepsilon=\min(\delta,1)/4$, $m=\lfloor A^\varepsilon\rfloor$. For every collection of at most $m$ arcs of width $w\le A^{-2-\delta}$, the combined visit count is $O_\delta(A/\log A)$.

**Proof.** F6's short-return count extends verbatim to $x_n\in I$, $x_{n+j}\in J$ for two independently chosen arcs: the constant $(16^j-1)\theta$ becomes $16^j\theta_I-\theta_J$. Thus fixing $j\le D$ and an ordered pair $I,J$ costs at most $C(1+A^3w)$ times. In each block of length $D$, every visit to the union after the first supplies one distinct short-lag transition between an ordered pair of the listed arcs (if a point belongs to several, assign one). Hence its total mass divided by $A$ is at most
\[
 O(1/D)+O\bigl(Dm^2(A^{-1}+A^2 w)\bigr)=O_\delta(1/\log A).
\]
For the pair count partition the circle into $b=\lceil1/w\rceil$ equal half-open bins of width $1/b\le w$, where now $w=A^{-2-\delta}$. Sort their mass fractions $p_i$ in decreasing order. The top $m$ together have mass $O_\delta(1/\log A)$, giving $\sum_{i\le m}p_i^2\ll_\delta1/(\log A)^2$. Since $p_{m+1}\le1/m$, the remaining sum of squares is at most $1/m$. Reverting to spatial bin order, points at circle distance at most $w$ have indices at most two bins apart (for large $A$, $bw<2$). By Cauchy–Schwarz each of the five shifted mass products has sum at most $\sum p_i^2$. Therefore $N_A(w)/A^2\le5\sum p_i^2\ll_\delta1/(\log A)^2$. Monotonicity covers smaller widths. This statement holds for the original selected trajectory, while also allowing every changed seed. A single interval containing order $A/\log A$ phases along an independently constructed epoch seed would show sharpness of this uniform-in-seed pair bound at the corresponding width.
