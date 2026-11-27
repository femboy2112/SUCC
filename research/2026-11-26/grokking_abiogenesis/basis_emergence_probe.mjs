// Standalone exact BigInt calibration; no dependencies or I/O except stdout.
// Run with a modern Node.js: node basis_emergence_probe.mjs
function runProbe() {
  const I=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>BigInt(i===j)));
  const mat=(pairs)=>{let m=I(4);for(const [i,j] of pairs)m[i-1][j-1]+=1n;return m};
  const mm=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,v,k)=>s+v*b[k][j],0n)));
  const add=(...rs)=>rs[0].map((_,i)=>rs.reduce((s,r)=>s+r[i],0n));
  const neg=r=>r.map(x=>-x);
  const same=(a,b)=>JSON.stringify(a,(_,v)=>typeof v==="bigint"?String(v):v)===JSON.stringify(b,(_,v)=>typeof v==="bigint"?String(v):v);
  const rank=rows=>{let m=rows.map(r=>r.slice()),p=0;for(let j=0;j<m[0].length;j++){let q=m.findIndex((r,i)=>i>=p&&r[j]!==0n);if(q<0)continue;[m[p],m[q]]=[m[q],m[p]];for(let i=p+1;i<m.length;i++){const a=m[p][j],b=m[i][j];if(b!==0n)m[i]=m[i].map((v,k)=>a*v-b*m[p][k]);}p++;}return p};
  const P=[[1n,0n,0n,0n]], rows=[];
  for(const [name,A,B,expectedRank,expectedCommute,expectedMixed] of [
    ["mixed_commuting",mat([[1,2],[3,4]]),mat([[1,3],[2,4]]),4,true,[0n,0n,0n,1n]],
    ["additive_null",mat([[1,2]]),mat([[1,3]]),3,true,[0n,0n,0n,0n]],
    ["mixed_order_sensitive",mat([[1,2]]),mat([[1,3],[2,4]]),4,false,[0n,0n,0n,1n]]
  ]){
    const a=mm(P,A)[0],b=mm(P,B)[0],ab=mm(mm(P,A),B)[0],ba=mm(mm(P,B),A)[0],res=add(ab,neg(a),neg(b),P[0]);const base=[P[0],a,b];
    let pure=[];for(let M of [A,B]){let u=P;for(let j=0;j<8;j++){pure.push(u[0]);u=mm(u,M);}}
    const commute=same(mm(A,B),mm(B,A)), mixedRank=rank([...base,ab,ba]),pureRank=rank(pure);
    if(pureRank!==3||mixedRank!==expectedRank||commute!==expectedCommute||!same(res,expectedMixed)||!pure.every(r=>r[3]===0n))throw Error(name+" failed");
    rows.push({name,P:P[0].map(String),PA:a.map(String),PB:b.map(String),PAB:ab.map(String),PBA:ba.map(String),mixed:res.map(String),commute,pureRank,mixedRank});
  }
  const scale2=[[2n]],scale3=[[3n]],p1=[[1n]],s2=mm(p1,scale2)[0],s3=mm(p1,scale3)[0],s23=mm(mm(p1,scale2),scale3)[0],scalarMixed=add(s23,neg(s2),neg(s3),p1[0]);
  if(!same(scalarMixed,[2n])||rank([p1[0],s2,s3,s23])!==1)throw Error("in-span nonzero contrast failed");
  const lattice=[];
  const pop=s=>{let k=0;while(s){s&=s-1;k++}return k};
  for(let m=1;m<=6;m++){
    const n=1<<m,p=Array(n).fill(0n);p[0]=1n;
    const apply=(r,i)=>{let y=r.slice(),bit=1<<i;for(let s=0;s<n;s++)if((s&bit)===0)y[s|bit]+=r[s];return y};
    const all=Array.from({length:n},(_,t)=>{let r=p;for(let i=0;i<m;i++)if(t&(1<<i))r=apply(r,i);return r});
    const mobius=Array.from({length:n},(_,t)=>{let r=Array(n).fill(0n);for(let u=t;;u=(u-1)&t){const sign=(pop(t)-pop(u))%2?-1n:1n;for(let s=0;s<n;s++)r[s]+=sign*all[u][s];if(u===0)break;}return r});
    if(!mobius.every((r,t)=>r.every((x,s)=>x===BigInt(s===t))))throw Error("Möbius failed");
    const ranks=Array.from({length:m+1},(_,k)=>rank(all.filter((_,t)=>pop(t)<=k)));
    const expected=Array.from({length:m+1},(_,k)=>Array.from({length:n},(_,t)=>pop(t)).filter(v=>v<=k).length);
    if(!same(ranks,expected))throw Error("rank failed");
    lattice.push({m,dimension:n,mobiusIdentity:true,ranks});
  }
  return {matrix_controls:rows,in_span_nonzero:{mixed:String(scalarMixed[0]),rank:1},lattice};
}
console.log(JSON.stringify(runProbe(), null, 2));
