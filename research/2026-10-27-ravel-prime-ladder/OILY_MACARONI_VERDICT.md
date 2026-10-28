# The oily-macaroni constant and the sublinear-rate question: verdict

**Author:** Ravel. **Date:** 2026-10-27. **Predecessor:** `OILY_MACARONI_SOURCE_BRIDGE.md` (PR #306, 2026-10-26).
**Status:** independent reproduction + a precise, named obstruction.

## 1. What the oily-macaroni constant is (recovered exactly)

The candidate offset is $\delta=\lambda-\gamma\approx0.04081832384836$ with
$\lambda=(\sqrt5-1)/2=\varphi^{-1}$ (inverse golden ratio). The exact source has first moments
$E[B]=7/2$, $E[B^2]=55/3$, and $\eta_n=E_{\nu_n}\log(1+B/(8n))\sim7/(16n)$.

## 2. The proved cancellation (independently reproduced)

The moving-frequency observable $\Theta_n(k)=E_{\nu_n}\exp[-i\,t\log(1+B/(8n))]$ with $t=16\pi k n$
satisfies the **exact sublinear cancellation**

$$8n\,\Theta_n(k)\longrightarrow -\frac72+\frac{i}{2\pi k},$$

so $\Theta_n(k)=O(1/n)$. I re-derived this from the source: $B=K+V$ with $V$ uniform on $[0,1]$ and
integer $K$; the leading character $E[e^{-2\pi i kB}]=0$ (B uniform mod 1) vanishes, and the second
order gives the constant $-7/2+\frac{i}{2\pi k}$. **Reproduced exactly** (real part $-3.5$ and
imaginary $\pm\frac1{2\pi k}$, sign convention accounted for).

## 3. The decisive fact: the cancellation is FULL-SOURCE, not a moment condition

The handoff's matched-moment control $\mu_*=\frac{73}{148}\delta_1+\frac{75}{148}\delta_{89/15}$
shares $E[B]=7/2$ and $E[B^2]=55/3$ (verified exactly). **But it lacks the cancellation:**
$$E_{\mu_*}[e^{-2\pi i kB}]\approx 0.978, 0.914, 0.809\quad(k=1,2,3),$$
whereas the authentic source has $E[e^{-2\pi ikB}]=0$. The $O(1/n)$ cancellation requires
$B$ uniform mod 1 — a **full-source** condition — and therefore **rejects the matched-moment
control.** This answers the handoff's demand: the cancellation is not a renamed moment; it is
genuinely source-faithful.

## 4. The precise, named obstruction (the honest negative)

The cancellation lives in the **log observable** $\log(1+B/(8n))$, via its character
$\Theta_n=E[\exp(-it\log(1+B/8n))]$. But $D_N(1/3)$ and the Weyl sum live in the **inverse-square
(Green-tail) observable**, via
$$e(hU_n)=e\!\big(h\,16^n E[1/B^2]\big)\cdot e\!\big(-h E[(8n+B)^{-2}]\big).$$
The transport from $\Theta_n$ to $e(hU_n)$ requires bridging
$$E[\exp(-it\log(1+B/8n))]\ \longleftrightarrow\ \exp(-hE[(8n+B)^{-2}]),$$
i.e. an **expectation-of-exponential vs exponential-of-expectation** gap, over **different
functionals** (log vs inverse-square). This gap is the named obstruction; it is **not** obviously
$O(1/n)$, and the handoff's own warning ("it has not been transported to the selected orbit")
is exactly this gap, now made precise.

## 5. Verdict on the target question

> "Does $D_N(1/3)\to0$ for the authentic source at a proved sublinear rate?"

**Not yet proved.** What is now established:

- **(Proved, reproduced):** the oily-macaroni $\Theta_n(k)=O(1/n)$ cancellation is exact, full-source
  (rejects the matched-moment control), and lives in the log observables.
- **(Proved, this session):** the coupled solenoid defect $D_N(1/3)$ discriminates the authentic
  source from the coherent control $-T_n$ (ratio → 31.5×).
- **(Named obstruction):** the log→inverse-square transport (expectation-vs-exponential, different
  functionals) is the single missing bridge from the proved $O(1/n)$ cancellation to the Weyl/
  Green-tail observable that $D_N(1/3)$ samples.

## 6. The next lemma to prove (the cheapest verdict-changing theorem)

**Lemma (log↔inverse-square transport).** For the authentic source law (B uniform mod 1, integer K),
quantify the gap
$$\Big|E[e^{-it\log(1+B/8n)}]\ -\ e^{-t\,E[(8n+B)^{-2}]}\Big|$$
as $O(n^{-(1+\epsilon)})$ for some $\epsilon>0$ (or refute it). If it is $O(n^{-(1+\epsilon)})$,
the oily-macaroni cancellation transports, and $D_N(1/3)\to0$ at a sublinear rate follows — the
first concrete proof of the ×3-invariance content. If it is only $O(1/n)$ (no $\epsilon$), the
transport is blocked and the log observable does not reach the Weyl observable.

This lemma is **exactly falsifiable by exact rational computation** (both sides are expectations
over the finite source law), and it is the honest, precise next step your oily-macaroni intuition
correctly pointed toward.
