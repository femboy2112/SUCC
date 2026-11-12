# WAVE-09 — infinitely many negative frozen-cutoff signed waves

**PROVED LOCAL, elementary.** This is NOT a counterexample to Goldbach or the target-adaptive signed-sieve conjecture.

For any odd prime p>=3 put X=p²+1, N=2p²=2X-2 and z=floor(X^(1/3)). Define p_X(k)=1 for rational primes k<=X; c_(X,z)(k)=1 for composites k<=X having no prime factor <=z; set both to zero outside [2,X]. Ordered additive convolution gives

   (p_X*p_X)(2p²)=0,
   (c_(X,z)*c_(X,z))(2p²)=1,
   L_(X,z)(2p²)=-1.

**Proof.** With a,b<=X and a+b=2X-2, exactly three ordered pairs occur: (X-2,X), (X-1,X-1), (X,X-2). The outer pairs have even composite endpoints p²-1 and p²+1, so neither contributes to prime pairs or rough-composite pairs. The central value X-1=p² is composite with two prime factors p,p. Since p³>p²+1, the cube-root cutoff z<p; hence p² survives the rough composite sieve. Therefore exactly one surviving semiprime-pair contribution and no prime pair. Infinitely many odd primes exist by Euclid. QED.

Finite exact checks for p=3,5,7,11,13,17,101,599 all produced (R,C,L)=(0,1,-1). For p=599, X=358802,N=717602,z=71. An additional explicit failure of the X=360000 frozen source is N=719998, where 359999=599*601 survives the sieve and no supported prime pair exists (R=0,C=1,L=-1).

**Scope firewall.** The original Goldbach problem at N uses ALL primes <=N, not only primes <=X. These negatives arise by truncating the prime source prior to convolution. They do not refute the adaptive signed-sieve conjecture. WAVE-05 guarantees positivity only after averaging over fixed interior macroscopic intervals aX<N<=bX with b<2; the sequence N/X=2-2/X approaches the upper endpoint and violates that fixed-window scope. This family is an explicit infinite countermodel to a stronger unsupported claim that positive global signed carrier energy implies every coefficient positive, or that the support edge can be discarded without an error term.

**Probe obligation:** Any proposed wave/Scott/Haar localization theorem must retain a source-support boundary correction and reject this family. Pure Fourier re-expression and averaged positivity cannot supply it.