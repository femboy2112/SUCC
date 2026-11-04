# Validation, origin and claim scope — Operation Möbius Mirror

**Original branch:** \`research/mobius-reciprocal-mirror-2026-11-02\` from EXACT PR #475 head \`20acb35a42b6ae5fb9260c041ed3a1aa47429484\`. All changes strictly additive research dossiers/oracles and root tests. Canonical SUCC source, U₀=0, formal kernel, frozen archives, workflows and main untouched.

**Actually executed locally:** Python stdlib isolated staging at /mnt/data/mobius_stage, \`python -m unittest discover -s tests -p 'test_*.py'\`: **31/31 tests PASS**, no skipped tests, Python compileall PASS. Two initial calibration issues were exposed and repaired before committing: the projective ∞/half-turn branch had wrongly returned ∞ instead of zero; a test had incorrectly applied the n≥2 bound r(n)<1/2 at n=1 where r(1)=47/15. A third no-op test guard was removed. The corrected staged source and exact two test modules were re-run with all 31 passing; no false initial PASS claimed.

**Exact mathematical calibration:** independent SymPy check of the Cayley reciprocal, failure of raw reciprocal to descend x mod1, degree-16 rational tangent polynomial relation \(\mathcal D_{16}(1/t)=1/\mathcal D_{16}(t)\) as a polynomial identity, original r(1)=47/15 and r(2)=106/819, original four meromorphic pole residues and cross-ratio 4 vs 5/2. Full exact Fraction recurrence with literal zero initial state and finite mirror axes through B=24. Numeric circle e() diagnostics always reduce exact rational phase mod1 before using floating trig. Tests covering B=1..256 certify finite original source cocycle and rational source/gamma differences; golden axes and q-sheet tests separately test the representation identity.

**Remote byte-identical re-fetch verification of locally staged files:**
- \`research/2026-11-02/mobius_mirror/mobius_mirror.py\` Git blob SHA: \`96860041fe53f2c0ad0b22fd6bcc521c42345b1b\`.
- \`tests/test_mobius_mirror.py\` Git blob SHA: \`f3244fe36732425f6394decf257ff0d9f21c5bbc\`.
- \`tests/test_mirror_fejer.py\` Git blob SHA: \`0a27ee7186dbbc1b0ba861c9013678cf316c48ef\`.

These are same-implementation/source integrity checks, not external mathematical independence. Classical sympy symbolic algebra is a separate implementation route for specified identities, not a blinded referee.

**Finite hostile controls:** a 15-root finite dihedral-invariant non-Haar measure; coherent same-positive-four-pole real seed \(s=-\pi/16\), seed 1/5, rational periodic 1/7; shifted source p-free / q-seed ensemble with square-root mean selected coherent; original positive r(1)≠r(n). No original real π normality claim.

**NOT executed or claimed:** full native SUCC ~11k+ suite, full scripts/verify_provenance.py, scripts/observer_foundations_probe.py, scripts/ordinal_succ_report_probe.py, new Lean kernel proof, hosted exact-head CI green or external independent referee. Native public GitHub clone fails DNS in this execution container; connected GitHub operations are used. Exact-head hosted workflows should be inspected when PR created; avoid redundant expensive reruns.

**Ledger:** projective reciprocal, autonomous centralizer, source meromorphic differential rigidity, finite Gamma mirror cocycle and cutoff inequality, two-axis golden criterion and q-sheet averaging = PAPER PROVED within declared types; finite tests OBSERVED for their specified inputs; source-selected all-A real mesoscopic collision \(o(\log A)\) remains UNVERIFIED, so π base-16 normality OPEN.
