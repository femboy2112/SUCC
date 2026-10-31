"""Certified complete selected characters on prime-clock windows.

Preregistered fresh frequencies 11,13 on p=1201,1213,1229,1237,1249,1277.
Finite candidate: squared normalized modulus <1/4 for each row. A crossing
refutes this finite candidate; passing never proves its unbounded extension.
The oracle separately retains both primary and complementary rational parts.
"""
import json
from pathlib import Path
import certified_band as c


def order(p):
    z,L=16%p,1
    while z!=1:z,L=z*16%p,L+1
    return L


def main():
    windows=[(p,(p+7)//8 if p%8==1 else (p+3)//8,order(p))
             for p in (1201,1213,1229,1237,1249,1277)]
    last=max(b+L-1 for p,b,L in windows)
    phases=dict(c.selected_intervals(last))
    rows=[]
    for p,b,L in windows:
        for h in (11,13):
            re,im=(0,0),(0,0)
            for n in range(b,b+L):
                x=phases[n]
                z=c.trig((h*x[0],h*x[1]))
                re,im=c.add(re,z[0]),c.add(im,z[1])
            norm2=c.div(c.add(c.square(re),c.square(im)),L*L)
            verdict='PASS FINITE' if norm2[1]<c.S//4 else 'FAIL FINITE' if norm2[0]>c.S//4 else 'AMBIGUOUS'
            rows.append({'p':p,'birth':b,'length':L,'h':h,'squared_modulus_lower':c.decimal_out(norm2[0],True),
                         'squared_modulus_upper':c.decimal_out(norm2[1],False),
                         'dyadic_lower':str(norm2[0]),'dyadic_upper':str(norm2[1]),'verdict':verdict})
    result={'status':'CERTIFIED FINITE ONLY','bits':c.P,'candidate':'each declared squared mean modulus <1/4',
            'rows':rows,'asymptotic_selected_bound':'DARK; no window-coverage theorem supplied'}
    dest=Path(__file__).parent/'receipts/signed-windows-data.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
