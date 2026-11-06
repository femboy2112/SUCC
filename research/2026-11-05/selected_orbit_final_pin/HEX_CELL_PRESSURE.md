# A weaker growth premise, with an exponential obstruction

Full proof: [front_referee/PROOFS.md](front_referee/PROOFS.md), R1–R3. For every times-16 invariant probability mu, let D_k=k log16-H_k be its block Shannon entropy deficit. Then

    log P_m(mu) >= D_m(mu) >= floor(m/k)D_k(mu).

Stationarity and entropy subadditivity prove the second inequality; Jensen proves the first. Non-Haar implies D_k>0 at some finite k. Thus non-Haar invariant measures have strictly positive exponential pressure growth, strengthening #518's mere divergence conclusion.

For the original epoch envelope C_m=limsup_A P_(A,m), it suffices that

    liminf_(m->infinity) log(C_m)/m = 0.                 OPEN

This permits an unbounded subexponential envelope and only cofinally many good depths, in place of one finite all-depth bound. A factor9 boundary-transfer lemma handles atomic limits. This is class C as a weaker quantitative envelope hypothesis; under asymptotic invariance it remains equivalent to normality. No upper estimate on the actual C_m was proved. Fixed-depth finite receipts cannot supply it.
