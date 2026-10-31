# Final proof and scope review

The constructor, analytic translator and selected-path adversary each read
the final synthesis and relevant proof dossiers after their initial work.
The root author also checked their formulas, imported implementations and
raw validation receipts. These are three separate same-system reviews,
not blind external refereeing or a formal proof assistant certificate.

## Corrections made before publication

1. The source-identification summary now states the exact class
   `sum_i c_i/(8n-b_i)`: at most four distinct simple poles, no polynomial
   part, clock 8 and the declared node domain. Merely saying “four poles”
   was too broad: a polynomial addition changes the source without changing
   those negative-power moments. The original S4 proof already had the
   correct class.
2. The prime-frame dossier now explicitly extends its principal-part
   alias to retained integral p-adic precision. Multiplying the omitted-
   prime seed by `L=product p^(K_p)` makes its full selected history invisible
   in each retained `Q_p/p^(K_p)Z_p`. The separate source-authentication
   dossier already proved this stronger version.
3. The general flat-shadow theorem now says that all asymptotic coefficients
   are preserved *whenever such an expansion exists*. The general O(n^-2)
   hypothesis alone does not assert an expansion. The authentic rational
   BBP source has the full expansion used in the application.
4. Earlier scope review fixed the general radix to an integer, required
   strict source decrease for the strict relative-error inequality, and
   explicitly specialized rational-boundary claims to u=0. The jointly
   holomorphic source-shift argument remains valid on the complex disk.
5. An overly strict coefficient-positivity assertion in the separate
   prime-frame oracle was corrected as recorded in ORACLE_CORRECTION.md.
   It was an implementation failure, not a failed source sign theorem.

## Independently rederived critical steps

- PF4's explicit diagonal gives an error below `6853/(54000 n^2)`;
  summing the character chord bounds gives exactly
  `6853*pi^3*abs(h)/162000` at every finite horizon.
- The minimal flat shadow has `q=47/240` and constant completed fractional
  part 2/15 for n>=1. Its tail is less than 2/15, proving actual carries
  3,2,2,... without a seam assumption. F8 follows from the rational l1
  tail budget.
- The full spectral expansion and all derivatives have the stated
  convergence domains; the prime-power transport scales the whole pole
  vector and has prefactor q^(-s-1).
- The all-order shadow lies outside the bounded rational-function class.
  It preserves polar data, not the entire analytic function or regular
  Laurent coefficients. No contradiction with finite source recovery
  remains.
- The proposed h=1 macroscopic gap is strictly weaker than normality:
  nonconstant periodic cycles can have a strict first-character gap.
  The target remains open for the authentic source.

The final reviews found no remaining mathematical blocker in the stated
local proofs. That finding is scoped to these reviewed proofs and is not
a claim that the global selected cancellation problem has been solved.
