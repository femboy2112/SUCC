# PREREGISTRATION ADDENDUM: source-selected continuum-radius census, N=4096 holdout

2026-11-06; committed *after exploratory* exact rational radius-grid tests at N=128,256,512,1024,2048, which are explicitly nonblind. The initial finite preregistration at 1714487e01759cf0cc43afca3b9454af04cba261 predates those initial controls but did NOT prespecify this K=3 all-radius hypothesis.

**New frozen untested holdout:** N=4096, authentic r(n), literal U0=0, exact rational states, no source mutation. For each N, let delta0=1/(N+1); radius grid starts at delta0, multiplies by 4/3 and terminates at 1/2. At each grid radius R count ALL ordered circular pairs including diagonal by sorted exact Fraction and monotone sliding window; assert (A_N(R)−N)≤(9/4)N²R, as integer cross multiplication. Since consecutive radii ratio≤4/3 and A_N(delta) is nondecreasing, this implies the full continuum inequality A_N(delta)≤N+3N²delta for EVERY real delta in [1/(N+1),1/2]. For the original rational odd denominators exactly distance 1/2 cannot occur, so ordered count covers each unordered close pair exactly twice.

**Prediction (before the new holdout):** K=3 full-radius cap PASS at N=4096. If it fails, preserve the first rational violating radius, exact A, and N and mark REFUTED FINITE for the hypothesis at N4096. If it passes, label CERTIFIED FINITE, **not** all-N source coercivity.

**Independent controls:** shadow H(n)=n/(2n−1)^4 and periodic 1/17 at N512, radius1/(N+1), expected to FAIL K3 badly. Additional raw excess-neighbor B_n(delta) one-step spikes already observed (not blind); no positivity-of-each-increment inference. All-N signed-averaged bound and π normality remain OPEN.

No new main merges, publication or claims that metric almost-everywhere theorems cover selected π.
