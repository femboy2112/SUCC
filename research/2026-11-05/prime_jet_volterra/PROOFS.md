# A joint Volterra bound for newly active prime shifts

Parent #517, a2905c9e1770fea519193839433bdca4bd29336f. Additive local analytic result; no RH, no completed-Weil coercivity, no global novelty claim.

## V1. Single shift

Let f belong to H1_0((0,D);C), D=a+delta, 0<delta<a, and w>0. Extend f by zero, put g(a)=integral f(x+a) conjugate(f(x)) dx, and J=-w(S_a+S_a*). Conjugating g does not change its real part. Define p(s)=f'(s) and q(t)=-f'(D-t) on (0,delta). The boundary conditions give

    f(x) = integral_0^x p(s) ds,
    f(a+x) = integral_0^(delta-x) q(t) dt.

Fubini therefore gives conjugate(g(a)) = integral integral (delta-s-t)_+ p(s) conjugate(q(t)) ds dt. All identities are valid for H1 by absolute integrability and the absolutely continuous representative.

The kernel K_delta(s,t)=(delta-s-t)_+ has Hilbert--Schmidt norm squared

    integral_0^delta integral_0^(delta-s) (delta-s-t)^2 dt ds = delta^4/12.

Cauchy--Schwarz in L2 of the square, followed by 2uv<=u^2+v^2 and disjointness of (0,delta) and (a,D), proves

    |<f,J f>| <= (w delta^2/sqrt(12)) ||f'||_2^2.                 (V1)

This improves the valid nonsharp pi/8 coefficient of #517 BG1, since 1/sqrt(12)<pi/8. We do not assert sharpness: Hilbert--Schmidt norm generally exceeds operator norm. It is an analytic inequality for every positive weight/shift, specialized to actual Euler weights below. It is not a source selector.

## V2. Joint active-prime coefficient

Let 0<D<2 log2. For every prime power p^k<exp(D), use exactly a_j=k log p, w_j=(log p)p^(-k/2), delta_j=D-a_j. If none are active set C(D)=0. Otherwise delta_* = max delta_j < D/2. On the common square (0,delta_*)^2 form K=sum_j w_j K_delta_j. The same boundary derivative vectors and the same Cauchy--Schwarz argument give

    |sum_j <f,J_j f>| <= C(D) ||f'||_2^2,
    C(D)^2 = sum_i,j w_i w_j u_ij^3(2v_ij-u_ij)/12,             (V2)
    u_ij=min(delta_i,delta_j), v_ij=max(delta_i,delta_j).

Indeed, for 0<u<=v,

    <K_u,K_v>_HS = integral_0^u z(u-z)(v-z) dz
                = u^3(2v-u)/12.

This is at most sum_j w_j delta_j^2/sqrt(12), the separate-jet triangle bound, and is strictly smaller when two distinct positive widths occur, by strict triangle inequality for nonproportional kernels. For log3<D<log4 the active prime powers are precisely 2 and 3. No composite or omitted prime power is substituted.

## V3. Exact interface with the completed form, and obstruction

Use F(z)=integral f(x)exp(izx) dx, h(z)=F(z)conjugate(F(conjugate(z))), and Omega(t)=Re psi(1/4+it/2)-log pi. The completed Guinand--Weil form is

    W(f)=h(i/2)+h(-i/2)+(1/(2pi)) integral |F(t)|^2 Omega(t) dt
         + sum_(p^k<exp(D)) <f,J_(p,k) f>.

For smooth compactly supported f in (0,D), V2 supplies the rigorous lower bound W(f)>=pole(f)+Gamma(f)-C(D)||f'||^2. This does NOT prove a positive lower bound. The pole pair is 2 Re(F(i/2)conjugate(F(-i/2))), not a universally positive rank-one term for complex f. The Fourier convention and all prime powers match the [Guinand explicit formula](https://www-users.cse.umn.edu/~garrett/m/complex/notes_2020-21/12g_guinand_explicit_fml.pdf).

One cannot close this bound by asserting Gamma+pole>=c||f'||^2 uniformly for any c>0: choose a fixed nonzero smooth phi supported inside (0,D) and f_R(x)=exp(iRx)phi(x). Its derivative norm squared is R^2||phi||^2+O(R), while the Gamma term is O(log(2+R)) by the digamma asymptotic and Schwartz decay of the translated Fourier transform. The pole terms decay faster than every inverse power of R by integration by parts. Thus the proposed uniform derivative coercivity is REFUTED by this explicit modulation family. This refutes that absorption argument, not completed-Weil positivity.

## Controls and scope

Matching left/right packets yield negative jet expectation; opposite packets yield positive expectation; a relative imaginary phase gives zero real expectation. Replacing the prime weight by a fake positive source still satisfies V1/V2, which makes their source-blind analytic scope explicit. Actual Euler coefficients are necessary for the Weil interface, but this estimate alone does not characterize them. No zeta zeros enter construction or tests. The BBP Gaussian character operator has no supplied intertwiner with this form.

The existing [Connes--Consani archimedean work](https://arxiv.org/abs/2006.13771) is a separate completed-form program; no claim to improve its positivity range is made. V1/V2 improve the inherited SUCC boundary estimate only. Next decisive probe: a Gamma-form-relative bound on the signed joint jet on a declared low-frequency subspace, with a separately controlled high-frequency complement. The derivative norm bound cannot supply that uniformly.
