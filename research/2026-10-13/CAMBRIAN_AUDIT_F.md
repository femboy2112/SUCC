# Auditor F — arithmetic source transport and the RH firewall

**Audited worker:** cluster E, not this auditor's original cluster B. **Original worker commit:** `c2c18c3ed638478448497fb6892a747f67ee6f9b`. **Audit base:** `fb3499dfb6da9bd491bf89d01abe9de716b5d7b5`, clean isolated branch `research/cambrian-audit-f-2026-10-13`. The audit changes only its own script/dossier/receipts. Frozen E source files and their original receipt are unchanged. This is a separate same-model investigator with genuinely different implementations, not a blind external referee or proof assistant.

## Verdict

**PASS, conditional on the declared oracle and source class:** finite causal ramp identification, four-query inversion, formal source reconstruction, strict horizon counterexample, p-adic codomain-sensitive obstruction, and positive self-dual auxiliary-multiplier countermodels. Independent exact calculations survive all tested mutants.

**REVISE one domain statement:** the two-bump construction proving the prime-only form is indefinite requires `a>log(2)/2`. For `0<a<=log(2)/2`, the compressed prime operator is zero. The original worker's bounded-operator and norm-bound claims survive; a universal all-width indefinite-form reading is refuted. This is a paper-scope correction, not an RH flaw or a production-code failure.

**No promotion:** source authentication, standard Gamma/completed-domain identification, full Weil positivity, RH, and an actual Gaussian-prime escape theorem remain unproved. The auxiliary multiplier's off-line roots are not identified as zeros of the actual Riemann zeta function.

## Independent instrument and frozen rivals

Before experiments the auditor froze `CAMBRIAN_AUDIT_F_HYPOTHESES.json`. Preferred hypothesis: the elementary finite theorem is sound under its explicit instrument contract. Rival: finite recovery or a self-dual positive completion was silently being promoted to a completed arithmetic sign theorem. The script independently constructs:

1. Dirichlet-log coefficients through **Omega-graded differentiation**, instead of the tested convolution power-series implementation.
2. Logarithm enclosures through the telescoping identity `log n=sum_(j=1)^(n-1) log((j+1)/j)`, instead of binary argument reduction.
3. Reciprocal-square-root intervals by rational binary bisection of `n*x²=1`, instead of integer-square-root decimal scaling.
4. Tuple interval arithmetic and a finite ramp oracle with no imports of production arithmetic helpers.

Only the clearly labelled differential-check boundary imports the **subject under test**. The audited four-query algorithm and exp helper are never used to generate an oracle or expected source coefficients. Both implementations still share ordinary rational arithmetic and the underlying analytical theorems; their agreement is not unconditional independence.

## F1 — Re-derivation of finite source reconstruction

In the finite Dirichlet-convolution algebra through horizon N, write a(1)=1. Let `Omega(n)` count prime factors with multiplicity, so `Omega(uv)=Omega(u)+Omega(v)`. The grading derivation `D a(n)=Omega(n)a(n)` obeys `D(a*b)=Da*b+a*Db` by divisors and additivity. The finite nilpotent logarithm therefore satisfies `D a=a*D b` for `b=log_*a`.

For each n>=2 this gives the triangular recurrence

`b(n)=[Omega(n)a(n)-sum_(d|n,2<=d<n) Omega(d)b(d)a(n/d)]/Omega(n)`.

Conversely, `a(n)=sum_(d|n,d>=2) Omega(d)b(d)a(n/d)/Omega(n)` with a(1)=1 reconstructs a uniquely. Every denominator is a positive integer; signed or zero rational coefficients require no analytic branch of log. This agrees with finite exp/log because the formal derivative identity holds in their nilpotent power series. The source map is nonlinear in a and linear in b, as stated by E.

The audit runs genuine a(n)=1, fake a(6)=2, and nonunit `a(n)=2^v2(n)` through horizon 40. It reconstructs every prefix exactly and checks the subject exp against this independent result. Genuine coefficients are independently recognized as `b(p^j)=1/j` and zero for non-prime powers. The fake coefficient b(6)=1 is detected; nonunit Euler weights keep prime-power support while violating genuine weights. No label called prime substitutes for the integer factorization predicate.

## F2 — Ramp, Laplace transform, sign, and strict observation horizon

For known actual event positions `ell_n=log n`, normalizer `w_n=log n/sqrt(n)>0`, and finite b define

`F_b(t)=-sum_(n=2)^N b(n)w_n(t-ell_n)_+`, t>=0.

Differentiation in distributions on (0,T) gives `F_b''=-sum b(n)w_n delta_(ell_n)`. If `T>log N`, the atoms have distinct positions strictly inside the domain; smooth disjoint bump tests recover every amplitude, division by w_n recovers b(n), and F1 recovers a. That is an injectivity theorem inside the known finite model class. It is not physical source authentication.

At `T=log N`, the last ramp is zero throughout [0,T]. Replacing b(N) by b(N)+1 changes a(N) but changes no recorded response. This refutes identification at the non-strict horizon even with the entire continuous response known. The audit adds one to b(40), verifies source coefficient a(40) changes, and checks equal exact interval response at four rational times certified below log40. The full endpoint equality is a separate exact symbolic proof, not an irrational time rounded into a certificate.

For a finite source, translate u=t-log n and integrate once by parts:

`integral_0^infinity e^(-zt)(t-log n)_+ dt = n^(-z)/z²`, Re z>0.

Hence `Laplace(F_b)(z)=-z^(-2)sum b(n)log(n)n^(-(z+1/2))`. There is no hidden zero input or analytic continuation. For the full genuine source, the absolutely convergent sum is `-zeta'/zeta(z+1/2)` only when Re z>1/2. Thus **the full ramp transform has sign +zeta'/zeta divided by z²** in that region. The E dossier's displayed finite formula has the correct sign; its reference to the negative logarithmic derivative refers to the positive sum, not the entire ramp transform. No extension into the critical strip was licensed.

## F3 — Four-query inversion, intervals, and mutation discrimination

On gaps between consecutive log events the response is affine. Subtracting the two adjacent gap slopes yields the atom jump `-b(n)w_n`; this proves the four-query formula. For independent bounded query errors of magnitude epsilon, triangle inequality bounds the coefficient error by

`(2epsilon/w_n)(1/gap_before+1/gap_after)`.

The audit's certified rational thirds avoid every event boundary. Both its independently inverted intervals and the subject intervals contain the exact b(n) for **27 source/event combinations**: three source families and n in {2,4,6,8,9,12,16,25,32}. The final readable receipt rounds interval bounds outward using exact denominator 10^15; assertions run on the full rational bounds first.

The shifted-log2 oracle moves the impulse to log3 and the event-2 recovered interval excludes b(2)=1. Wrong n^-1 density instead of n^-1/2 also excludes b(2)=1, independently recovering the scaled coefficient near 1/sqrt2. Large sound query intervals retain the true coefficient but fail the sufficient denominator-100 uniqueness criterion. Each result concerns the **declared normalizer and clock**. None claims that the altered response is an authentic Weil distribution for a different L-function.

For reduced rationals of denominator <=D, separation is at least 1/D², so interval width below that value gives **at most one** admissible coefficient. It gives neither existence nor validation of the denominator prior. E states this distinction explicitly. Oracle soundness, its source identity, coefficient-size bounds, runtime, and physical measurement cost remain separate hypotheses.

## F4 — Clock coherence and topology

Uniform cylinder weights `mu(a+p^r Z_p)=p^-r` satisfy normalization and refinement because the p children each have weight p^-(r+1). As real-valued probabilities they give ordinary Haar measure. As Qp-valued cylinder weights their norm is p^r, so a functional applied to a norm-one cylinder indicator has unbounded output norm as r grows. This forbids a bounded Qp-valued integration functional on the sup-norm continuous functions.

Conversely, uniformly bounded compatible Qp cylinder weights define bounded integration of locally constant functions by the ultrametric inequality; compact uniform continuity makes those functions dense, giving a unique bounded extension. Compatibility alone therefore fails precisely in the stated **codomain/norm**, rather than proving no probability measure or no projective limit exists. The audit verifies twelve finite refinements over p in {2,3,5} and levels {1,2,4,8}; unboundedness is a paper all-level proof.

The direct continuous additive `Z_p->R` obstruction also survives: compact image is a compact subgroup, and a nonzero real subgroup contains an unbounded sequence of integer multiples. Diagonal rational source lifts evade that obstruction by using different embeddings; they do not identify an arbitrary residue with a unique real source.

## F5 — Fresh auxiliary completion multiplier, with DZ8/DZ9 retained

Using the classical Gaussian Fourier identity independently, set `r=9`, `w=4/5`, and

`f(x)=[w exp(-pi x²)+exp(-pi r² x²)+r^-1 exp(-pi x²/r²)]/(w+1+r^-1)`.

The two scaled Gaussians swap under Fourier transform, the central Gaussian is fixed, and all coefficients are positive. Therefore f is a positive Schwartz self-dual function with f(0)=integral f=1. Direct Mellin substitution gives the **auxiliary multiplier**

`C(s)=[4/5+9^-s+9^(s-1)]/(4/5+1+1/9)`.

It obeys C(s)=C(1-s), C(0)=C(1)=1, and the independent exact check gives `C(2)=C(-1)=1987/387`. Put y=9^(s-1/2). The zero equation becomes

`y²+(12/5)y+1=0`, with discriminant 44/25.

Both roots are negative because their product is 1 and their sum is -12/5. Their moduli are `R=(6+sqrt11)/5` and 1/R. The strict inequalities `1<R<3` follow by squaring rational comparisons; equivalently `2<12/5<3+1/3`. Thus the multiplier has roots

`s=1/2 +/- log(R)/log9 + (2j+1)pi*i/log9`, j integer,

strictly inside 0<Re s<1 and off Re s=1/2. At the lower threshold coefficient 2, y=-1 is repeated and the roots lie on the line. At coefficient 10/3, roots -3 and -1/3 reach Re s=1 and 0. These sharp controls are kept in the receipt.

The independent multiplier evaluations recover **DZ8 C_2(2)=3/2** and **DZ9 C(2)=413/188**. These historical negative controls remain live. Multiplying the standard completed function by C produces an auxiliary completion with extra roots while retaining finite Euler factors and pole normalizations. It changes the real test function; **actual zeta and its standard completion are unchanged**. No unknown nontrivial zero locations were read, simulated, or imported. Function positivity and Fourier self-duality are not completed-Weil positive definiteness.

## F6 — Actual primes, operator support, and required revision

The sieve point `(1,30)` has norm 901=17*53, divisible by none of {2,5,13}. Both coordinates are nonzero, so its Gaussian primality would require its norm to be prime. Independent trial division refutes that; more decisively, exact Gaussian multiplication gives `1+30i=(4+i)(2+7i)` with two nonunit factors of norms 17 and 53. A periodic-sieve translation witness therefore remains a sieve witness; it cannot become a Gaussian-prime walk by changing its label. This audit did not prove or refute the external all-step Gaussian-prime theorem.

For the finite compressed prime operator on L²(-a,a), shifts by log n have norm <=1, opposite shifts are adjoints, and the triangle bound `||B_a||<=2sum|w_n|` is valid. But if `2a<=log2`, every prime shift is zero almost everywhere: no two interior points can differ by a shift of at least log2. In particular at **a=1/4**, the independent log2 lower enclosure certifies `2a<log2`, and B_a=0. The two-bump indefinite form cannot exist there.

**Exact replacement wording requested for E30:**

> The finite compressed prime operator is self-adjoint and obeys the stated norm bound. If 0<a<=log(2)/2, it is zero. If a>log(2)/2, choose two equal smooth normalized bumps inside (-a,a) separated by log2 and narrow enough to avoid every other active prime shift. Their compressed prime-form matrix has zero diagonal and nonzero off-diagonal entries, so the prime-only form takes both signs. This does not determine the sign of the completed Weil form.

The threshold is strict because shifts touching only interval endpoints are zero on L². For larger a, two centers fit with positive boundary margins; finitely many distinct active log shifts admit a positive avoidance width, establishing the repaired two-bump construction.

## Primary-source domain check and proof boundary

Opened [Suzuki, *Weil's quadratic form via the screw function*, v3](https://arxiv.org/html/2606.09096v3), especially its introduction and §2.5. Its prime term has the negative signed impulse/shift coefficients used here; its complete distribution also contains distinct archimedean and pole terms. Compact smooth test functions and the full closed form/operator domains are different objects. The audit accepts E's compact prime-side bridge and rejects any silent substitution of its bounded finite shift operator for the entire completed operator.

Opened [NIST DLMF §25.4](https://dlmf.nist.gov/25.4) to check standard reflection/completion normalization. Neither cited source supplies positivity for the newly constructed ramp or licenses identifying C*xi with the actual xi. No unknown-zero representation was used as a construction input.

Written re-derivations provide local analytic proofs; executable assertions provide finite calibrated evidence. There is no new Lean verification or external blind review. Provenance independence is strongest for the algorithmic representations and weakest for shared classical premises. Full completed sign and priority are left UNVERIFIED.

## Reproduction and integration

```sh
python scripts/cambrian_audit_f.py
python -m unittest discover -s tests -p 'test_cambrian_e_arithmetic_transport.py'
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

`CAMBRIAN_AUDIT_F_RESULT.json` contains the source hashes, exact rounded enclosures, independent source coefficients, clock and multiplier controls, and the support-threshold counterexample. `CAMBRIAN_AUDIT_F_VALIDATION.json` preserves actual command outputs. The original worker commit and its frozen receipt must remain unchanged; apply the requested one-sentence domain repair in a separate integration commit. No shared ledger/CI files were edited and no push was attempted.
