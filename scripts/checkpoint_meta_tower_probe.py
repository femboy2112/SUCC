#!/usr/bin/env python3
"""Finite exact E meta-observer policy and proof-order receipt."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.checkpoint_meta_tower import meta_tower_demo

if __name__ == '__main__':
    result = meta_tower_demo()
    assert result['destructive_full_order_enumeration'] == 'MODEL_CERTIFIED_NO_FINITE_POLICY'
    assert result['adaptive_succeeds_where_fixed_length_two_fails'] is True
    assert result['conditional_worst_case_depth'] == 2
    assert result['rule_growth_from_old_evidence'] == [False, True]
    assert result['rule_growth_requires_new_empirical_events'] is False
    assert result['checkpoint_e_knowledge'] == [
        {'index': 1, 'proved': False}, {'index': 2, 'proved': True}]
    assert result['physical_infinity_completed'] is False
    assert result['source_authentication_claimed'] is False
    print(json.dumps(result, indent=2, sort_keys=True))
