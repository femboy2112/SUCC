"""Exact source-specific figure-eight/16-step/Hensel/second-gluing tests.

Paper statements are justified in PROOFS.md; finite tests are calibrations and
adversarial controls, not proofs of pi normality or universal Weyl saving.
"""
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
import importlib.util

P = Path(__file__).resolve().parents[1]/'research'/'2026-11-03'/'figure_eight_pow2'/'pow2_fig8.py'
spec=importlib.util.spec_from_file_location('pow2_fig8_source',P)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)


class ExactChiralClock(unittest.TestCase):
    def test_original_eight_taps(self):
        self.assertEqual(m.TAPS,(4,0,0,-2,-1,-1,0,0))
        self.assertEqual(sum(m.TAPS,F(0)),0)
        self.assertEqual(sum(m.PLUS,F(0)),F(15,4))
        self.assertEqual(sum(m.MINUS,F(0)),F(-15,4))

    def test_clock_at_two_four_eight_sixteen_and_more(self):
        self.assertEqual(m.power_of_two_clock(2),m.expected_clock(2))
        for k in range(3,12):
            self.assertEqual(m.power_of_two_clock(k),m.expected_clock(k))
        scalar=F(1,256)
        self.assertEqual(m.power_of_two_clock(4),tuple(tuple(scalar*x for x in row)
                         for row in m.IDENT))

    def test_two_step_torus_vs_two_lobe(self):
        t2=m.power_of_two_clock(1)
        expected=((0,F(-1,2),0,0),(F(1,2),0,0,0),
                  (0,0,F(1,2),0),(0,0,0,F(1,2)))
        self.assertEqual(t2,expected)
        self.assertEqual(m.matmul(m.T,m.CHI),m.matmul(m.CHI,m.T))

    def test_8_16_32_shell_exact_coefficients(self):
        for k in range(3,8):
            taps=m.octaves(k)
            self.assertEqual(len(taps),1<<k)
            for i,c in enumerate(taps):
                self.assertEqual(c,m.TAPS[i%8]/16**(i//8))
            self.assertEqual(m.endpoint_jets(k)[0],0)

    def test_all_power2_first_jet_exact(self):
        for k in range(3,9):
            value,d1,d2=m.endpoint_jets(k)
            self.assertEqual(value,0)
            self.assertEqual(d1,m.finite_source_jet_expected(k))
            self.assertEqual(F(-16)-d1,m.jet_gap(k))
        self.assertEqual(m.endpoint_jets(3)[1],-15)
        self.assertEqual(m.endpoint_jets(4)[1],F(-255,16))
        self.assertEqual(m.jet_gap(4),F(-1,16))
        self.assertEqual(m.jet_gap(5),F(-1,4096))

    def test_second_jet_finite_block_formula(self):
        for k in range(3,9):
            B=1<<(k-3)
            sj=sum((F(1,16**j) for j in range(B)),F(0))
            jweight=sum((F(j,16**j) for j in range(B)),F(0))
            d2=-44*sj-240*jweight
            self.assertEqual(m.endpoint_jets(k)[2],d2)
        self.assertEqual(m.endpoint_jets(3)[2],-44)

    def test_exact_finite_transfer_identity_on_rational_samples(self):
        for k in range(3,7):
            B=1<<(k-3)
            taps=m.octaves(k)
            for t in (F(0),F(1,9),F(2,7),F(1,2),F(7,8),F(1)):
                prefix=sum((c*t**j for j,c in enumerate(taps)),F(0))
                numerator=4-2*t**3-t**4-t**5
                denom=1-t**8/F(16)
                self.assertEqual(prefix,(1-(t**8/F(16))**B)*numerator/denom)

    def test_16_microstep_no_extra_primitive_character(self):
        self.assertEqual(m.power_of_two_clock(4),m.matmul(m.power_of_two_clock(3),m.power_of_two_clock(3)))


class SourceValuationTree(unittest.TestCase):
    def test_source_compact_polynomial_and_four_poles_exact(self):
        for n in range(1,1000):
            self.assertEqual(m.source_fraction(n),m.source_collapsed(n))
            self.assertEqual(m.source_denominator(n)%2,1)

    def test_channel_local_v2_from_481(self):
        for n in list(range(1,80))+[128,256,512,1024]:
            p=m.channel(n,m.PLUS);q=m.channel(n,m.MINUS)
            self.assertEqual(p+q,m.source_fraction(n))
            self.assertEqual(m.v2_rat(p),-5-m.v2_int(n))
            self.assertEqual(m.v2_rat(q),-5-m.v2_int(n))
            self.assertGreaterEqual(m.v2_rat(p+q),0)

    def test_Hensel_simple_root_exists_unique_through_mod2_13(self):
        for bits in range(1,14):
            root=m.hensel_simple_root(bits)
            modulus=1<<bits
            self.assertTrue(0<=root<modulus)
            self.assertEqual(m.source_numerator(root)%modulus,0)
            if bits<=11:
                self.assertEqual(sum(1 for n in range(modulus)
                                     if m.source_numerator(n)%modulus==0),1)
        self.assertEqual(m.hensel_simple_root(7),16)
        self.assertEqual(m.hensel_simple_root(8),144)
        self.assertEqual(m.hensel_simple_root(10),656)
        self.assertEqual(m.hensel_simple_root(16),13968)

    def test_Hensel_root_compatibility_through_40_bits(self):
        roots=[m.hensel_simple_root(k) for k in range(1,41)]
        for k in range(1,40):
            self.assertEqual(roots[k]%(1<<k),roots[k-1])
            self.assertEqual(m.source_numerator(roots[k])%(1<<(k+1)),0)

    def test_isometric_polynomial_factor_and_rational_odd_denom(self):
        root=m.hensel_simple_root(20)
        for n in list(range(-63,128))+[144,656,1680,13968,2**12]:
            if (n-root)%(1<<20):
                self.assertEqual(m.v2_int(m.source_numerator(n)),m.v2_int(n-root))
            for j in (n+1,n+2,n+16,n+127):
                self.assertEqual(m.v2_int(m.source_numerator(n)-m.source_numerator(j)),m.v2_int(n-j))
                self.assertEqual(m.v2_rat(m.source_collapsed(n)-m.source_collapsed(j)),m.v2_int(n-j))

    def test_exact_one_Hensel_residue_class_at_every_precision(self):
        for bits in range(1,17):
            for A in (0,8,16,128,256,1024):
                L=256
                exact=sum(1 for n in range(A,A+L) if m.source_numerator(n)%(1<<bits)==0)
                self.assertEqual(m.residue_count(A,L,bits),exact)
                self.assertLessEqual(exact,(L+(1<<bits)-1)//(1<<bits))

    def test_dyadic_epoch_genuine_exceptional_set_budget(self):
        for j in range(3,11):
            A=1<<j
            for bits in range(1,15):
                count=m.residue_count(A,A,bits)
                if bits<=j:self.assertEqual(count,1<<(j-bits))
                else:self.assertIn(count,(0,1))

    def test_power_two_index_valuation_exception_at_16(self):
        for k in range(0,15):
            n=1<<k
            predicted=k if k<=3 else 7 if k==4 else 4
            self.assertEqual(m.v2_int(m.source_numerator(n)),predicted)
        self.assertEqual(m.source_numerator(16),29312)
        self.assertEqual(F(m.source_numerator(16),128),F(229))

    def test_two_stage_gluing_deduction_power_indices(self):
        for k in range(1,15):
            data=m.two_stage_power2(k)
            self.assertEqual(data['lane_v2'],-5-k)
            self.assertEqual(data['channel_to_source_bits'],data['r_v2']+k+5)
            self.assertEqual(data['source_prev_to_state_bits'],max(k-4,0))
        self.assertEqual(m.two_stage_power2(4)['channel_to_source_bits'],16)
        self.assertEqual(m.two_stage_power2(7)['source_prev_to_state_bits'],3)

    def test_2adic_F0_boundary_and_isometry_integer_controls(self):
        for bits in (8,12,20,32,48,64):
            self.assertEqual(m.p_adic_particular_mod(0,bits),0)
            for n in (1,2,3,7,16,31,32,63,64,127,128):
                self.assertEqual(m.v2_int(n),m.v2_int(m.p_adic_particular_mod(n,bits)))
            for a,b in ((0,1),(3,7),(11,32),(16,128),(63,88)):
                self.assertEqual(m.v2_int(a-b),m.v2_int((m.p_adic_particular_mod(a,bits)-m.p_adic_particular_mod(b,bits))%(1<<bits)))

    def test_2adic_main_U_n_equals_recursion_all_finite(self):
        for bits in (8,12,24,40):
            values=m.source_states_mod(256,bits)
            for n in range(0,257):
                self.assertEqual(values[n],m.p_adic_particular_mod(n,bits))
                if n>=1 and n%(1<<bits)!=0:
                    self.assertEqual(m.v2_int(values[n]),m.v2_int(n))
        exact=m.original_states(128)
        for n in range(129):
            if n>=1:
                self.assertEqual(m.v2_rat(exact[n]),m.v2_int(n))
            self.assertEqual(m.source_states_mod(n,20)[n],m.source_states_mod(128,20)[n])

    def test_16_stage_follows_previous_val4_no_extra(self):
        states=m.original_states(128)
        for k in (4,5,6,7):
            n=1<<k
            prev=16*states[n-1]
            r=m.source_fraction(n)
            self.assertEqual(states[n],prev+r)
            self.assertEqual(m.v2_rat(prev),4)
            self.assertEqual(m.v2_rat(r),7 if k==4 else 4)
            self.assertEqual(m.v2_rat(states[n]),k)
            if k>=5:
                self.assertEqual(m.v2_rat(states[n])-4,k-4)


    def test_preregistered_fresh_high_power_modular_receipts(self):
        import json
        receipt=Path(__file__).resolve().parents[1]/'research'/'2026-11-03'/'figure_eight_pow2'/'HOLDOUTS.json'
        record=json.loads(receipt.read_text())
        bits=24
        for row in record['epochs']:
            n=row['n']; k=row['k']
            U=m.source_states_mod(n,bits)
            got={'k':k,'n':n,'U_n_mod_2_24':U[n],
                 'r_n_mod_2_24':m.source_mod(n,bits),
                 '16Uprev_mod_2_24':(16*U[n-1])%(1<<bits),
                 'v2_U_n':m.v2_int(U[n]),
                 'v2_r':m.v2_int(m.source_mod(n,bits)),
                 'v2_prev':m.v2_int((16*U[n-1])%(1<<bits)),
                 'extra_dynamic_bits':k-4,
                 'match_particular':U[n]==m.p_adic_particular_mod(n,bits)}
            self.assertEqual(got,row)
        for k,r in record['root_mods'].items():
            self.assertEqual(m.hensel_simple_root(int(k)),r)


class BoundarySourceControls(unittest.TestCase):
    def test_all_micro_octaves_recover_original_source_mellin_prefix(self):
        for K in (1,2,3,4,8,16):
            summation=sum((m.TAPS[j]/F(16**(b+1)*(8*b+j+1))
                           for b in range(K) for j in range(8)),F(0))
            self.assertEqual(summation,m.completion(K))
            self.assertEqual(m.completion(K,m.PLUS)+m.completion(K,m.MINUS),m.completion(K))

    def test_source_changed_first_jet_no_longer_cancels(self):
        broken=list(m.TAPS);broken[0]+=1
        for B in (1,2,4,8):
            vals=[F(x)/16**b for b in range(B) for x in broken]
            self.assertEqual(sum(vals,F(0)),sum(F(1,16**b) for b in range(B)))
            # A spurious nonzero boundary mass reintroduces an O(16^-B/B) tail.

    def test_same_original_source_coherent_wrong_seed_passes_all_boundary_identity(self):
        for B in (8,16,32):
            seed,completed=m.source_control_shadow(B)
            self.assertNotEqual(seed,0)
            self.assertTrue(all(v%1==F(1,5) for v in completed))
            real_states=m.original_states(B)
            for n in range(B+1):
                self.assertEqual(real_states[n]+m.finite_future(n,B),16**n*m.completion(B))

    def test_gamma_tail_first_boundary_orders_both_channels(self):
        # Strict finite rational telescoping checks and positive true tail
        # cutoffs; full global endpoint asymptotic is proved analytically.
        for B in (2,8,16,32):
            a=m.completion(B)
            self.assertGreater(a,0)
            self.assertEqual(m.completion(B,m.PLUS)+m.completion(B,m.MINUS),a)
            U=m.original_states(B)
            for n in (0,B//2,B):
                self.assertEqual(U[n]+m.finite_future(n,B),16**n*a)

if __name__=='__main__':unittest.main()
