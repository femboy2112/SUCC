# E7. Every prescribed growing residue-energy gate has a normal counterexample of irrationality exponent at most four

**Status: PROVED on paper; root and separate derivations audited.** This strengthens E6's finite-type obstruction. It is not a statement about the authentic zero-selected pi orbit, and no external priority is claimed.

## Theorem and quantifiers

Let M:N->N be any prescribed positive-integer schedule satisfying M(N)->infinity and M(N)/N->0. There exists a base-16 normal real alpha in [0,1] with irrationality exponent at most four such that, for every fixed integer h,

$$\liminf_{j\to\infty} E_\alpha(2^j,M(2^j),h)\ge\frac14.$$

where

    z_n=e(h16^{n-1}alpha),
    E_alpha(N,m,h)=(m/N^2) sum_{t mod m}|sum_{1<=n<=N,n=t mod m}z_n|^2,
    e(x)=exp(2 pi i x).

The same one alpha handles all fixed h. The theorem includes every admissible prescribed growing CRT schedule. It does not assert a uniform lower approximation bound C q^{-4}; its irrationality-exponent conclusion is obtained separately for every exponent greater than four.

## 1. Construction and the fresh-word probability space

Put N_0=0, N_j=2^j for j>=1, L_j=N_j-N_{j-1}, and m_j=M(N_j). Stage j will be the first L_j digits of the periodic repetition of a word W_j of length m_j. Concatenate these finite stages to define alpha.

For j>=2 the already fixed prefix has length P=N_{j-1}, and stage j has length P. Let d be the next digit that the previous word W_{j-1} would supply by periodic continuation. Prescribe the first digit of W_j as b_j=0 if d>=2 and b_j=3 otherwise. This marker differs from d by at least two. Early stages may use any words obeying this marker rule. The remaining choice below applies eventually, when m=m_j is large and m<=P.

Let alpha_old be the rational truncation of the already fixed first P digits, with zeros thereafter. For 1<=n<=P, put

    z_n^old(h)=e(h16^{n-1}alpha_old).

Temporarily choose W uniformly among all 16^m words, independently of this fixed prefix. Let A be its base-16 integer value, Q=16^m-1, beta_W=A/Q, and define the periodic unit phase for all n by

    w_n(h;W)=e(h16^{r(n)} A/Q),
    r(n)=(n-P-1) mod m, 0<=r(n)<m.

Thus the phase is aligned at the start of the new stage. The uniform A range is 0,...,16^m-1 inclusive, containing both A=0 and A=Q; that duplicated circle endpoint is intentional.

Define

    H=floor(m^{1/8}), delta=m^{-1/8},
    R=max{r>=0:16^{8r}<=m}.

Call W good if both conditions hold:

1. For every 1<=h<=H,

       |sum_{n=1}^P z_n^old(h) conjugate(w_n(h;W))| <= delta P.

2. For every radix word v of length 1<=r<=R, its cyclic frequency F_W(v) differs from 16^{-r} by at most delta.

Choose the lexicographically first good W whose first digit is the marker b_j. The following bounds prove such a word exists at every sufficiently late stage. For computable M the choice can in principle be made effectively: all finite phase values are roots of unity, and the finite correlation comparisons are comparisons of explicit real algebraic numbers. This is not a claim that these enormous searches were executed.

## 2. Exact random-period second moment and marker conditioning

For two distinct residues r,s modulo m and nonzero h with |h|<16^{m/2}+1,

    Q does not divide h(16^r-16^s).

Indeed gcd(Q,16^{|r-s|}-1)=16^{gcd(m,|r-s|)}-1, and the proper divisor gcd(m,|r-s|) is at most m/2. Hence Q/gcd(Q,16^{|r-s|}-1)>=16^{m/2}+1. Multiplying by a power of 16 does not change this divisibility. Our H is in the permitted range for all sufficiently large m.

The finite geometric sum over A gives exactly

    E_A e(h(16^r-16^s)A/Q) = 16^{-m}, r!=s,

and the diagonal expectation is one. The extra 16^{-m} comes from the duplicated endpoint, not from an independence assumption.

Group the old phases by r(n), writing C_r=sum_{n<=P,r(n)=r}z_n^old(h). Then the exact second moment is

    E_A |sum_n z_n^old(h) conjugate(w_n(h;W))|^2
      =(1-16^{-m}) sum_r |C_r|^2 +16^{-m}|sum_r C_r|^2.

For m<=P, the residue class sizes c_r satisfy

    sum_r |C_r|^2 <= sum_r c_r^2
       <= P^2/m+P <= 2P^2/m.

Markov's inequality and a union bound over 1<=h<=H therefore bound the probability of failure of condition 1 by

    2m^{-5/8} + m^{3/8}16^{-m}.                         (E7.1)

For condition 2, assume 2R<=m. A cyclic r-word indicator depends on r distinct uniform digits. Two such indicators are independent unless their windows overlap; for each starting position there are at most 2r-1 possibly dependent positions. Thus

    E F_W(v)=16^{-r},     Var F_W(v)<=2r/m.

Chebyshev and the union bound over all words through length R give

    Prob(condition 2 fails)
      <=2m^{-3/4} sum_{r=1}^R r16^r
      <=(32R/15)m^{-5/8},                              (E7.2)

because 16^R<=m^{1/8} and sum_{r<=R}16^r<=16^{R+1}/15.

The event that the first digit equals the prescribed marker has probability exactly 1/16. Conditioning on this event increases any failure probability by at most sixteen. Hence the conditional failure probability is at most

    16[(2+32R/15)m^{-5/8}+m^{3/8}16^{-m}]
       <=(36+512R/15)m^{-5/8}.                         (E7.3)

The last inequality uses 16m16^{-m}<=4 for m>=1. This tends to zero as m->infinity. Consequently the good-word/marker intersection is nonempty eventually. The other elementary range requirements also hold eventually; finitely many earlier words may be arbitrary subject to their marker. Negative h need no further union bound because their correlations are complex conjugates.

## 3. Normality at every prefix

Fix a word v of length r. Since R_j->infinity and delta_j->0, eventually W_j has cyclic v-frequency within delta_j of 16^{-r}. A prefix of L starting positions in its periodic continuation has discrepancy at most

    delta_j L+2m_j,

by removing complete periods and bounding the remaining partial period. Comparison with the actual concatenation costs at most r starts per stage boundary.

At a prefix ending inside stage j, sum these bounds over completed stages and the current partial stage. The finite early stages cost a constant. The delta terms are o(N), by first discarding finitely many stages and then bounding every later delta by an arbitrary positive epsilon. Also

    sum_{i<=j}m_i=o(N_j),

because m_i/N_i->0 and sum_{i<=j}N_i<2N_j. For a prefix in stage j>=2, N>=N_{j-1}=N_j/2, so the same sum is o(N), uniformly within the stage. Finally j/N->0. Every fixed finite word therefore has limiting frequency 16^{-r} at every prefix, proving normality.

## 4. A uniform finite energy lower bound

Fix a late stage j, write N=N_j, P=N/2, m=m_j, and use the chosen periodic phase w_n. The actual alpha and its old truncation differ by at most 16^{-P}. Consequently

    sum_{n=1}^P |e(h16^{n-1}alpha)-z_n^old(h)|
       <=2 pi |h| sum_{n=1}^P16^{n-1-P}
       <=2 pi |h|/15.                                 (E7.4)

For n in the new stage, the actual radix expansion and the periodic word share all s=N-n+1 remaining stage digits. Their circle distance is at most 16^{-s}, including the possible circle endpoint convention. Therefore

    sum_{n=P+1}^N |e(h16^{n-1}alpha)-w_n(h)|
       <=2 pi |h| sum_{s=1}^P16^{-s}
       <=2 pi |h|/15.                                 (E7.5)

For every 1<=|h|<=H_j, the good-word correlation condition, (E7.4), and (E7.5) imply

    Re sum_{n=1}^N e(h16^{n-1}alpha) conjugate(w_n(h))
       >= P-delta_j P-4 pi |h|/15.

Because w is m-periodic and has unit modulus, Cauchy--Schwarz over the m residue classes gives the exact bound

$$E_\alpha(N_j,m_j,h)\ge
\left(\frac12-\frac{\delta_j}{2}-\frac{4\pi|h|}{15N_j}\right)_+^2.\tag{E7.6}$$

Every fixed h is eventually in the growing band H_j. Taking lower limits proves the asserted 1/4. For h=0 the energy is at least one directly. No deterministic lag coordinates are treated as independent random variables; the auxiliary word randomization only proves existence of the selected word at each finite construction stage.

## 5. Irrationality exponent at most four

Let A_j be the rational radix number which agrees with alpha through position N_{j-1}, then repeats W_j forever. It has a positive denominator Q_j, not necessarily reduced, bounded by

    Q_j <16^{N_{j-1}+m_j}.

It agrees with alpha through position N_j. At position N_j+1, the marker in stage j+1 differs by at least two from the periodic continuation of W_j. The remaining tail can compensate by at most one digit unit. Thus

    16^{-(N_j+1)} <= |alpha-A_j| <=16^{-N_j}.          (E7.7)

Fix epsilon with 0<epsilon<1/4. Eventually m_j<=epsilon N_j. Put a=1/2-epsilon>0, b=1/2+epsilon. Then Q_j<=16^{bN_j}. Given a sufficiently large integer denominator q, choose the least j in this eventual range for which

    2q<=16^{aN_j}.

For sufficiently large q the preceding index is also in the range. Since N_j=2N_{j-1}, minimality gives

    2q>16^{aN_j/2},     16^{N_j}<(2q)^{2/a}.         (E7.8)

If p/q!=A_j, rational separation and (E7.7) imply

    |alpha-p/q| >=1/(qQ_j)-16^{-N_j}
       >=1/(2qQ_j) >=(2q)^{-(1+2b/a)}.

If p/q=A_j, (E7.7)-(E7.8) imply

    |alpha-p/q| >=(1/16)(2q)^{-2/a}.

Here 2/a=4/(1-2epsilon), whereas 1+2b/a=(3+2epsilon)/(1-2epsilon), which is smaller. Thus for every fixed epsilon in this range and all sufficiently large q, every integer p satisfies

    |alpha-p/q| >=(1/16)(2q)^{-4/(1-2epsilon)}.         (E7.9)

Letting epsilon decrease to zero proves that the irrationality exponent is at most four. Normality already guarantees irrationality. Constants and onset in (E7.9) may depend on epsilon and the prescribed schedule; no fixed C q^{-4} lower bound is claimed.

## 6. Exact-forcing changed-selector corollary and boundary

Retain the authentic BBP forcing r and its future Green tail T_n, but choose V_0=(alpha-pi)/16. Then V_n=16^{n-1}alpha-T_n obeys exactly V_{n+1}=16V_n+r(n+1). Its completed carrier is normal and has irrationality exponent at most four, yet the source-authentic energy stability bound

    |E_V(N,M,h)-E_alpha(N,M,h)|
       <= (4 pi |h| B/N)(1+M/N)

preserves the lower limit 1/4 at N=2^j. Thus for every prescribed schedule tending to infinity with M(N)=o(N), normality and finite irrationality type together do not make that moving energy gate necessary, even with the same four-pole forcing at a changed real selector.

The theorem does not disprove a sufficient energy bound at the actual U_0=0 orbit. The changed V_n are generally irrational; no authentic 2-adic U-state is assigned to them. Authentic CRT labels can only be used here as external relabelings of the time-residue partition. This is a genuine strict-implication obstruction, not a pi normality proof or a claim that the auxiliary random-word law generates pi.
