# Closing delta audit: 97c7433 to 9ff8544c

## Pin and scope

Latest fetched branch head inspected:
`9ff8544c799b5e4c8eb1db33127438bc3f221045` on
`origin/research/pi-normality-crucible-frontier-2026-11-17`.
Comparison base: `97c7433371feca631991a1b8227b656e92e4abcb`.

This is a read-only delta audit. The new head includes merges of the earlier
Pro dossier at `1d33174c39625b39b54d49533b2aac028952d3ec` and the sister
wavelet/Pascal/Gamma branch, followed by new FQR material. Consequently the
large aggregate diff is not all newly authored mathematics.

No donor files, refs, or worktrees were modified. No test suite was run.
The parent and prime-arithmetic agent are separately auditing FQR arithmetic;
this addendum focuses on persistence of the original findings and FQR-10's
analytic/source-control claims.

## Original findings remain at the latest head

The original manuscript is byte-for-byte unchanged, Git blob
`379c014f8ebdf7df82d433f26659660942fa1bbf`.
The code delta only appends new functions; the original character and shadow
functions are unchanged. Thus the previous exact audit still applies:

| Finding | Latest status |
|---|---|
| Wrong first-log sign in ANC7 | Uncorrected; null-seed conclusion remains repairable |
| ANC13 confuses `4 alpha_3` with `4(alpha_3-alpha_4)` | Uncorrected on the eight-dimensional domain |
| ANC14 permits positive integer poles of `h` | Domain gap uncorrected |
| ANC12 says reduced denominator is preserved | Still false at `B=3`, where the shadow loses factor `3` |
| ANC12 says `16^B Pi_star < Q` for every `B>=2` | No finite-to-all-B repair in that manuscript |

The validation document removed the old sentence claiming that `log Q_N/N`
convergence was "verified through N=80" and that the shadow-fit inequality
was verified for all `B>=2`. This is a real receipt change. The new FQR paper
separately attempts a proof of reduced-denominator growth using the prime
survival machinery; that must be assessed as a new argument, not ignored
because the older manuscript was wrong. Even a valid asymptotic gives only
eventual fitting without an effective finite threshold check, and does not
repair the exact-denominator counterexample.

Latest blob pins:

| File | Blob |
|---|---|
| `observational_succ/adelic_bbp_normality_crucible.py` | `beddee1e63137466e6ebd6f46d2b509816556331` |
| `tests/test_adelic_bbp_normality_crucible.py` | `bf9799c912bcdc6f1954286c8f017dcc5589e18d` |
| `ADELIC_BBP_NULL_SEED_VALIDATION.md` | `e63e159356e981836e06750aca67d777c395962e` |
| `FERMAT_QUADRATIC_RECIPROCITY_SELF_DUALITY_AND_RAMIFIED_CARRY.md` | `460495d29d184148ff46ac2ef20b613b0ccd6734` |

The latest validation now reports **25/25** focused tests, `2.875s`, and
additional merged suites. Those are donor-reported runs, not runs performed
by this audit. The historical 15-test receipt remains attached to 97c7433.

## FQR-10: the backward-seed assertion about H-01..03 is false

The new manuscript asserts that H-01..03 have backward seed `-q != 0`.
Their explicit meromorphic extension is instead

\[
\widetilde r_{\rm mer}(z)=r(z)+F(z),\qquad
F(z)=\sum_{n=M+1}^{\infty}\delta_n e^{-(z-n)^2}
\operatorname{sinc}(\pi(z-n)).
\]

At every nonpositive integer `k`, all indices `n` are distinct from `k`.
Each sinc factor is exactly zero. Local uniform convergence is proved in
H-03, so

\[
F(k)=0\quad(k\le0),\qquad
\widetilde r_{\rm mer}(-m)=r(-m)\quad(m\ge0).
\]

The 2-adic backward seed is therefore well-defined on these rational integer
values and satisfies

\[
\boxed{\sum_{m\ge0}16^m\widetilde r_{\rm mer}(-m)
=\sum_{m\ge0}16^m r(-m)=0,}
\]

using the repaired authentic null-seed theorem. It is not `-q`.

This does **not** give a common analytic function on `Z_2`, or show that the
positive integer forcing values are all 2-adically integral. H-03 explicitly
provides a complex meromorphic extension and does not promise a 2-adic
analytic clock. Those properties must remain distinct.

FQR-10 also describes the construction's superexponential error tolerances
as if they were the actual perturbation terms, and infers a quadratic
2-adic valuation asymptotic. A real upper bound on rational errors does not
establish their 2-adic valuations. No derivation of that asymptotic for the
actual truncation-defined H source is supplied. The new test suite does not
test the H backward-seed claim; its FQR-10 test covers only GG and GSC.

## Other controls and limits

- GG's winding erasure changes the original late-shell 2-adic residue when
  its gauge shift is nonzero. If the original terminal word is already zero,
  the chosen erasing shift is zero. An unconditional assertion that the shift
  is always nonzero needs another argument; it does not follow from its
  definition.
- GSC is a genuine rational coboundary perturbation with backward seed
  `-delta_B`; unlike the H extension, that conclusion follows by a legitimate
  two-sided rational telescoping identity. This additional invariant can
  reject GSC. It does not refute the theorem GSC established about positive
  moment closeness and source-labelled observer data alone.
- None of these older hostile controls claimed to preserve the entire
  authentic 2-adic analytic clock. Showing that stronger source data
  distinguish a counterfeit is useful discrimination, not a refutation of
  the old conditional no-go statement.
- FQR-01's asserted valuation range `v_p(U_N) in {-1,0}` is too narrow:
  `U_1=47/15`, `p=47` gives valuation `+1`. The valid elementary consequence
  is `v_p(U_N)>=-1`, or denominator exponent in `{0,1}`. This exact issue was
  also independently noticed by the prime-arithmetic agent.

## New instruments and mathematical verdict

FQR-08's grid calculation is consistent with the Fourier normalization:
when `9|N`, only frequencies divisible by `N` survive, and the sine term
vanishes, yielding exactly

\[
\mathcal V_N^{\rm grid}=\frac{576}{417605N^4}.
\]

FQR-09's Fejer lower bound

\[
\mathcal V_N\ge(c_\star^\sharp)^2
\frac{M-N}{N(M-1)^4}\quad(M>N)
\]

is a valid instrument refinement. Its claimed `4N/3` bandwidth is
asymptotically optimal for this relaxed bound, not an exact finite-integer
optimization; the implementation uses `floor((4N+3)/3)`, which differs from
`ceil(4N/3)` when `3|N`. The inequality itself survives that choice.

The original-source R0 and full-normality targets remain explicitly **OPEN**
in the new paper. The new CRT/fiber description, even when repaired and
proved, must still exclude low-domain-wall authentic words. Knowing that a
word lies in a subexponential list does not by itself do so, and multiplying
the word by a shell-dependent odd cofactor requires a proved transport of
any proposed domain-wall lower bound back to the original word.

Historical audit findings should be cited at 97c7433, with the latest-head
status supplied by this addendum. This review does not promote the FQR
prime-survival or ramified-carry claims beyond the separate arithmetic audit.
