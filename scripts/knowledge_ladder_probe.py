#!/usr/bin/env python3
"""Reproduce lawful two-observer Hard-SUCC knowledge ladder.

The source truth is supplied ONLY to each local observation simulator;
the recipient is given the shared basis and a finite relayed transcript.
No authentication of real-world evidence, physical speedup or infinity.
"""
import json

from observational_succ.knowledge_ladder import knowledge_ladder_demo


def main():
    result = knowledge_ladder_demo()
    assert result["status"] == "EXACT_FINITE_INTEROBSERVER_KNOWLEDGE_LADDER"
    assert result["discovery_succ_steps"] == 6
    assert result["receiver_knowledge_aided_steps"] == 3
    assert result["end_source_class"] == ["B"]
    assert result["full_shared_semantics_and_causal_records_match"] is True
    assert [r["local_discovery_steps"] for r in result["rungs"]] == [2, 2, 2]
    assert [r["receiver_informed_steps"] for r in result["rungs"]] == [1, 1, 1]
    assert result["sender_outcomes_cryptographically_authenticated"] is False
    assert result["physical_time_speedup_proved"] is False
    assert result["infinite_ladder_executed"] is False
    assert result["RH_claimed"] is False
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
