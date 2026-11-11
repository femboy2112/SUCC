# SUCC Cursed Computation V — finite-height Farey shields

**Research-only continuation, 2026-11-10/11.** Based on PR #595 exact head `4e311d03e3ac9c3dbcbdc32477cd113f2ac0743b`, with PR #594 as the earlier Dedekind–Yoneda construction. Additive files only; no source/seed/provenance/Lean/CI changes.

> **The corrective theorem:** A finite Stern–Brocot observer should *not* be defeated by a rational sharing an enormous finite prefix. For every integer H it computes one exact certificate excluding **all** rationals with denominator <=H from the actual irrational value, with positive rational separation margin. This is a quantified infinite-domain theorem implemented by a finite program, not an infinite experiment.

## One line of load-bearing arithmetic

For Farey neighbors `a/b<c/d`, `bc-ad=1`, each reduced rational `p/q` strictly between them obeys

`q = d(bp-aq)+b(cq-dp) >= b+d`.

Thus a bracket with `b+d>H` separates **every** denominator<=H candidate at once. Starting from `[3,4]` it requires at most `H-1` elementary L/R arrow outputs. One further finite tightening of an authenticated source interval yields an explicit **positive** rational margin valid for every such candidate. Source precision and execution time have **no claimed uniform bound**.

## The cursed compiler

`farey_height_shield.py` constructs and checks compressed `L^k`/`R^k` arrows using exact integer/`Fraction` residual quotients. It has three certified semantics:

- `circle_beta`: Euclidean circle integral, geometric beta-matrix rational source from #595, without a pi value/float/digit oracle in production.
- `bbp_four_pole`: the *same* unchanged signed four-pole BBP source, with the literal zero-seed completed value. Classical BBP identification with pi is an imported theorem.
- `sparse_nonnormal`: explicit factorial-sparse base-16 irrational, a hostile **nonnormal** source that passes all the same finite-height/categorical tests.

The two pi sources are mathematically different constructions, sharing the classical identification of pi and not external referees. A finite verifier reconstructs all source intervals, replays compressed Farey arrows, checks global height/shield bounds and rejects forged margins and detached stages.

Run locally from this directory:

```sh
python -W error -m unittest -v test_height_shield.py
python -m compileall -q farey_height_shield.py test_height_shield.py
python farey_height_shield.py 1000 --source circle_beta
python farey_height_shield.py 66317 --source bbp_four_pole
python farey_height_shield.py 1000 --source sparse_nonnormal
```

## Two specific receipts

For `H=1000`, **29 elementary arrows in four macro certificates** (`L^6 R^15 L R^7`) produce

`2818/897 < pi < 355/113`, with `897+113=1010 > 1000`.

There are **304,193** distinct reduced rationals in `[3,4]` with denominator <=1000. The 29-arrow certificate decides all these rational cut probes without 304,193 independent comparisons.

For `H=66317`, the machine emits 316 elementary arrows in six run certificates, ending at

`208341/66317 < pi < 104348/33215`.

The rational `208341/66317` that formerly looked like a catastrophic near-miss is now the **certified lower endpoint** and is definitively excluded. Both pi sources produce the same Farey bracket. Their positive rational separation margins differ because their finite enclosures have different widths; the statement about the limit is identical.

## The coherent categorical result

For each H, the finite ordered rational-probe category `Q_H` (denominator<=H in `[3,4]`) receives the full lower-cut presheaf truth values from **one** height shield. Whenever H<=K, restricting the K-level functor to Q_H agrees exactly with the H-level functor. The compatible family recovers the full Dedekind/Yoneda lower cut of the value because the probe union contains every rational. This is the sense in which an infinite computation is controlled by *a finite algorithm with a proof of its quantified behavior*.

## The decisive boundary

The same procedure works for the provably nonnormal irrational `3+sum 16^(-j!)`. Also, any two distinct computably named reals can eventually be separated by a rational witness, while equality can remain forever UNKNOWN. Hence **no** normality or signed Fourier cancellation follows from productivity or rational-cut completeness. These are representation theorems and proof contracts, not spectral estimates.

See [HEIGHT_SHIELD_THEOREMS.md](HEIGHT_SHIELD_THEOREMS.md) for paper derivations, [HOSTILE_GATES.md](HOSTILE_GATES.md) for falsifiers, [VALIDATION.md](VALIDATION.md) for exact local receipts, and [height_shield_receipt.json](height_shield_receipt.json) for selected replay data.

**Status:** source/cut/productivity theorem PROVED PAPER with finite calibration; full SUCC integration, typed lambda compiler and source-selected signed cancellation OPEN/UNVERIFIED. No main merge requested. Long CI is deliberately avoided at research-branch publication.
