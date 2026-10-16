# Source-preserving continuation across prime 3 and prime-square 4

**PAPER_PROVED, classical transport applied to the pinned Suzuki source.**
The exact computation below concerns finite low compressions. It establishes
neither high coercivity at a new radius nor any new Schur sign. Source blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178` remains unchanged. The primary
source is [Suzuki, version 3, (1.3)](https://arxiv.org/html/2606.09096v3).
The founding import manifest is a different provenance lineage.

## AR-X1: a common Hilbert carrier with exact metric

For 0<a<=1 let H_a=L²_0(-a,a) with Lebesgue measure and set
U_a f(t)=sqrt(2a) f(2at), t in (-1/2,1/2). Change of variables proves
U_a unitary. The transported convolution kernel is

    g_a(t,s)=2a g(2a(t-s)).

Mean-zero compression commutes with this transport. Physical Legendre modes
P_j(x/a) map to sqrt(2a) P_j(2t), so all low/high polynomial subspaces are
fixed on the reference interval. Physical form entries are divided by 2a
when represented on reference modes P_j(2t); their metric is
W=diag(1/3,1/5,1/7,1/9). Direct substitution in the primitive integral gives

    U_a V_a U_a^-1 = 2a V_ref,    U_a K_a U_a^-1 = (2a)^2 K_ref.

This transports definitions, not a source inequality between different G_a.
In particular the certified kappa at a=1/2 cannot be reused at another radius.

## AR-X2: norm continuity, including arithmetic events

On each bounded displacement interval the infinite real-Gamma screw series
converges uniformly: each summand has absolute value at most 4/(4j+1)^2.
The other signed channels are continuous and the prime-power hinge sum is
locally finite. Hence g is uniformly continuous on [-2,2]. On the unit-area
reference square, with delta=|a-b|, M=sup_[0,2max(a,b)]|g|,

    ||G_a-G_b|| <= ||g_a-g_b||_HS
      <= 2delta M + 2min(a,b) omega_g(2delta).

The same estimate holds after orthogonal mean-zero or fixed low/high
compression. For an explicit computable budget, finite Gamma J has the
source-derived Lipschitz constant L_J supplied by lipschitz_safe, and uniform
kernel tail tau_J=1/(4J+1)+4/(4J+1)^2. Since g_J(0)=0,

    M <= 2max(a,b)L_J+tau_J,
    omega_g(h) <= L_J h+2tau_J.

For any desired accuracy first choose J large enough, then delta small.
The paper theorem allows arbitrary finite J; the executable demonstration
caps J at 128. The bound tends to zero with suitable increasing J, but the
fixed-J displayed budget has a nonzero error floor. No full-kernel Lipschitz
claim is made: its derivative has a logarithmic singularity at zero.

At 2a=log n a genuine hinge enters with zero operator. The separate hinge
theorem gives HS²=w_n²(2a-log n)_+^4/6 and derivative HS²=w_n²(2a-log n)_+².
Thus entry is quadratic in displacement in HS norm and linear in derivative
HS norm. The derivative formula is in the physical coordinate; under U_a
the differentiated transported kernel has norm 2a times that physical norm.
These statements do not yield continuity of a zero-shift Schur short.
The compact changing-cross countermodel in COMPACT_SOURCE_GALERKIN remains
a counterexample to that inference. A positive shift admits separate
resolvent stability; removing the shift needs an authenticated tail modulus.

## AR-X3: actual finite source across the next two events

The exact source program uses existing Legendre correlation/OU integrals,
the real Gamma factor, both pole channels and the contact. It extends the
hinge integration to every genuine active source address, rather than
calling the old first-prime-only low adapter at an invalid radius.

| Radius | Certified active addresses (address, parent prime) |
|---|---|
| 1/2 | (2,2) |
| 9/16 | (2,2), (3,3) |
| 11/16 | (2,2), (3,3) |
| 7/10 | (2,2), (3,3), (4,2) |

For each pair of modes, integrate (r-log n)_+ against the exact correlation
polynomial and multiply by log(p)/sqrt(n). In particular the coefficient at
4 is log(2)/2, not log(4)/2. Logarithms and square roots use outward rational
intervals from the pinned source. Ambiguous endpoint comparisons fail closed.
Endpoint equality gives zero hinge almost everywhere; the executable does
not guess equality from an uncertain interval. Fake primitive composite 6
is refused even where its numerical hinge would be invisible.

The returned low form bracket is

    midpoint - rho I <= P G_a P
      <= midpoint + rho I + tau_Gamma W,

where rho is the maximum row sum of entry radii after unitary scaling and
tau_Gamma=2/(4J+1)^2+16/(4J+1)^3. Positivity of the omitted mean-zero Gamma
operator proves the lower direction; its whole operator norm proves the
upper. This operator tail is not substituted for a derivative tail anywhere.
Exact parity zeros follow from reflection of the complete source. Individual
whole-line cosine factors are not used as finite-interval eigenvalues.

Run `python scripts/cross_prime_wavefront_probe.py --output /tmp/cross.json`.
The retained Gamma64 receipt contains complete rational interval matrices
for all four radii. This is an actual source study beyond prime2, with no
all-test, all-radius, high-coercivity or Schur-sign claim.

## AR-X4: finite-place observers and the common rational source

For q in Q*, unique factorization gives
|q|_infinity product_p p^(-v_p(q))=1. Only finitely many factors differ from
one for each fixed q. The existing exact rational product and additive
character reciprocity interfaces are reused without a new p-adic model.
A uniformly fixed finite prime menu is insufficient on all rational inputs:
choose a prime r outside it. Inputs 1 and r have identical observed
valuations but different real absolute values. With q=7/12 and observed
primes2,3 the partial norm product is7; adding the missing place7 gives1.
The additive global character is separately trivial because the real
rational minus the sum of its local fractional parts is an integer.

Neither reciprocity identity identifies the Gamma normalization or bounds
the Suzuki inverse spectral mass. They constrain the common rational input;
they contain no inequality about D's eigenvectors or the cross columns B*.
No Q_p-to-R convergence as p grows, dynamical resonance, or prime-indexed
eigenmode is asserted. The missing analytic bridge is retained explicitly.
