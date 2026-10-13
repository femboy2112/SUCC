# X06 independent review: C24, F45, and the typed resource bridge

Base reviewed: `71eaf11e48ca3ccb349858bba64abf36b59ee6f5`. This investigator did
not implement the A/B/C/F cohorts and did not change their files.

## C24

The statement is correct for every nonempty finite source map. The proof uses
a lower bound on every fiber and a matching fiberwise numbering; it does not
silently replace maximum fiber with mean fiber, entropy, or source cardinality.
The implementation returns exactly that numbering. The new independent oracle
searches candidate label assignments directly for 430 finite maps and reproduces
the optimum and injectivity in every case.

The phrase reversible realization must retain C24's formal definition:
injective encoding into output times auxiliary memory. Full ambient products
can have different cardinalities, so no bijection between those products is
implied. X06 gives bijections only between reachable encoded images and states
the extra obligations for circuit/physical models. A report register containing
an erased bit can reduce residual auxiliary memory to one label; that register
itself is retained information and cannot disappear from total storage accounting.

C24's source theorem is therefore **PROVED LOCAL, independently survives**.
The thermal equality and its initially correlated countermodel were read, but
no new thermodynamic verification is claimed by this finite-map assignment.

## F45

The telescoping proof is correct for positive rational parameters, including
the strict boundary. For r<a, the service partial sums approach b/(a−r) from
below; equality does not cross at any finite stage. The r=a case has a linear
normalized sum, and r>a has a divergent positive geometric sum.

The independent audit uses the distinct explicit formulas

    a^n D₀ − b(a^n−r^n)/(a−r),                 a != r,
    a^n D₀ − n b a^(n−1),                    a = r.

All 3,328 values agree with the iterative implementation. Of 256 tested
parameter tuples, 194 have a concrete finite nonpositive term. The other 62
have a certificate a>r, D₀−b/(a−r)≥0 and b/(a−r)>0, which makes the exact
closed form a sum of a nonnegative and a positive term for every finite n.
This last conclusion is an algebraic proof from the parameter inequalities,
not inference from a finite no-crossing search.

`debt_stages` returns the unconstrained recurrence even after the first
nonpositive term. This is useful algebra but its negative continuation is not
an operational claim that completed tasks execute further debt steps. The
original dossier explicitly stops the operational process at first completion.

The recurrence result is **PROVED LOCAL, independently survives**. Its use
as a universal model of knowledge or storage growth remains unsupported. The
new one-reset/identity control has constant residual memory debt, and B16's
source-state quantity admits independent controls in both directions. These
do not refute F45's explicitly posited model; they refute identifying its
premises with other resource invariants without a proved map.

## New combined theorem and limitations

The weighted composite-fiber identity is exact. The common-buffer construction
colors final fibers, which also separates every preceding finer fiber. Both
proofs use the same original index throughout. A purported sequence that
splits an erased endpoint fiber without a retained original-access register
fails the deterministic-map premise and is rejected by the implementation.
The separate regression for report deletion confirms that losing the record
restores the buffer requirement.

Composition carries subadditive logarithmic rank, not additive consumption.
Minimal surjective countermodels and 38,084 exact pairs discriminate these
claims. The common-buffer existence theorem may inspect the complete known
finite program; it proves neither a future-oblivious online algorithm nor an
optimal circuit for a restricted gate set.

The mathematical labeling also requires original access at encoding time or
an initially injective preparation. If e₀ already merges originals and the
observer can initialize only m=k e₀, the pair (e₀,m) cannot distinguish any
merged pair. The complete-program buffer theorem is not a method for recovering
information unavailable to the observer at the initial stage. This boundary
is explicit in the dossier and has an exhaustive two-original negative control.

Actual validation: eight new regression tests passed, and the independent
probe completed all checks before saving `X06_RECEIPT.json`. No failed proof
candidate was deleted: strict product/additivity failures remain explicit
countermodels. No source correction was needed. No full suite, web priority
survey, Lean verification, or physical experiment was performed by X06.
