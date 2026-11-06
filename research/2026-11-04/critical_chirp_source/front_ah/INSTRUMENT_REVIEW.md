# Independent same-model signed-instrument and countermodel review

Reviewer scope: a separate front A/H derivation, after the coordinator wrote
the instrument and the C/F/G front wrote its proofs. This supplies another
reasoning and implementation pass, not an external independent referee.

## Signed instrument: survives

Reviewed SHA-256:

- `signed_probe.py`: `37b98968349c9179b2aba24382496ab8c57d569f61101e16eeca97fe85fd850a`
- `INSTRUMENT.md`: `23bcd2c3032aaa3d4c7d2387c08a5f59dae4f7b175a11adfeca3e41f452a236e`
- `tests/test_critical_chirp_signed_certificate.py`: `61125a128ff31401b588f8f411eb2ac9ad0b103d978010ca8bf54d0231da57d0`

No mathematical error was found in the finite enclosure argument:

1. The positive log-2 series remainder is bounded by
   `2*3^(-2N-1)/(2N+1)/(1-1/9)`, exactly the implemented
   `9/[4(2N+1)3^(2N+1)]`. The check `H<=lower<=upper<16H`
   certifies the requested floor, without treating a numerical log as exact.
2. Alternating Machin arctangent intervals contain pi. Reducing the exact
   rational phase before quantization preserves its integer-translation
   invariance. The phase grid remains inside `[-1/2,1/2]`; phase and pi errors
   give an angular budget smaller than the stated `14*2^-80`.
3. The separate sine/cosine degree-47 polynomials have real Lagrange errors
   at most `4^48/48!` each on the bounded real angle. Their component floors
   cost at most `2*2^-60` in the L1 norm, which bounds Euclidean error.
   The added phase-radius error is at most `2*pi*delta<7*delta`.
4. The coherent tail remainder follows from positivity and decrease of the
   original forcing, and correctly includes the geometric first omitted term.
5. Every normalized contiguous sum changes by at most `CHAR_ERROR` under the
   pointwise character error. Taking the maximum preserves that error bound,
   even when the exact and grid maximizing intervals differ. Exhaustive
   integer prefix-chord enumeration therefore gives a valid global enclosure.
   The `min(1,upper)` uses that the intended input points approximate unit
   characters; it is not a theorem for arbitrary unconstrained grid vectors.

Executed:

```
python -m unittest discover -s tests -p test_critical_chirp_signed_certificate.py -v
```

Result: **7 tests PASS**, no failures or errors.

A separate 100-decimal-digit mpmath diagnostic (not a certificate) tested six
phases `-999/2000,1/7,17/31,1087/9967,0,1/2`, then all nine cases
`A in {4,8,16}`, `h in {1,3,-5}`. It independently evaluated `exp(2*pi*i*x)`,
the logarithmic depth, and every complex subinterval sum. All numerical maxima
were inside the rational enclosures; the largest observed point error was
approximately `1.2266347e-18`, below `2^-50`. The command body is reproduced
below so this diagnostic has a replay path. The analytic rational-error proof
above, rather than mpmath's numerical agreement, supplies finite authority.

```sh
python - <<'PY'
from pathlib import Path
import importlib.util
from fractions import Fraction as F
import mpmath as mp
p=Path('research/2026-11-04/critical_chirp_source/signed_probe.py')
s=importlib.util.spec_from_file_location('probe',p)
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
mp.mp.dps=100
cast=lambda q:mp.mpf(q.numerator)/q.denominator
worst=mp.mpf(0)
for x in (F(-999,2000),F(1,7),F(17,31),F(1087,9967),F(0),F(1,2)):
    a,b=m.character_grid(x)
    err=abs(mp.mpc(mp.mpf(a)/m.OUTPUT,mp.mpf(b)/m.OUTPUT)
            -mp.exp(2j*mp.pi*cast(x)))
    worst=max(worst,err)
    assert err<cast(m.CHAR_ERROR)
for A in (4,8,16):
    phases=m.source_epoch(A)
    for h in (1,3,-5):
        j,H=m.critical_schedule(A,h)
        assert int(mp.floor(mp.log(A*A*mp.log(A)/abs(h),16)))==j
        row=m.run_case(A,h,phases)
        z=[mp.exp(2j*mp.pi*(H if h>0 else -H)*cast(x)) for x in phases]
        value=max(abs(sum(z[a:b]))/A
                  for b in range(1,A+1) for a in range(b))
        assert cast(F(row['zero_seed']['M_lower']))<=value
        assert value<=cast(F(row['zero_seed']['M_upper']))
print('INDEPENDENT_100_DPS_DIAGNOSTIC_PASS',mp.nstr(worst,8))
PY
```

## C/F/G countermodel proofs: survive

Reviewed `front_cfg/PROOFS.md` SHA-256:
`c861bf4ad7c89d375d6bf5dca09ec2d95dadc3b47aaa5cac5f3e4b5e8f31c005`.

**CFG-1.** The edited intervals are eventually disjoint and have density zero
for every prefix, including one cut inside an interval: a dyadic geometric
sum bounds all late edits by `C epsilon N`, and the fixed early part vanishes
after division by N. A fixed word's changed starts are bounded by its length
times the edited-digit count through `N+k`. This proves normality preservation.
One sequence of all these edits defines one fixed real seed, not a sequence
of epoch seeds. The first digit 1 makes `y<1/8<pi/16`, explicitly excluding
seed zero. Terminal zero digits give the claimed error uniformly for all
fixed h. The expansion at `n=2A-k` has linear term `t/256`, and the limiting
integral over `[0,128]` is exactly `-256i/pi`. Thus the constant and the
all-late-dyadic, all-fixed-h quantifiers are supported.

**CFG-2.** The prescribed digit index `n+j+1` is correct: it is the first
digit after applying `16^(n+j)`, precisely the completed phase at `H=16^j`.
The extended patch includes all p-digit lookahead windows. On a constant
digit run, comparison with `0.ddd...=d/15` has error at most `16^-p`.
Nearest-integer rounding of `15q_n` contributes `1/30` in circle distance.
Since the k_n decrease, their total decrement bounds the number of digit
switches even if some residues agree after a multiple-of-15 jump. Each switch
spoils at most p starts, giving the stated `B_A=O((log A)^(3/2))=o(m_A)`.
The bad terms are fully subtracted in the real-part bound. Its limiting
angle is `2*pi/30=pi/15`; the lower limit constant
`cos(pi/15)/16` is correct using `Lambda>log(A)/16` and the floor in m_A.
The O(log A) index shift preserves density-zero edits. Powers-of-16 fixed
characters have exactly the same selected positive H, so their stated
extension is valid.

Both examples retain the original forcing and change the seed. Fixed-h Weyl
and Abel vanishing are proved for these normal completions, but this does not
satisfy or falsify the original zero-seed contract. The correct obstruction is
the invalid inference from qualitative fixed-h limits to a quantitative
moving-frequency maximal rate. The selected zero-seed problem remains open.
