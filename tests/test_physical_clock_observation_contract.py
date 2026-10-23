"""Synthetic only: calibrate the observer protocol and kill false physical inference."""
import unittest
from observational_succ.observation_pinned_geometry import ObservationContractError
from scripts.physical_clock_observation_contract import analyze


def simulated(p=2):
    fine=[f'fine-{i}' for i in range(p*p)]
    return {
        'source_id':'SYNTHETIC_DEVICE_NOT_OBSERVED',
        'instrument_id':'SIMULATED_PHASE_SENSOR',
        'candidate_primes':[2,3,5,7],
        'phase_labels':[f'phase-{i%p}' for i in range(3*p+1)],
        'second_level':{
            'phase_labels':fine+[fine[0]],
            'coarse_phase_for_fine_sequence':[f'phase-{i%p}' for i in range(p*p)],
            'multiplier_p_outputs':[fine[(p*i)%(p*p)] for i in range(p*p)],
        }
    }


class IndependentPhysicalSourceContract(unittest.TestCase):
    def test_two_stages_choose_model_but_not_physical_ontology(self):
        for p in (2,3,5):
            j=analyze(simulated(p))
            self.assertEqual(j['selected_prime'],p)
            self.assertEqual(j['second_level_result'],'SECOND_LEVEL_HELD_OUT_PREDICTIONS_MATCH')
            self.assertFalse(j['source_hypotheses_global_verified'])
            self.assertFalse(j['physical_measurement_authentication_by_script'])
            self.assertFalse(j['spacetime_geometry_identified'])

    def test_hidden_ring_mutation_killed_by_heldout_multiplier(self):
        x=simulated(2)
        x['second_level']['multiplier_p_outputs']=['fine-0']*4
        r=analyze(x)
        self.assertEqual(r['second_level_result'],'REJECT_FUCC_MULTIPLICATION_HOLDOUT')
        self.assertEqual(r['selected_prime'],2)

    def test_sensor_alias_killed_by_complete_fine_cell_census(self):
        x=simulated(3)
        x['second_level']['phase_labels']=['fake']*10
        self.assertEqual(analyze(x)['second_level_result'],
                         'REJECT_INCOMPLETE_OR_ALIASED_FINE_CLOCK')

    def test_source_map_mismatch_killed_independently(self):
        x=simulated(2)
        x['second_level']['coarse_phase_for_fine_sequence']=['phase-0']*4
        self.assertEqual(analyze(x)['second_level_result'],
                         'REJECT_INCOMPATIBLE_RING_QUOTIENT_MAP')

    def test_unverified_first_stage_never_upgraded(self):
        x=simulated(2)
        del x['second_level']
        self.assertEqual(analyze(x)['second_level_result'],'NOT_SUPPLIED')
        del x['source_id']
        with self.assertRaises(ObservationContractError):analyze(x)


if __name__=='__main__':unittest.main()
