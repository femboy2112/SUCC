import sys,time,json
sys.path.insert(0,'/tmp')
exec(open('/tmp/lonely_walk.py').read().split('N=int(sys.argv[1])')[0])
nums=['0','15799/40560','61501/162240','12299/27040','16219/32448','6673/13520','1645417/1784640','2702/27885','12291/13520','2617/8112','248957/324480','10811/13520','99791/137280']
rng=np.random.default_rng(20261028);v=np.arange(1,19);best=1.;start=time.time()
for trial in range(30):
 s=np.array([float(F(x)) for x in nums]+rng.random(5).tolist());d=1/16
 for step in range(30):
  p=lp(v,s,d,rng,False)
  if p is None:print(json.dumps({'trial':trial,'step':step,'failure':'optchain'}),flush=True);break
  s,d,cl=p
  if d<best-1e-10:
   best=d;print(json.dumps({'trial':trial,'step':step,'best':best,'target':1/19,'seconds':time.time()-start}),flush=True)
   open('/tmp/lonely18_best.json','w').write(json.dumps({'v':v.tolist(),'s':s.tolist(),'delta':d,'trial':trial,'step':step}))
  if d<1/19-1e-9:sys.exit(0)
  p=lp(v,s,d,rng,True)
  if p is None:break
  s,d,cl=p
 if trial%5==0:print(json.dumps({'trial':trial,'best':best,'seconds':time.time()-start}),flush=True)
