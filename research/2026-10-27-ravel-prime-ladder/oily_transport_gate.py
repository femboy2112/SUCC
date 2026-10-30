"""The transport question: does oily-macaroni O(1/n) cancellation reach D_N(1/3)?

The proved result: Theta_n(k) = O(1/n) (exact, via 8n Theta_n -> constant).
Theta_n(k) = E_{nu_n} exp(-i t log(1+B/(8n))) is an AUXILIARY observable -- a smooth
average over the source law B.  It is NOT the orbit's Weyl sum, and NOT D_N(1/3).

The handoff's explicit warning: "It has not been transported to the selected orbit."
And the matched-moment control mu_* = (73/148) delta_1 + (75/148) delta_{89/15} shares
the first two moments (E[B]=7/2, E[B^2]=55/3) yet is non-normal.

Let me verify the matched-moment control's moment matching, and then determine the
CRUCIAL fact: does the O(1/n) cancellation of Theta_n depend ONLY on the first two
moments (in which case it CANNOT distinguish the non-normal control, and the transport
is blocked) or on the FULL source law (in which case transport might work)?

This is the exact gate the handoff demands: a proof must reject mu_* by a FULL-SOURCE
condition, not a renamed variable.
"""
import mpmath as mp
mp.mp.dps = 40

# Matched-moment control: mu_* = (73/148) delta_1 + (75/148) delta_{89/15}.
p1 = mp.mpf(73)/148
p2 = mp.mpf(75)/148
b1 = mp.mpf(1)
b2 = mp.mpf(89)/15

E_B = p1*b1 + p2*b2
E_B2 = p1*b1**2 + p2*b2**2
print("=== matched-moment control mu_* = (73/148)d_1 + (75/148)d_{89/15} ===")
print(f"  E[B] = {mp.nstr(E_B, 10)}  (target 7/2 = {mp.nstr(mp.mpf(7)/2,10)})")
print(f"  E[B^2] = {mp.nstr(E_B2, 10)}  (target 55/3 = {mp.nstr(mp.mpf(55)/3,10)})")
print(f"  moment match: E[B]={abs(E_B-7/2)<1e-30}, E[B^2]={abs(E_B2-mp.mpf(55)/3)<1e-30}")

# Does Theta_n(k)'s O(1/n) cancellation depend only on E[B], E[B^2]?
# Theta_n(k) = E exp(-i t log(1+B/(8n))), t = 16 pi k n.
# Expand: log(1+B/(8n)) = B/(8n) - B^2/(128 n^2) + B^3/(...n^3) + ...
# -i t log(1+B/8n) = -2 pi i k B + i pi k B^2/(8n) + O(B^3/n^2).
# First-order: E[exp(-2 pi i k B)] -- depends on FULL law of B mod 1, not just moments!
#   For mu_*, B is NOT uniform mod 1 (it's a 2-point law), so E[exp(-2piikB)] != 0.
#   => mu_* does NOT have the cancellation!  Theta_n(k) for mu_* does NOT -> 0.

print()
print("=== CRUCIAL: does mu_* (control) have the O(1/n) cancellation? ===")
for k in [1,2,3]:
    # Theta_n(k) for mu_* at large n -> E[exp(-2 pi i k B)] (first order, since log expansion)
    char = p1*mp.e**(-2j*mp.pi*k*b1) + p2*mp.e**(-2j*mp.pi*k*b2)
    print(f"  k={k}: E_mu*[exp(-2pi i k B)] = {mp.nstr(char,10)}  |.|={mp.nstr(abs(char),8)}  (must be 0 for cancellation)")

print()
print("=== INTERPRETATION ===")
print("The O(1/n) cancellation of Theta_n requires E[exp(-2pi i k B)] = 0, i.e. B uniform mod 1.")
print("The matched-moment control mu_* has NONZERO E[exp(-2piikB)] (B not uniform), so it LACKS the")
print("cancellation.  Therefore the cancellation does NOT depend only on the first two moments:")
print("it depends on the FULL law (B uniform mod 1), which IS a full-source condition.")
print()
print("This means the oily-macaroni O(1/n) cancellation CAN distinguish the matched-moment control,")
print("provided it transports to D_N(1/3) via the FULL source law (B uniform mod 1), not just moments.")
