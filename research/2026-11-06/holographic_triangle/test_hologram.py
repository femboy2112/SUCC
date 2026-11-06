"""Predeclared exact original-source, parity, seam, and hostile controls."""
import unittest
from fractions import Fraction
from hologram import (
    forcing,combined_forcing,state,mod_fraction,Center,Edges,
    center_from_rational,edge_encode,edge_decode,boundary_step,real_step,
    numerator_from_shadow,primitive_h,state_from_primitive,
    source_denominator_witness,first_pole,is_prime,
)

class TriangleSuite(unittest.TestCase):
    def test_original_source_exact(self):
        for n in range(1,81):self.assertEqual(forcing(n),combined_forcing(n))

    def test_fraction_denominators_odd(self):
        for n in range(0,81):self.assertEqual(state(n).denominator%2,1)

    def test_edge_kernel_parity_exhaustive_small(self):
        for k in (1,2,3,4):
            m=1<<k
            image=set()
            zero=[]
            for a in range(m):
                for b in range(m):
                    for x in range(m):
                        p,q,s=(a+b)%m,(a+x)%m,(b+x)%m
                        image.add((p,q,s))
                        if p==q==s==0:zero.append((a,b,x))
            self.assertEqual(set(zero),{(0,0,0),(m//2,m//2,m//2)})
            self.assertEqual(len(image),m**3//2)
            self.assertTrue(all((p+q+s)%2==0 for p,q,s in image))
            # Surjectivity onto parity-allowed boundary triples.
            self.assertEqual(len(image),sum((p+q+s)%2==0 for p in range(m) for q in range(m) for s in range(m)))

    def test_physical_seam_exhaustive(self):
        for k in (1,2,3,4):
            m=1<<k
            image=set()
            for b in range(m):
                for x in range(m):
                    a=(b+x)%m
                    e=edge_encode(Center(a,b,x,k))
                    self.assertEqual(e.defect(),0)
                    self.assertEqual(edge_decode(e),Center(a,b,x,k))
                    image.add((e.p,e.q,e.s))
            self.assertEqual(len(image),m*m)
            self.assertEqual(len(image),sum((p+q-3*s)%m==0 for p in range(m) for q in range(m) for s in range(m)))

    def test_incompatible_edge_rejected(self):
        for k in (1,2,4,8,16,40):
            e=Edges(0,0,1,k)
            self.assertNotEqual(e.defect(),0)
            with self.assertRaises(ValueError): edge_decode(e)

    def test_dynamical_atlas_original(self):
        for k in (1,2,4,8,16,40):
            u=Fraction(0)
            for n in range(0,65):
                center=center_from_rational(u,k)
                self.assertEqual(center.seam,0)
                e=edge_encode(center)
                self.assertEqual(edge_decode(e),center)
                nxt,carry=real_step(u,forcing(n+1))
                expected=edge_encode(center_from_rational(nxt,k))
                self.assertEqual(boundary_step(e,forcing(n+1),carry),expected)
                u=nxt

    def test_dynamical_atlas_mutant_and_rational_seed(self):
        for seed, source in ((Fraction(1,5),forcing),
                             (Fraction(0),lambda n:forcing(n,(5,-2,-1,-1)))):
            u=seed
            for n in range(35):
                ed=edge_encode(center_from_rational(u,28))
                nxt,carry=real_step(u,source(n+1))
                self.assertEqual(boundary_step(ed,source(n+1),carry),
                                 edge_encode(center_from_rational(nxt,28)))
                u=nxt

    def test_h_shadow_exact_and_phase_nonhaar(self):
        # Exact rational 2-adic-isometric shadow, real values tend to zero.
        H=lambda n:Fraction(n,(2*n-1)**4)
        u=Fraction(0)
        for n in range(1,65):
            rr=H(n)-16*H(n-1)
            new,carry=real_step(u,rr)
            ed=edge_encode(center_from_rational(u,16))
            self.assertEqual(boundary_step(ed,rr,carry),edge_encode(center_from_rational(new,16)))
            self.assertEqual(new,H(n))
            u=new
        self.assertLess(float(H(64)),1e-4)

    def test_zero_defect_is_not_real_haar(self):
        ed=edge_encode(center_from_rational(Fraction(0),16))
        for _ in range(50):
            self.assertEqual(ed.defect(),0)
            ed=boundary_step(ed,Fraction(0),0)
        self.assertEqual(ed,Edges(0,0,0,16))

    def test_carry_injection_detected(self):
        # Inconsistent edge injection opens source/realization defect.
        ed=Edges(0,0,0,12)
        good=boundary_step(ed,Fraction(5,7),2)
        bad=Edges((good.p+1)%4096,good.q,good.s,12)
        self.assertEqual(good.defect(),0)
        self.assertEqual(bad.defect(),1)
        future=boundary_step(bad,Fraction(5,7),2)
        self.assertEqual(future.defect(),16)

    def test_fractional_numerator_reconstruction(self):
        for n in (0,1,2,7,19,43,73):
            u=state(n)
            b=u.numerator//u.denominator
            x=u-b
            d=x.denominator
            k=max(1,d.bit_length())
            e=edge_encode(center_from_rational(u,k))
            self.assertEqual(numerator_from_shadow(e,d),x.numerator)
            self.assertEqual(Fraction(numerator_from_shadow(e,d),d),x)

    def test_resolution_too_low_rejected(self):
        u=state(21)
        d=u.denominator
        k=max(1,d.bit_length()-2)
        self.assertGreater(d,2**k)
        with self.assertRaises(ValueError):numerator_from_shadow(edge_encode(center_from_rational(u,k)),d)

    def test_harmonic_gamma_abel_identity(self):
        for n in range(0,36):
            self.assertEqual(state_from_primitive(n),state(n))
            self.assertEqual(primitive_h(n+1)-primitive_h(n),forcing(n+1))

    def test_denominator_bertrand(self):
        for N in (9,16,31,64,127,257):
            p,n,d=source_denominator_witness(N)
            self.assertGreater(p,N)
            self.assertLess(p,2*N)
            self.assertLess(n,N)
            self.assertEqual(d%p,0)
            self.assertGreater(d,N)

    def test_prime_birth_no_previous_p(self):
        for p in range(7,150):
            if not is_prime(p):continue
            n,c=first_pole(p)
            self.assertEqual(state(n).denominator%p,0)
            for j in range(0,n):self.assertNotEqual(state(j).denominator%p,0)
            self.assertEqual((p*forcing(n)).denominator%p!=0,True)
            self.assertEqual((p*forcing(n)).numerator*pow((p*forcing(n)).denominator,-1,p)%p,
                             c.numerator*pow(c.denominator,-1,p)%p)

    def test_source_mutant_harmonic_diverges(self):
        # original sum weights 0, mutant sum weights 1 -> 1/(8n) leading term.
        for n in (50,200,1000):
            r0=forcing(n)
            r1=forcing(n,(5,-2,-1,-1))
            self.assertEqual(r1-r0,Fraction(1,8*n-7))
            self.assertGreater(n*r1, Fraction(1,9))
            self.assertLess(n*r0,Fraction(1,10))

    def test_gamma_pi_finite_abel_identity(self):
        # Finite exact identity whose limit is the Gamma/harmonic pi representation.
        for n in (1,2,3,7,13,29):
            left=sum((Fraction(1,16**j)*forcing(j) for j in range(1,n+1)),Fraction())
            right=Fraction(15,16)*sum((Fraction(1,16**j)*primitive_h(j) for j in range(1,n+1)),Fraction())
            right+=Fraction(1,16**(n+1))*primitive_h(n)
            self.assertEqual(left,right)

    def test_native_atom_factorization_and_pisot_linear_no_go(self):
        # (s²-1/2)(s²-s+1/2)=s^4-s^3+s/2-1/4.
        a=(Fraction(-1,2),Fraction(0),Fraction(1))
        b=(Fraction(1,2),Fraction(-1),Fraction(1))
        p=[Fraction(0)]*5
        for i,x in enumerate(a):
            for j,y in enumerate(b):p[i+j]+=x*y
        self.assertEqual(p,[Fraction(-1,4),Fraction(1,2),Fraction(0),Fraction(-1),Fraction(1)])
        # If L(phi*x)=16L(x) and phi²=phi+1, then 239L(x)=0.
        self.assertEqual(16**2-16-1,239)
        # If L(delta*x)=16L(x) and delta²=2delta+1, 223L(x)=0.
        self.assertEqual(16**2-2*16-1,223)

    def test_mod_fraction_rejects_even_denominator(self):
        with self.assertRaises(ValueError):mod_fraction(Fraction(1,2),8)

if __name__=='__main__':unittest.main()
