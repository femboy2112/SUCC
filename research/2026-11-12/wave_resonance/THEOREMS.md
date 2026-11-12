# Exact results and the Goldbach localization obstruction

**2026-11-12. Paper derivations on finite-support arithmetic carriers and classical PNT/AP; external mathematical refereeing and Lean proofs NOT performed.**

## WAVE-01 — additive SUCC and multiplicative FUCC have distinct frequency transport

Let e(t)=exp(2 pi i t), H=ell^2(N_>=2), M_theta|n>=e(n theta)|n>, V_l|n>=|l n>, and Delta_+|N>=sum_(a+b=N, a,b>=2)|a,b>. On the common algebraic core:
   
   (M_theta tensor M_theta) Delta_+ = Delta_+ M_theta;
   M_theta V_l = V_l M_(l theta);
   V_l S = S^l V_l.

The first formula conserves additive Fourier frequency under addition; the second shows multiplicative dilation twists the frequency. These laws hold also for composite l; a prime-only operator requires authentic prime source metadata. A multiplicative factor split ab=N does not in general preserve the additive phase e(theta N), since a+b != ab. Noncommutation is structural, not proof of Goldbach or nontrivial physical gauge curvature.

## WAVE-02 — unit Haar water and Ramanujan response

For modulus M>=2 let U_M=(Z/MZ)^×. Multiplication by l coprime to M permutes U_M; therefore its normalized Haar state is invariant under prime or composite unit dilations. Its additive character response is c_M(a)/phi(M), with c_M(a)=sum_(u in U_M)e(a u/M), the Ramanujan sum.

The normalized unit-residue distribution cannot distinguish the multiplicative factor-count grade Omega=1 from Omega=2. Extra source and high-frequency information are necessary.

## WAVE-03 — actual prime and rough-semiprime waves share rational resonance

Fix A>0 and 0<t<=1. For M<=log^A X and unit residue u, classical Siegel–Walfisz yields uniformly

   #{p<=tX: p=u mod M} = tX/[phi(M)log X] (1+o(1)).

Let z=floor(X^(1/3)), c_X(k) denote composite k<=X with least prime factor >z. Factor each c_X integer uniquely as k=ell r, primes z<ell<=r. For fixed u mod M, since ell>z>M for large X,

   C_X(t;M,u) = sum_(z<ell<=sqrt(tX), ell prime)
       ( pi(tX/ell; M,u ell^(-1)) - pi(ell-1; M,u ell^(-1)) ).

All inner prime arguments grow at least like sqrt X. Apply uniform PNT/AP and partial summation to obtain

   C_X(t;M,u) = (log 2) tX/[phi(M)log X] (1+o(1)),

uniform in M,u and fixed t bounded away from zero. Indeed the main integral over log ell/log X in [1/3,1/2] is int du/[u(1-u)] = log 2. Small primes dividing M and prime squares contribute lower-order terms. Thus for rational mode a/M, the prime Fourier field P_X(a/M) and the rough-semiprime field C_X(a/M) share the same Ramanujan phase c_M(a)/phi(M), with amplitudes P_X(0)~X/log X and C_X(0)~(log 2)X/log X. The source-specific asymptotic needs PNT in arithmetic progressions; it is not a random wave premise.

## WAVE-04 — exact squared Ramanujan waves equal the Goldbach CRT factor

Put K_M(r)=#{(u,v) in U_M^2: u+v=r (mod M)}. Fourier inversion in the finite cyclic group gives

   K_M(r) = (1/M) sum_(a mod M) c_M(a)^2 exp(-2 pi i a r/M).

For each prime power ell^k || M, the number of allowable units u is ell^(k-1)*(ell-1) if ell|r, otherwise ell^(k-1)*(ell-2). CRT multiplication yields

   Sigma_M(r)=M K_M(r)/phi(M)^2
     = product_(ell|M) [ell/(ell-1) if ell|r;
                        ell(ell-2)/(ell-1)^2 otherwise].

For even M and r, Sigma_M(r) >=2*C_2, where C_2=prod_(ell>2)(1-1/(ell-1)^2)>0. This is strict positivity of congruence-class admissibility, NOT of prime pairs.

## WAVE-05 — UNCONDITIONAL MACROSCOPIC RESIDUE-CLASS POSITIVITY

Fix 0<a<b<2 and A>0. Let X tend to infinity; fix z=floor(X^(1/3)), restrict p_X,c_X to 2..X. Let M range over even moduli 2<=M<=log^A X, and r over even residues modulo M. Let T(t) be the triangular cumulative distribution:
  T(t)=0 for t<=0;
  T(t)=t^2/2 for 0<=t<=1;
  T(t)=1-(2-t)^2/2 for 1<=t<=2;
  T(t)=1 for t>=2.

Then uniformly over M,r:

   sum_(aX<N<=bX, N=r mod M) [ (p_X*p_X)(N)-(c_X*c_X)(N) ]
     = [1-(log 2)^2] [Sigma_M(r)/M] [T(b)-T(a)]
       X^2/(log X)^2 + o_(a,b,A)( X^2/(M(log X)^2) ).

In particular the sum is strictly positive for EVERY admissible M,r at sufficiently large X. The theorem also holds when z is replaced at each output N by z_N=floor(N^(1/3)), keeping each source endpoint truncated at X.

Proof: WAVE-03 gives one-body equidistribution on each unit residue class in every macroscopic subinterval, with error uniform in polylog modulus via Siegel–Walfisz. Product measures converge to Lebesgue area on the triangular region a<x+y<=b. Exactly K_M(r) unit residue pairs sum to r. Subtracting the semiprime-pair product measure from prime-pair gives factor 1-(log 2)^2, and the mass of the region is T(b)-T(a). Approximate the triangle by rectangles to control boundary errors uniformly, taking the mesh to zero slowly; the strong PNT/AP error handles all M<=log^A X. Small primes dividing M contribute negligible boundary terms. For the adaptive z_N, monotonicity L_z(N) in z gives a pointwise sandwich between fixed z_-=floor((aX)^(1/3)) and z_+=floor((bX)^(1/3)), whose one-body density constants remain log 2. Their macroscopic sums have the same main term.

**Boundary:** A positive sum of many signed coefficients does not imply any individual coefficient is positive. The threshold arising from Siegel–Walfisz may be ineffective. This is a classical-input consequence in new SUCC notation, NOT a pointwise Goldbach theorem and not a claimed priority result.

## WAVE-06 — the exact high-frequency and Haar proof debt

In a fixed even residue channel, take K successive output targets N_j=r+jM and signed coefficients f_j=L_(N_j,z_Nj)(N_j). Let mu=(1/K) sum_j f_j. Discrete Fourier inversion yields

   f_j = mu + (1/K) sum_(k=1)^(K-1) fhat(k) exp(2 pi i jk/K).

The sufficient inequality max_j |f_j-mu|<mu implies f_j>0 everywhere. A stronger Fourier sufficient condition is sum_(k>0)|fhat(k)|<K mu. Parseval gives the exact exceptional-set estimate

   #{j:f_j<=0} <= (1/(K mu^2)) sum_(k>0) |fhat(k)|^2,

for mu>0. Dyadic Haar reconstruction says each leaf equals the block mean plus its SIGNED ancestral details. Our macroscopic theorem estimates only the zero mode; it provides no source-selected bound on the high modes. Neither positive energy nor low-frequency phase matching pays this missing signed estimate.

## WAVE-07 — genuine-prime-only rational-mode camouflage

For any Q set M=lcm(2,1,...,Q). Dirichlet supplies arbitrarily large primes p=1 mod M and q=-1 mod M. Their even sum N is divisible by M and has a Goldbach witness. Start from ALL primes <=N and remove one prime from each unordered Goldbach pair summing N. No removed prime divides M when N>2M: its partner would otherwise be a larger multiple of that prime and could not be prime. Replace each deleted prime by a distinct genuine prime greater than N in the SAME residue modulo M (Dirichlet again). The new finite source has zero pairs summing N but the same number of prime states and the exact same residue histogram modulo M. Thus all rational Fourier values with denominators <=Q agree exactly. This is a proven bounded-observer no-go only: the modified source does not contain every original prime <=N and is caught by complete source authentication.

Concrete independent exact witness: Q=7, M=420, N=4200. Complete source has 574 prime states, 165 unordered Goldbach pairs (R=330 ordered), surviving semiprime pair count 50, signed margin +280. Swapped genuine-prime source retains 574 states and all rational q<=7 modes but has 0 Goldbach pairs; against the unchanged genuine composite background its signed margin is -50. A second trial-division implementation reproduces the data.

## WAVE-08 — low rational alignment does not imply full Fourier coherence

Because p_X and c_X have disjoint supports, Parseval gives int_0^1 P_X(alpha) conjugate(C_X(alpha))dalpha=0. Furthermore

   int |C_X(alpha)-(log 2)P_X(alpha)|^2 dalpha
     = #rough_semiprimes + (log 2)^2 #primes.

The normalized low rational waves agree asymptotically, but the entire Fourier fields are orthogonal. The missing fine-scale data are essential.

**Conclusion:** all finite CRT channels have source-authenticated positive averaged signed mass asymptotically, but the original-source pointwise inequality L_ad(N)>0 remains OPEN, as does binary Goldbach. The next valid bridge must furnish a target-uniform signed major/minor-arc localization estimate (or different arithmetic lower bound), while passing prime-only source camouflage and nonnormal/fake-source controls.

**Inputs and provenance:** Granville, PNT in progressions https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf ; Bhowmik–Grimmelt (2026) https://link.springer.com/article/10.1007/s10476-026-00191-z ; Tao, circle-method limitations https://terrytao.wordpress.com/2012/05/20/heuristic-limitations-of-the-circle-method/ ; parent SUCC dossiers in adjacent research subtrees.