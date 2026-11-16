# What drops out when causal volumes reach negative order

**Research continuation of [draft #637](https://github.com/femboy2112/SUCC/pull/637).**
Parent `55bcde3d0c5ceb47d50cb499bd39f4a97c96bfc5`; original four poles,
radix 16, and selected zero seed preserved.

The user's proposed connecting structure has a precise realization:
Gamma-normalized positive-time volumes extend to a holomorphic group
of signed causal distributions. Their negative integer orders are
derivatives of the Dirac delta. The *full original BBP source* also has
a causal convolution inverse, including its exact endpoint atoms and
decaying memory. Neither construction requires negative-time support.

The suspected connection from `Gamma(k+2)` to negative integers is real,
but its zero pattern is now determined exactly. A BBP causal face of
depth `k` has the `k+1` simple real zeros `0,-1,...,-k`. Infinitely many
faces, after a stated normalization, converge locally uniformly on the
entire complex plane to `1/Gamma(s)`. This produces all nonpositive
integer zeros. Zeta's *even-only* pattern instead comes from the
reflection parity of its own positive counting kernel; the authentic
BBP source does not possess that parity.

## Main results

| Result | Scope and evidence |
|---|---|
| `Phi_s=t_+^(s-1)/Gamma(s)` continues to `Phi_-m=D^m delta` | Classical distribution-valued entire convolution group; CN-01 |
| Forward atoms construct `D^m delta` | Exact signed binomial stencil; smooth-test error `mhM/2`, noise gain `2^m/h^m`; CN-02 |
| Full source convolution inverse | `J=delta''/15+59 delta'/225-164 delta/3375+Hk`, with exact rational transfer for `k`; CN-03 |
| Negative Mellin values read boundary derivatives | `Z_f(-m)=(-1)^m f^(m)(0)`, with explicit subtraction and domains; CN-04 |
| Native BBP family has one real zero | Only `s=0`; at `-2` its value is `-112`, and every negative real value is strictly negative; CN-05--06 |
| Face Gamma shape determines a consecutive zero block | `B_(z,k)(s)=(s)_(k+1)L_(z,k)(s)`, with `L>0` on all real `s`; CN-06 |
| Convolution shape `Gamma(2j)` has its own exact block | Real zeros `0,-1,...,-(2j-2)`; first negative contact `-15^j`; CN-07 |
| Infinite face limit recovers reciprocal Gamma | With `A_k=log(k)/8`, `A_k^(1-s)B_k(s)/B_k(1) -> 1/Gamma(s)` locally uniformly; CN-08 |
| Zeta parity is a separate source identity | `1/(e^t-1)+1/(e^-t-1)=-1` gives `zeta(-2n)=0`; a positive perturbation breaks the implication from Gamma alone; CN-09 |
| Universal causal faces construct eta and zeta | Inherited positive Pascal/Hasse grade averaging gives `1/(e^t+1)`; the same averaging on authentic BBP faces gives value 8 at -2, preserving the source distinction; CN-09 |
| Density/compactness and integer samples are insufficient alone | Explicit lost-information map, analytic rivals, and noise amplification; compact-group recurrence is stated with its extra hypothesis; CN-10 |

## The most useful exact rule

If a positive kernel admits

$$f(t)=t^r\int_{\lambda\ge c>0}e^{-\lambda t}\mu(d\lambda),$$

where `r` is a nonnegative integer and the positive rate measure has
every polynomial moment, then

$$\frac1{\Gamma(s)}\int_0^\infty t^{s-1}f(t)dt
=(s)_r\int\lambda^{-s-r}\mu(d\lambda).$$

The right factor is entire and strictly positive on the real axis.
Thus the real zeros are exactly `0,-1,...,-(r-1)` when `r>=1`;
there are no real zeros for `r=0`. The same endpoint order yields the
positive Laplace zoom `Gamma(r+1)`. This makes the relation between
causal volume, Gamma shape, and negative-order zeros an exact rule.

## Review and reproduce

- [Literal forward paths through the companion solenoid construction](CONCURRENT_SUSPENSION.md), reviewed from concurrent [draft #638](https://github.com/femboy2112/SUCC/pull/638); its code and test counts are separate.
- [Complete proofs CN-01 through CN-11](THEOREMS.md).
- [Hole contract and discriminating probes](HOLE_CONTRACT.md).
- [Classical and repository provenance](PROVENANCE.md).
- [Claim ledger](CLAIM_LEDGER.json).
- [Validation receipts and actual counts](VALIDATION.md).
- [Next source-preserving dependency cut](NEXT.md).
- [Constructor proof and inverse audit](CONSTRUCTOR_NOTES.md).
- [Adversarial controls](ADVERSARY_NOTES.md).
- [Independent translation and limit proof](TRANSLATION_NOTES.md).
- [Exact forward-difference, Mellin, and heat-jet code](../../../observational_succ/causal_negative_orders.py).
- [Exact full-source inverse code](../../../observational_succ/bbp_causal_inverse.py).

The general fractional-calculus results and positive source semigroup
are classical/inherited. The explicit negative-depth interface, source
real-zero classifications, and normalized face limit are proved here;
scholarly novelty has not been established. Computation is a finite
audit of the proofs. No physical sampling or reverse-time mechanism is
asserted. The original chronological phase/carry estimate, pi normality,
and RH remain open.
