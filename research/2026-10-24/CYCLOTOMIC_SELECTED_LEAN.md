# Cyclotomic selected-source finite kernel authority

This additive module is based on PR #257 at
`5435497dc77a313d1ebbc56ac96c11e593db2619`. It imports the actual BBP
source and the finite transport theorems already present through PR #253.
No code or mathematical premise is imported from sibling PR #256. Its
prime-clock interpretation is independently supplied by the paper audit.

**Status: KERNEL_CHECKED locally.** All 13 new declarations compiled after
fresh rebuilds of the four inherited source modules. Actual type expressions
and axiom lists were exported, and all four positive/mutant pairs passed
their intended gate. The [receipt](cyclotomic_selected_receipts/lean/kernel-observation.json)
records commands, exit codes, source hashes, source immutability and log
hashes. Only `propext`, `Classical.choice`, and `Quot.sound` occur.
Hosted CI authority is reported separately by the delivery receipt.

The first complete checker run successfully rebuilt and exported all 13
declarations, but its Abel positive-control wrapper used simplified numeric
casts with an `exact` proof retaining explicit natural casts. That wrapper
failed by type mismatch. The [failed gate](cyclotomic_selected_receipts/lean-control-wrapper-failure/kernel-observation.json)
and both generated wrapper statements are preserved. After aligning the
wrapper with the theorem's exact type, a second fresh run passed. The
mathematical source did not change between these two runs.

## Exact authority

Source: `formal/duck_pi/CyclotomicSelectedSource.lean`, namespace
`ObservationalSUCC.CyclotomicSelectedSource`.

1. `selected_zero_lift`: for every n, the unchanged BBP recurrence started
   at `-tail 0` has real lift exactly `-tail n`. This is a real initial-state
   control. It does not assert a rational primary decomposition of that
   changed orbit.
2. `dyadic_lift_difference` and `dyadic_state_erased`: for every integer c
   and natural K,n, starting at c/16^K changes the lift at time K+n by
   exactly 16^n*c and changes its circle state by zero. Hence this finite
   transient restores the complete authentic future after K. The separate
   paper statement about odd-primary projections is not formalized here.
3. `selected_state_error`, `selected_character_error`,
   `selected_window_error`: the finite sensitivity to an arbitrary real
   initial state s is exactly 16^n(s+T_0), with its resulting complex
   Fourier error budget. No horizon-uniform continuity is assumed.
4. `selected_zero_window_bound`, `selected_window_constant_bound`: write
   phase(a,x)=exp(i*a*x), and

       W(a,s;J,L)=sum_(j<L) phase(a,liftedFrom(s,J+j+1)).

   For all real a,s and natural J,L, the kernel proves

       |W(a,s;J,L)-L|
         <= |a|*|s+T_0|*sum_(j<L)16^(J+j+1)
            + |a|/[32*(J+1)].

   The second term uses the previously proved authentic BBP tail
   telescoping majorant. Set a=2*pi*h for integer Fourier mode h. This
   certifies the finite error of rational selected-state controls; it does
   not give this small error at the authentic s=0 without paying the
   exponentially magnified first term.
5. `prefixSum_succ`, `centered_abel_identity`, `centered_abel_bound`: for
   arbitrary complex u,v, put U_k=sum_(s<k)u_s. For all n,

       sum_(s<=n)u_s*(v_s-v_0)
         = U_(n+1)*(v_n-v_0)
           -sum_(s<n)U_(s+1)*(v_(s+1)-v_s).

   If |U_k|<=M for every k<=n+1, the modulus is at most
   M*(|v_n-v_0|+sum_(s<n)|v_(s+1)-v_s|). The hypothesis requires all
   incomplete prefixes. A bound on the complete-period sum alone is not
   substituted for it.
6. `twisted_clock_identity`, `twisted_clock_square_bound`: for every finite
   abelian group G, any complex u, and any unit-modulus character chi with
   chi(s+d)=chi(s)chi(d), put

       R(d)=sum_s u(s+d)*conj(u(s)).

   The actual complex identity, including its character sign, is

       |sum_s u(s)chi(s)|^2 = sum_d R(d)chi(d).

   The identity is exported as equality in C between the sum times its
   conjugate and the displayed correlation sum. If |R(0)|<=C and
   |R(d)|<=E for every nonzero d, the kernel proves

       |sum_s u(s)chi(s)|^2 <= C+(card(G)-1)*E.

   Thus the paper's specialization C=L, E=L*epsilon controls every temporal
   twist by normalized squared bound 1/L+(1-1/L)*epsilon. This finite
   step does not invoke a weighted BGK theorem. The number-theoretic
   derivation of the required local lag bounds, its good-prime domain,
   BGK constants, and the complementary weight's Wiener norm remain
   separate paper/external-theorem obligations.

## Source and proof boundaries

The inherited modules `BaileyCrandall`, `BBPIntegral`, `PiSource`, and
`BBPSourceGenesis` are rebuilt from the present worktree by the new checker.
They authenticate the exact four-pole source and `Real.pi`; their existing
historical authority is unchanged. None of the new declarations asserts
vanishing of the authentic interference I_p, a sublinear pi Fourier sum,
equidistribution, or normality. There are no new axioms and no `sorry`.

The new checker is additive:

```sh
python scripts/check_cyclotomic_selected_lean.py \
  --dependency-project /home/leah/SUCC-rf/formal/mathlib_bridge \
  --output /tmp/cyclotomic-selected-lean-final2
```

Omit `--dependency-project` when the checked dependency cache is under
`formal/duck_pi`. The checker verifies dependency Git revisions and tracked
cleanliness against the existing manifest, uses Lean 4.14.0 with one worker
and a 4 GiB cap, hashes every source, recompiles all five modules, exports
actual elaborated theorem types and axiom lists, and checks that sources
did not change during the run. The allowed standard kernel axioms are
`propext`, `Classical.choice`, and `Quot.sound`.

Four paired controls alter an exact dyadic lift difference, the selected
zero-tail sign, the centered Abel subtraction sign, and the twisted-clock
correlation sign. A mutant passes the hostile gate only when its matching
positive compiles and the mutant fails with a type mismatch rather than
missing imports or syntax errors. These checks delimit the actual exported
propositions; they are not statistical evidence for pi normality.

**PI NORMALITY PROVED: NO.**
