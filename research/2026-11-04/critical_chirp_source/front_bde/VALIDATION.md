# Exact validation for B/D/E

Commands, executed from the isolated research worktree:

    python3 research/2026-11-04/critical_chirp_source/front_bde/probe.py > research/2026-11-04/critical_chirp_source/front_bde/FINITE_RECEIPT.json
    python3 -m unittest discover -s research/2026-11-04/critical_chirp_source/front_bde -p 'test_*.py' -v

Both exited zero. Four focused tests passed. The receipt checks 540 original
states through direct four-pole Fraction and polynomial integer-LCM recurrences,
540 exact mutated state denominators, 540 intrinsic prefix LCMs, and all 8,128
unordered pairs in [257,385). Of those pairs, 7,519 have genuine ternary height
above the conservative intervention grid 27 and all preserve the exact reduced
gap denominator. Twenty-five of the remaining pairs actually change denominator;
these failures are retained, rather than pretending every pair is protected.

Reset corrections at 86,191,296,401,506 are respectively 0,0,2/3,11/27,8/9.
Their rational completed-character intervals are retained in FINITE_RECEIPT.json.
The nonnegative corrections demonstrate forcing positivity and explicitly show
that this variant does NOT have tiny forcing defects. The first two zero resets
are harmless startup cases. The finite startup caps D below 8(t-1)/27; it is
asymptotically redundant.

The radial tail/derivative interval checks use development n=8,16,32 and fresh
n=37,83,173 declared before this run. All four derivative orders 0,1,2,3 lie
inside the analytic remainder bound; the second derivative is positive and the
third negative. The exact recurrence value is inside the order-zero interval.
The opposite angular channel is rejected. A nonunit modular frequency is rejected.

These are exact finite checks and implementation controls, not proofs of the
asymptotic resetting regime, original cancellation, or external CI. The parent
coordinator owns full native validation and exact submitted-head hosted status.
