// Standalone exact calibration. Run: node probe.mjs
function probe() {
  const counts={};const check=(g,ok)=>{if(!ok)throw Error(g+" failed");counts[g]=(counts[g]??0)+1};
  const nodes=mask=>[0,1,2].filter(i=>mask&(1<<i));
  let reachableGraphs=0,trapGraphs=0;
  for(let a=1;a<8;a++)for(let b=1;b<8;b++){
    const es=[nodes(a),nodes(b),[2]];
    const reachable=i=>{const q=[i],s=new Set(q);for(let k=0;k<q.length;k++)for(const j of es[q[k]])if(!s.has(j)){s.add(j);q.push(j)}return s.has(2)};
    const both=reachable(0)&&reachable(1);if(both)reachableGraphs++;else trapGraphs++;
    for(let start=0;start<2;start++){
      let v=[0n,0n];v[start]=1n;
      const walks=(i,k)=>i===2?0n:k===0?1n:es[i].reduce((s,j)=>s+BigInt(6/es[i].length)*walks(j,k-1),0n);
      for(let t=1;t<=12;t++){
        let w=[0n,0n];for(let i=0;i<2;i++)for(const j of es[i])if(j!==2)w[j]+=v[i]*BigInt(6/es[i].length);
        v=w;let surv=v[0]+v[1],den=6n**BigInt(t);
        if(t<=4)check("graph_dp_vs_walks",surv===walks(start,t));
        if(both&&t%2===0){const k=BigInt(t/2);check("graph_uniform_block_tail",surv*9n**k<=den*8n**k);}
        if(!reachable(start))check("graph_unreachable_survival",surv===den);
      }
    }
  }
  let masks=Array(16).fill(0n);masks[0]=1n;const coupon=[];
  const choose=[1n,4n,6n,4n,1n];
  for(let t=0;t<=20;t++){
    const total=4n**BigInt(t),all=choose.reduce((v,c,j)=>v+(j%2?-1n:1n)*c*BigInt(4-j)**BigInt(t),0n);
    check("coupon_inclusion_exclusion",all===masks[15]);
    if(t>0)check("coupon_union_bound",total-all<=4n*3n**BigInt(t));
    if([0,4,8,12,20].includes(t))coupon.push({t,complete:String(all),total:String(total)});
    let next=Array(16).fill(0n);for(let m=0;m<16;m++)for(let j=0;j<4;j++)next[m|(1<<j)]+=masks[m];masks=next;
  }
  let n=1n,d=1n,n2=1n,d2=1n;
  for(let t=1n;t<=50n;t++){
    n*=(t+1n)**2n-1n;d*=(t+1n)**2n;n2*=t;d2*=t+1n;
    check("summable_hazard_telescoping",n*2n*(t+1n)===d*(t+2n));
    check("infinite_mean_hazard_telescoping",n2*(t+1n)===d2);
  }
  for(let K=2;K<=24;K++){
    let D=2n**BigInt(K)-1n;const H=j=>2n**BigInt(K-j)-1n;
    check("tree_boundary",H(0)===D&&H(K)===0n);
    for(let j=1;j<K;j++)check("tree_harmonic",3n*H(j)===H(j-1)+2n*H(j+1));
    check("tree_return_below_half",2n*H(1)<D);
  }
  const A=x=>[x[0]+x[1],x[1],x[2]+x[3],x[3]], B=x=>[x[0]+x[2],x[1]+x[3],x[2],x[3]];
  const A0=x=>[x[0]+x[1],x[1],x[2],x[3]], B0=x=>[x[0]+x[2],x[1],x[2],x[3]];
  for(let a=-2;a<=2;a++)for(let b=-2;b<=2;b++)for(let c=-2;c<=2;c++)for(let d=-2;d<=2;d++){
    const x=[a,b,c,d],cells=[a,A(x)[0],B(x)[0],A(B(x))[0]];
    check("mixed_decoder",cells[3]-cells[1]-cells[2]+cells[0]===d);
    check("mixed_commute",A(B(x)).every((v,i)=>v===B(A(x))[i]));
    check("additive_null",A0(B0(x))[0]-A0(x)[0]-B0(x)[0]+a===0);
    const y=[a,b,c,d+1];let u=x,v=y,w=x,z=y;
    for(let k=0;k<4;k++){check("pure_history_alias",u[0]===v[0]&&w[0]===z[0]);u=A(u);v=A(v);w=B(w);z=B(z);}
  }
  const primes=[2,3,5],valuation=(n,p)=>{if(n===0)throw Error("zero valuation");let v=0;while(n%p===0){v++;n/=p}return v};
  const smooth=[];for(let n=1;n<=128;n++){let ex=primes.map(p=>valuation(n,p));if(ex.reduce((v,e,i)=>v*primes[i]**e,1)===n)smooth.push({n,ex});}
  const alias={};for(let q of [4,8]){let pairs=[];for(let i=0;i<smooth.length;i++)for(let j=i+1;j<smooth.length;j++){let a=smooth[i],b=smooth[j];let same=a.ex.every((e,k)=>(e-b.ex[k])%q===0);if(same)pairs.push([a.n,b.n]);let matches=true;for(let u=0;u<q;u++)for(let v=0;v<q;v++)for(let w=0;w<q;w++){let z=[u,v,w];let f=a.ex.reduce((s,e,k)=>s+e*z[k],0)%q,g=b.ex.reduce((s,e,k)=>s+e*z[k],0)%q;if(f!==g)matches=false;}check("phase_grid_separation",same===matches);}alias[q]=pairs;}
  check("phase_positive_control",alias[4].some(([a,b])=>a===1&&b===16));check("phase_refinement",alias[8].length===0);
  const N=12,ps=[2,3,5,7,11],q=8;
  const root=n=>n&&ps.every(p=>valuation(n,p)%q===0)?n:0;
  const V=(m,n)=>n&&m*n<=N?m*n:0,adj=(m,n)=>n&&n%m===0?n/m:0,E=(m,n,k)=>V(m,root(adj(n,k)));
  for(let k=1;k<=N;k++)check("root_selector",root(k)===(k===1?1:0));
  for(let m=1;m<=N;m++)for(let n=1;n<=N;n++)for(let k=1;k<=N;k++)check("matrix_units",E(m,n,k)===(k===n?m:0));
  for(let m=1;m<=N;m++)for(let n=1;n<=N;n++)for(let k=1;k<=N;k++)for(let l=1;l<=N;l++)check("matrix_unit_product",E(m,n,E(k,l,l))===(n===k?m:0));
  const mod=x=>((x%5)+5)%5,grades=Array.from({length:25},(_,i)=>[i%5,Math.floor(i/5)]);
  const plus=(a,b)=>[mod(a[0]+b[0]),mod(a[1]+b[1])],c=(a,b)=>mod(a[1]*b[0]);
  for(const a of grades)for(const b of grades)for(const d of grades){
    check("cocycle",mod(c(a,b)+c(plus(a,b),d))===mod(c(b,d)+c(a,plus(b,d))));
    check("hexagon_left",c(plus(a,b),d)===mod(c(a,d)+c(b,d)));
    check("hexagon_right",c(a,plus(b,d))===mod(c(a,b)+c(a,d)));
  }
  return {scope:"Exact finite calibration; no neural data, no infinite theorem or full SUCC validation",counts,graphs:{reachableGraphs,trapGraphs},coupon,phase:{smoothCount:smooth.length,aliases:alias},tree:{limit:"1/2 from depth 1"},hazards:{summable_limit:"1/2",divergent_survival:"1/(k+1)"}};
}
console.log(JSON.stringify(probe(), null, 2));
