"""Test whether the oily-macaroni cancellation transports to the discriminating defect D_N(1/3).

The proved moving-frequency cancellation (oily macaroni):
   Theta_n(k) = Psi_n(2 pi k a), a = 8n, and
   8n * Theta_n(k) -> -7/2 - i/(2 pi k).
So Theta_n(k) = O(1/n), i.e. the auxiliary source pushforward has EXACT 1/n cancellation.

The question: does D_N(1/3) -- my coupled (real x 3-adic) solenoid defect -- inherit a
sublinear rate from this?  Or does the transport fail (as the handoff warns)?

Let me first REPRODUCE the oily-macaroni cancellation exactly, then check the transport.

The source: B = K + V, K in {0,1}, V uniform [0,1], with the exact law giving
E[B]=7/2, E[B^2]=55/3.  eta_n = E_{nu_n} log(1+B/(8n)) ~ 7/(16n).

Theta_n(k) = E_{nu_n} exp(-i t log(1+B/(8n))) with t = 2 pi k * 8n.
Claim: 8n Theta_n(k) -> -7/2 - i/(2 pi k).

Let me verify this limit numerically (exact rational where possible), then test whether
the SAME structure appears in D_N(1/3).
"""
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi
e = lambda x: mp.e**(2j*mp.pi*x)

# The source law for B: B = 1 + V where V ~ uniform[0,1]?  E[B]=7/2 means E[K+V]=7/2.
# From the handoff: B=K+V with V independent uniform unit cell, E[B]=7/2, E[B^2]=55/3.
# E[K] = 7/2 - 1/2 = 3, so K is NOT in {0,1} with E=1/2.  Let me derive K's law:
# E[B]=7/2, E[V]=1/2, so E[K]=3.  E[B^2]=55/3, E[V^2]=1/3, E[V]=1/2:
# E[B^2]=E[K^2]+2E[K]E[V]+E[V^2] = E[K^2] + 2*3*(1/2) + 1/3 = E[K^2]+3+1/3.
# So E[K^2] = 55/3 - 10/3 = 45/3 = 15.  E[K]=3, E[K^2]=15, Var=6.
# K = 3 + (something)?  Actually the exact source: K takes values giving B in specific cells.
# The "d,v" pairs are (3,2),(4,1),(5,1): the source is a mixture over B in cells [8j-7, ...].

# Rather than reconstruct the full source, verify the KEY asymptotic directly from the
# handoff's stated formulas, then focus on the transport question.

# eta_n ~ 7/(16n).  Verify: eta_n = E log(1+B/(8n)), expand log(1+x)=x-x^2/2+...
# = E[B]/(8n) - E[B^2]/(2*64 n^2) + ... = 7/2/(8n) - (55/3)/(128 n^2) + ...
# = 7/(16n) - 55/(384 n^2) + ...  matches eta_n ~ 7/(16n).  GOOD.

# Theta_n(k) = E exp(-i t log(1+B/(8n))), t = 2 pi k * 8n = 16 pi k n.
# log(1+B/(8n)) = B/(8n) - B^2/(128 n^2) + ...
# exp(-i t [B/(8n) - B^2/(128 n^2)]) = exp(-i 16pi k n * B/(8n)) * exp(i 16pi k n B^2/(128 n^2))
# = exp(-2 pi i k B) * exp(i pi k B^2/(8n)).
# So Theta_n(k) = E[ exp(-2 pi i k B) * exp(i pi k B^2/(8n)) ].
# As n->inf, the second factor -> 1, so Theta_n(k) -> E[exp(-2 pi i k B)] = char function of B.
# But the handoff says 8n Theta_n(k) -> -7/2 - i/(2 pi k), so Theta_n(k) -> 0.
# That means E[exp(-2 pi i k B)] = 0, i.e. B mod 1 is uniform (Haar) -- consistent with
# "B modulo one is Haar" from the handoff.  So the FIRST order vanishes, and 8n*Theta_n
# captures the SECOND order = -7/2 - i/(2 pi k).

# Verify: E[exp(-2 pi i k B)] with B = K+V, K integer (so exp(-2pi i k K)=1), V uniform:
# E[exp(-2pi i k B)] = E[exp(-2pi i k V)] = integral_0^1 exp(-2pi i k v) dv = 0 for k!=0. GOOD.
# Second order: 8n * E[ exp(-2pi i k B) * (i pi k B^2/(8n)) ] = i pi k * E[ B^2 exp(-2pi i k B) ].
# = i pi k * E[ (K+V)^2 exp(-2pi i k V) ]  (since K integer, exp(-2piikK)=1)
# = i pi k * [ K^2 E[e^{-2piikV}] + 2K E[V e^{-2piikV}] + E[V^2 e^{-2piikV}] ].
# E[e^{-2piikV}] = 0.  E[V e^{-2piikV}] = -1/(2 pi i k) (standard).  E[V^2 e^{-2piikV}] = ?
# Standard: int_0^1 v^2 e^{-2pi i k v} dv = 1/(2 pi^2 k^2) + ... let me compute numerically.

print("=== verify oily-macaroni: 8n Theta_n(k) -> -7/2 - i/(2 pi k) ===")
for k in [1,2,3]:
    # 8n Theta_n(k) -> limit.  Compute limit via the second-order expansion.
    # limit = -7/2 - i/(2 pi k).  Let's check against direct numerical quadrature.
    # E[V e^{-2piikV}] = -1/(2 pi i k) = i/(2 pi k).  So -i/(2 pi k)?  sign check.
    # 8n Theta_n -> i pi k * 2 * E[K] * E[V e^{-2piikV}]  (the 2K cross term, K=E[K]=3)
    # = i pi k * 2 * 3 * (i/(2 pi k)) = i pi k * 6 * i/(2 pi k) = -6/2 = -3.
    # Plus K^2 term: i pi k * E[K^2] * 0 = 0.  Plus V^2 term.
    # So far -3 (from 2K cross = -6/2=-3? let me recompute: i*pi*k*6*i/(2pi k)= -6/2 = -3). 
    # The V^2 term gives the remaining -1/2: E[V^2 e^{-2piikV}] integral.
    import mpmath as mp
    def E_Vsq(k):
        return mp.quad(lambda v: v*v*mp.e**(-2j*pi*k*v), [0,1])
    v2 = E_Vsq(k)
    cross = mp.mpc(-3)  # from 2*K*E[V e^{-2piikV}] with K=E[K]=3 -> -3
    v2term = mp.mpc(0,1)*pi*k * v2
    limit = cross + v2term
    expected = mp.mpc(-7,0)/2 - mp.mpc(0,1)/(2*pi*k)
    print(f"  k={k}: 8n Theta_n limit (computed) = {mp.nstr(limit,10)},  expected -7/2-i/(2 pi k) = {mp.nstr(expected,10)}")
