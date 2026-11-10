# Independent root instrument and formal-scope review

Reviewer: carry_theory front. Same model family and repository; independent mathematical derivation and execution, not external refereeing. No held-out source file or measured result was read.

## Verdict

**PASS within the stated finite source scope.** One malformed-input defect was found and repaired before this review was closed.

- `analytic_bounds` uses the slightly sharper source estimate `epsilon = pi|h|[16^-k+2/(8(n0-k)+1)^2]`. This follows from the exact positive decomposition `r(t)=6/[d(d+3)]+4/[d(d+4)]+5/[d(d+5)]<15/d^2`, d=8t-7, and `sum16^-j<1/15`. The signed boundary term2k/N, padded-window factor, outward square roots and optional residue-word exception costs agree with CCV7.
- The reconstruction is genuinely causal retrodiction: last k literal carries locate the phase k steps earlier. The code does not call that a current-phase prediction. The three certificates separately retain the mean model contribution; none discards its resonant signal.
- Comparing a measured interval LOWER endpoint with a proved upper bound checks noncontradiction. The code correctly does not treat that comparison as proof that its independently wider numerical upper endpoint is below the analytic estimate.
- Found and resolved: `run` formerly zipped phase boxes and predictions without validating full clock lengths. A truncated phase row could have been tested with the wrong normalization metadata. The final file rejects carry-stream length, epoch length, phase length and phase-start mismatches. The new regression independently passed. No claim that the authenticated existing source fixture was malformed.

## Independently executed checks

- `/tmp/succ-learning-yoneda-venv/bin/python -m unittest discover -s research/2026-11-08/chronology_carry -p test_retro_probe.py -v`: **4 tests PASS**. Includes336 exact original-source ancestor identities, causal/literal spill checks, coherent retained-phase controls, and malformed-row rejection.
- `lean research/2026-11-08/chronology_carry/CarryPoisson.lean`: **exit0** using Lean4.14.0, commit410fab728470. Four theorem axiom audits contain only `propext` and `Quot.sound`; no `sorryAx` in this execution.

## Exact Lean authority

The kernel checks integer-coordinate finite telescoping, Poisson summation under an explicit pointwise law, its defect version, and the frozen-control finite-sum split. Clearing the denominators of a finite Gaussian-rational table permits coordinatewise application. The source file does not formalize construction of P or psi, BBP forcing bounds, complex analytic estimates, finite-field arithmetic, inverse limits, Weyl decay, or normality. The retained earlier cast-name failure log is historical failed validation; it is not the final kernel result.

## Separate cross-front review

EI1–5 in `crucible/EXPLICIT_INNOVATION.md` were independently checked: midpoint geometric factor,17pi|h|/15 literal-next-carry bound, uniform memory tail, Z16 descent through the authenticated integer lift, common finite-to-infinite factor, and coherent Phi_h(-1,15)=1. No substantive defect found. This is a bounded observable and an equivalence with the open Weyl gate, not signed decay. The CCV2b occupation formula was clarified after the crucible review: literal carry16 has reference probability0, not1/16.

## Reviewed SHA256 pins

- `retro_probe.py`: `0ec65d0db7d52e93b8a47051ce9fac4f789886b17b7d8fe4307c678924e501a8`
- `test_retro_probe.py`: `0600e4f2f4716d18c8efe7928bc2509ec84941b475e7009819213fcbd3648e4d`
- `signed_probe.py`: `151c66bf090a6432501be98bf093fb0eb3871180849b3dceb4a1c27f23d8197f`
- `CarryPoisson.lean`: `28cb3c557544f678d13ec01bf4b9bc4112aba91feeedc861ae1c04767fe8f58a`
- `crucible/EXPLICIT_INNOVATION.md`: `45d0ae4c35e8cf6045c56a1e921cdf1cf739ed5bb66f9cae89cea9a2bd8e826d`
- `theory/THEOREMS.md`: `deab12908b98d19e8aed67cfc30027bb3e8b5884e9b2908ad4fbe2f6f43db9fc`

**Pi base16 normality: OPEN. RH: OPEN.**
