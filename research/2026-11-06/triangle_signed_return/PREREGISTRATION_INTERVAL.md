# Interval-certificate preregistration — added after existing float survey, before exact interval computation

Post-hoc **certification** target: previously seen float signs at N=512,h=1,Q=4,8,16. This is NOT a blind sign discovery; prove a rational upper error bound by quantizing exact Fraction phases to 2^-16, taking a rigorous Machin/arctan bracket for pi, and using bounded Taylor remainder for sin/cos. Predeclare a uniform per-phase complex error ε=1/5000 and return-energy error <1/2400. If the rational enclosure straddles the diagonal 1/M, report ambiguous; never fit ε after seeing output.

Fresh **non-fitted holdout** target: N=768, h=2, Q in {4,8,16}. No sign predicted; output rational interval and only label the sign when the interval excludes 1/M. Also retain full exact-source zero seed and a periodic non-Haar shadow check. The construction is an elementary finite certificate only, not an asymptotic π theorem.

If precision or runtime prevents exact arithmetic, record blocker, do not assert certification. Compare a second float implementation after the exact run but do not count it as independent theorem authority.
