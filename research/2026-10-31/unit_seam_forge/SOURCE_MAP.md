# Source-map adequacy — what counts as the same “duck” in SUCC?

Every arrow below has a defined domain, preservation law, finite countermodel and no automatic upgrade to arithmetic normality.

| Source / representation | Actual map | Retains | Loses / condition for a valid inference |
|---|---|---|---|
| Free ordered word carrier | `word -> (a,m)` affine endpoint | exact input/output function | intermediate states, length, prestate charges; a path functional descends **iff constant on endpoint fibers** |
| Integer successor/dilation | `S=x+1`, `V_m=mx`, `V_m S=S^m V_m` | genuine integer addresses and full laws | cannot represent `47/15` BBP source translation without localization |
| Signed rational source | Original four poles, zero seed | original exact source identity | matching first finitely many jets does not identify the complete source |
| Positive Hausdorff measure | `f(z)=int u^z dmu`, `Re z>-1/8` | full original integer moments, all finite differences, canonical complex interpolation in this class | finite moments don't identify the measure; analyticity domain and choice of completion must be declared |
| Pascal/Newton atoms | `a_k=(-1)^k Delta^k r(1)` | every finite integer source value through finite binomial inversion | a finite *fixed* truncation cannot represent the whole source: `a_k>0` for all k |
| Extruded Pascal-16 | `(a_0,...,a_(N-1)) -> (U_1,...,U_N)` | full finite original source and zero seed, integral unimodularity | discarding signs/offdiagonal phase/history loses the target Fourier character |
| Green tail | `mu -> mu/(16-u)` | positive source, analytic tail, exact bound, 15-tau unit recurrence | without decay/boundedness, the 15-tau recurrence has nonunique explosive homogeneous solutions |
| Circle shadow | `alpha_J` vs `alpha=π/16` | first M complex characters within an exact source-derived bound when J=2M | fixed rational alpha_J nonnormal; J depends on M, no all-horizon π proof |
| Unit-moment successor | `(A c)_k=c_k-c_(k+1)` | shift via multiplication by u | truncating coefficients can lose future shift data |
| Unit-moment dilation | `B_m: p_m(v)^k` coefficients | actual positive-measure pushforward under u->u^m; exact diamond `A B_m=B_m A^m` | kth output requires input through mk; explicit two-measure counterexample for shallower truncation |
| Pisot extension | `Z[φ]`, two colored unit directions | Fibonacci-type exact integer path laws | Golden ratio does not become original four-pole BBP source or selected real phase by analogy |
| Real circle | `e(h U_n)` and complete signed lag/alias source | the π-normality predicate, IF all h and all horizons are controlled | no generic positive Gram, static Pascal cancellation or interval arithmetic can produce missing `o(N)` cancellation |

## Operational quotient law

Given a carrier `X`, observer report `q:X->Y`, and target `P:X->Z`, **there exists** `P_bar:Y->Z` with `P=P_bar∘q` iff P is constant on every q-fiber. For dynamical updates `F`, a well-defined descended `F_bar` requires `q(F(x))` constant on each q-fiber too. This is the same target-descent principle already used in SUCC `operational_yoneda_descent` and `prime_clock_yoneda`, not a rival new category.

**Actual counterexample to finite jet descent.** For each m>=2, define two strictly positive measures on u_j=1-j/m whose k-th Newton moments agree for all k<m. The pushforward by `u->u^m` yields first Newton moments differing by `(-1)^(m+1)m!/(2^m m^m)`. Therefore the true dilated observation is NOT constant on the original finite moment fiber. A "duck-shaped" report that forgets those higher jets is not an adequate mathematical substitute.

**Action path, not just quotient.** The free path witness stores ordered operations, actual intermediate states and a toy edge charge. The example `S;V3` vs `V3;S;S;S` has the same endpoint and different charges. An arithmetic phase transport along the original BBP path must independently show that its charge either descends or has a measured defect. Do not silently impose `q`-commutation, quantum phases or holonomy.

**Place completion firewall.** This analytic positive `mu` is real/complex and converges for `Re z>-1/8`. The same rational source has a different 2-adic completion; PR #437 proves the associated positive Laurent series is 2-adically divergent despite its rational sum being in Z2. The p-local prime clocks can be transported only by actual prime-local finite maps and proved norm bounds.
