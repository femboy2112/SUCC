# SUCC claim supplement — Oily–Macaroni / BBP zero–one boundary

Research-only child of #338. Full proof: [Oily One-Boundary Dossier](../research/2026-10-27/OILY_ZERO_ONE_LOG_GERM_BRIDGE.md).

| Claim | Status | Proof and boundary |
|---|---|---|
| OZO-1: exact positive packet lift of BBP source generating function G(Q) | PROVED LOCAL | P=(16−x^8)R, R=Σp_j, entire positive source kept |
| OZO-2: packet masses π_j=16∫p_j=2^(j+1)/((2j+1)binom(2j,j)) | PROVED/CLASSICAL identity | Exact Beta integral; identity attributed to Euler via OEIS A000796. Source-specific packet correspondence is new to current lineage |
| OZO-3: graded moment first two coefficients 15C/(64n²)+(151C+30H)/(512n³) | PROVED LOCAL | Endpoint Taylor jet plus exact Beta moments |
| OZO-4: first and second graded q=1 logarithmic coefficients 15C/64 and (209C−30H)/1024 | PROVED LOCAL | Li₂/Li₃ singular expansions; residual C² at endpoint |
| OZO-5: Gamma(2) and Euler gamma shared endpoint geometry | CLASSICAL/INHERITED | R(x)~1−x, Y=8n(1−X)→Gamma(2,1); golden-centered γ coefficient grade-dependent |
| First two graded 1-germ coefficients imply selected Weyl cancellation | UNVERIFIED/NOT ESTABLISHED | Unchanged forcing, changed seed −T_n preserves packet/source germs but real phases →1; scalar Oily decoration cannot save Weyl order |

**Local instrument:** scripts/oily_one_boundary_exact_probe.py (stdlib Fraction), 33 exact integrated packet identities and 20 character/response combinations PASS; separate independent SymPy endpoint symbolic 10 packet cases PASS; no full native SUCC suite, hosted CI, or Lean authority claimed. Actual π normality OPEN.
