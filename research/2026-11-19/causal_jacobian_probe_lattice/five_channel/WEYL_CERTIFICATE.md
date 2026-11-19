# A rational certificate for the fixed signed Weyl probe

**Scope:** one finite chronological shell of the authenticated source, with
explicit arithmetic error. No floating-point value is used to certify a sign,
threshold, source digit, or statistical assertion.

## 1. Preregistration and sampling

The committed configuration099e36d0 fixes `B=131073`, all `B` indices
`n=B,...,2B-1`, modes `(1,7,11,15,720885,117440505)`, phase width16 hex digits,
table grid4096 and scale `2^44`. This shell is beyond the previously inspected
prefix through131072. Prime repair does not delete or reweight its indices.

The finite stress target is `abs(W_B(h))<=1/16` at every fixed tested h, with
the separate one-sided mode1 threshold `Re W_B(1)<=15/16`. These are finite
predictions. Failure does not refute normality or R0; success does not prove
them. An interval crossing a threshold returns AMBIGUOUS rather than guessing.

## 2. Source prefix from the original BBP law

The unchanged `observational_succ/bbp_spatial_haar_lift.py` builds an outward
integer enclosure using `duck_bbp.forcing`. For requested prefix length L and
guard24, let K=L+24 and

\[
A=\sum_{j=1}^{K}\left\lfloor16^{K+1-j}r(j)\right\rfloor.
\]

Every rounding loss is less than1. The original positive decreasing source tail
after K contributes `T_K<r(K+1)/15<1` in these units. Therefore

\[
A\le16^K\pi<A+K+1.
\]

Matching the requested hexadecimal cells of both endpoints certifies the
prefix. Otherwise the code fails and requires more guard precision. No oracle
for pi is supplied. The current run constructs262161 fractional hex digits
using262185 original source terms. The prefix SHA-256 is
`f9d6043183d523155ad6a04c1aa54a500abc7e830cb0df3eaa6f080f03032cec`.

For `Y_n=16^(n-1)pi`, width w=16, and q=16^w, the word starting at prefix
index `n-1` gives a rational phase approximation `u_n=word/q` with circle error
less than `1/q`. Index zero is the first fractional digit of pi. Seven small
positions are independently checked against exact rational U_n plus paid tails.

## 3. A trigonometric table with a proof of its error

Machin's identity is `pi=16 atan(1/5)-4 atan(1/239)`. It follows from tangent
addition and the range `0<4 atan(1/5)-atan(1/239)<pi/2`; that angle has tangent1.
For each arctangent, adjacent alternating-series partial sums give an exact
rational interval. Sixteen terms suffice for the declared table precision.

Let `[pi_-,pi_+]` be this interval, and p a dyadic approximation with certified
error `epsilon_pi=max(abs(p-pi_-),abs(p-pi_+))`. For
`0<=j<Q/4`, use the rational argument `t_j=2p j/Q`, which lies in[0,2).
Evaluate cosine through degree24 and sine through degree25, exactly as rational
polynomials. Taylor's theorem bounds each remainder by `2^25/25!`; the degree25
sine remainder is smaller. Replacing pi by p costs at most `epsilon_pi/2` in
each component. Flooring the two polynomial values at scale S=2^44 costs less
than1/S. Extend the quarter table by exact signed quadrant symmetries.

Thus a table entry at grid point j/Q differs in each signed component from
`e(j/Q)` by at most

\[
E_{table}=\epsilon_\pi/2+2^{25}/25!+1/S.
\]

This table is checked against a separate full-angle rational Taylor algorithm
using a BBP-derived pi interval, so the audit does not merely repeat Machin's
formula or the same quarter-table implementation.

## 4. Phase quantization and complete signed averages

For each fixed integer h, compute the table index

\[
j_{n,h}=\left\lfloor Q\frac{h\,word_n\bmod q}{q}\right\rfloor.
\]

The circle character is globally Lipschitz with constant `2pi|h|` before
multiplication by h, and constant2pi after it. Branch crossings cause no extra
discontinuity for this circle-valued comparison. Since `2pi<44/7`, each signed
component error is at most

\[
E_h=E_{table}+\frac{44}{7}\left(\frac1Q+\frac{|h|}{q}\right).
\]

The code sums signed table integers over **every chronological sample**, divides
by `BS`, and places a rational interval of radius E_h around each component.
The largest possible squared modulus in the resulting rectangle is computed
with exact rational squares. Comparing it with1/256 certifies the finite
modulus threshold. The displayed decimal midpoint is not used in that decision.

For a decimal upper bound with denominator10^6, choose the smallest integer t
such that `(t/10^6)^2` dominates the rational squared-modulus upper bound. This
is why the summary's upper bounds are outward, even though their decimal
presentation is shorter than the underlying exact intervals.

The raw source mean `B^-1 sum e(hU_n)` differs from the completed mean by at most
`(44/7)|h| r(B+1)/15`. This separate debt is included in the raw-source component
intervals. High-frequency completed and raw means are not silently identified.
The two large modes correspond to the old corrected-lag characters on U_n.

## 5. Calibration and finite boundary

The positive finite calibration is a complete uniform grid whose signed means
vanish for the declared odd frequencies. A locally locked chart is accepted
when its compensator is retained. Omitting that compensator turns the display
into the negative all-one control and is detected. Other controls preserve the
255-point lag-bank blind spot, a factorial cold shell, and biased sample selection.

The independent implementation additionally catches an off-by-one source index
and a reversed Fourier sign. The complete source prefix, exact signed intervals,
configuration hash, and audit receipts are retained. None of these finite
objects supplies the missing uniform all-large-B estimate.
