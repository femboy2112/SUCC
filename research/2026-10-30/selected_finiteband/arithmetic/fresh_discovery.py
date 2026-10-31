"""Fresh dimensions/grid after the first four quadrature witnesses were fixed."""
import json
from quadrature import discover
if __name__=='__main__':
 print(json.dumps({'rows':[discover(M,J,step=64,blocks=6) for M,J in ((1,5),(5,2),(6,0))]},indent=2))
