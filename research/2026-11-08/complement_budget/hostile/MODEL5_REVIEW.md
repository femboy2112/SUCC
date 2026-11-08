# Additive independent audit of CBM5

This review supplements the earlier `REVIEW.md`; its historical proof pins
are preserved. The exact new model proof hash is recorded separately in
`MODEL5_REVIEW_RECEIPT.json`. Same model family and workspace; no external
scholarly refereeing is claimed.

**Verdict: proof survives the following independent derivation checks.**

1. **Escape modulo constants.** If T preserves the finite set of branch
   classes modulo constants, its invertibility makes it a permutation of at
   most K classes. Every nonzero coefficient of degree d>=2 would then obey
   `m | t(d-1)` for some `t<=K`, contradicting `KD<m`. Therefore a branch
   escapes modulo constants against every candidate target branch. Affine
   intercepts are correctly excluded: `P=X+1` has only a constant defect.
2. **Uniform interval constant.** For any arc, the p-grid count differs from
   its length by at most1/p. Its nonzero normalized DFT coefficient is at
   most `1/(p sin(pi|k|/p))<=1/(2|k|)`. Pairing the positive and negative
   frequencies therefore gives exactly `delta H_((p-1)/2)`, without a
   missing factor2. The declared Weil lift is nonconstant of degree
   at most `D(p-1)/m<p`; multiplying by nonzero k preserves that condition.
3. **Phase anchors.** Fixed arbitrary unit anchors rotate the near-collision
   arc by a known constant. Since the discrepancy estimate is uniform in
   origin, no extra loss is required. Independently rotating anchors as x
   varies would invalidate this step and are excluded by the statement.
4. **Mass, orientation and boundary.** The escaping atom is in `mu_(16x)`;
   it has mass at least w_min even if source-side atoms coalesce. Every
   coupling must transport that mass at least its nearest distance to the
   support of `pow16_*mu_x`. Removing the final clock edge costs1/m in the
   proportion, not a forcing-period extension. The actual source comparison
   uses only interior edges and charges17 times the full law error.
5. **Layer-cake improvement.** For nearest chord distance Y, set to zero at
   the omitted boundary, `Pr(Y>=r)>=[a-Kr/2]_+`. Integrating to `2a/K<=2`
   gives `E Y>=a²/K`. This doubles the one-threshold estimate and supports
   the stated asymptotic floor `w_min/(17K)`.
6. **Quantifiers and conclusion.** The error term requires
   `D sqrt(p) log(p)/m ->0`, automatic for fixed D under PR1. Merely
   `D=o(Lambda)` would not suffice; the final statement does not make that
   leap. Fixed K and a positive lower weight are necessary to retain a
   positive limit. The lower bound concerns the **whole conditional law in
   W1**, and explicitly does not assert a lower bound on PR8's first-moment
   approximation error. This distinction is essential.

The new theorem is an unconditional restriction on how the actual source
law can be modeled by the declared bounded nonlinear positive families.
It also applies to suitable same-forcing controls, and therefore is not a
literal-zero selection theorem or a normality proof. Affine mixtures and
more general signed first-moment models remain live routes.

## Separate exact finite oracle

`model5_review_oracle.py` imports no sibling model implementation. It checks
finite coefficient-family escape, including duplicate classes modulo
constants; exact circular interval discrepancy and its invariance under
rational anchor rotation; the nearest-distance layer-cake lower bound; and
the declared PR3 harmonic discrepancy budget. All these comparisons use
integers and Fraction, with an outward rational square-root bound.

The large p88001 clock is source-blind algebra on the preregistered prime,
not another evaluation of the original BBP orbit or a fresh empirical holdout.
The source asymptotic conclusion follows from the proof, not the finite
tests. Reproduce from the repository root:

```sh
/tmp/succ-learning-yoneda-venv/bin/python research/2026-11-08/complement_budget/hostile/model5_review_oracle.py --output research/2026-11-08/complement_budget/hostile/MODEL5_REVIEW_RECEIPT.json
```

Executed successfully:313 coefficient-family escape checks, one affine
countermodel, nine exact rotated-discrepancy equalities and six nearest-
distance cases. Five exact-arc layer-cake floors and one uniform-PR3-grid
floor are strictly positive. At p88001,K1,D2 the latter lower bound on
the **unweighted interior nearest distance** is0.1537269930; the exact
rational nearest-distance lower is greater than1.002. A model-error floor
must still multiply by w_min, subtract the forcing cost and divide by17.
The receipt does not silently relabel distance as model error.

Pi base-16 normality: OPEN. RH: OPEN.
