# APHEX TWIN → SUCC: the Formula equation, the joke, the model, and its adversary

**Authorial provenance and mathematical crucible, 2026-11-09.** This is a history of a user-supplied *research prompt*, not a claim that the musician intended to describe the SUCC system. The 1999 recording, the 2011 mathematical question, the 2026 user request, the subsequent assistant interpretation, and the exact SUCC derivations are **different sources**.

> USER–DIRECT (November 9): “for fucking shits and giggles, can we make use of the aphex twin equation lmao?”

The answer was yes **as a prompt for a deliberately defined adaptive observer**, not because the track title secretly proves something about physical inverse mass, π, or quantum mechanics.

## 1. Before SUCC: what the musical source does and does not tell us

Warp Records lists track two of Aphex Twin's **Windowlicker** EP as **Formula**, released **March 22, 1999**. A printed mathematical expression served as its physical-release title; **Equation** is another conventional shorthand. It is printed on the record's reverse sleeve. It is *not* evidence of an independently documented physics theorem or a known original variable glossary.

**A commonly reproduced transcription** (the same structural reading the user brought into this conversation) is:

```math
\Delta M_i^{-1}=-\alpha\sum_{n=1}^{N}D_i[n]
\left[
\sum_{j\in C[i]}F_{ji}[n-1]
+F_i^{\mathrm{ext}}[n^{-1}]
\right].
```

**Transcription warning.** Release databases transcribe some glyphs differently (including alpha versus a derivative-like character, order of subscripts and the final index). Some entries have **n−1** where others print **n^{-1}**. An image of an original sleeve is a stronger witness to typography than OCR/database text, but the present audit has **not** independently resolved every glyph of the original printing. Preserve these source variants in a provenance note; do not quietly typeset a preferred variant as the indisputable 1999 original.

**No authenticated semantics.** The suggested meanings "inverse mass" for M, "measured displacement/error" for D, internal forces F_{ji}, and external force F^{ext} are physically plausible **guesses** from a familiar notation. A MathOverflow question in 2011 likewise displayed the formula and expressly lacked variable definitions; that discussion did not supply an authenticated origin. These hypotheses are not Aphex Twin's documented intention. The notation n^{-1} is especially unsafe to relabel as a time lag without an explicit modeling choice.

**The spectrogram footnote.** The track is independently reported to encode a picture of Richard D. James's face in its spectrogram. That is an authored time-frequency artwork. It illustrates how a different representation can disclose intentionally encoded structure, but it is NOT evidence that magnitude-only spectrograms are always invertible, that hidden real arithmetic phases follow a music encoding, or that a graphical resemblance entails a theorem.

External source family and URLs:
- Label/date/official digital title: https://aphextwin.warp.net/release/68151-aphex-twin-windowlicker
- Reissue/sleeve/track-title variants: https://musicbrainz.org/release/2166f834-752d-4623-84c5-e3ec82fb02b8 and https://musicbrainz.org/release/0a25ae72-8a79-37f4-a697-591f4364e0ab
- Open question with one transcription: https://mathoverflow.net/questions/56489/where-does-aphex-twins-windowlicker-equation-come-from
- Original sleeve visual for independent inspection: https://vinylreveals.com/blog/2021/11/30/reveal-0447-aphex-twin-windowlicker
- Reported spectrogram artwork and its context: https://www.cs.cmu.edu/~15322/book/ch10/09.html and https://mixmag.net/feature/spectrogram-art-music-aphex-twin

## 2. Actual 2026 discovery chronology: who proposed what

**(a) An independent music question.** In an earlier conversation the user asked, USER–DIRECT: “does that aphex twin song, with the name that is the equation, does the equation mean anything lmao?” The reply suggested a possible inverse-parameter update, with M^{-1} as "possibly mass," alpha a gain/learning rate, D a displacement or error, and F interacting forces. This was a *speculative interpretation*, not source-verified scientific attribution.

**(b) The connection request.** The user then pasted that explanation with the displayed formula and explicitly asked whether we could use it “for fucking shits and giggles” within the ongoing SUCC research. The user **did not** claim to have derived gradient descent from the track title. They supplied the equation and the impetus to cross-pollinate it with the pinbed.

**(c) What SUCC already had.** The user had previously proposed (USER–DIRECT) that “the Haar wavelet literally looks like a superposition of positive and negative unit succ,” then requested a joint Haar-measure and signed-wavelet assault on π normality. Earlier, the user described an embedded observer unable to leave its carrier but able to prove global asymptotics through sufficiently structured internal observations and relations. This motivated a Fourier–Yoneda pinbed of coherent probes. The BBP source/CRT parity branch provided an exact decomposition of real digit sign into a prime-local sign and a global complementary sign. **Those inputs precede the Aphex interpretation**; the song did not generate them.

**(d) Assistant steelman, carefully credited.** The assistant *chose* to define an Aphex-shaped inverse-response parameter as a feedback gain, D as a prediction residual, and the sum of internal/external F terms as authenticated source-derived feature responses. This choice is a new model, not a transcription of the musician's variables. In particular the model turns one sum into an epoch-averaged deterministic least-squares gradient, rather than claiming literal equality with the original track's unknown physical formula.

**(e) GitHub realization.** Research draft [#573](https://github.com/femboy2112/SUCC/pull/573) implemented and tested that chosen update. Draft [#574](https://github.com/femboy2112/SUCC/pull/574) established an exact *binary conditional Haar contrast* and a sharp source error budget. Codex integrated the audited ancestry in [Main XXII #575](https://github.com/femboy2112/SUCC/pull/575), keeping the zero-seed source and open mathematical statuses intact.

**(f) Why provenance now matters.** The user later explicitly asked for a provenance round that explains *how the question arose, the strongest defensible steelman, and where the intuition fails reality's tests*. That request should not be collapsed into “the Aphex equation was a known optimizer” or “SUCC derived new physics from a song.”

## 3. The strongest SUCC interpretation — after we type the symbols

Let the original zero-seeded four-pole BBP recurrence be

```math
r(n)=\frac4{8n-7}-\frac2{8n-4}
-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
```

From the authenticated original source, the real completed hexadecimal parity is factored as

```math
s_n=(-1)^{d_n}=a_n b_n.
```

Here **a_n=±1** is the selected genuine balanced-prime local parity, while **b_n=±1** is the **complete** remaining factor, retaining the 2-adic clock, every other odd-prime power, global CRT winding, inherited carry history and real Green-tail boundary correction. The complement is NOT an independently sampled random variable. In the true data, it is correlated with a_n.

For one actual source epoch [A,2A), write m=mean(a), mu_b=mean(b), x_n=a_n-m and y_n=b_n-mu_b. Introduce a chosen observer parameter \(\beta\), a reference inverse gain \(g_{\rm ref}\), and the declaration

```math
g=M^{-1}_{\mathrm{observer}}=g_{\mathrm{ref}}+\beta.
```

It is an **observer gain**, not a measurement of physical inverse mass. Define the residual \(D_n=\beta x_n-y_n\) and source feature \(F_n=x_n\). The *new* Aphex-shaped update is

```math
\mathcal L_A(\beta)=\frac1{2A}\sum_{n=A}^{2A-1}(y_n-\beta x_n)^2,\qquad
\beta_{\mathrm{new}}=\beta-\eta\left(V_A\beta-C_A\right),
```

where \(V_A=\mathrm{Var}_A(a)\) and \(C_A=\mathrm{Cov}_A(a,b)\). This is ordinary deterministic least squares. For \(V_A>0\) and \(0<\eta<2/V_A\),

```math
\mathcal L_A(\beta)-\mathcal L_A(\beta_{\rm new})
=\eta(1-\eta V_A/2)(V_A\beta-C_A)^2\ge0.
```

The minimizing coefficient is \(\beta_A^*=C_A/V_A\). Starting at zero with gain \(\eta=1/V_A\) reaches the optimum in one exact batch update. That proves an algorithmic optimization claim; **it does not prove that the arithmetic covariance tends to zero as A grows**.

**Correspondence table for the new SUCC model (not the track's historical meaning):**

| Track-title symbol | Newly declared mathematical role | Provenance limitation |
|---|---|---|
| M_i^{-1} | Observer inverse-response gain \(g_{\rm ref}+\beta\) | Not verified physical inverse mass; require positivity if modeled as such |
| \(\alpha\) | Calibrated step size \(\eta/A\) or batch \(\eta\) | Units/normalization depend on our chosen loss |
| \(D_i[n]\) | Centered predicted-minus-observed complement residual | Defined by SUCC, not known from liner notes |
| \(F_{ji}\) | Internal signed source/Haar interaction features | Requires a real authenticated observation map |
| \(F_i^{ext}\) | Exogenous original BBP forcing/carry/prime observation | Actual source constraints must be preserved |
| \(C[i]\) | Declared graph of incident probe channels | Cannot invent missing information/rank |
| Time index | Source history/lag *in a defined implementation* | The original n^{-1}/n−1 ambiguity survives |

## 4. The genuinely exact result: the gain is a binary Haar contrast

Condition on the **actual two values of the prime-sign feature**. Write

```math
u_+=\mathbb E_A[b\mid a=+1],\qquad
u_-=\mathbb E_A[b\mid a=-1].
```

If both fibers contain observations, the optimizer identity becomes

```math
\boxed{\beta_A^*=\frac{u_+-u_-}{2}}.
```

This is a **signed two-fiber Haar detail** of the complementary response. It is not the full 16-child future-conditioned Haar measure of [#565](https://github.com/femboy2112/SUCC/pull/565). Define the *common* response \(t=(u_++u_-)/2\). Direct two-point probability algebra gives

```math
\mathbb E_A[b]=t+m\beta,\qquad
P_A:=\mathbb E_A[ab]=\beta+mt,\qquad
\mathrm{Cov}_A(a,b)=(1-m^2)\beta.
```

Therefore the **sharp finite parity certificate** is

```math
\boxed{|P_A-\beta_A^*|\le |m_A|}.
```

The bound is sharp: if b is constantly +1 and m≠0, then beta=0 but P=m. A source-specific estimate for the prime-local mean m supplies a rigorous **instrument approximation error**. By #554/#572, that estimate is itself **conditional on imported prime-selection and exponential-sum theorems**. It does NOT give beta→0.

The optimal conditional residual half-energy is exactly

```math
\mathcal L_{\min}
=\frac12\left[p_+(1-u_+^2)+p_-(1-u_-^2)\right].
```

For approximate complement readouts with mean absolute error epsilon, the conditional contrast moves by at most \(\varepsilon/(1-|m|)\). This is a paid observation-precision result, NOT a proof that the true complementary sign mixes.

## 5. The exact finite source receipt — not an asymptotic experiment

The pre-registered original-zero BBP study in [#572](https://github.com/femboy2112/SUCC/pull/572) examined 512 source times on [512,1024), selecting p=1217. No new digit holdout was opened for #573/#574; the same earlier data were reused.

| a (prime sign) | b=+1 | b=−1 | Row total |
|---|---:|---:|---:|
| +1 | 133 | 121 | 254 |
| −1 | 125 | 133 | 258 |

The exact finite values are

```math
m=-\frac1{128},\quad
u_+=\frac6{127},\quad u_-=-\frac4{129},
\quad\beta^*=\frac{641}{16383},\quad
P_A=\frac5{128}.
```

The true finite calibration gap is \(|P_A-\beta^*|=133/2097024\). This is smaller than the paid upper bound \(1/128\). The conditional fitted half-loss is \(1046843/2097024\). The prime p-local sample visited 76 out of 1217 residues with large **positive** collision pressure while its signed prime-parity mean was −1/128. Signed cancellation and positive concentration measure different effects.

The receipt establishes exactly those finite numbers and their source selection, no global rate and no academic novelty.

## 6. The adversarial reality check that MUST stay in the story

#572 constructs an explicit **epoch-dependent p-integral rational wrong seed**, using the authentic four-pole forcing but changing initial condition. On the tested epoch it preserves the selected p-local source sign and 2-adic clock, yet gives **all even completed real digits**. For this control, \(b_n=a_n\), so

```math
u_+=1,\quad u_-=-1,\quad
\beta^*=1,\quad P_A=1,\quad\mathcal L_{\min}=0.
```

**Perfect observer prediction fits a maximally parity-biased trajectory.** This kills the claim that lowering prediction loss, making the residual small, or calibrating inverse gain is sufficient to make the carrier Haar. The failed inference has an exact witness; the original-zero conjecture remains untouched.

The counterseed depends on the epoch. It is not a fixed new rational seed shown to make π nonnormal for all times. Indeed the repository distinguishes **fixed rational seed shifts**, which preserve normality status through Wall's rational-addition invariance, from the irrational globally coherent seed and epoch-dependent finite-horizon spoofing controls. Never erase that distinction.

Additional reality checks:
- **Retrospective leakage.** Fitting beta uses the complement b, which is itself derived from the real digit parity. The fitted coefficient is a *representation of the answer*, not a source-only prediction of an unknown future answer.
- **Calibration gauge.** Changing the units of x rescales beta without changing the predictive observable. The coefficient only has meaning with a declared probe normalization.
- **Missing rank cannot be learned away.** Diagonal gain adjustment cannot restore a channel absent from the source-observation matrix; the balanced prime epoch had to change actual probe geometry.
- **Wrong "Haar" object.** A binary conditional Haar detail is not a 16-branch full-tail law, a real-circle Haar measure or normality.
- **Wrong "Fourier" object.** The digit parity character h=8 on Z/16 is a discontinuous step function of the real phase, NOT the continuous Weyl character \(e(8x)\). Its circle Fourier series has infinitely many modes and jump conventions.
- **Spectrogram analogy is bounded.** A visible image in a spectrogram is an authored encoding. A sound-derived observation surface with missing phases is not automatically invertible, and no physical mass coupling is established by such an image.

## 7. The strongest remaining theorem; pass, fail and ambiguous outcomes

Under the explicitly imported balanced-prime local estimate \(m_A\to0\), the true original-zero hexadecimal parity balance is equivalent to

```math
\boxed{
\beta_A^*=\tfrac12\left(
\mathbb E_A[b\mid a=+1]-
\mathbb E_A[b\mid a=-1]\right)\longrightarrow0.
}
```

This is **OPEN**. To improve on the representation rather than rediscover it, a new source-authenticated proof must control these conditional complementary responses using all old prime powers, winding, original zero seed, carries, temporal ordering and Green-tail boundaries—without reading the target real parity and without assuming independence.

**PASS:** a rigorous all-integer-epoch original-zero signed saving, with rates and source assumptions, and a clear reason the p-integral coherent wrong seed fails the proof.

**FAIL:** an explicit countermodel destroys the proposed new intermediate inequality, or the bound applies equally to the wrong seed.

**AMBIGUOUS:** fixed finite windows show small fitted beta, optimization converges rapidly, numerical covariance is small, or an observer predicts the previously inspected digit block well. These are reproducible diagnostics, not the needed theorem.

Even a proved **parity** balance would not imply base-16 normality. The other first-digit characters and all finite word frequencies remain distinct obligations.

## 8. Credit, verdict and the story we must not overwrite

- **User originality:** curiosity about the musical equation, willingness to repurpose a foreign mathematical shape, the prior signed successor/wavelet and Yoneda pinbed intuitions, demand for honest source-relative certification.
- **Assistant interpretation:** defining a new inverse-response/least-squares observer and attaching the mysterious symbols to specific SUCC measurements; the mapping was proposed, NOT recovered from Aphex Twin or derived by the user.
- **Classical imports:** least squares and gradient descent, Haar contrasts, Fourier on finite groups, source-specific exponential-sum machinery from mathematical literature.
- **Repo result:** exact binary two-fiber contrast, sharp finite error, source-compatible spoofing controls, signed covariance as an honest remaining problem; tested/merged through Main XXII with scoped analytic status.
- **Unpaid claim:** original-zero all-epoch signed complementary contrast tending to zero. Base-16 π normality and RH remain OPEN.

**Final verdict:** an apparently whimsical question generated a mathematically legitimate, falsifiable **measurement architecture**. Its strongest conclusion concerns the exact information the observer can certify and the exact error it must pay. The intuitive leap from adaptive fitting to real arithmetic mixing **failed** under an explicit source-preserving countermodel. The broader strategy—build an internally valid relational probe that may one day support a global proof—**survives as a program**, not as an already solved theorem.
