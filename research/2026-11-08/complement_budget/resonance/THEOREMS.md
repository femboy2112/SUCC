# Resonance must obey the source cocycle

**Status: PROVED PAPER for the stated finite hypotheses. Pi normality and RH: OPEN.**
This front supplies a quantitative restriction on models of the actual folded
complement. It does not prove that the remaining affine resonance decays.
No external novelty, external refereeing, or Lean certification is claimed.

Use the authenticated source and original boundary exactly:

```
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
U_0=0, U_n=16 U_(n-1)+r(n), e(t)=exp(2 pi i t).
```

Let p=1 mod8 be prime, L=(p-1)/4, n0=L+1, m=ord_p(16),
q=L/m, and I={n0,...,n0+L-1}. The pinned PE1--9 source identity gives
`x_n=p[U_n]_p=xi*16^(n-n0) modp` throughout I, where
`xi=4*16^(n0-(p+7)/8) modp`. Thus m divides L. The actual p-principal
part is `x_n/p`; it is not the reduction of a floating real phase. Fix an
integer h and set

```
a_n=e(h*x_n/p), b_n=e(h*(U_n-x_n/p)),
B_r=(1/q) sum_(j=0)^(q-1) b_(n0+r+jm), 0<=r<m.
```

All norms and averages below are normalized finite counting norms. No seed
ensemble is used. A *unit chirp model* has the form
`v_r=kappa e(P(x_(n0+r))/p)`, where |kappa|=1 and P is reduced modulo
`X^m-xi^m` before its degree is read. Let
`rho=mean_r |B_r-v_r|`. The scalar kappa is an explicitly retained common
phase anchor; independent phase rotations at different r are forbidden.

## CR1. Exact lifting of a unit folded model

For every such unit v, repeated periodically on I,

```
E_I |b_n-v_n|^2 = 2-2 Re E_r[B_r conjugate(v_r)] <= 2 rho.      (CR1)
```

**Proof.** Expand the squared modulus using |b_n|=|v_n|=1, then average
replicas. Since `Re[(v_r-B_r)conjugate(v_r)] <= |v_r-B_r|`, the inequality
follows. In particular, approximating the folded mean by a unit value also
forces its individual source replicas to align. This step fails for models
whose modulus is appreciably below one; that is a load-bearing restriction.

The source has the exact interior cocycle

```
b_(n+1)=b_n^16 e(h r(n+1)),   n0<=n<n0+L-1.                (CR2)
```

Indeed `x_(n+1)-16 x_n` is an integer multiple of p on this clean interval,
so removing the principal part changes the lifted recurrence only by an
integer. The recurrence is not extended across the next p-pole.

Write `f=2 pi |h| r(n0+1)`. It bounds `|e(h r(n+1))-1|` throughout the
interior. To verify monotonicity without an asymptotic approximation,

```
r(n)=int_0^1 x^(8n-8) (4-2x^3-x^4-x^5) dx,
4-2x^3-x^4-x^5=(1-x)(4+4x+4x^2+2x^3+x^4)>0 on [0,1).
```

Hence r(n) decreases strictly, and
`0<r(n)<=15/[(8n-7)(8n-6)]`. This also proves f tends to zero for fixed h.

## CR2. A positive approximation floor for every low-degree nonlinear chirp

Suppose `2<=d=deg P<m`, and put

```
delta=min(1,d sqrt(p)/m),
t=[ sqrt(max(0,2-2delta-4/L))-f ]_+.
```

Then, for the actual original folded complement and every global anchor kappa,

**`rho >= t^2/578`.**                                      (CR3)

Consequently, on any sequence of covering clean source clocks with
`p->infinity` and `d sqrt(p)/m->0`,

**`liminf rho >= 1/289`.**                                 (CR4)

In particular, an accurate single nonlinear unit chirp of degree within
PR8's vanishing arithmetic budget is impossible. This theorem constrains
approximation, rather than assuming approximation from a local character
bound. It applies even when P and kappa are chosen adaptively after seeing
all source data.

**Proof.** Put `D(X)=P(16X)-16P(X)` in F_p[X]. Its leading coefficient is
the leading coefficient of P multiplied by `16^d-16`. This factor is nonzero:
`1<=d-1<m`, whereas 16 has order m. Thus D has degree d. PR3, with its
explicitly declared Weil import, gives

`|E_r e(D(x_r)/p)| <= delta`.

The squared cycle defect of v is therefore

```
E_r |v_(r+1)-v_r^16|^2
 =2-2 Re[kappa^(-15) E_r e(D(x_r)/p)] >=2-2delta.          (CR5)
```

The same average over L source times consists of q identical cycles. Its
last term is the only one without an interior source recurrence, and is at
most 4. Thus the L-normalized squared defect on the L-1 legitimate edges is
at least `max(0,2-2delta-4/L)`.

On each such edge, triangle inequality and (CR2) give

```
|v_(n+1)-v_n^16|
 <= |v_(n+1)-b_(n+1)|+|b_n^16-v_n^16|+|e(h r(n+1))-1|
 <= |v_(n+1)-b_(n+1)|+16|b_n-v_n|+f.
```

The second inequality follows by factoring z^16-w^16 for unit z,w. Apply
Minkowski to the finite L-normalized edge norm. Each shifted error norm is
at most the full error norm in (CR1), giving

`sqrt(max(0,2-2delta-4/L)) <=17 sqrt(2rho)+f`.

Rearrangement proves CR3, including the positive-part and zero cases. Under
the asymptotic hypotheses its right-hand side tends `2/578=1/289`. QED.

**Scope.** The bound is conservative, not sharp. It does not cover arbitrary
complex sums of many chirps, arbitrary subunit amplitude models, or degrees
whose reduced degree equals or exceeds m. Quotient aliases such as
`P=-hX+(X^m-xi^m)Q` reduce to the affine exception and must not be classified
as nonlinear. The bound is a source-dynamic restriction, but it is also true
for rational same-forcing seeds whose denominators avoid p and hence retain
the same clean principal parts. It does not select literal zero by itself.

## CR3. The affine exception retains exactly the expected fixed-phase anchors

For `v_r=kappa e(c*x_r/p)`, c any residue, the same proof yields

**`|1-kappa^15| <=17 sqrt(2rho)+f+2/sqrt(L)`.**              (CR6)

**Proof.** The exact full cycle defect is the constant
`|1-kappa^15|`. Completing the interior defect norm adds at most `2/sqrt(L)`
by the triangle inequality on the omitted coordinate, then apply the
preceding edge estimate. QED.

Thus if rho tends to zero, kappa must approach the set of fifteenth roots
of unity. This is a restriction on the common anchor, not on the slope c.
A polynomial intercept can always be absorbed into kappa; claiming that its
formal constant coefficient must vanish would be a gauge error.

For c not equal to -h modp, PR3 bounds the actual mean by

`|W_I| <= rho + sqrt(p)/m`.

For the retained resonant slope c=-h, instead

**`|W_I-kappa| <= rho`.**                                  (CR7)

Both follow by multiplying B-v by a and averaging. CR7 explains why a good
model of this exceptional kind preserves a strong signal rather than proving
normality.

These surviving anchors are genuine hostile mechanisms. For fixed h!=0 and
k in Z, set `theta=k/(15h)` and the real same-forcing seed
`s=theta-pi/16`. The exact Green identity gives

`e(hU_n(s))=e(k/15) e(-hT_n)`.

Indeed `(16^n-1)/15` is integral. Since T_n tends to zero, the h-character
converges to the fifteenth-root anchor. For h=1 these are the familiar fixed
completed circle orbits k/15; for general h they are fixed only after the
h-character observation and need not be fixed circle states. These irrational
seeded states do not have canonical rational p-principal parts. They are
real forcing controls, not a claim of matching the full arithmetic source.
The finite oracle separately uses rational matched seeds that do preserve
the selected principal parts and make the c=-h, kappa=1 model accurate.

## CR4. The exact approximation tradeoff is not a new resonance-decay proof

For any unit chirp v=kappa conjugate(a), CR1 reads exactly

`E_I |b-v|^2=2-2 Re[conjugate(kappa) W_I]`.

Optimizing the common anchor gives `2-2|W_I|`. Consequently, estimating the
resonant coefficient by this projection merely measures the original Weyl
mean. It cannot serve as an independent premise proving its own decay.
The new paid theorem here is CR3's *nonlinear-model exclusion* and CR6's
*anchor restriction*. The affine inverse slope's original-zero amplitude
remains OPEN, as do useful multi-atom approximation errors.

## Dependencies and falsification opportunities

- Source/clean clock: PE1--9 at the pinned prior dossier; canonical forcing
  from `observational_succ.duck_bbp`; no frozen source file was edited.
- Polynomial character bound: PR3 in
  `../../signal_frontier/prime_resonance/THEOREMS.md`, inherited with its
  source-pinned classical import. This front adds no external analytic input.
- `oracle.py` independently checks actual source cocycles as rational
  congruences, tests interval-enclosed model errors, and checks a rational
  same-forcing coherent control. The implementation reuses the audited
  outward phase primitive; this is not independent provenance of that primitive.
- The sharpness target is to improve 17 or replace the single unit chirp by
  a dynamically closed model class. The present constant is not claimed optimal.
- The decisive arithmetic target is still an original-zero bound on surviving
  affine resonance, or a multi-atom approximation with controlled residual
  and weighted degree. No such decay is established here.
