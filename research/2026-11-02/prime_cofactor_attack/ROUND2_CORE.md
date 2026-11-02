# Round 2 — f₄ edge isolation and the mixed cross-term

**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`. **Agent:** Ravel (main).

## 1. The fₘ decomposition (PROVED, exact, elementary)

The four-pole forcing admits an exact decomposition into three "difference-of-poles" pieces:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=2f_3(n)+f_4(n)+f_5(n),
\qquad
f_m(n)=\frac1{8n-7}-\frac1{8n-7+m}.
$$

Verification is the elementary identity `(2+1+1)/(8n-7) − 2/(8n-4) − 1/(8n-3) − 1/(8n-2)`. Each `f_m` is a telescoping-pair difference with asymptotics
$$
f_3(n)\sim\frac{3}{64n^2}+\frac{33}{512n^3},\quad
f_4(n)\sim\frac1{16n^2}+\frac5{64n^3},\quad
f_5(n)\sim\frac5{64n^2}+\frac{45}{512n^3}.
$$

## 2. The prime pole is isolated in f₄ (PROVED)

For `p≡5 mod 8`, birth `a_p=(p+3)/8` has `p=8a_p-3`. Then
$$
f_4(a_p)=\frac1{8a_p-7}-\frac1{8a_p-3}=\frac1{p-4}-\frac1{p},
$$
so the `-1/p` pole (coefficient `c_p=-1`) is carried **exclusively** by the `f_4` edge at `j=a_p`. The other two edges `f_3(a_p)=1/(p-4)-1/(p-1)` and `f_5(a_p)=1/(p-4)-1/(p+1)` are p-free (p-integral). Therefore, within the window `[a_p,(p+1)/2)`:

$$
U_n=-\frac{16^{n-a_p}}{p}+V_{p,n},\qquad
V_{p,n}=\underbrace{2\sum_{j\le n}16^{n-j}f_3(j)}_{f_3\text{-part}}+\underbrace{\sum_{j\le n}16^{n-j}f_5(j)}_{f_5\text{-part}}+\left[\sum_{j\le n}16^{n-j}f_4(j)+\frac{16^{n-a_p}}p\right],
$$
where the bracket is the `f_4`-tail with the single pole removed, hence **p-free**. (Each sum is the 16-geometric accumulation of its forcing edge.)

**Status: PROVED (exact rational arithmetic).** This is a *cleaner* separation than SPP-01: the clock `-16^{n-a_p}/p` and the cofactor `V_{p,n}` now come from **disjoint forcing edges** (`f_4(a_p)` vs. `f_3,f_5`, and the `f_4`-tail).

## 3. Does the isolation transfer the clock's BGK saving? (OPEN, obstruction identified)

PWI-05 (inherited) gives the isolated clock a genuine saving:
$$
\frac{|C_p(h)|}{L_p}\le\frac13+o_h(1)
$$
outside a density-zero exceptional set, via BGK on the subgroup `⟨16⟩`.

**The transfer fails for a precise reason.** The cofactor increment is
$$
V_{p,n+1}-V_{p,n}=15V_{p,n}+r(n+1),
$$
which is of the *same* magnitude as `V_{p,n}\approx16^{n-1}\pi`. There is **no slow variation**: the cofactor phase `e(hV_{p,n})` oscillates as fast as the leading lacunary phase `e(h\,16^{n-1}\pi)`. Partial summation (Abel) therefore cannot move the clock's `C_p` saving onto `W_p`: the total variation of `e(hV_{p,n})` over the window is `O(|h|\,16^{n})`, which dwarfs the window length `L_p\sim3p/8`.

**Concretely (Abel):** `W_p=\sum_n e(\text{clock})e(\text{cofactor})` with the cofactor as "weight" gives
$$
W_p=e(hV_{p,b_p})C_p(h)-\sum_{n}(e(hV_{p,n+1})-e(hV_{p,n}))C_{p,\le n}(h),
$$
and each weight difference `|e(hV_{p,n+1})-e(hV_{p,n})|\approx 2\pi|h|\,|V_{p,n+1}-V_{p,n}|=O(|h|16^n)`, whose sum over the window is `O(|h|16^{p/2})` — astronomically larger than any saving. **The transfer is blocked, not by a technicality, but by the cofactor's full lacunary magnitude.**

**Status: OBSTRUCTION PROVED (structural).** The `f_m` isolation makes the separation *cleaner* but does not make the cofactor *slower* or *smaller*; the cofactor is still a full-magnitude 16-geometric sum.

## 4. What the isolation *does* give (PROVED, negative value)

The `f_4`-isolation proves a precise **decoupling at the forcing level**: the clock and cofactor arise from *disjoint* edges of the four-pole source. This rules out a specific "conspiracy" mechanism — a conspiracy could not come from the `f_4(a_p)` term itself, because that term is *exactly* the clock and contributes nothing to `V_{p,n}`. Any re-coherence must arise from the *other* edges (`f_3,f_5`, and the `f_4`-tail), which are p-free.

But this is a **negative/structural** fact: it does not bound the cofactor's phase. It sharpens the statement "the cofactor is p-integral" into "the cofactor is p-free *and* disjoint from the pole's own forcing edge," which is necessary but far from sufficient for a signed bound.

## 5. Honest bottom line for this round

- The `f_m` decomposition and `f_4` pole-isolation are **new, exact, and PROVED** (cleaner than SPP-01).
- They **do not** transfer the isolated-clock BGK saving to the full sum — the cofactor's lacunary magnitude blocks partial summation (PROVED obstruction).
- They **do** rule out one specific conspiracy mechanism (pole-edge vs. cofactor are disjoint in the forcing).

The remaining lemma is unchanged: `\sup_{1\le|h|\le16^{m-1}}|S_N(h)|=O(N^\theta)`, `\theta<1`. π normality and RH remain OPEN.
