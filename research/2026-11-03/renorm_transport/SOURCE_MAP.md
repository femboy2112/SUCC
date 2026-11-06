# Source map — RENORM transport

Typed dependency chain from the immutable source to this result. Every arrow is add-only;
no inherited receipt is modified.

```
original four-pole source  r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),  U_0=0,  U_n=16U_{n-1}+r(n)
        |                                   (immutable; byte-identical to main manifest a8805a8e…)
        v
exact rational epoch  x_n={U_n}, n∈[A,2A)   ──(independent odd-conductor blind evaluator; identical)
        |
        v
Fourier coefficient  c_A(h)=A⁻¹ Σ_{n=A}^{2A-1} e(hU_n)        [instrument, calibrated: c_A(0)=1]
        |
        |  arithmetic ×16 self-similarity:  e(hU_n)=e(16hU_{n-1})·e(hr(n))
        v
RENORM-1  c_A(h)=c_A(16h)+ε_A(h)             [RT-01, exact]
        |
        |  boundary ≤2/A ;  forcing ≤ 2π|h| Σr(n) ,  Σr(n)<15/(8(8A-15))  [via merged SC-6]
        v
RENORM-1 bound  |ε_A(h)| ≤ 2/A + 15π|h|/(4A(8A-15))          [RT-02, rigorous; receipt 0 violations]
        |
        |  iterate at COMMON depth j=⌊log₁₆(A^{3/2}/H)⌋ (×16 injective on ℤ, fixed j);
        |  corrected geometric accumulation 2j/A+π|h|(16^j−1)/(4A(8A−15)) = o(1) up to freq ≤A^{3/2}
        v
RENORM-2 barrier  low band → DISTINCT high band ≤A^{3/2}, each modulus preserved up to o(1)   [RT-03]
        |
        |  one-directional sufficiency (NOT ⇔): band ⟹ J ⟹ E ⟹ normal; converse J⟹band FALSE (RT-00)
        v
SC-8 gate  Σ_{1≤|h|≤q_A²}|c_A(h)|² = o(K_A)   ──►  **OPEN**  ⟹ π normal;  π normal ⟺ S_N(h)=o(N)
```

**Pins.** Source manifest blob `a8805a8e4d64f35ff61937a36755d9b6d1ba3fae` (unchanged). SC-6
numerator `P(t)=(1-t)(t²+2)(t²+2t+2)` on the merged selected-current front. No π digits enter.
