import mpmath as mp, math
mp.mp.dps=30
# (a) Lemma 2.3 kernel is real: H(v)=sqrt(v)L(log2 1/v), L 2-periodic mean 0 => int_1^2 H(c/u^2)du = 0 for all c
L=lambda s: mp.cos(mp.pi*s)+mp.mpf(1)/3*mp.sin(3*mp.pi*s)
H=lambda v: mp.sqrt(v)*L(mp.log(1/v,2))
print("max |int_1^2 H(c/u^2)du| over c grid:",mp.nstr(max(abs(mp.quad(lambda u:H(c/u**2),[1,2])) for c in [mp.mpf(i)/37 for i in range(1,37)]),3))
# (b) monotonicity is load-bearing: F=a+v+eps*H is non-monotone near 0 for EVERY eps>0 (Lemma 2.4 needs it)
for eps in [1e-1,1e-3,1e-6]:
    s=0; found=None
    for j in range(0,400):
        v=mp.mpf(2)**(-j/4.0); w=v/4
        if (v+eps*H(v))-(w+eps*H(w))<0: found=float(v);break
    print("eps=%g: F(v)<F(v/4) at v=%s"%(eps,found))
# (c) the CB-2' remark witness. Paper: G(t)=eps*A*sin(2pi log2(t/A)) (A fixed) is bounded => all window defects o(A).
#     Correct witness: G(t)=eps*t*sin(2pi log2 t); realise as a 0/1 sequence (x in [0,1/2) or not) by greedy tracking.
eps=0.05; N=2**21; cnt=0; c=[0]
for t in range(1,N+1):
    target=0.5*t+eps*t*math.sin(2*math.pi*math.log2(t))
    bit=1 if cnt+1-target<=target-cnt else 0
    cnt+=bit; c.append(cnt)
fr=lambda a,b:(c[b]-c[a])/(b-a)
j=19; A=2**j
print("dyadic window [2^19,2^20) freq =",round(fr(A,2*A),5),"; sub-window [1.5*2^19,2^20) freq =",round(fr(int(1.5*A),2*A),5),
      "; non-dyadic window [1.5*2^19,3*2^19) freq =",round(fr(int(1.5*A),3*A),5))
