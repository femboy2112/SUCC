# The folded complement has an exact moment memory

The source's known equal replica weights make more reconstruction possible
than a generic moment hierarchy suggests. The [paper proofs](THEOREMS.md)
give a finite codec and its exact failure modes. They do not prove signed
cancellation.

For q replicas, q complex moments recover their complete unordered phase
law by classical Newton identities. Because every split source clock has
even q, only q/2 moments suffice on the chart where the middle elementary
symmetric coefficient is nonzero. The q-moment codec covers the exceptional
set too. These are ideal exact complex reports, not fixed finite-bit memory.

For the important q=2 clock, the source's **odd denominators** exclude the
one exact first-moment alias: the antipodal pair. Therefore a single exact
nonzero first moment s determines the entire unordered complementary law:

    M_16 = (s/|s|)^16 T_16(|s|).

For h=1 this is the original complementary law. At general h it is the law
after taking hth powers. Near s=0, decoding is unstable, and arithmetic
nonvanishing supplies no uniform precision bound. Storing a second moment
avoids this division singularity. The closure is nonlinear; M_16=s^16 is
still false.

The law also forgets which phase belongs to which source time. For a declared
two-assignment observation fiber, one bit resolves the next-mean ambiguity.
Its exact minimax prediction radius is

    (|z^16-w^16|/2) |sin(pi h[f-g])|.

For an actual internal source transition, the upper radius is at most
240 pi |h| m/[(8n+1)(8n+2)(8n+3)]. Full literal-zero replay has a singleton
history and can recover labels; the one-bit lower bound does not apply there
without an explicit restriction on access. This distinguishes mathematical
information from computational working memory.

The [connection audit](CONNECTIONS.md) links this construction to SUCC's
archived hidden-memory Schur/Prony work, factorial Fourier hologram, twisted
two-wire source observer and current learning Yoneda carrier. The transfer
is a shared finite reconstruction mechanism; it does not identify the RH and
BBP source carriers. The circle's barycenter becomes an explicit disk map,
with the 17-cycle control and root's sharp energy theorem as exact tests.

The [receipt](RECEIPT.json) covers twelve historical source configurations,
not fresh holdouts: 792 exact unwrapped/carry checks, 396 actual principal
parts, 198 nonzero moment closures, 186 chronology radius certificates,
372 exact phase cocycles and 600 rational forcing bounds. Eight focused
tests include Gaussian-rational Newton recovery, alias/conditioning controls,
chronology targets, and deterministic-source replay. The source code and
phase primitive are shared with earlier work; this is not independent data.

Commands from the repository root:

```sh
PYTHONPATH="$PWD" python -m unittest discover -s research/2026-11-08/frontier_connections/observer -p 'test_*.py' -v
PYTHONPATH="$PWD" python research/2026-11-08/frontier_connections/observer/oracle.py
PYTHONPATH="$PWD" OPENBLAS_NUM_THREADS=1 python research/2026-11-08/frontier_connections/observer/cross_review.py
```

The cross-front review additionally checks all 483 integer matrix centers in
three small quadratic scans by Python arbitrary-precision scalar sums.
It shares phase/quantization inputs, while its contraction algorithm is
independent of NumPy's. Root energy and arithmetic proofs were separately
reviewed; [cross-review hashes](CROSS_REVIEW.json) pin the inspected files.

The next substantive arithmetic target is to control the **phase-aligned**
first moment mean e(h x_r/p) B_r(h) using the authenticated initial boundary.
Moment memory can represent that signal and bound an observation error;
it does not make the retained signal small. **Pi normality: OPEN. RH: OPEN.**
