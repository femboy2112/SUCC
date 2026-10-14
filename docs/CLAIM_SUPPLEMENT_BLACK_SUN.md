# Claim supplement: Operation Black Sun independent campaign (2026-10-14)

Branch `research/black-sun-independent-campaign-2026-10-14`. **RH PROVED: no.**
Full dossier: `research/2026-10-14/BLACK_SUN_INDEPENDENT_CAMPAIGN.md`; machine
receipt: `research/2026-10-14/BLACK_SUN_RECEIPT.json`.

| ID | Statement (actual scope) | Status | Validation |
| --- | --- | --- | --- |
| BS-A0 | Contact constant identity `int_0^inf (e^{-x/2}-e^{-x})/(1-e^{-2x}) = log2/2+pi/4`, giving `C_G = gamma+pi/2+3log2+log pi` | PROVED LOCAL | hand proof + 25-digit check, test_black_sun_window |
| BS-A1 | Windowed Carleman representation of the completed Weil form (independently re-derived; prime cutoff at `n < e^{2a}` exact) | PROVED LOCAL | flat test 25 digits; random-v within documented layer-tail bound |
| BS-A2 | Elementary barrier: `rho_a = Kbar(x+a)+Kbar(a-x)`, `Kbar(z) = 1/2 log((1+e^{-z/2})/(1-e^{-z/2})) + arctan(e^{-z/2})` | PROVED LOCAL | closed form vs series, 24+ digits |
| BS-A3 | Archimedean+pole windowed form has multiplier `Omega(u) = Re psi(1/4+iu/2)-log pi`, `Omega(0)=-C_G`, negative band exactly `\|u\| < 2pi`, asymptotic `log(u/2pi)` | PROVED LOCAL (rep) / TESTED MODEL (band edge) | digamma checks |
| BS-A4 | First-window spectrum: `lambda_min(0.36)=+8.5e-4`; `lambda_min in [0.42,1.0]` within `3e-4` of zero (sign uncertified); A-part `-0.43` rescued by prime-2; two near-nulls at Shannon `4a=2` | TESTED MODEL | Rayleigh–Ritz, M≤3200, refinement documented |
| BS-A5a | Fake-6 exactly invisible on first window, visible at `2a ≥ log 6` | PROVED LOCAL | support argument + test |
| BS-A5b | Contact error `±2log2` moves `lambda_min` by `∓2log2+o(1)`: the margin is exactly contact-bookkeeping scale | TESTED MODEL | spectrum with injected error |
| BS-A-trap | Contact tail: the `[2a,∞)` part of the Gamma/contact integral is exactly `+2 h(0) atanh(e^{-2a})`; truncation at supp(h) breaks the identity by `0.77` at `a=1/2` | PROVED LOCAL | regression locked |
| BS-B1 | Transfer `A(x)=log x+C+O(x^{-δ}) ⇒ S(x)=x+O(x^{1-δ})`, explicit constant, no positivity | PROVED LOCAL | exact Abel identity on integers |
| BS-B2 | Sharpness: spike sequences realize the worst case; `θ(δ)=δ` optimal in the nonnegative class | PROVED LOCAL | δ=1/2 constants match (worst scaled error 2.02 < 3, mass 867 vs 871) |
| BS-B3 | Two-way `Λ`-dictionary: `A(x)=log x−γ+O(x^{-δ}) ⟺ ψ(x)=x+O(x^{1−δ})`; classically ⟺ zero-free `Re > 1−δ` | PROVED LOCAL (transfer) + classical imports | E_A vs (ψ−N)/N tracking |
| BS-B4 | `D_N−(1−γ) = [A(N)−logN+γ] − E_fac(N)`, `E_fac = ½log(2πN)/N+O(N^{-2})`: the defect is a zero-detector at the same exponent | PROVED LOCAL | log N! identity 5e−48; residual ≤ 30/N at N=20000 |
| BS-C1 | Collatz defect cocycle: `2^m(word map)(x) = 3^k x + c_ε` as affine maps over ℚ; m-cycles ⟺ `n = c_ε/(2^m−3^k) ∈ ℤ_{>0}` | PROVED LOCAL | exact Fraction checks |
| BS-C2 | Valuation dictionary: no cycle element divisible by 3; `v_p(n)=v_p(c_ε)−v_p(2^m−3^k)`; `p=5` lattice condition `m ≡ 3k (mod 4)` | PROVED LOCAL | exhaustive checks m≤24,k≤12; candidates length≤16 coprime to 3 |
| BS-C3 | No nontrivial positive m-cycle for m ≤ 18 through the exact cycle equation | TESTED MODEL (exact finite certificate) | full enumeration, only trivial cycle found |

**Interaction with existing lines:** PR #70's CG6b absorption bound is
consistent with and complemented by BS-A4 (the prime-2 term rescues the
archimedean negativity to a near-null system, not to a positive-definite
one); IH-02's conditional contract is sharpened to the explicit two-obligation
program IH-2′ (elementary window inequality with κ(a) > zero-side truncation
bound) in the campaign doc §5/§9; PR #77's qualitative D_N ↔ PNT equivalence
is upgraded quantitatively by BS-B1–B4. The repo's unexplained PR #70 trial
quotient 0.0006 at a=0.54 is explained by the Shannon-number mechanism (BS-A3).

**Next verdict-changing probe:** the first-window margin lemma (campaign doc
§9): interval-arithmetic certification of `λ₀(0.36) > 0`, then the
single-prime inequality `IH-2′` via [elementary barrier BS-A2] + [rank-2
perturbation lemma] + [PR #70 CG5 exact path spectrum].