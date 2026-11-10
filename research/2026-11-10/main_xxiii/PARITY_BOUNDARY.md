# Quantitative parity boundary control

**Status.** The odd-mode transfer is a proved conditional result, independently derived here from the two exact circle maps. The Fejér boundary estimate is a proved finite result for every consecutive radix-16 orbit. The signed estimate for the literal BBP zero seed remains open.

## Source and target

Write $`e(t)=\exp(2\pi i t)`$, $`T(y)=16y\pmod1`$, and $`R(y)=y+1/2\pmod1`$. Take $`y_n=\{8\cdot16^{n-1}\pi\}`$ and let $`\nu_A=A^{-1}\sum_{n=A}^{2A-1}\delta_{y_n}`$. The binary observable $`b(y)=\lfloor2y\rfloor`$ on $`[0,1)`$ gives the parity of the $`n`$th hexadecimal digit at $`y_n`$. The target is $`\widehat\nu_A(k)=\int e(ky)\,d\nu_A(y)\to0`$ for each fixed odd $`k`$. See the [source contract](../../../docs/PI_FRONTIER_CONTRACT.md) and [Cayley boundary proofs](../../2026-11-09/cayley_source_observer/BOUNDARY_PROOFS.md).

## Conditional transfer to every parity word

**PROVED CONDITIONAL.** If the displayed limit holds as $`A\to\infty`$ through integers, then every fixed length-$`d`$ parity word occurs with epoch and ordinary Cesàro frequency tending to $`2^{-d}`$.

For any continuous circle function $`g`$, the exact difference of its epoch integrals before and after $`T`$ is $`[g(y_{2A})-g(y_A)]/A`$. Hence any subsequential weak limit $`\nu`$ is $`T`$-invariant. Translation by $`1/2`$ acts on the $`k`$th Fourier coefficient by $`(-1)^k`$, so odd-mode vanishing and Fourier uniqueness give $`R_*\nu=\nu`$. Since $`0,1/2\in T^{-1}\{0\}`$,
```math
\nu(\{0\})=\nu(T^{-1}\{0\})\geq\nu(\{0\})+\nu(\{1/2\})=2\nu(\{0\}).
```
Thus $`\nu(T^{-j}\{0\})=0`$ for every $`j\geq0`$. All discontinuities of a length-$`d`$ parity cylinder lie in $`T^{-d}\{0\}`$, so the cylinder is a $`\nu`$-continuity set.

The identities $`TR=T`$ and $`b(Ry)=1-b(y)`$ hold everywhere with the half-open convention. Thus $`R`$ bijects the two choices of first bit over any fixed future parity event. Invariance under $`R`$ gives half the future-event mass to each choice, and invariance under $`T`$ identifies the future-event mass with that of the shorter cylinder. Induction gives $`2^{-d}`$ for each length-$`d`$ word. Portmanteau and compactness give convergence along all integer epochs. To pass to ordinary Cesàro frequency, recursively remove the epoch $`[\lfloor B/2\rfloor,2\lfloor B/2\rfloor)`$ from $`[1,B)`$, starting with $`B=N+1`$. Each split discards at most one endpoint, and the prefix below any fixed epoch threshold is bounded independently of $`N`$.

## A finite boundary estimate with sharp exponent

**PROVED.** For any exact $`T`$-orbit and integers $`A,J\ge1`$, set
```math
\Delta_{A,J}=\max_{\substack{0<|k|<16^J\\ k\,\text{odd}}}|\widehat\nu_A(k)|.
```
Writing $`d(y,0)`$ for circle distance to zero gives
```math
\nu_A\!\left\{d(y,0)\le\frac1{2\cdot16^J}\right\}
\le \frac{\pi^2}{4}\left[2^{-J}+(1-2^{-J})\left(\Delta_{A,J}+\frac1A\right)\right].
```
For the strip around $`T^{-d}\{0\}`$, use radius $`1/(2\cdot16^{J+d})`$ and add $`d/A`$ to the bound.

Define the normalized Fejér peak
```math
F_N(y)=\left|\frac1N\sum_{r=0}^{N-1}e(ry)\right|^2
=\sum_{|k|<N}\frac{N-|k|}{N^2}e(ky).
```
The geometric sums give $`F_{16N}(y)=F_N(Ty)F_{16}(y)`$. The Fourier formula gives $`\sum_{r=0}^{15}F_{16}(y+r/16)=1`$. Its terms are nonnegative and $`TR=T`$, so the $`r=0,8`$ terms give
```math
F_{16N}(y)+F_{16N}(Ry)\le F_N(Ty).
```
For even $`N`$, the sum of the odd Fourier weights of $`F_N`$ is $`1/2`$, because $`F_N(0)=1`$ and $`F_N(1/2)=0`$. Thus
```math
\left|\int(F_{16^j}-F_{16^j}\circ R)\,d\nu_A\right|\le\Delta_{A,J}
\qquad(1\le j\le J).
```
The time shift costs at most $`1/A`$ since $`0\le F_N\le1`$. For $`a_j=\int F_{16^j}\,d\nu_A`$ and $`a_0=1`$, this gives $`2a_j\le a_{j-1}+\Delta_{A,J}+1/A`$. Iteration gives the claimed bound on $`a_J`$. On $`d(y,0)\le1/(2N)`$, the sine quotient gives $`F_N(y)\ge4/\pi^2`$ using $`\sin(\pi Nd)\ge2Nd`$ and $`\sin(\pi d)\le\pi d`$. The deeper estimate follows from $`d(T^dy,0)=16^d\operatorname{dist}(y,T^{-d}\{0\})`$ and the endpoint shift by $`d`$.

### Adversarial controls and limits

- **Sharp exponent.** Independent fair hexadecimal digits $`0,8`$ for $`y`$ give a $`T`$- and $`R`$-invariant law supported in $`[0,8/15]`$. At radius $`16^{-j}`$ for $`j\ge1`$, the strip has exactly mass $`2^{-j}`$, since the first $`j`$ digits must all be zero. At radius $`1/(2\cdot16^j)`$, $`j+1`$ leading zeros suffice, so the mass is at least $`2^{-j-1}`$. Thus a uniform estimate for this invariant class cannot improve the exponent $`1/4=\log_{16}2`$.
- **Coherent wrong seed.** For $`U_0=-\pi/16`$, the same forcing and future tail give the completed orbit zero, so every odd Fourier coefficient and the strip mass equal $`1`$. The [rational p-integral epoch control](../../2026-11-09/pi_parity_pressure/PROOFS.md) separately preserves the selected prime history and yields a fully biased digit epoch.
- **Boundary status.** The estimate gives a finite boundary payment in measured odd modes and the endpoint term. Bounding the odd modes for the literal zero seed remains **OPEN**. A source-specific signed estimate must distinguish the literal zero seed from coherent wrong-seed controls.

The [finite coefficient probe](parity_boundary_probe.py) checks the exact Fejér product, all-branch partition, and odd-weight contrast with integer Laurent coefficients. The proof covers arbitrary $`N`$ and any consecutive orbit.

## Fixed rational seed shifts preserve the entire odd-mode gate

**PROVED.** For a consecutive radix-16 orbit $`y_n`$, suppose all its fixed odd epoch modes vanish. For each fixed modulus $`q`$ and class $`r`$, every fixed odd mode also vanishes when the empirical average is restricted to $`n\equiv r\pmod q`$. Consequently, for the BBP forcing, the all-odd-mode gate holds for the literal zero seed if and only if it holds for any one fixed rational seed.

For the first statement, along any sequence of epochs take a simultaneous weak limit $`\nu_r`$ of the normalized empirical measures of each class. Each $`\nu_r`$ is $`T^q`$-invariant by telescoping on its arithmetic progression. All class sizes are $`A/q+O(1)`$, so $`\nu=q^{-1}\sum_r\nu_r`$ is the corresponding unconditioned limit. The odd-mode hypothesis makes $`\nu`$ invariant under $`R`$, and ordinary telescoping makes it $`T`$-invariant. Because $`\nu_r\le q\nu`$, write $`f_r=d\nu_r/d\nu`$ with $`0\le f_r\le q`$. Invariance of $`\nu_r`$ gives
```math
\int f_r(f_r\circ T^q)\,d\nu=\int f_r^2\,d\nu .
```
Invariance of $`\nu`$ gives $`\|f_r\circ T^q\|_2=\|f_r\|_2`$. Subtracting twice the displayed inner product from the sum of the squared norms gives $`f_r=f_r\circ T^q`$ almost everywhere. Since $`T^qR=T^q`$ and $`R_*\nu=\nu`$, this yields $`f_r\circ R=f_r`$ almost everywhere. Every $`\nu_r`$ is therefore $`R`$-invariant and all its odd modes vanish. The argument applies to every simultaneous subsequential limit.

Changing $`U_0`$ by $`s`$ adds $`8\cdot16^n s`$ modulo one to $`y_n`$. For fixed rational $`s`$, this contribution is eventually periodic, since it is generated by multiplication by sixteen on a finite residue group. Take $`q`$ to be its period. On each class the phase factor of any odd mode is constant for all sufficiently large $`n`$, so classwise vanishing implies the same gate after the shift. The shift by $`-s`$ gives the converse.

This theorem concerns the entire gate and does not promote cancellation of any one odd mode to classwise cancellation. The finite rational wrong-seed control varies its seed with the epoch, so the proof has no fixed period to use there. The coherent seed $`-\pi/16`$ is irrational. These remain the discriminating controls. A purported asymptotic proof of the entire gate cannot use failure at a single fixed rational seed as its required separator.
