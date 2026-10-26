"""Independent exact rational and high-precision gamma/BBP bridge regressions."""
import unittest
from fractions import Fraction as Q
import mpmath as mp

from observational_succ.zero_one_gamma_bridge import (
  GammaBridgeError,logarithmic_successor_unit,log_positive_interval,
  gamma_defect_interval,generalized_defect_integer,gamma_field_certificate,
  authentic_bbp_forcing,bbp_polynomial,bbp_factor,
  bbp_gamma_cell_certificate,bbp_gamma_quadratic,
  beta_integer,finite_jet_moment_mutant,gamma_r_finite_bracket,shared_resolvent_certificate,
)


class ZeroOneGammaChartTests(unittest.TestCase):
 def test_integer_successor_not_natural_log_one(self):
  a=logarithmic_successor_unit(1,30)
  self.assertEqual(a['additive_successor'],1)
  self.assertEqual(a['multiplicative_ratio'],2)
  self.assertEqual(a['normalized_log_unit'],1)
  self.assertLess(a['log_increment'].upper,Q(1))
  self.assertGreater(a['log_increment'].lower,Q(1,2))

 def test_all_x_logarithm_outward_intervals(self):
  with mp.workdps(440):
   for x in [Q(1,4),Q(1),Q(5,4),Q(2),Q(13,3),Q(101)]:
    L=log_positive_interval((x+1)/x,65)
    val=mp.log((mp.mpf(x.numerator)+x.denominator)/x.numerator)
    self.assertLessEqual(mp.mpf(L.lower.numerator)/L.lower.denominator,val)
    self.assertGreaterEqual(mp.mpf(L.upper.numerator)/L.upper.denominator,val)
    self.assertGreater(L.lower,0)

 def test_delta_log_cell_matches_mpmath(self):
  with mp.workdps(230):
   for x in [Q(1,2),Q(1),Q(2),Q(5),Q(97)]:
    interval=gamma_defect_interval(x,30)
    numerical=1/(mp.mpf(x.numerator)/x.denominator)-mp.log1p(mp.mpf(x.denominator)/x.numerator)
    self.assertLessEqual(mp.mpf(interval.lower.numerator)/interval.lower.denominator,numerical)
    self.assertGreaterEqual(mp.mpf(interval.upper.numerator)/interval.upper.denominator,numerical)
    self.assertGreater(interval.lower,0)

 def test_gamma_origin_transport_and_strict_decrease(self):
  with mp.workdps(210):
   for x in [1,2,3,5,10]:
    a=mp.log(x)-mp.digamma(x)
    b=mp.log(x+1)-mp.digamma(x+1)
    d=gamma_defect_interval(x,35)
    difference=a-b
    self.assertGreater(difference,0)
    self.assertLessEqual(mp.mpf(d.lower.numerator)/d.lower.denominator,difference)
    self.assertGreaterEqual(mp.mpf(d.upper.numerator)/d.upper.denominator,difference)
   self.assertLess(abs(mp.log(1)-mp.digamma(1)-mp.euler),mp.mpf('1e-60'))
   self.assertLess(abs((mp.log(1)-mp.digamma(1))-
                       (mp.log(2)-mp.digamma(2))-(1-mp.log(2))),mp.mpf('1e-60'))

 def test_gamma_finite_carrier_tail_bounds(self):
  with mp.workdps(75):
   for x,N in [(Q(1),4),(Q(1),64),(Q(2),15),(Q(3,2),50),(Q(19),20)]:
    cert=gamma_field_certificate(x,N,45)
    v=mp.log(mp.mpf(x.numerator)/x.denominator)-mp.digamma(mp.mpf(x.numerator)/x.denominator)
    self.assertLessEqual(mp.mpf(cert.total.lower.numerator)/cert.total.lower.denominator,v)
    self.assertGreaterEqual(mp.mpf(cert.total.upper.numerator)/cert.total.upper.denominator,v)
    self.assertEqual(cert.tail.lower,Q(1,2*(x+N)))
    self.assertEqual(cert.tail.upper,Q(1,x+N))

 def test_higher_jet_integer_links(self):
  # Delta_2(x)=1/[x^2(x+1)] = -d/dx Delta_1(x).
  for x in (Q(1),Q(3,2),Q(2),Q(13)):
   self.assertEqual(generalized_defect_integer(2,x),Q(1)/(x*x*(x+1)))
   for r in range(2,7):
    self.assertGreater(generalized_defect_integer(r,x),0)
  # Gamma_2(1)=zeta(2)-1 is a derivative of Gamma_1(x) at x=1.
  with mp.workdps(70):
   g2=mp.zeta(2)-1
   self.assertLess(abs(g2-(mp.polygamma(1,1)-1)),mp.mpf('1e-60'))

 def test_integer_gamma_r_tower_exact_bounds(self):
  with mp.workdps(95):
   for r in (2,3,4,5):
    for x,N in ((Q(1),5),(Q(1),42),(Q(3,2),15),(Q(5),7)):
     interval=gamma_r_finite_bracket(r,x,N)
     a=mp.mpf(x.numerator)/x.denominator
     truth=mp.zeta(r,a)-a**(1-r)/(r-1)
     self.assertLessEqual(mp.mpf(interval.lower.numerator)/interval.lower.denominator,truth)
     self.assertGreaterEqual(mp.mpf(interval.upper.numerator)/interval.upper.denominator,truth)
   gamma2=gamma_r_finite_bracket(2,Q(1),500)
   pi2=6*(mp.mpf(gamma2.lower.numerator)/gamma2.lower.denominator+1)
   self.assertLess(pi2,mp.pi**2)

 def test_bad_log_chart_rejections(self):
  for x in (0,-1,.5,True):
   with self.assertRaises(GammaBridgeError):gamma_defect_interval(x)
  with self.assertRaises(GammaBridgeError):log_positive_interval(2,0)


class SharedMomentGeometryTests(unittest.TestCase):
 def test_original_four_pole_authentication(self):
  for n in range(1,101):
   correct=Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
   self.assertEqual(authentic_bbp_forcing(n),correct)
   self.assertGreater(correct,0)
  self.assertEqual(authentic_bbp_forcing(1),Q(47,15))

 def test_positive_endpoint_zero_and_equality_of_polynomial_charts(self):
  for t in [Q(0),Q(1,10),Q(1,3),Q(1,2),Q(9,10),Q(1)]:
   self.assertEqual(bbp_polynomial(t),(1-t)*bbp_factor(t))
   self.assertEqual(bbp_polynomial(t),4-2*t**3-t**4-t**5)
   self.assertGreaterEqual(bbp_polynomial(t),0)
  self.assertEqual(bbp_polynomial(Q(1)),0)
  self.assertEqual(bbp_factor(Q(1)),15)

 def test_analytic_all_index_factor_bound_with_rational_intervals(self):
  for n in range(1,251):
   cert=bbp_gamma_cell_certificate(n,22)
   self.assertTrue(cert.verified_with_rational_bounds)
   self.assertGreater(cert.lower_ratio,4)
   self.assertLess(cert.upper_ratio,30)
   self.assertEqual(cert.x,8*n-7)

 def test_ratio_strict_increasing_and_approaching_30_with_certified_bounds(self):
  previous=None
  for n in [1,2,3,4,5,10,20,40,80,200,500,1000]:
   cert=bbp_gamma_cell_certificate(n,30)
   if previous is not None:
    self.assertLess(previous.upper_ratio,cert.lower_ratio)
   previous=cert
  self.assertGreater(previous.lower_ratio,Q(299,10))  # > 29.9

 def test_all_dimensional_hankel_dominance_finite_quadratic_probes(self):
  for c in [(Q(1),),(Q(1),Q(1)),(Q(1),Q(-1)),(Q(1),Q(-2),Q(1)),
            (Q(2),Q(-1),Q(3)),(Q(1),Q(0),Q(-1),Q(1))]:
   witness=bbp_gamma_quadratic(c,60)
   self.assertLess(4*witness['gamma_form'].upper,witness['bbp_form'])
   self.assertLess(witness['bbp_form'],30*witness['gamma_form'].lower)

 def test_moment_integral_source_authentication_independent_sympy(self):
  import sympy as sp
  t=sp.Symbol('t',real=True)
  P=(1-t)*(t*t+2)*(t*t+2*t+2)
  for n in range(1,26):
   integrand=sp.Poly(sp.expand(t**(8*n-8)*P),t)
   direct=sum(Q(int(coeff.p),int(coeff.q))*Q(1,int(power[0])+1)
              for power,coeff in integrand.terms())
   self.assertEqual(direct,authentic_bbp_forcing(n))

 def test_shared_positive_operator_resolvent_brackets_pi(self):
  with mp.workdps(115):
   gamma0=mp.nsum(lambda k: (1/(8*k+1)-mp.log(1+1/(8*k+1)))/16**k,
                   [0,mp.inf])
   for N in (0,1,2,4,7,15):
    rec=shared_resolvent_certificate(N,35)
    lo,hi=rec.gamma_resolvent.lower,rec.gamma_resolvent.upper
    self.assertLessEqual(mp.mpf(lo.numerator)/lo.denominator,gamma0)
    self.assertGreaterEqual(mp.mpf(hi.numerator)/hi.denominator,gamma0)
    l,u=rec.pi_outer.lower,rec.pi_outer.upper
    self.assertLessEqual(mp.mpf(l.numerator)/l.denominator,mp.pi)
    self.assertGreaterEqual(mp.mpf(u.numerator)/u.denominator,mp.pi)
    self.assertLess(rec.unseen_gamma_tail.upper,Q(16,15)/16**N)

 def test_nontrivial_gamma_log_kernel_ratio_bracket(self):
  # Rational point sample / numerical independent oracle, not universal proof.
  with mp.workdps(80):
   for tv in [Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(9,10)]:
    t=mp.mpf(tv.numerator)/tv.denominator
    W=1-(1-t)/(-mp.log(t))
    Qpoly=(t*t+2)*(t*t+2*t+2)
    ratio=Qpoly*(1-t)/W
    self.assertTrue(4<ratio<30)


class HostileFiniteMomentMutants(unittest.TestCase):
 def test_orthogonal_mutants_match_any_selected_finite_prefix(self):
  for K in range(1,6):
   for M in (1,2,3,4):
    mut=finite_jet_moment_mutant(K,M)
    self.assertEqual(len(mut.polynomial_coefficients),K+1)
    self.assertEqual(mut.polynomial_coefficients[-1],1)
    self.assertGreater(mut.first_unmatched_moment_shift,0)
    self.assertGreater(mut.source_polynomial_at_16,0)
    self.assertLess(mut.resolvent_shift_bracket.lower,mut.resolvent_shift_bracket.upper)
    for j in range(K):self.assertEqual(mut.moment_shift(j),0)
    self.assertEqual(mut.moment_shift(K),mut.first_unmatched_moment_shift)

 def test_positive_source_and_same_boundary_jets(self):
  for K,M in ((1,2),(3,4),(5,2)):
   mut=finite_jet_moment_mutant(K,M)
   for tv in [Q(0),Q(1,16),Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(15,16),Q(1)]:
    p=mut.kernel_at(tv)
    self.assertGreaterEqual(p,3*(1-tv))
    self.assertEqual(p if tv==1 else 0,0)
    if tv<1:self.assertGreater(p,0)
    self.assertEqual(mut.kernel_at(Q(0)),4)
    self.assertEqual(mut.kernel_at(Q(1)),0)
    # Mutation factor (1-t)^(M+1) retains endpoint Taylor jets through M.

 def test_resolvent_delta_positive_source_separation(self):
  for K in range(1,5):
   mut=finite_jet_moment_mutant(K,3)
   R=mut.resolvent_shift_bracket
   # independent finite exact Neumann partial sum with tail from |poly|
   p=Q(0)
   for j in range(K+45):
    p+=mut.moment_shift(j)/16**j
   self.assertLess(R.lower,p)
   self.assertGreater(R.upper,p)

 def test_orthogonality_next_moment_is_positive_gram_norm(self):
  for K in range(1,6):
   mut=finite_jet_moment_mutant(K,2)
   c=mut.polynomial_coefficients
   norm=sum((c[i]*c[j]*beta_integer(8*(i+j)+2,4)
              for i in range(K+1) for j in range(K+1)),Q())
   self.assertEqual(mut.first_unmatched_moment_shift,mut.epsilon*norm)

 def test_source_mutation_distinguished_from_authentic(self):
  m=finite_jet_moment_mutant(3,2)
  self.assertEqual(m.moment_shift(0),0)
  self.assertEqual(m.moment_shift(1),0)
  self.assertEqual(m.moment_shift(2),0)
  self.assertGreater(m.moment_shift(3),0)
  self.assertNotEqual(m.kernel_at(Q(1,2)),bbp_polynomial(Q(1,2)))

 def test_invalid_mutant_parameters(self):
  with self.assertRaises(GammaBridgeError):finite_jet_moment_mutant(0,3)
  with self.assertRaises(GammaBridgeError):finite_jet_moment_mutant(2,0)
  with self.assertRaises(GammaBridgeError):finite_jet_moment_mutant(9,2)
  with self.assertRaises(GammaBridgeError):finite_jet_moment_mutant(1,2).kernel_at(Q(3,2))

if __name__=='__main__': unittest.main()
