# How much does the odd-eight gate ask for?

**PROVED PAPER** for explicit base-16 orbits. The original-zero π gate
remains open. A point generic for each indicated finite-alphabet Bernoulli
process exists by the ergodic theorem. Cesàro convergence gives convergence
on every integer epoch $[A,2A)$ by subtraction. A countable intersection
handles all fixed words and Fourier modes.

1. **Full hexadecimal normality implies the odd-eight gate, strictly.**
   Use independent fair digits in $\{0,1\}$. In a sample $x$, changing
   only the first digit from 0 to 1 adds $1/16$, so $8x$ translates by
   $1/2$. Its odd modes vanish. Digits 2 through 15 have zero frequency.

2. **The odd-eight gate implies fair parity words, strictly.** Let
   $b_j$ be independent fair bits indexed by $\mathbb Z$, and choose
   digit $d_j=2b_{j-1}+b_j$. Its parity process is exactly the Bernoulli
   bit process. For $x=\sum_{j\ge0}d_j16^{-j-1}$,

   $$8x=b_{-1}+\frac9{16}b_0+\sum_{j\ge1}\frac9{16^{j+1}}b_j.$$

   The $k=1$ odd mode factors into $(1+e(9/16))/2$ times the expectation
   of the tail phase. The first factor is nonzero. Tail turns lie in
   $[0,3/80]$, so their real parts are strictly positive. The mode fails
   to vanish, despite every parity word being fair. The next full digit
   records the first parity in its second-lowest bit.

3. **Fair parity words imply one-digit parity balance, strictly.**
   Repeating hexadecimal digits 0,1 gives equal parity frequencies and
   misses both words 00 and 11.

The examples distinguish control of the complete real future, control
of the binary future, and control of a single digit. They calibrate the
[parity-boundary proof](PARITY_BOUNDARY.md).
