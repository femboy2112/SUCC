"""Exact fresh Wronskians for the atom-count lower bound; no float authority."""
import json, math
from fractions import Fraction as F
import sympy as s

def main():
 rows=[]
 for J,m,b in ((0,1,F(1,8)),(0,4,F(7,16)),(1,3,F(2,7)),(2,4,F(11,5)),
               (3,2,F(19,13)),(4,3,F(1,31)),(0,5,F(3,2)),(5,2,F(127,64))):
  a=[]
  for i in range(m):
   k=J+1+i
   a.append([F((-1)**k*math.factorial(k+1))*(16/(b+n-1)**(k+2)-1/(b+n)**(k+2)) for n in range(1,m+1)])
  determinant=s.Matrix([[s.Rational(x.numerator,x.denominator) for x in row] for row in a]).det()
  assert determinant*(-1)**(m*(J+1))>0
  rows.append({'J':J,'m':m,'b':str(b),'determinant':str(determinant),'sign':(-1)**(m*(J+1))})
 print(json.dumps({'status':'PASS','rows':rows,'scope':'finite exact checks; universal ECT proof in dossier'},indent=2))

if __name__=='__main__':main()
