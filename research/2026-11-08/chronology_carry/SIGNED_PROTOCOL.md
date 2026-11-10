# Signed-residual extension, before the held-out clock is opened

This is an additional fixed test, after PROTOCOL.md was pushed at `8c43eaf1`
but before any source phases on the held-out interval [55003,110004] were read.
The original L1 test and its threshold stay in force, regardless of this result.
The training tables, h=1,3, source selector and source provenance are unchanged.

For every frozen table g, form f_n=e(h U_n) and e_n=f_n-g(w_n) on the full
clean interval, in chronological order, without folding. Also evaluate g=0.
For the fixed apertures H=32,128,512 compute

    V_H(e)=(N+H-1)/(N^2 H^2) * sum_t |sum_(j=0)^(H-1)e_(t+j)|^2,

where e is zero outside 0..N-1 and t runs 1-H..N-1. These are all windows,
including both incomplete ends. Exact Cauchy gives

    |mean f| <= |mean g| + sqrt(V_H(e)).

Report all apertures and both carry depths, including the zero-model baseline.
The same <=1/4 finite threshold applies. Compare paired certificates, without
choosing a best table for any subsequent theorem. An observed improvement is
a finite instrument result, not a bound for all epochs. Separately retain the
signed lag contribution V_H minus the appropriately normalized diagonal term.
No replacement of signed cross terms by presumed random cancellation.

Use the uniform-append de Bruijn operator P only as a stipulated reference
operator on words, not as the actual zero-source transition law. For regular
digits 0..15 and depth k, compute exactly mu=uniform mean g and
psi=sum_(j=0)^(k-1) P^j(g-mu). Verify (I-P)psi=g-mu. Evaluate the signed
transition innovation and boundary using available adjacent states. If an
exceptional carry is present, retain it and pay a separate explicit error;
do not silently reduce it modulo16. The innovation is measured, not granted
mean zero by a martingale assumption. Its source-selected bound remains open.

The new theorem target is a conditional, deterministic control-variate gate:
frozen carry mean/innovation plus signed residual window energy tend to zero,
with the actual clock coverage cost tending zero, for every fixed h!=0.
This can bypass a vanishing L1 approximation error. It does not itself prove
either required original-zero estimate. The prior signed_covariance_round2
window identity is reused and cited; no novelty claimed for van der Corput.

Implementation uses outward integer arithmetic or separately proved error
enclosures; floating results are diagnostics only. Root will independently
cross-check small windows by direct pair expansion and selected source phases
by a distinct interval implementation. Raw later-source phases/carries will
be retained with deterministic compression and hashes for replay.

Pi base-16 normality: OPEN. RH: OPEN.
