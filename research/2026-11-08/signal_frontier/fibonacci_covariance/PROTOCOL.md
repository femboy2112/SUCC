# Fibonacci covariance observer: fixed experiment protocol

Scope: integer-clock realization of the calibrated observer, exact golden
phase labels, and source-faithful signed responses. No source cancellation
is presumed. Original source and all shared files remain read-only.

Before executing the new source probe:

- Development A=149; holdout A=673. These are new observer configurations,
  not independent source datasets: the parent already sampled these epochs.
- h=1,3; M=4,16; Fibonacci clock lengths q=13,55,233.
- Original literal-zero source; matched rational same-forcing seed preserving
  the selected principal phase; synthetic coherent complement b=conjugate(a).
- The selected p, exact source builder, matched-seed builder and outward
  phase engine are inherited and credited. Every golden partition label is
  computed exactly in Q(sqrt5), without floating-point sorting or binning.
- All 72 cases are retained. Expected calibration is sinc²(pi h/M) W, with
  error <=2pi|h|D_local+4pi|h|[1/q+(q-1)alpha^k/q]. Neither the matched nor
  the synthetic coherent control may be mistaken for decay.
- Independent exact Fibonacci/grid comparison and discrete discrepancy
  checks include k=3..20. Frame tests use q=13,34,89; harmonics H=1,2,4
  when q>2piH. Compare actual sampled polynomial energies with the paper
  frame bounds using outward phase intervals.
- Hostile tests include an aliased M|h sensor, independently rotating
  clock gauges, homometric circle laws, and a source-preserving coherent
  wrong seed in the paper proof. Magnitude-only measurements cannot be
  silently promoted to anchored phase observations.

A finite certificate certifies only its stated finite inequalities. The
all-epoch acquisition theorem is paper-proved. Original-zero covariance
and pi normality remain OPEN.
