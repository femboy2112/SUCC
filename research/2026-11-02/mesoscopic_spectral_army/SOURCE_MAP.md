# Provenance and exact source-map contract

**Pinned starting branch:** SUCC draft #474 `research/line-sheet-gamma-sublog-multiprime-2026-11-02`, SHA `f60ebe5885c1de1f618d52445de77e089e841d3a` on 2026-11-02. Its base is draft #473 SHA `80dc4d8b54574e03843f198ff833e2add469422a`; #471 and #470/#468/#461 are inherited. Main XIX exact head at inspection: `81045770234a114247e43eb08ae5c6d446e9514a`. Separate #472 oily-hbar work is NOT imported and is NOT a source witness.

**Original immutable source:** `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U0=0`, `U_n=16 U_(n-1)+r(n)`. No coefficients altered; no original theorem or frozen file overwritten. BBP quotient/real completion: `alpha=pi/16=sum_(n>=1)r(n)/16^n`, `X_n=16^n alpha=U_n+T_n`, `0<T_n<1/((8n+1)(8n+2))` from #474's source-authentic Gamma derivation.

**Inherited ingredients (not new):** PGC-10 fine-to-coarse occupancy Cauchy (#473); real Gamma tail upper bound and square-checkpoint Ward/Gamma procedure (#471/#473); original simultaneous prime windows/selected cofactor and sublog self-scale condition (#474); classical Weyl criterion, Fejer kernel and PNT-AP. Paper authors Bailey–Crandall (2001), and critical orbit-equivalence caveat Lagarias (2001).

**Novel-to-this-round derived lemmas:** MSA-02 cyclic near-pair versus cell-energy bound; MSA-03 two-sided local Fejer energy bounds with stated constants; MSA-04 explicit Fourier-Hilbert difference estimate at self-scale; MSA-05 mesoscopic conditional normality for any fixed beta>0 and all prefixes; MSA-06 prime-band bookkeeping. General Fourier/Fejer tools are classical: no broader originality claimed.

**Implementation provenance:** self-contained exact rational/integer recurrences under `research/2026-11-02/mesoscopic_spectral_army`, only new files; independent online modulus and Fraction tests; no external data or pi-digit lookup in numerical certificates. The all-A source-selected mesoscopic collision theorem is not in this source map because it remains UNPROVED.
