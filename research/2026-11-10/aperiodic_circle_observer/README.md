# Aperiodic circle observer: finite rules, infinite execution

**Round V.** The circle/line observer now has an all-time nonreturn proof,
an executable certificate against every proposed repeating tail, a maximal-run
compiler, and finite rational probes that distinguish its normalized states.
This is a productive computation with unbounded integer registers. There is
no prescribed final arrow.

The preceding [geometric construction](../circle_line_lr_observer/README.md)
supplies the circle, line, Euclidean metric and rational interval source.
This round strengthens what the resulting execution can prove about itself.
The code consumes those exact geometric bounds; no numerical pi constant or
precomputed digit table supplies its answers.

## 1. The result

Let `w=w_0 w_1 ...` be the certified L/R stream for geometric pi, starting
with the Farey bracket `[3,4]`. All indices below start at zero.

**Theorem, within the stated classical domain.**

1. Every next-arrow request finishes after finitely many rational operations.
2. At completed source/output transitions, the semantic pair of rational
   intervals never returns to a previous value, even with all counters removed.
3. The normalized real residuals at successive output states are pairwise
   distinct. The output is not eventually periodic:

   \[
   \forall N\ge0\ \forall p\ge1\ \exists n\ge N:\quad w_n\ne w_{n+p}.
   \]

4. There is a total finite algorithm taking `(N,p)` which first produces a
   rational certificate and finite output deadline, then produces a mismatch
   witness before that deadline. Deadline construction reads exactly the
   first `N+p` arrows and no later arrows.
5. Every maximal constant-letter run is computable as a natural number
   without expanding its individual arrows. Every finite family of normalized
   states can be distinguished by a computable finite family of rational
   threshold observations.

The productivity statements use irrationality and the proved source bounds.
Residual distinction and rejection of every periodic tail use nonquadraticity;
the classical transcendence of pi supplies it. Accepted individual rejection
certificates use only finite rational arithmetic and the source theorem.
The proof of their universal existence retains the classical dependency.

The proofs are written mathematical arguments, not new proof-assistant
formalizations. The [claim ledger](CLAIM_LEDGER.md) and
[validation record](VALIDATION.md) keep universal arguments and finite runs
separate.

## 2. Run it

From the repository root:

```sh
cd research/2026-11-10/aperiodic_circle_observer

# A finite certificate against the proposed tail beginning at22 with period1.
python aperiodic_observer.py period --start 22 --period 1

# Stop after constructing the deadline: do not read the future output.
python aperiodic_observer.py period --start 22 --period 1 --plan-only

# Finite observations of productive streams.
python aperiodic_observer.py runs --count 48
python aperiodic_observer.py pinbed --states 0,6,21,22,100,314,512,1024

# No preset horizon: one certified object per JSON line.
python aperiodic_observer.py periods --forever
python aperiodic_observer.py runs --forever
python aperiodic_observer.py transitions --forever

# Independent finite replay, hostile controls and bound checks.
python -W error aperiodic_probe.py --output audit_receipt.json
python cycle_independent_probe.py
```

`--source rotations` uses the independently derived rational-rotation name
of the same geometric number. The default is the beta-matrix source.
`--extra 8` means eight fixed source refinements after the first successful
polynomial separation; this sharpens the practical deadline. It is selected
before examining any future output. `--extra 0` is also mathematically valid.

`periods --forever` enumerates `(N,p)` by increasing `N+p`. Each request
terminates, so each candidate eventually receives its rejection certificate.
This is a fair sequential enumeration; no uniform small latency or bounded
memory claim is made. Closing a finite consumer's pipe stops the stream cleanly.

## 3. A proposed cycle becomes a polynomial

Write a current bracket and its endpoint matrix as

\[
J=[a/b,c/d],\quad bc-ad=1,\qquad
E=\begin{pmatrix}a&c\\b&d\end{pmatrix}.
\]

For the first proposed block `v=w_N...w_(N+p-1)`, multiply its L/R matrices
to obtain `W`. Hypothetical repeated cylinders have endpoint matrices `EW^r`.
Their unique limiting value `xi_v` is fixed by

\[
F=EWE^{-1}=\begin{pmatrix}A&B\\C&D\end{pmatrix}.
\]

Hence the proposed infinite cycle carries the exact integer polynomial

\[
\boxed{P_v(X)=CX^2+(D-A)X-B.}
\]

Mixed blocks give quadratic candidates. Pure blocks converge to a rational
endpoint, so their canonical certificates use `bX-a` for `L^p` and `dX-c`
for `R^p`. This avoids an unnecessary squared polynomial and its weaker gap.

Refine the circle interval `I_k` until the **exact** range `P_v(I_k)` excludes
zero. Quadratic range evaluation includes an interior vertex when present.
Let `epsilon>0` be its distance from zero, and put

\[
M=\max_{x\in J}|P_v'(x)|,
\qquad \Delta=\epsilon/M.
\]

The mean value theorem gives `abs(pi-xi_v)>=Delta`. Compute the least `r`
for which the hypothetical cylinder width satisfies

\[
|J_r|=1/(b_rd_r)<\Delta.
\]

Both the periodic candidate and a matching true prefix would lie in `J_r`;
its width is too small to contain both. Therefore the true word must diverge
by output index

\[
\boxed{B=N+rp-1.}
\]

If `j` is the first mismatch with the repeated candidate, then the actual
period witness is `n=j-p`, not `j`. Thus `w_n != w_(n+p)` and
`n<=N+(r-1)p-1`. The implementation and verifier check this indexing explicitly.
See [CYCLE_ESCAPE_PROOF.md](CYCLE_ESCAPE_PROOF.md) for the full derivation.

### Quantitative strength

Every mixed block contracts the Farey cylinder by strictly less than `1/5`.
The optimal universal real factor is

\[
\boxed{3-2\sqrt2\approx0.171573.}
\]

The latter is a supremum approached by rational denominator ratios; no
rational ratio attains equality. The convenient rational `1/5` bound avoids
radical arithmetic in certificates. The stronger proposed `1/6` bound is
false: a valid chart gives the exact ratio `35/204>1/6`.

Pure blocks have slower, exact widths:

\[
|J_r|=\frac1{b(d+rpb)}\quad(L^p),
\qquad
|J_r|=\frac1{d(b+rpd)}\quad(R^p).
\]

A classical transcendence measure also gives a uniform worst-case budget.
For `H=max(16,height(P_v))` and `K=2^43`, Waldschmidt's 1978 Corollary3.2
implies `abs(P_v(pi))>H^(-K)`. Consequently

\[
|\pi-\xi_v|>\frac1{9H^{K+1}},\qquad
k_*=(K+1)\operatorname{bit\_length}(H)+4.
\]

Stage `k_*` suffices for exact polynomial sign separation for either source.
For a mixed period, `k_*` complete copies also suffice for escape. The pure
bound `9H^(K+1)` is retained as a symbolic expression. These are theorem-backed
budgets, far too large to execute; the adaptive geometric certificates are
usually much sharper. [UNIFORM_BOUNDS.md](UNIFORM_BOUNDS.md) states and derives
the precise specialization, with primary-source links. This is an application
of the classical theorem, not a new transcendence measure.

## 4. The machine can predict long runs as natural numbers

The increasing normalized residual is

\[
z=\frac{b\pi-a}{c-d\pi}.
\]

On `R`, it changes to `z-1`. On `L`, it changes to `z/(1-z)`; equivalently,
`1/z` changes to `1/z-1`. Therefore the next maximal run is

\[
R^{\lfloor z\rfloor}\quad(z>1),\qquad
L^{\lfloor1/z\rfloor}\quad(0<z<1).
\]

The observer refines the rational source until the lower and upper transformed
bounds have the same floor. This certifies the whole run at once. Its initial
output is

\[
L^6R^{15}L^1R^{292}L^1R^1L^1R^2L^1R^3L^1R^{14}\cdots.
\]

At the start of the fourth run the chart is `[333/106,355/113]`. Beta source
stage28 certifies

\[
292<\frac{106\pi-333}{355-113\pi}<293.
\]

The run compiler therefore emits the natural number292 directly. It has
expanded zero of that run's individual arrows to discover the count. The
saved certificate supplies the actual rational endpoint bounds.

The run numbers have a small categorical interpretation too: for a fixed
letter `G`, natural-number addition represents composition `G^m G^n=G^(m+n)`.
An execution block can be opened into a labeled finite chain with `n`
successor edges; gluing matching endpoints models concatenation, with total
edge count `m+n`. Retaining letter labels distinguishes mixed words that have
equal total length. The existing [numeric-arrow/family constructions](../cursed_categorical_computation/README.md)
give fuller categorical presentations; this compiler supplies actual natural
numbers extracted from the circle execution.

The compressed **letters** alternate and are periodic. The letter/count pairs,
and the positive count sequence itself, retain the nonperiodic information.
An eventually periodic count sequence would, after at most doubling its run
period to preserve parity, give an eventually periodic expanded L/R word.

## 5. Finite rational observations distinguish the changing real states

The all-time state proof is short. Put

\[
\Phi(I_k,J)=|I_k|\,|J|=W_k/(bd)>0.
\]

A source transition multiplies it by `j/(2j+1)`, an L transition by `d/(b+d)`,
and an R transition by `b/(b+d)`. Every factor is strictly below one, so an
earlier interval pair cannot return. Positive rational descent permits an
infinite execution; it does not supply a termination argument.

For normalized real residuals, returning to an earlier state would make that
state fixed by a nonidentity rational Möbius map. The fixed-point equation
has degree at most two. Rationally transporting it back to pi contradicts
nonquadraticity. Thus each pair of normalized states differs.

For each positive irrational residual `z`, define its rational cut presheaf

\[
D_z(q)=\begin{cases}\{*\},&q<z,\\\varnothing,&q\ge z,\end{cases}
\qquad D_z:\mathbb Q^{op}\longrightarrow\mathbf{Set}.
\]

Then

\[
\operatorname{Nat}(D_x,D_y)=
\begin{cases}\{*\},&x\le y,\\\varnothing,&x>y,\end{cases}
\qquad
D_z\cong\operatorname*{colim}_{q<z}y(q).
\]

This preserves and reflects the order arrows. The category of elements is
the rational lower cut with its order arrows and rational labels: the real
is presented coherently by a filtered family of rational representables.
These elementary formulas are proved in
[PRODUCTIVE_GEOMETRY.md](PRODUCTIVE_GEOMETRY.md), Section7.

Given any `m` distinct normalized states, refinement eventually produces
pairwise disjoint rational enclosures. Choose one rational threshold between
each adjacent pair. Their `m-1` lower-cut membership bits distinguish all
states. This count is optimal for a fixed nonadaptive threshold family;
adaptive comparison trees have a different cost model.

The saved eight-state example uses states `0,6,21,22,100,314,512,1024` and
seven thresholds at common beta stage344. Each comparison is a finite witness
about the represented real state. Chronological L/R transitions are separately
typed Möbius transformations; they are not all order-natural transformations
between these cut presheaves.

A useful warning emerged from this calculation: the bare rational-Möbius
action groupoid on a nonquadratic orbit is equivalent to the terminal category.
Forgetting probes and chart data can therefore erase the entire computational
story while preserving a categorical equivalence. The useful object retains
the rational probes, source names, chart labels and resource measures.

## 6. What was executed

All following numbers describe finite runs; the preceding theorems carry the
all-time quantifiers.

| Check | Saved result |
|---|---|
| Root period replay |43 beta candidates and3 rotation candidates; every prospective certificate and mismatch passed independent scalar-source/tuple-matrix verification. |
| Root declared holdouts | `(1601,11)`: deadline1666, mismatch1663; `(2333,17)`: deadline2706, mismatch2693; `(3072,23)`: deadline3117, mismatch3095. |
| Independent constructor holdout | `(4003,31)`: deadline24121, mismatch24050, witness start24019; independent baseline replay through24051 arrows. |
| Semantic state potential |1024 outputs,340 source refinements,1364 strict decreases. |
| Maximal-run compiler |48 runs,637 expanded arrows; independent rotation replay and every following branch change checked. |
| Finite rational family |8 states distinguished by7 thresholds; singleton case needs zero thresholds. |
| Periodic quadratic control | `(9-sqrt(5))/2` yields `(LR)^100`;477 interval-potential decreases coexist with periodic labels. Its valid cycle polynomial remains zero-compatible in80 source enclosures. |
| Corruption controls |13 rejected mutations, including polynomial/gap/deadline, source-clock rollback, erased theorem dependency, overstated optimality and a fractional block count. |
| Unbounded CLI |Five run records observed from `--forever`, then the consumer closed the pipe cleanly. |

The separate constructor and translator scripts have their own recorded
finite scopes. Shared Euclidean source semantics and same-model reviewers
are disclosed; different implementations are useful checks, not blind
external mathematical witnesses.

## 7. Reading map and remaining obligation

| File | Purpose |
|---|---|
| [HOLE_CONTRACT.md](HOLE_CONTRACT.md) | Targets, acceptance criteria and dependency cut declared before implementation. |
| [CYCLE_ESCAPE_PROOF.md](CYCLE_ESCAPE_PROOF.md) | Polynomial obstruction, exact contraction, pure periods and deadline indexing. |
| [UNIFORM_BOUNDS.md](UNIFORM_BOUNDS.md) | Primary theorem import and explicit uniform corollaries. |
| [PRODUCTIVE_GEOMETRY.md](PRODUCTIVE_GEOMETRY.md) | Infinite execution, normalized states, run compiler, finite probes and Yoneda construction. |
| [HOSTILE_PERIODS.md](HOSTILE_PERIODS.md) | Quadratic control, sign/domain traps and audit repair history. |
| [aperiodic_observer.py](aperiodic_observer.py) | Finite productive programs and JSON certificates. |
| [aperiodic_probe.py](aperiodic_probe.py) | Independent certificate checker, mutation controls and saved root receipt. |
| [cycle_independent_probe.py](cycle_independent_probe.py) | Guarded prospective construction and separate algebraic replay. |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Quantifiers, hypotheses, evidence and truth states. |
| [VALIDATION.md](VALIDATION.md) | Exact validation versions, repository gates and publication scope. |

This round resolves a concrete gap: qualitative nonperiodicity now has a
source-derived finite certificate interface, prospective escape deadlines,
compressed natural-number execution and separating rational observations.
The next quantitative improvement would be a useful size-dependent bound
between the enormous uniform theorem and the sharp adaptive certificates.
The repository's signed statistical cancellation and normality questions
retain their existing status; no such estimate is supplied by nonreturn alone.
