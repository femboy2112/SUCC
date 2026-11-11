# H-hostile gate matrix: infinite near-misses are not a refutation

## Steelman

A finite program can be **proved** to emit arbitrarily long correct finite prefixes, and its totality can be proved for every rational comparison without executing an actual infinity. The proof is the quantifier exchange `forall rational q exists finite source stage S(q)` and, more strongly, `forall integer H exists finite S(H), one Farey shield solves all denominator<=H rationals`. The source is still required to identify the selected x; this is not the same as assuming arbitrary candidates are distinguishable from finite data.

## Crucible / negative controls

1. **Arbitrarily close rationals:** 355/113 and 208341/66317 agree with pi for long finite L/R prefixes, but H>=denominator yields an exact global family certificate that classifies them. The latter is the lower endpoint at H=66317. No prespecified uniform *precision* bound is claimed.
2. **Equal rational mediator:** a source oracle converging to rational 7/2 remains ambiguous at the initial mediant. With a limited budget the run procedure must return `UNKNOWN`, not silently choose a branch. The pi totality theorem depends on imported irrationality.
3. **Two equal real names:** the two-oracle inequality semidecider returns UNKNOWN under any finite budget. Equality is not decidable in the general represented-real interface.
4. **Two distinct real names extremely close:** pi and pi+16^-60 share many finite numerical probes; early budget returns UNKNOWN, deeper exact intervals produce a rational separating them. No accidental false negative is accepted.
5. **Nonnormal irrational:** `3+sum_(j>=1)16^(-j!)` is irrational, source-computable, and passes *every* Farey height shield. Its hexadecimal frequency of digit 1 tends to zero. This is a decisive negative control against upgrading reconstruction to normality.
6. **Forged interval and stage:** replay reconstructs the claimed source interval from its specific arithmetic recurrence and rejects changed endpoint/stage, detached quotient bounds, altered arrow ancestry or altered final positive margin. A hash or a Python helper is not a proof of the semantic BBP/pi or circle/pi identity.
7. **Coherent wrong seed:** translating the completed original BBP phase by -pi/16 makes the observable circle orbit zero; its rational value is not inside the irrational-only category. The full real-cut and source/seed passports must be retained.
8. **Rational seed alias:** translation by +1/16 changes the original first digit but leaves all later phase classes aliased, despite exact finite cut transport. A later-phase-only observer cannot authenticate the source origin.
9. **Four-pole mutation:** the source identity is exactly the frozen 4-pole formula, not an arbitrary rational sequence with similar positivity. Source-shape compatibility cannot be used to import a selected signed estimate.
10. **Unknown statistical implication:** the H-shield and Yoneda reconstruction furnish neither `W_N(h)->0` nor a bound on the #591 signed overlap or #593 two-time joining. Even perfect rational-separation certificates for all heights are consistent with base-16 nonnormality.

## Verdict

The previous assertion that “some rational shares any finite prefix” is not a blocker to a **uniform finite program plus a universal termination theorem**. What survives as a genuine frontier is the lack of a new source-derived signed cancellation inequality. The H-shield strengthens exact identification of the real/cut, not statistical properties of the path. Do not claim higher claims on the strength of this finite observer.
