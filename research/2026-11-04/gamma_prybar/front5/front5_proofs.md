### Radial saturation inside a convergent source frame

Write the original and second four-pole sources as tap vectors
\(P=(4,0,0,-2,-1,-1,0,0)\), \(P^\sharp=(0,8,4,4,0,0,-1,0)\).
For any taps \(w\), let \(r_w(n)=\sum_{j=1}^8 w_j/(8(n-1)+j)\);
\(X^w_0=0\), \(X^w_n=16X^w_{n-1}+r_w(n)\), over the rationals without reduction modulo one.
Use \(U=X^P, V=X^{P^\sharp}, Y=(2U+V)/4\), and \(Z=U-Y=(2U-V)/4\).
The radial taps are \(R=(2,-2,-1,-2,-1/2,-1/2,1/4,0)\).
Inherited #497 PF-06 proves \(0<Z_n<1/(32n+16)\) for every \(n\ge1\);
#499 PQ-02 proves the group fixes \(R\). All ranges below refer to the authentic zero seeds.

**Theorem.** For each fixed \(0<\epsilon<1\) there is \(N_\epsilon\) such that every odd prime
\(\epsilon N<p\le8N-7\) at every \(N\ge N_\epsilon\) satisfies \(v_p(Z_N)=-1\).
In particular \(\log\operatorname{den}(Z_N)=(8+o(1))N\).
For \(1\le q=o(A)\) the radial orbit has
\(q(1-q/(32A+16))\le J_{A,q}(Z)\le q\). Thus the angular conductor and macroscopic simple-pole survival can *both* occur in a zero-seeded projection of the same eight-tap module with asymptotically maximal collision energy. This refutes the implication from these two properties alone. It does not transfer radial concentration to the original or angular orbit.

**Proof.** Let \(a=p\bmod8\), \(j_a(l)\in\{1,\ldots,8\}\) represent \(al\bmod8\), \(f_a(l)=(2/p)^l2^{(l+8-j_a(l))/2}\), where \((2/p)\) is the Legendre symbol. For multipliers \(m=8k+l\), \(1\le l\le8\), put \(t=(mp+8-j_a(l))/8\). With \(p>8\), \(p^2>8N\) and \(t\le N\), the normalized rational representative of \(pZ_t\bmod p\) is
\[
 C_{a,k,l}=\frac{f_a(l)}{16}\left(16Z_k+\sum_{j=1}^l \frac{R_j}{8k+j}\right).
\]
Indeed the transport from \(kp\) to \(t\) is \(16^{t-kp}\equiv f_a(l)\) by Euler's criterion. At \(kp\) the shadow is \(Z_k\) by the trivial character and #499 PQ-2 (at \(k=0\) both sides vanish). The injection at slot \(j\) contributes \(R_{j_a(j)}/(8k+j)\), times transport \(f_a(l)/f_a(j)\). Multiplying out the fixed-vector identity gives \(R_{j_a(j)}/f_a(j)=R_j/16\). These statements also hold at slots with zero injection.

Denote the parenthesis by \(B_l\). Since \(R_8=0\), \(B_7=B_8=Z_{k+1}>0\).
The exceptional intermediate slot satisfies
\[
 B_6=Z_{k+1}-\frac1{32k+28}<\frac1{32k+48}-\frac1{32k+28}<0.
\]
But \(B_5=B_6+1/(16k+12)>0\), and \(B_1\ge B_2\ge B_3\ge B_4\ge B_5\). Thus every normalized slot is nonzero for *every* \(k\ge0\), with the one extra minus sign at slot six beyond the Legendre transport.

All four odd taps of \(R\) are nonzero. So \(p\le8N-7\) has its first slot by time \(N\); for \(p>\epsilon N\) only finitely many rational normalizers can occur (\(m\le8/\epsilon\)). For large \(N\) the prime exceeds all prime divisors of their reduced numerators and denominators. Between the last slot and \(N\), transport by a power of 16 preserves the nonzero residue. This proves the uniform macroscopic survival. Denominators of all moments divide \(4\operatorname{lcm}(1,\dots,8N)\), so PNT gives limsup at most 8. The surviving primes give liminf at least \(8-\epsilon\); let \(\epsilon\downarrow0\). On the epoch every pair has circle distance at most \(1/(32A+16)\), which gives the energy bounds directly. In particular the interval \([0,1/q)\) contains all radial states for large \(A\).

The extra inert primes have an exact explanation. For \(4N<p\le8N-7\), \(p\equiv3\bmod4\), none of the four original denominator progressions can contain \(p\) (the first odd multiple is in an absent slot and \(2p>8N\)). For sufficiently large \(N\), \(v_p(Y_N)=v_p(Z_N)=-1\) and \(pY_N=-pZ_N\pmod p\) because \(U_N=Y_N+Z_N\). Their combined residue for the original phase is zero. These primes have log mass \(2N+o(N)\) by fixed-modulus PNT. The observation concerns this specified band, and leaves joint constraints involving other primes available for further study.

### Signed radial finite part in closed form

Write \(\Delta_n=V_n-2U_n=-4Z_n\), \(d_n=r_{P^\sharp-2P}(n)\), with taps \(b=(-8,8,4,8,2,2,-1,0)\) summing to 15. Then the constant \(C=\sum_{n\ge1}[\Delta_n+1/(8n)]\) from #497 PF-09 is explicitly
\[
 C=\frac{\pi(5\sqrt2+3)/2 +15\sqrt2\log(1+\sqrt2)-34\log2}{120}.
\]
Proof: telescoping the unwrapped recurrence gives \(15\sum_{n=1}^N\Delta_n=16\Delta_N-\sum_{n=1}^N d_n\), and \(\Delta_N\to0\). The elementary identity \(\sum_{k=0}^{N-1}1/(k+x)=\psi(N+x)-\psi(x)\) and \(\psi(N+x)=\log N+o(1)\) at fixed \(x>0\) give \(120C=\sum_{j=1}^7 b_j[\psi(j/8)+\gamma]\). In Gauss's rational digamma formula, the weighted cotangent sum is \(-5\sqrt2-3\); the cosine sums at frequencies 1,2,3 are \(-8-15\sqrt2/2,-2,-8+15\sqrt2/2\). Pairing conjugate frequencies gives the expression above using \(\sin(3\pi/8)/\sin(\pi/8)=1+\sqrt2\) and \(\sin(\pi/8)\sin(3\pi/8)=\sqrt2/4\). The \(k=4\) logarithm after conversion to log-sines vanishes. This sign uses \(V-2U\), the orientation of PF-09. Classical identity: [NIST DLMF 5.4.19](https://dlmf.nist.gov/5.4.E19).

Both statements are paper derivations. The finite part measures the signed displacement accumulated across frames. The fixed-character decay estimate needed for normality concerns either individual frame and remains open.

### Cross-time denominator loss costs vanishing tent energy

Fix any of the three zero-seeded sources \(X=U,Y,Z\) above and write \(D_t=\operatorname{den}(X_t)\), \(D_{tn}=\operatorname{den}(X_t-X_n)\) (including \(\operatorname{den}(0)=1\)). Define the lost prime mass
\[
 \Lambda_X(t,n)=\log (D_t/\gcd(D_t,D_{tn})),\qquad A\le n\le t<2A .
\]
There is an absolute constant \(C\) for all three sources and all integer \(A\ge 2\), uniformly in the later endpoint \(t\), such that
\[
 \sum_{n=A}^t \Lambda_X(t,n)\le C A^{3/2}.
\]
This is an estimate on exact differences along the selected chronological orbit. It also holds with an altered fixed rational seed with an additive constant depending on its denominator, by the same proof after excluding that seed's primes. No signed phase cancellation or real lower spacing of order \(1/q_A\) is implied.

**Proof.** All source states in this epoch have denominators dividing \(4\operatorname{lcm}(1,\ldots,16A)\). For each \(p\le4\sqrt A\), its total logarithmic contribution at a fixed pair is at most \(\log(64A)\). The elementary Chebyshev prime bound \(\pi(x)\ll x/\log x\) bounds the combined small-prime loss by \(O(\sqrt A)\) per pair. In what follows \(4\sqrt A<p\le16A\), so a state can have at most a simple pole there. We only count primes dividing \(D_t\). At such primes the loss equals \(\log p\) exactly when \(b_n=pX_n\bmod p\) equals \(b_t=pX_t\bmod p\neq0\).

A possible injection occurs at time \(j\) when one of \(8(j-1)+l,1\le l\le8\), is divisible by \(p\). These eight consecutive integers in each shell form a disjoint partition of the integer positions. Thus in \([A,t]\) there are at most \(1+8A/p\) possible injection times. Partition the epoch at those times, starting a new block at each injection. Within each block values propagate by \(b_{j+1}=16b_j\bmod p\). A zero block gives no match to \(b_t\). On a nonzero block of length \(H\), a given residue occurs at most \(H/o_p+1\) times, where \(o_p=\operatorname{ord}_p(16)\). Hence the total hits per prime are at most \(A/o_p+2+8A/p\).

The stock of small multiplicative orders gives a power saving even without any primitive-root conjecture. Let \(W(s)=\sum_{p\le16A,\,p\text{ odd},\,o_p\le s}\log p\). Since every such prime divides \(\prod_{1\le k\le s}(16^k-1)\), we have \(W(s)\ll s^2\) for \(s\ge1\), while Chebyshev gives \(W(s)\ll A\). Consequently
\[
 \sum_{2<p\le16A}\frac{\log p}{o_p}
  =\int_1^\infty \frac{W(s)}{s^2}\,ds\ll \sqrt A.
\]
Also \(\sum_{p\le16A}\log p/p\ll\log(2A)\) by partial summation from Chebyshev. After summing the hit estimate weighted by \(\log p\), its order term is \(O(A^{3/2})\); its two block-count terms are \(O(A\log(2A))\). Adding the small-prime budget proves the assertion, including the diagonal.

**Energy consequence.** Give ordered pairs the same loss after sorting their time coordinates. For any \(H>0\), at most \(2C A^{5/2}/H\) ordered pairs have loss greater than \(H\). Their tent-energy contribution at mesh \(q\ge1\) is at most \(2C q\sqrt A/H\), by positivity and the pointwise kernel bound. In particular at \(H=\sqrt A(\log A)^2\) and the specified \(q_A\le(\log A)/2\), the whole discarded contribution is \(O(1/\log A)\). On the complementary pairs
\[
 D_{tn}\ge D_t\exp[-\sqrt A(\log A)^2].
\]
For \(X=U\), #497 PF-05 gives \(\log D_t=(6+o(1))t\); the analogous coefficient for both \(Y\) and \(Z\) is 8. This deduction uses all sufficiently large \(t\), so it holds uniformly on dyadic epochs. All remaining energy can therefore come from differences having almost all the later state's conductor, measured prime by prime. The preceding radial theorem shows this restriction is compatible with \(J/q\to1\) on a zero-seeded frame of the very same source module. The open obligation concerns the centered residues of those *surviving* differences. Any estimate based on centered residues must also respect their shared real lift and the source addition \(U=Y+Z\).

### An individual lower bound for every original difference

Let \(X=U\) be the literal zero-seeded four-pole orbit. Uniformly as \(A\to\infty\) for every integer \(A\le n<t\le2A\), \(d=t-n\), one has
\[
 \log\operatorname{den}(U_t-U_n)\ \ge\ 6d+4n-t+(2n-4t/3)_+-d\log16-o(A)
 \ \ge\ (11/3)n-o(A).
\]
The first lower bound measures the prime mass known to survive in *each* difference. In particular every pair in a sufficiently late dyadic epoch has distinct circle phases. The conclusion supplies no lower bound at the reciprocal-logarithmic real resolution.

**Proof.** Count four disjoint prime sets. For the two fresh sets take split primes \(p\equiv1\pmod4\) in \((8n,8t-7]\) and inert primes \(p\equiv3\pmod4\) in \((4n,4t-1]\). Each has no pole by \(n\); by \(t\) it has valuation \(-1\) in \(U_t\) by #497 PF-05, since these primes exceed \(t\) and meet the exact first-birth cutoffs. Thus every such prime divides the reduced gap denominator. The two sets together have logarithmic mass \(6d+o(A)\) by PNT in the two fixed progressions modulo four.

For the two inherited sets take split primes in \((2t,8n-7]\) and inert primes in \((8t/3,4n-1]\), an empty range contributing zero. In a split class the first pole occurs at multiplier \(m=1\), the next at \(m=4\); in an inert class the first two are \(m=2,3\). This follows directly from the four signed denominator offsets modulo eight (#497 PF-01). The upper endpoints ensure a first injection by \(n\); the lower endpoints rule out a second through \(t\). The first pole has nonzero residue since \(p>5\) and the seed is zero. Thus \(p(U_t-U_n)\equiv(16^d-1)pU_n\pmod p\), with \(pU_n\ne0\pmod p\). All such primes except divisors of \(16^d-1\) survive. The summed logarithms of the exceptions over *both* sets are at most \(d\log16\). PNT-AP gives their pre-exclusion mass \(4n-t+(2n-4t/3)_++o(A)\). All PNT errors here are uniform endpoint errors on \([A,16A]\); an empty interval at the bounded endpoint offsets alters at most \(O(\log A)\). Summing proves the first bound. For \(d\le n/2\) the coefficient is \((11/3)n+(11/3-\log16)d\); for \(d>n/2\) it is \(3n+(5-\log16)d\ge(11/3)n\). No prime-gap assertion enters. No inference from a large reduced denominator to the centered numerator is made.

**All later times and prior art.** For \(2n\le t\le4n\) use the single fresh split window \(8n<p\le8t-7\). It has one injection, since \(p>8n\ge2t\), and contributes \(4(t-n)+o(n)\ge4n+o(n)\). For \(t>4n\), use \(2t<p\le8t-7\) instead, obtaining \(3t+o(t)\). These bounds and the dyadic theorem imply \(\liminf_{n\to\infty}\inf_{t>n}\log\operatorname{den}(U_t-U_n)/n\ge11/3\). Main's DPF-01 in research/2026-11-02/macrolag_prime_witness/PROOFS.md already proved this statement with constant \(12/(5+\log16)\), as well as eventual nonrepetition. The improvement above adds disjoint survivor sets and includes the inert classes; prior DPF-02 gave a related coherent changed-*source* counterexample. CT1 in research/2026-10-30/zero_boundary_dispersion/crt/CRT_DOSSIER.md already treats sublinear lags using short-interval LCM bounds. The average loss theorem here covers the macroscopic lags that CT1 does not address.

**Strengthening with two more inherited intervals.** The same method actually gives
\[
 \liminf_{n\to\infty}\inf_{t>n}\frac{\log\operatorname{den}(U_t-U_n)}n
 \ \ge\ \frac{79}{14}-\log 4=4.25656278\ldots .
\]
In the dyadic proof add two disjoint sets. For split primes with \(8t/9<p\le(8n-7)/6\) the multiplier-6 pole has occurred by \(n\) and the next possible multiplier is 9, beyond \(t\). For inert primes with \(8t/7<p\le(8n-7)/4\) the corresponding consecutive pole multipliers are 4 and 7. In either band #497 PF-05 ensures \(v_p(U_n)=-1\) for all large \(n\), uniformly since \(p\gg n\). Hence the same integer \(16^d-1\) controls simultaneous losses over *all four* inherited bands. The extra masses are \((2n/3-4t/9)_++(n-4t/7)_++o(n)\). After setting \(x=(t-n)/n\in[0,1]\), the normalized lower bound up to \(o(1)\) is
\[
 (6-\log16)x+3-x+(2/3-4x/3)_+
 +(2/9-4x/9)_++(3/7-4x/7)_+ .
\]
It is convex. The left derivative at \(x=1/2\) is \(6-\log16-1-4/3-4/9-4/7<0\); its right derivative is \(6-\log16-1-4/7>0\). Evaluating the minimum at \(1/2\) proves the constant. For \(2n\le t\le4n\) the two fresh sets of the dyadic proof continue to count: their primes exceed \(t/2\), so PF-05 applies uniformly at \(t\) even with multiple events. They contribute \(6(t-n)+o(n)\ge6n+o(n)\). The previous \(t>4n\) bound handles the remaining range. This is a lower bound; the optimal constant is unknown.
