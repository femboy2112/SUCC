"""Focused exact tests of the primitive operational triangle; no π-normality assertion."""
import unittest
from fractions import Fraction as F
from itertools import product
from math import comb
from operational_triangle import (
    R, r, endpoint_mass, joint_path, joint_source, posterior_laplace,
    posterior_prediction, source_superposition, harmonic_path, harmonic_source,
    gamma_difference, joint_first_jet, joint_fake_first_jet,
    joint_source_defect, phase_frequency_terms, fourier_coefficient, bbp_state,
    frac, carry, endpoint_prediction_variance, shared_vs_reset,
)


class SourceFaithfulOperationalTriangle(unittest.TestCase):
    def test_original_four_signed_poles(self):
        for n in range(1, 31):
            a=8*n-7
            self.assertEqual(r(n),4/F(a)-2/F(a+3)-1/F(a+4)-1/F(a+5))
            self.assertGreater(R(a),0)

    def test_both_routes_of_joint_superposition(self):
        for a,m,z,t in product((1,9,25),(0,1,2,3,4,6),
                                (F(0),F(1,3),F(2,3),F(1)),(F(0),F(1,2),F(2))):
            self.assertEqual(joint_source(a,m,z,t),joint_path(a,m,z,t))
            self.assertEqual(sum(source_superposition(a,m)),1)
            self.assertEqual(joint_source(a,m,1,t),R(F(a)*(1+t))/R(a))

    def test_posterior_is_predictive_and_superposes_prior(self):
        for a,m in product((1,9,17),(1,2,3,4,5)):
            row=source_superposition(a,m)
            for j,q in enumerate(row):
                self.assertGreater(q,0)
                f,s=posterior_prediction(a,m,j)
                self.assertEqual(f+s,1)
                self.assertTrue(0<f<1)
                self.assertTrue(0<s<1)
                self.assertEqual(posterior_laplace(a,m,j,F(0)),1)
                self.assertEqual(f,posterior_laplace(a,m,j,F(8,a)))
            for t in (F(1,3), F(2)):
                self.assertEqual(sum((q*posterior_laplace(a,m,j,t)
                                      for j,q in enumerate(row)),F()),
                                 R(F(a)*(1+t))/R(a))

    def test_endpoint_forward_update(self):
        for a,m in product((1,9,17),(0,1,2,3,4,5)):
            row=source_superposition(a,m)
            nex=[F()]*(m+2)
            for j,q in enumerate(row):
                f,s=posterior_prediction(a,m,j)
                nex[j]+=q*f
                nex[j+1]+=q*s
            self.assertEqual(tuple(nex),source_superposition(a,m+1))

    def test_history_count_and_flat_diamonds(self):
        # Independently enumerate every word and its exact polynomial in u=e^-8X.
        # A failure contributes u; a success contributes 1-u.
        for a,m in product((1,9,17),range(0,7)):
            summed=[F()]*(m+1)
            for word in product((0,1), repeat=m):
                polynomial={0:1}
                for bit in word:
                    new={}
                    for exponent,coefficient in polynomial.items():
                        if bit==0:
                            new[exponent+1]=new.get(exponent+1,0)+coefficient
                        else:
                            new[exponent]=new.get(exponent,0)+coefficient
                            new[exponent+1]=new.get(exponent+1,0)-coefficient
                    polynomial=new
                weight=sum((coefficient*R(a+8*exponent)/R(a)
                            for exponent,coefficient in polynomial.items()),F())
                summed[sum(word)]+=weight
                self.assertEqual(weight,endpoint_mass(a,m,sum(word))/comb(m,sum(word)))
            self.assertEqual(tuple(summed),source_superposition(a,m))
            if m>=2:
                p01=R(a+8)/R(a)-R(a+16)/R(a)
                self.assertEqual(endpoint_mass(a,2,1),2*p01)

    def test_memory_and_strict_postselection_information(self):
        for a in (1,9,17,33):
            self.assertGreater(shared_vs_reset(a),0)
            self.assertGreater(endpoint_prediction_variance(a),0)
            # Two distinct posteriors share parity=even: j=0 and j=2 at m=2.
            self.assertNotEqual(posterior_prediction(a,2,0)[0],
                                posterior_prediction(a,2,2)[0])

    def test_harmonic_three_routes(self):
        for a,m in product((1,9,25,41),range(0,10)):
            h=harmonic_path(a,m)
            self.assertEqual(h,harmonic_source(a,m))
            self.assertEqual(h,gamma_difference(a,m))

    def test_joint_first_jet_and_mutants_exact(self):
        for z,t in product((F(0),F(1,4),F(1,2),F(1)),(F(0),F(1,2),F(1),F(3))):
            d=2+t-z
            b=z-1
            independently_assembled = (F(59,240)*(2/d**2-2/d**3)
                                       + F(7,4)*b/d**3-3*b*(1+b)/d**4)
            self.assertEqual(joint_first_jet(z,t),independently_assembled)
            self.assertEqual(joint_first_jet(z,t)-joint_fake_first_jet(z,t),
                             joint_source_defect(z,t))
            self.assertEqual(joint_source_defect(z,t),
                             F(59,120)*(1+t-z)/(2+t-z)**3)
            if z==1 and t==0:
                self.assertEqual(joint_first_jet(z,t),0)

    def test_exact_seed_frequency_tomography(self):
        for n,h,seed in product((1,2,4,6),(-2,1,3),(F(0),F(1,5),F(-2,7))):
            terms=phase_frequency_terms(n,h,seed,depth=5)
            self.assertEqual(sum((mass for _,mass,_,_ in terms),F()),1)
            self.assertEqual(len(set(k for k,*_ in terms)),len(terms))
            for j,(freq,mass,phase,integer_carry) in enumerate(terms):
                self.assertEqual(freq,h*16**j)
                self.assertGreater(mass,0)
                self.assertEqual(phase,frac(h*bbp_state(n+j,seed)))
                self.assertEqual(integer_carry,carry(n+j,seed))
                self.assertEqual(fourier_coefficient(terms,freq),((mass,phase),))
                self.assertEqual(fourier_coefficient(terms,freq+1),())

    def test_ordered_paths_are_not_always_sufficiently_collapsed(self):
        # Latent A/B, each prior probability 1/2. At step 1, P(L)=P(R)=1/2.
        # After L, P(R|A)=3/4, P(R|B)=1/4.
        # After R, P(L|A)=1/4, P(L|B)=3/4.
        # Both words have grade J=1 but their posterior on A is unequal.
        p_LR_A=F(1,2)*F(3,4)
        p_LR_B=F(1,2)*F(1,4)
        p_RL_A=F(1,2)*F(1,4)
        p_RL_B=F(1,2)*F(3,4)
        self.assertEqual(p_LR_A+p_RL_A,p_LR_B+p_RL_B)
        self.assertEqual(p_LR_A/(p_LR_A+p_LR_B),F(3,4))
        self.assertEqual(p_RL_A/(p_RL_A+p_RL_B),F(1,4))


if __name__=='__main__':
    unittest.main()
