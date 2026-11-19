"""Regenerate finite source energy and artifact receipts from the repository root."""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
from clock_bridge import source_states, source_shell_certificate, periods


def main():
    scale = 2**40
    states = source_states(512)
    rows = []
    for B in (16,32,64,128,256):
        lo,hi = source_shell_certificate(states,B)
        low = (lo.numerator*scale)//lo.denominator
        high = -((-hi.numerator*scale)//hi.denominator)
        rows.append({"B":B,
                     "count_selected_carries":sum(x.numerator//x.denominator%4 in (1,2)
                                                  for x in states[B:2*B]),
                     "energy_lower":[low,scale], "energy_upper":[high,scale],
                     "approx_interval":[low/scale,high/scale]})
    output = {"source":"original four signed poles; U0=0; exact rational forward states",
              "scope":"existing index range through512, finite calibration, not a fresh pi-digit holdout",
              "tail_bound":"0<T_n<r(n+1)/15",
              "energy":"mean ||16^n*pi/16||_T^2 for B<=n<2B",
              "construction_uses_pi_numeric_value":False, "rows":rows}
    (HERE/"validation/source_energy.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"source_calibration_rows":len(rows),
                      "joint_clock_examples":[{"a":a,"b":b,"periods":periods(a,b),
                                               "source_clock":2**a*3**b}
                                              for a,b in ((1,1),(4,2),(5,3),(7,4))],
                      "R0_proved":False,"pi_normality_proved":False},indent=2))


if __name__ == "__main__":
    main()
