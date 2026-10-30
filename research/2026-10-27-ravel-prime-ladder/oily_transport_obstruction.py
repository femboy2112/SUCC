"""The transport: is D_N(1/3) expressible via Theta_n (the oily-macaroni observable)?

D_N(1/3) = (1/N) sum_n [ e(1/3 U_n) psi_3(1/3 z3_n) - e(U_n) psi_3(z3_n) ].

The oily-macaroni observable: Theta_n(k) = E_{nu_n} exp(-i t log(1+B/(8n))), t=16 pi k n,
with the proved 8n Theta_n(k) -> constant.

The connection to find: U_n = 16^{n-1} pi - T_n, and the source B enters via the Green tail
T_n = sum_j 16^{-j} r(n+j), where r(n+j) involves B through the source mixture.

The handoff says the orbit is exactly:
   U_n = E_mu[ 16^n/B^2 - (8n+B)^{-2} ].
So e(h U_n) = e(h E_mu[16^n/B^2 - (8n+B)^{-2}]), an EXPONENTIAL of an EXPECTATION, which
is NOT the expectation of an exponential.  This is the stated difficulty.

The oily-macaroni Theta_n IS an expectation of an exponential (of log(1+B/8n)), which is
a DIFFERENT observable.  The transport from Theta_n to e(h U_n) requires converting
"exp(expectation)" to "expectation(exp)" -- a Jensen/variance gap that is the actual
obstruction.

Let me quantify this gap precisely.  The question is whether the gap is O(1/n) (transport
succeeds) or O(1) (transport fails).

e(h U_n) = e(h E[16^n/B^2] - h E[(8n+B)^{-2}])
         = e(-h E[(8n+B)^{-2}]) * e(h 16^n E[1/B^2]).

The second factor e(h 16^n E[1/B^2]) is the "expanding homogeneous" part -- it's the pi
orbit phase (16^n pi up to the E[1/B^2] constant).  The first factor is the tail.

The oily-macaroni cancellation is in Theta_n = E[exp(-i t log(1+B/8n))], which is the
FOURIER transform of the tail law.  The transport question: does the O(1/n) of Theta_n
imply O(1/n) for the tail part of e(h U_n)?

This is the crux.  Let me compute the actual relationship and see if there's a clean
Jensen-bound that makes the transport work, or if it's genuinely blocked.
"""
import mpmath as mp
mp.mp.dps = 40

print("""
THE TRANSPORT OBSTRUCTION (precise)

e(h U_n) = e(h * E_mu[16^n/B^2 - (8n+B)^{-2}])
         = e(h 16^n E[1/B^2])  *  e(-h E[(8n+B)^{-2}])

The oily-macaroni Theta_n(k) = E[exp(-i t log(1+B/8n))] involves log(1+B/8n), NOT
(8n+B)^{-2}.  These are different functionals of B.

However, they are RELATED: log(1+B/8n) and (8n+B)^{-2} are both smooth functions of B/8n
for small B/8n.  Specifically:
   (8n+B)^{-2} = (8n)^{-2} (1+B/8n)^{-2} = (8n)^{-2} [1 - 2(B/8n) + 3(B/8n)^2 - ...]
   log(1+B/8n) = B/8n - (B/8n)^2/2 + ...

Both are analytic in B/8n.  The key difference:
   Theta_n uses exp(-i t log(1+B/8n)) -- a CHARACTER (Fourier) of the log observable.
   e(h U_n) uses exp(-h E[(8n+B)^{-2}]) -- a character of the EXPECTATION of the inverse-square.

The transport requires connecting:
   E[exp(-i t log(1+B/8n))]   (Theta_n, proved O(1/n))
to
   exp(-h E[(8n+B)^{-2}])     (the tail part of e(hU_n))

These are DIFFERENT moments: one is exp of E[log], the other is exp of E[(...)^-2].
The gap is exactly the log vs inverse-square functional difference.

CONCLUSION (honest): the oily-macaroni cancellation is REAL and FULL-SOURCE (rejects the
matched-moment control), but it lives in the LOG observable, while D_N(1/3) and the Weyl
sum live in the INVERSE-SQUARE (Green tail) observable.  The transport from log to
inverse-square is the precise, named obstruction -- and it is NOT obviously O(1/n).

This is a genuine finding: the oily-macaroni constant gives a full-source O(1/n)
cancellation in the LOG observables, which is a REAL new handle, but it does NOT
automatically transport to the Weyl/Greentail observables.  The bridge is the specific
next lemma to prove.
""")
