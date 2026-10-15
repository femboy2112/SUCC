# Residue-clock L2(w) approximation — numerical experiment receipt

Status: **TESTED MODEL / numerical observation — NOT a proof.**
Floating/interval digits are not a certificate; no rigorous error bounds were attached.

Task: compute the optimal L2(w) approximation error of the constant 1 by the first N
residue clocks r_n(k) = (k mod n)/n, weight w_k = 1/(k(k+1)).

## Setup and method (exact statement)

- Inner product <f,g> = sum_{k>=1} f(k) g(k) / (k(k+1)); note <1,1> = 1 (telescoping).
- E_N* = min_{a_2..a_N} || 1 - sum a_n r_n ||^2 = 1 - b^T G^{-1} b,
  G_{mn} = <r_m, r_n>, b_n = <1, r_n>.
- Periodicity: r_m r_n has period L = lcm(m,n), so
  G_{mn} = sum_{r=0}^{L-1} (r mod m)/m * (r mod n)/n * S_r(L)
  with S_r(L) = sum_{k>=1, k==r mod L} 1/(k(k+1)), a digamma-type sum.
- S_r(L) computed in closed form: S_r(L) = (1/L)[ psi((k0+1)/L) - psi(k0/L) ],
  k0 = r if r>=1 else L.  (mpmath psi, dps = 60.)

## Instrument calibration (all passed)

1. Identity sum_{r=0}^{L-1} S_r(L) = 1 for L in {2,3,4,5,6,7,8,12,60,420}: exact 1.0.
2. Independent-route cross-check S_r via mp.nsum (convergence-accelerated) vs digamma:
   max |diff| = 3.889384548663213567e-62 over all r, L in {2..8,12,60}.
3. N=2 closed form (the task's receipt):
   computed a_2 = 2.0 (expected exactly 2), G_22 = ln2/4, b_2 = ln2/2,
   E_2* = 0.3068528194400546905827678785418234319244998656397447459 = 1 - ln 2 exactly
   (|E_2* - (1-ln2)| = 0.0 at 60 dps).
4. Second implementation of every E_N*: direct residual norm
   E = sum_{r=0}^{L-1} (1 - sum_n a_n (r mod n)/n)^2 * S_r(L) with S_r via mp.nsum.
   Agreement with the matrix-inverse route: |diff| <= 1.31e-61 for all N = 2..8.
5. Identity E_N* = 1 - sum_n a_n b_n verified for all N (diff <= 7.8e-62).

## DATA — optimal error E_N* (50 significant digits, dps=60)

N   E_N*
2   0.30685281944005469058276787854182343192449986563974
3   0.095747783927754026614308119340147090031056908828729
4   0.06595169421556965355895907941992572044740051585557
5   0.036319017938186960474227491357509818063943729552671
6   0.036208034636905628401748853208189281039144137050035
7   0.024388367885244006446141660284248660931035252186411
8   0.024244525306522673148205833167911204995277936381056

## Optimal coefficient vectors a_n (n=2..N)

N=2:  a_2 = 2.0
N=3:  a_2 = 1.1567613541518938296940904988331633805980906623922
      a_3 = 1.3745047793255554457207041305715306612355155406931
N=4:  a_2 = 0.86355783829985439237186030616120886812894056266905
      a_3 = 1.0611747691774172100657193290231514087055996292071
      a_4 = 0.7102544018735938306619820994123093803083727155197
N=5:  a_2 = 0.86348483073811287687077928404954519512010846132509
      a_3 = 0.86780828339604185276609037368277847987726574506945
      a_4 = 0.29805194078596790578914599202525729885808656280514
      a_5 = 0.755941136085435294775295462172767991115907502146
N=6:  a_2 = 0.86730913148417387689672833428178696717153344052617
      a_3 = 0.88453241646964347274530117914452493953269316122447
      a_4 = 0.30413793733136776422562936493750034243166556431633
      a_5 = 0.78112610823151188616570660580417516265814799528861
      a_6 = -0.058785256000071168986171096186882019522259807978712
N=7:  a_2 = 0.89399780493897096110105203652018145792006241943962
      a_3 = 0.89678325578038973711434488190505427294281696603452
      a_4 = 0.19585319902172897259801525467930808665853529576912
      a_5 = 0.67578479328628601850669596133871920782089076260323
      a_6 = -0.39971338905073091865015839571545622377540367668546
      a_7 = 0.61632580726199276596343004627844909725579961676807
N=8:  a_2 = 0.89645409597514262276960184968891844086186518487603
      a_3 = 0.90041776346193444739039683974009175279563690765376
      a_4 = 0.17174089171974144926801165104683638730433240139454
      a_5 = 0.67361995567602614655825706582064993308872561741167
      a_6 = -0.41102335440658936811530140146360471882432743914864
      a_7 = 0.57747949387686661182494382444745916131831981596046
      a_8 = 0.081527048319300140172810797073809498908283842388908

## SECONDARY — error under fixed Baez-Duarte-type coefficients a_n = -mu(n)/n

N   constrained E
2   0.6967481085050239271299609468620477514669686912173883263
3   0.50771038639272573259832035920607796473753618890942519
4   0.50771038639272573259832035920607796473753618890942519
5   0.4180391993111783527903592746542901939047373467959792202
6   0.4851255639994217748056244390716856678392593420377129154
7   0.4294502068468469553259405444459636682370459573474146866
8   0.4294502068468469553259405444459636682370459573474146866
(mu(4)=mu(8)=0, so a_4=a_8=0 and N=4==N=3, N=8==N=7, as expected.)

## Observations (fenced, data-only)

- E_N* is monotonically non-increasing in N (each larger set contains the previous).
- The optimal coefficients are NOT the source-first family; the -mu(n)/n family is
  substantially worse (e.g. E=0.697 vs 0.307 at N=2, 0.429 vs 0.024 at N=7).
- At N=5 a large error drop (0.066 -> 0.036) coincides with the first appearance of a
  clock r_5 whose period is coprime to {2,3,4}'s lcm=12, i.e. new residue information.
- These are numerical observations; no induction is claimed.

## Boundary (what this does NOT cover)

- No rigorous error bounds / interval arithmetic: values are high-precision floating
  point, not certificates.
- Coefficients are real optima; the task says "rational coefficients" loosely — the
  optimum over reals is what was computed (entries are transcendental, so the true
  optimizer is generally irrational; we did not solve a rational-restricted problem).
- Only N=2..8; no asymptotics in N, no limit statement.

## Reproduce

  python3 dsv4_periodic_tail_residue_ls.py
  (mpmath 1.2.1, sympy 1.12, numpy 2.5.0; dps=60)

Files: dsv4_periodic_tail_residue_ls.py (harness), dsv4_periodic_tail_residue_ls_RECEIPT.txt (full run log).
