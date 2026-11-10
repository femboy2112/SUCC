# SUCC zero-origin statistical walk and spectral flux — complete finite theorem dossier

**Status, 2026-11-08:** Finite exact identities and rational source-digit certificates; exploratory finite numerical spectra. **π base-16 normality remains OPEN.** The user asks for a conservation/redistribution model that permits local digit clumps but detects persistent organization. This dossier distinguishes an exact **constant-norm increment law** from an unproved **restoring-force hypothesis**. No conjectural asymptotic decay is promoted from a finite trace.

## ZOS-01 — literal four-pole zero-source and digit origin (imported classical BBP + proved certificate algorithm)

Retain exactly

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

The already-proved Green identity from the authentic BBP series is

\[
U_n+T_n=16^{n-1}\pi,\qquad T_n=\sum_{j\ge1}16^{-j}r(n+j),\quad0<T_n\le r(n+1)/15.
\]

Thus hexadecimal fractional digit \(d_n\) (1-indexed) is the unique integer in \(\{0,\ldots,15\}\) represented by \(\lfloor16\{U_n+T_n\}\rfloor\). The module preserves \(x_n=\{U_n\}\) exactly as a `Fraction` and tests both endpoints of a rational enclosure for \(T_n\); if a digit boundary is crossed it increases the exact tail depth, otherwise it certifies the digit. A failed enclosure aborts rather than inventing digits. Note that `floor(16(x_n+t)) % 16` works even if the positive tail crosses the circle's zero boundary.

**Finite observation:** all first 16,384 digits were certified (zero extra tail refinements in this finite run); independent rational Machin intervals confirm the first 128 digits. A finite prefix does not establish normality, even at any fixed word depth. The classical BBP identification, not the script alone, identifies this number with π.

## ZOS-02 — conserved local step size, signed global interference (PROVED algebraically)

Fix a finite alphabet of \(B=16^k\) length-\(k\) words and a chronological list \(w_1,\ldots,w_M\). Let \(e_w\) be the standard basis and \(u=B^{-1}(1,\ldots,1)\), and let

\[
R_M=\sum_{i=1}^{M}(e_{w_i}-u),\quad D_k(M)=\|R_M\|_2^2.
\]

Each step has **constant squared norm**

\[
\boxed{\|e_w-u\|_2^2=1-1/B,}\tag{ZOS2a}
\]

independently of the digit/word value. However the cumulative displacement energy is *not conserved*. Writing \(C_M(w)\) for the previous count of the arriving word \(w\),

\[
\boxed{D_k(M+1)-D_k(M)=1-1/B+2[C_M(w)-M/B].}\tag{ZOS2b}
\]

The second term is the signed interference/work of the new word against history. Arrival of an overrepresented word reinforces the accumulated discrepancy; arrival of an underrepresented word can reduce it. Neither the sign nor the conditional expectation of that term is fixed by mass conservation. Exactly,

\[
D_k(M)=M(1-1/B)+2\sum_{i<j}\left({\bf1}_{w_i=w_j}-1/B\right).
\tag{ZOS2c}
\]

For k>1 the windows overlap, so one may not blindly use an iid one-step conditional law. The `online_word_surplus` instrument uses **noncyclic** windows and checks this identity with exact `Fraction` at every arrival. This is the precise conservative-step/variable-interference mathematical model behind the user's suggestion.

## ZOS-03 — exact orthogonal spectral refinement, not automatic restoration (PROVED)

For a **fixed finite N**, periodize the N observed digits and count all N cyclic starts. Let \(p_{k,N}(w)\) be the empirical law on \(G_k=(\mathbb Z/16\mathbb Z)^k\), with \(\sum_a p_{k+1,N}(wa)=p_{k,N}(w)\). Define

\[
E_k(N)=16^k\sum_{w\in G_k}\left(p_{k,N}(w)-16^{-k}\right)^2.
\]

For every character \(\chi_h(w)=\exp(2\pi i\sum_j h_jw_j/16)\) and Fourier coefficient \(\widehat p_{k,N}(h)=\sum_w p_{k,N}(w)\chi_h(w)\), finite-group orthogonality and Parseval give

\[
\boxed{E_k(N)=\sum_{h\in G_k\setminus\{0\}}|\widehat p_{k,N}(h)|^2.}\tag{ZOS3a}
\]

Since \(\widehat p_{k+1,N}(h,0)=\widehat p_{k,N}(h)\), the precise **new-coordinate spectral energy** is

\[
\boxed{E_{k+1}(N)-E_k(N)=\sum_{\substack{h\in G_k\\g\in\mathbb Z/16,\ g\ne0}}|\widehat p_{k+1,N}(h,g)|^2\ge0.}\tag{ZOS3b}
\]

Character orthogonality also gives exactly

\[
\boxed{E_{k+1}-E_k=16^{k+1}\sum_{w,a}\left(p_{k+1,N}(wa)-p_{k,N}(w)/16\right)^2.}\tag{ZOS3c}
\]

The program computes these as exact rationals via integer window counts, checks equality, and never claims the PSD addition forces a downward time trend. **At fixed N, information uncovered by greater depth is nonnegative; at growing N, each energy can increase or decrease.** These are different variables and limit orders. If one instead uses ordinary noncyclic windows, the k and k+1 start sets differ by a boundary term; the script does not silently equate them.

## ZOS-04 — full temporal spectral power is conserved, not its distribution (CLASSICAL Parseval)

For a specified nonzero symbol character \(h\in\{1,\ldots,15\}\), put \(z_n=e(hd_n/16)\) and use the unnormalized N-point DFT \(\widehat z_m=\sum_{n=0}^{N-1}z_n e(-mn/N)\). Then

\[
\boxed{\sum_{m=0}^{N-1}\frac{|\widehat z_m|^2}{N^2}=\frac1N\sum_{n=0}^{N-1}|z_n|^2=1.}\tag{ZOS4}
\]

- A constant digit is a coherent DC line, power one.
- Repeating `0123456789ABCDEF` has perfectly balanced one-digit marginals but a pure *nonzero* temporal line, power one for h=1.
- Sorting a prefix preserves its one-digit count energies but can create a near-pure low-frequency line.
- A de Bruijn order-three cycle has E1=E2=E3=0 and E4=15, but is periodic and may have nontrivial temporal spectral lines.

Power conservation alone is satisfied by every one of these mutually incompatible worlds. **No no-clumping/nonconcentration theorem follows from it.** A normality theorem would require a *source-selected upper estimate* on appropriate Fourier/word modes, rather than a Parseval identity.

## ZOS-05 — signed spectroscope / no assumed compensating force (PROVED finite identity)

For any fixed symbol/temporal character pair \((h,m/q)\), define \(v_n=e(hd_n/16-mn/q)\), \(S_M=\sum_{n<M}v_n\). The update is

\[
\boxed{|S_{M+1}|^2-|S_M|^2=1+2\operatorname{Re}(\overline{S_M}v_M).}\tag{ZOS5}
\]

The signed term is **measured**, not fitted to a negative sign. Large coherent spectra reinforce, and a negative signed work records local cancellation. A period-16 sequence concentrated on the corresponding frequency has \(S_M=M\) and mean signed work proportional to M; a constant sequence has a DC line but no period-16 line. Hence test a *complete frequency family* before calling anything unbiased. Numerical output reports conditional work only with its sample count, never extrapolates tiny high-threshold bins.

## ZOS-06 — three positive BBP source channels and chronological joint phases (EXACT)

Let \(a_n=8n-7\) and \((d_i,w_i)=(3,2),(4,1),(5,1)\). Then

\[
r_i(n)=\frac{w_id_i}{a_n(a_n+d_i)}>0,\qquad \boxed{\sum_{i=1}^3r_i(n)=r(n)}.
\]

Starting all three channels at zero, \(U_{i,n}=16U_{i,n-1}+r_i(n)\) gives \(U_n=\sum_i U_{i,n}\), and

\[
\boxed{e(hU_n)=\prod_{i=1}^3e(hU_{i,n})}.\tag{ZOS6}
\]

This realizes a genuine source/phase **joint** readout, instead of multiplying independently averaged sources. It does **not** authenticate the initial real seed from the positive channels alone. The instrument independently verifies all channel fractions only through **n=1024** on the full 16,384-digit run; it tracks the full original source and certified digits at all later times without asserting unseen individual channel checks.

## ZOS-07 — exact original signed lag energy, preserving cancellation (INHERITED / RECHECKED)

For any finite original-source phase list \(f_n=e(hU_n)\), zero-extended outside the epoch of length N, the averaged moving-sum energy is

\[
\mathcal E_H=\frac1{NH^2}\sum_{t\in\mathbb Z}\left|\sum_{j=0}^{H-1}f_{t+j}\right|^2
=\frac1H+\frac2H\sum_{\ell=1}^{H-1}(1-\ell/H)\operatorname{Re}\left[\frac1N\sum_{n=0}^{N-\ell-1}f_{n+\ell}\overline{f_n}\right].
\]

Also \(|N^{-1}\sum_n f_n|^2\le(N+H-1)\mathcal E_H/N\). The script reconstructs both sides independently by temporal sums and signed lag coefficients, with numerical agreement. This is inherited from #544 and does not bound \(\mathcal E_H\) on the zero seed for all epochs. The coherent constant control gives Weyl power 1 and never passes a false-decay gate.

## ZOS-08 — finite observed shape and hostile controls (OBSERVED, reproducible)

The extension protocol was committed to GitHub **before** the 16,384-digit run. All measurements are finite, including the independent 16 shuffled baselines. Values below are **observations**, not mathematically proven asymptotics; the energies are exact rationals internally and decimals only for display.

| 16,384 samples | E1 | E2 | E3 | largest non-DC temporal power (h=1) |
|---|---:|---:|---:|---:|
| Authentic BBP U0=0 | 0.0006529093 | 0.0152759552 | 0.2445373535 | 0.000600298 |
| One same-count shuffle | 0.0006529093 | 0.0141448975 | 0.2498168945 | 0.0006313 |
| Same-count sorted | 0.0006529093 | 14.979227 | 254.168610 | 0.987072 |
| Balanced 16-periodic | 0 | 15 | 255 | 1 |
| Period-4096 de Bruijn(3) repeated | 0 | 0 | 0 | 0.088983 |
| Coherent constant | 15 | 255 | 4095 | 0 (its DC power = 1) |
| Toy spectral feedback, beta 0.65 | 0.0004823 | 0.0159302 | 0.2618713 | 0.001019 |

Sixteen same-count reshufflings had depth-2 energy range [0.0132122,0.0173569], depth-3 energy [0.236542,0.259674], non-DC peak range [0.00051235,0.00068765]. The BBP sample lies inside all three ranges; this is **not** a significance test or an iid claim. The feedback toy suppresses a chosen period-16 line but gives *worse overall peak and E3* than the BBP sample in this run. No special active compensation was demonstrated.

The earlier N=8192 exploratory run and the later N=16384 extension show decreasing **finite** discrepancies, roughly of size 1/N, but such a finite trend proves no asymptotic bound. Its statistical comparison is exploratory; neither sample is an independent mathematical witness of normality.

## ZOS-09 — the actual all-epoch frontier (OPEN)

What would really move the π-normality verdict is a proof that the authentic original-zero selected signed work or its source-corrected lag aggregate has subquadratic accumulation **for every sufficiently large integer epoch and every fixed Fourier character**, while preserved source/seed controls fail. This is essentially the Weyl criterion in another representation, so a mere reformulation is *not* a new cancellation theorem.

A plausible genuinely discriminating attack: use the three exact chronological source channels, literal base-16 integer carries and balanced prime-birth clock to *predict a signed conditional flux* at large spectral amplitude that is absent for the coherent same-forcing seed. State a quantitative source-derived inequality, test it against counterseeds and previously unused epochs, then try to derive it analytically. Such a theorem is **UNVERIFIED**. The present program is an instrument and a finite negative/positive-control baseline, not that theorem.

## Primary dependency and provenance

- Canonical four-pole source, recurrence, tail enclosure and BBP/π identification: main `observational_succ/duck_bbp.py`, `formal/duck_pi/`, original import manifest. **Source and normality remain distinct.**
- Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions*, Experimental Mathematics 10 (2001), 175–190, DOI: `10.1080/10586458.2001.10504441` — the original recurrence/normality program and its conditional dynamical hypothesis.
- Lagarias, *On the Normality of Arithmetical Constants*, Experimental Mathematics 10 (2001), 355–368, DOI: `10.1080/10586458.2001.10504456` — general shadowing occurs even in other, potentially nonnormal classes.
- SUCC #544 signed forcing-corrected lag identities; SUCC #552 three-channel positive source; #554 balanced clock; #555 pointed spectral fingerprints. This dossier does not rewrite or claim priority over them.
