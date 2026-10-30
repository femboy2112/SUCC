# Initial instrument failures and exact corrections

1. **Focused test harness failure**: independent sympy oracle computed `(-integer)**(negative exponent)` as Python float when the sign was a plain Python int. `Fraction(float)` rejected it. Replaced with `sympy.Integer(factor)**exponent`, yielding exact rationals. Original mathematical equality of local Morita ratios survived; no formula was altered.
2. **Independent symbolic oracle assertion**: `sympy.expand(expr)` was compared to an algebraically equal but unexpanded RHS, causing false failure. Replaced with `expand(lhs-rhs)==0`. Source coefficients and integrality theorem unchanged.
3. **Removable singular integration**: independent positive integral oracle now uses exact factorization `Q(u)=(1-u)(u²+2)(u²+2u+2)` to evaluate the endpoint smoothly. Earlier direct `0/0` at u=1 was avoided by an explicit limit; replacing it prevents numerical cancellation without changing the integral.

The final focused tests and independent oracle have passed. These were instrument problems, not refutations of the research theorem. Original failed command output exists in the execution transcript; it is not repackaged as if a separately saved raw log were available.
