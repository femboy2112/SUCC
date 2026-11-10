# Finite covariance certificate and its authority

The instrument certifies finite complex rectangles. It does not prove any
asymptotic rate, source typicality, or independence assumption.

## Exact source and independent computation

For final time B, let D=lcm{8n-j:1<=n<=B,j=7,4,3,2}. Starting at S0=0,
compute Sn=16S_(n-1)+sum_j c_j D/(8n-j), with c=(4,-2,-1,-1).
Then Un(0)=Sn/D exactly, including its unwrapped integer part. The instrument
hashes every unwrapped Sn (length-delimited big-endian integers) and every
carry floor(Un)-16floor(U_(n-1)). The D hash is recorded separately; this
common-denominator representation depends on the final horizon B.

An independent algorithm checks selected circle states by the finite sum
sum_(j<=n,k) c_k (16^(n-j) mod (8j-k))/(8j-k) modulo1. This uses modular
exponentiation, not recurrence. A third check compares all states through140
against the inherited literal Fraction recurrence. It also compares principal
parts at five primes. These are independent implementations of one source;
they are not independent source families or scholarly referees.

For any representation x=N/D, write D=p^e d with p not dividing d. The
canonical p-principal part is ((N*d^(-1)) mod p^e)/p^e. This works even when
N/D is not reduced: cancellation in N removes the same p factors from the
displayed residue. Integer lifts have zero principal part.

The AR seed is selected by exact rational quantization, with the old proof
and implementation as independent controls. The receipt preserves its exact
numerator/denominator in hexadecimal and labels its failed zero and support
authentication. It cannot be silently substituted for the original source.

## Outward trigonometry

Every interval endpoint is an integer divided by 2^80. Addition is exact on
that grid; multiplication takes the minimum/maximum of the four endpoint
products and rounds outward. Division by a positive integer also rounds
outward. Complex multiplication retains both cross terms.

For exact rational turns t, select the nearest quarter q/4, leaving
u=t-q/4 in [-1/8,1/8]. A rational alternating Machin bracket encloses pi
independently of the BBP states. Therefore x=2*pi*u has |x|<=pi/4<1. Evaluate
cos through degree26 and sin through degree27 with outward Horner arithmetic.
These are also the Taylor polynomials through degrees27 and28 respectively,
since the missing coefficient is zero. Taylor's derivative remainder theorem
bounds errors by 1/28! and 1/29!, paid by outward grid units. Rotate back by
the exact quarter turn. Every step is rational/integer; float summaries are
display only. Calibration covers negative turns, quarter/eighth seams and
huge denominators, plus an independent rational Taylor oracle.

## Covariance and sparse projection

For each finite chronological epoch compute W=E e(hUn), a=E e(h[Un]_p),
b=E e(h(Un-[Un]_p)), and C=W-ab. There is **no conjugation** in this
covariance. A regression case with samples (1,i) distinguishes it from the
Hermitian covariance. The squared modulus interval is compared exactly with
16/A for the preregistered finite R4 candidate.

For a clean prime cycle, folding repeated residues gives B_j, j in Z/m.
With normalized DFT Bhat_k=E_j B_j e(-kj/m), Parseval gives
min_(support size<=s) ||B-v||2² = ||B||2² - sum of the s largest |Bhat_k|².
Using the s largest upper (respectively lower) coefficient endpoints bounds
the optimal captured energy above (respectively below), whether or not the
ordering itself is interval-resolved. Thus the reported optimum-residual
rectangle is sound. All Fourier coefficients are computed, not sampled.
The signed identity E_j a_j B_j=sum_k ahat_k Bhat_(-k) is checked against
direct source evaluation. The same computation is made for the AR control.

Finite pass labels apply only to the listed cases. A finite violation refutes
the explicit finite rate/compression proposal; it cannot refute normality.
