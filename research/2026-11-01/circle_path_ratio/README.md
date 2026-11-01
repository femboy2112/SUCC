# Circle path quotient and original BBP: radix-16 self-realization

**Draft research only. π base-16 normality and RH remain OPEN.** Original four signed BBP poles and literal U0=0 are preserved; no archived, production, or canonical theorem file has been altered.

## Central insight

The literal geometric ratio can be obtained from two same-endpoint paths: straight diameter length 2 and upper semicircular arc length π. Approximate the curved path by iteratively bisecting arcs; every stage is generated from the previous via a Pythagorean radical, not a decimal π input. Four subdivisions are one radix-16 scaling cell. A Cayley uniformization turns the circle's ×16 map into four rational projective doublings.

**New source-attested finite bracket (G5):** let `B_N=16Σ_(j<=N)16^-j r(j)` be the authentic rational BBP lower truncation, `Π_(4N)` be the 16^N-chord geometric path quotient, and `W_N` the PR #446 Wilson source curvature upper truncation. Then, for all N>=1,

    B_N < Π_(4N) < π < W_N,
    W_N = B_N + (16/(15*16^N))r(N+1).

The bracket is derived using the *known* BBP identity and classical geometry. It is not a proof that the BBP formula follows from polygon dynamics, nor a π digit-normality proof. For N=1 the geometric comparison is an exact outward radical certificate; for N>=2 it is an all-horizon tail inequality.

**Rigorous path integral (G4):** two declared 1D heat/Wick path channels with the same endpoints and lengths `2` and `Π_k` satisfy a normalized logarithmic Gaussian-kernel ratio whose square-root reproduces Π_k **for every heat time**. It is a true convergent stochastic path integral, not physical tunneling or a built-in BBP quantum probability law. An additional control is needed to superpose path channels.

**Two completion clocks (G6):** the geometric chord tower uses 2-power cyclotomic angles; exact original BBP phases are odd-conductor roots of unity. CRT provides a common *finite* carrier with declared labels; it does not imply selected signed cancellation.

## Read and run

- [Full proofs](PROOFS.md), [scoped claim ledger](CLAIMS.md), [source map](SOURCE_MAP.md), [next proof-gates](NEXT.md), [validation](VALIDATION.md), [exact rational receipts](FINITE_RECEIPT.json).
- `python -m unittest discover -s tests -p 'test_circle_path_ratio.py' -v` (44 exact stdlib tests, original source and independently derived oracles).
- `python research/2026-11-01/circle_path_ratio/symbolic_probe.py` (SymPy checks of rational circle, differential transport, source and Cayley 16-fold power).

Tests verify the finite algebra and interval enclosures; classical infinite-limit arguments are paper proofs, not executable proof assistant certificates. Full SUCC tree CI and external refereeing are separate.
