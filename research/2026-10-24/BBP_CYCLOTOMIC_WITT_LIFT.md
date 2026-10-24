# CBCW-10: Exact filtered BBP p² return, Fermat quotient shear, carry-safe lift

**Research-only paper proof, separate exact tests; scholarly novelty UNVERIFIED.** Companion to CBCW-01–09 in [the earlier dossier](BBP_CYCLOTOMIC_BIRTH_AND_LAG.md). Parent is the authentic BBP source in PR #252, with the Green/source transport of #254. No π normality, signed cross-prime cancellation, RH, or Weil positivity inferred.

## 1. Typed source

Fix a rational prime `p=8m+1` and set `M=(p²−1)/8=m(p+1)`. For `1<=k<=m`, the authentic four forcing-index denominators generate p²-pole events at

    N_(k,a)=(8k−a)M+k,  a=7,4,3,2;
    8N_(k,a)−a=p²(8k−a).

**Filter ONLY those four p²-pole impulses** from the original forcing. At each event the p² contribution has value `A_a(k)/p²` with

    A_7=4/(8k−7),  A_4=−2/(8k−4),
    A_3=−1/(8k−3), A_2=−1/(8k−2).

The true full BBP source also contains numerous earlier p-pole impulses and other primes. Those are NOT assumed zero. The construction below is a graded filtered source, not the entire π-selected rational trajectory. The range k<=m guarantees the denominators 8k−a are p-units, so p² reduction is valid.

## 2. Fermat quotient is the exact higher-clock return

Define

    q_p=(16^m−1)/p mod p
       =(2^((p−1)/2)−1)/p mod p.

Because p≡1 mod8, quadratic reciprocity implies 16^m≡1 modp. The standard Fermat quotient `Q_p(2)=(2^(p−1)−1)/p mod p` satisfies

    Q_p(2)=2q_p mod p.

Therefore q_p=0 precisely for the corresponding base-2 Wieferich primes; this makes no claim about their distribution.

Since M=m(p+1), the binomial theorem gives

    16^M=1+pq_p mod p²,
    16^(tM)=1+t p q_p mod p²   for t>=0.

At the mod-p level the return is identity; at p² it is generally not.

## 3. Proved twisted affine recurrence

Let C_0=0, and let C_k be **p² times the unwrapped filtered p²-source phase at event N_(k,2)**, reduced mod p². The four within-group time gaps are 3M,M,M, so at the group endpoint the coefficients A_7,A_4,A_3,A_2 have been transported through 5M,2M,M,0 steps. The resulting source impulse is

    r(k)+p q_p [5A_7+2A_4+A_3]
    =r(k)+p q_p [20/(8k−7)−4/(8k−4)−1/(8k−3)]  mod p².

The distance between consecutive **group endpoints** is 8M+1 (not 3M+1, which reaches only the next group's first pulse). Thus, using 16^(8M+1)=16(1+8pq_p) mod p², the exact recurrence is

    C_k=16(1+8p q_p) C_(k−1)
        +r(k)
        +p q_p [20/(8k−7)−4/(8k−4)−1/(8k−3)]  (mod p²),
       1<=k<=m.

Proof is finite modular event transport, multiplication of the exact four pole readouts, and the binomial expansion. Mod p it reduces to CBCW-08. The p² correction contains both a **transport shear** and a **signed source shear**. Omitting either produces a false lift whenever the corresponding residual is nonzero.

This is a sound commutation theorem for the declared filtered source. **It does not identify C_k/p² with the p² part of the entire BBP phase** without also transporting all lower-order p-pole contributions.

## 4. Independent probes, mutation controls, next discriminator

`observational_succ/bbp_cyclotomic_witt.py` implements (i) exact modular jumps between all authentic filtered p² source events and (ii) an independent calculation via the twisted recurrence. The methods agree for p=17,41,73,97,113,137,193,257,313, through k<=min(m,10), with only modular integer/Fraction arithmetic. `tests/test_bbp_cyclotomic_witt.py` includes three tests: Fermat quotient relationship, independent event-versus-recurrence check, and rejected malformed p-adic-source domain/carry mutants. No supplied π digits, external zero positions, or statistical oracle enter.

A calibrated negative test replaces the group-end time gap 8M+1 with 3M+1, or drops q_p; these are false when q_p is nonzero. Testing a filtered p² stream does not validate the unfiltered source's global Fourier limit.

**Next decisive target:** construct a faithful two-channel p/p² observer and preserve the entire forcing readout, then derive a new signed estimate for the full cross-clock interference `I_p(h)`. Even a perfect lift at all finite p-adic depths is not by itself an `o(N)` Weyl theorem. That outstanding estimate is **UNVERIFIED**.
