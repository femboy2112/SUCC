# Operation SUCC Variable-Length Source Memory — Exact Conditional Bitcode

**2026-10-27. Research-only child of [Codex PR #328](https://github.com/femboy2112/SUCC/pull/328), base commit 68c00f5eee86c215dd09271b35b0647a5b56f16e.** Original four signed BBP source poles, U0=0, frozen archives and main untouched. **π base-16 normality remains OPEN.** Explicitly credit PR #328 for prior partial-sheet counts, conditional entropy and Markov-order-two source history. This new appendix gives a minimum variable-length binary selector and independently validated constructive Hensel inversion.

## 1. Observer-relative complexity (not field-only complexity)

Given finite source-labelled observation O on Z/p^L, a known output a and its fiber F_a={x modp^L:O(x)=a} of size m_a, the minimal **fixed length within that fiber** needed for an extra binary selector is

$$\boxed{\ell_O(a)=\lceil\log_2m_a\rceil.}\tag{VC-1}$$

This follows by pigeonhole and enumeration. The receiver must already know p,L,O,a; without that side information, the selector is **not** a code for x. Code length varies with the value a, and the conditional codes are prefix-free. Under uniform Haar X modp^L, each fiber is conditionally uniform and

$$\boxed{H(X\mid O(X))=\frac1{p^L}\sum_x\log_2m_{O(x)}.}\tag{VC-2}$$

A source-code must transmit the observation if it is not supplied: H(O(X))+H(X|O(X))=L log_2 p. These are Shannon bits, not algorithmic Kolmogorov complexity, CPU work, intrinsic physical probabilities, or π normality.

## 2. Source-exact quadratic branching and minimum bits

Use the authentic cleared numerator A(x)=120x²−89x+16, not the complete r=A/D nor the state U. At p=2,3,5, A is a bijection modulo every p^L, and the needed **extra selector length is 0**.

For p>=7 put b=89/240 in Z_p, c=A(b)=−241/480, q=p^L. Exact source identities:

$$A(x)-c=120(x-b)^2,\qquad A'(x)=240(x-b).$$

For observed a with delta=(a-c)/120 modq, if delta is a nonzero square with valuation 2v<L, fix a canonical Hensel root w of delta/p^(2v) modulo p^(L−2v). Every compatible state is **uniquely** one of

$$\boxed{x=b+p^v(\pm w+p^{L-2v}j)\pmod q,\quad 0\le j<p^v.}\tag{VC-3}$$

Thus the side code has one orientation bit and a lift index of size p^v:

$$\boxed{\#F_a=2p^v,\quad\ell_O(a)=1+\lceil v\log_2p\rceil,\quad v=v_p(A'(x)).}\tag{VC-4}$$

If delta=0 modq, the two orientations merge, and all states are x=b+p^ceil(L/2)j with 0<=j<p^floor(L/2). The critical target needs exactly ceil(floor(L/2)log_2p) bits **without** a distinct sign bit. Odd valuations and nonsquare nonzero units yield empty fibers and are rejected.

At p=7, typical mod7 values need 1 bit, but the critical A(6)=1 has one state (0 bits). Mod49 the critical value 29 has seven states (3 bits): 6,13,20,27,34,41,48. Mod343, A(6)=29 has fourteen states (4 bits); the critical target A(139)=176 has seven states (3 bits). At mod2401 the critical fiber contains 49 states (6 bits). The pole-contact flag of the former 2-bit system is derivable from the reconstructed x, not an independent bit. PR #328 independently proves its constancy on each partial-sheet class.

## 3. The exact information law — bounded average, unbounded worst case

Under uniform X modp^L, orientation is uncertain with probability 1−p^(−ceil(L/2)), while the number of lift base-p digits is min(v_p(X−b),floor(L/2)). Summing tail probabilities gives E min(v_p(X−b),floor(L/2))=(1−p^(−floor(L/2)))/(p−1). Consequently,

$$\boxed{H(X\mid A(X))=
1-p^{-\lceil L/2\rceil}
+\frac{\log_2p}{p-1}(1-p^{-\lfloor L/2\rfloor}).}\tag{VC-5}$$

This *recovers* the prior #328 next-output conditional entropy under conversion to bits. In particular as L→∞ it tends to 1+log_2p/(p−1), which at p=7 is **1.467892487... bits**. Yet the rare critical target needs ~L log_2(p)/2 selector bits. A local observer may therefore see near-constant **mean** description cost and arbitrarily large **exceptional** cost in the same field.

Classical Shannon coding bounds give H≤E length<H+1. The separate complete standalone Hensel encoder/decoder and seven focused tests independently confirmed this at p=2,3,5,7,11,241 and 7^5,11^4,241^2, with separate exact stdout, SHA-256 manifest and download in the research chat. The present GitHub appendix is not asserted byte-identical to those locally tested files.

## 4. SUCC successor recovers the information

The original numerator satisfies A(x+1)−A(x)=240x+31. For every p>=7, 240 is invertible modulo p^L, yielding

$$\boxed{x=(A(x+1)-A(x)-31)/240\pmod{p^L}.}\tag{VC-6}$$

Hence observing **two consecutive values** makes the state fiber a singleton; the side-bit cost becomes zero. More precisely I(X;A(X+1)|A(X))=H(X|A(X)). The missing bits were hidden in a coarse observation, not destroyed or replaced with independent stochastic events. PR #328 independently established exact Markov order two for the finite A-output process and zero entropy rate of the deterministic periodic clock. For the full projective four-pole source, PR #328 proves that **three consecutive** source values are minimally needed at p=7. The number of measurements and coding cost depend on the chosen observer.

## 5. What this does not prove

Even exact minimal source codes are changes of coordinates. If the code fully reconstructs n mod p^L it is precisely the old time-residue partition. Codex [#327](https://github.com/femboy2112/SUCC/pull/327) and [#328](https://github.com/femboy2112/SUCC/pull/328) already proved that prescribed growing conditional Fourier-energy gates may remain positive on genuinely normal finite-type carriers, so there is **no free real-character cancellation from variable-bit encoding**.

The only sufficient authentic target remains S_N(h)=Σ_(n<N)e(hU_n)=o(N) for every fixed nonzero integer h. A valuable next probe is to stratify real signed correlations by the new exact arithmetic statistic v_p(A'(n)), with zero selector and every original pole retained, and defeat changed-seed, strongly 2-adic-isometric nonnormal and finite-energy countermodels. Any lift of p-adic bits to real Fourier phases must be independently proved.

Classical background: [Hensel lifting](https://math.uchicago.edu/~may/REU2013/REUPapers/Marohnic.pdf) and [Kraft/Shannon source coding](https://theory.stanford.edu/~blynn/pr/symbol.html). Original source: [#325](https://github.com/femboy2112/SUCC/pull/325). Prior entropy: [#328](https://github.com/femboy2112/SUCC/pull/328).
