// Principia Intermedia exact research probe. Run: node probe.mjs
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a}

function q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d}let g=gcd(n,d);return[n/g,d/g]}

function add(a,b){return q(a[0]*b[1]+b[0]*a[1],a[1]*b[1])}

function neg(a){return q(-a[0],a[1])}

function sub(a,b){return add(a,neg(b))}

function mul(a,b){return q(a[0]*b[0],a[1]*b[1])}

function div(a,b){return q(a[0]*b[1],a[1]*b[0])}

function pow(a,n){if(n<0)return pow(q(a[1],a[0]),-n);return q(a[0]**BigInt(n),a[1]**BigInt(n))}

function cmp(a,b){let x=a[0]*b[1]-b[0]*a[1];return x<0n?-1:x>0n?1:0}

function abs(a){return a[0]<0n?neg(a):a}

function fmt(a){return a[0].toString()+"/"+a[1].toString()}

function val(a,p){if(!a[0])throw Error("valuation zero");p=BigInt(p);let x=a[0]<0n?-a[0]:a[0],y=a[1],v=0;while(x%p===0n){x/=p;v++}while(y%p===0n){y/=p;v--}return v}

function check(b,msg){if(!b)throw Error(msg)}

function primitive(k,t){return [[4,1],[-2,4],[-1,5],[-1,6]].reduce((z,[c,j])=>add(z,mul(q(c,8*k+j),pow(t,8*k+j))),q(0))}

function primitiveFactored(k,t){let z=q(0);for(let j=0;j<5;j++){let c=[4,4,4,2,1][j],a=8*k+j+1;z=add(z,mul(q(c),sub(div(pow(t,a),q(a)),div(pow(t,a+1),q(a+1)))))}return z}

function sourceMoment(k){return add(sub(q(4,8*k+1),q(2,8*k+4)),sub(q(-1,8*k+5),q(1,8*k+6)))}

function signedMoment(k,cuts,first=1){let v=q(0),last=q(0),s=first;for(let t of [...cuts,q(1)]){check(cmp(last,t)<0,"ordered interior cuts");v=add(v,mul(q(s),sub(primitive(k,t),primitive(k,last))));last=t;s=-s}return v}

function signedOracle(k,cuts,first=1){let z=mul(q(first*((cuts.length%2)?-1:1)),primitiveFactored(k,q(1)));for(let i=0;i<cuts.length;i++)z=add(z,mul(q(2*first*(i%2?-1:1)),primitiveFactored(k,cuts[i])));return z}

function* choose(n,k,start=0,prefix=[]){if(k===0){yield prefix;return}for(let i=start;i<=n-k;i++)yield* choose(n,k-1,i+1,[...prefix,i])}

function medianGrid(B){let lo=0,hi=B;while(hi-lo>1){let m=Math.floor((lo+hi)/2);if(cmp(signedMoment(0,[q(m,B)]),q(0))<0)lo=m;else hi=m}let cand=[lo,hi].filter(x=>x>0&&x<B);return cand.map(a=>({a,B,D:signedMoment(0,[q(a,B)])})).sort((a,b)=>cmp(abs(a.D),abs(b.D)))[0]}

function solve(A,b){let n=b.length,M=A.map((row,i)=>[...row,b[i]]);for(let i=0;i<n;i++){let j=M.findIndex((row,j)=>j>=i&&row[i][0]!==0n);if(j<0)return null;[M[i],M[j]]=[M[j],M[i]];let t=M[i][i];M[i]=M[i].map(v=>div(v,t));for(let j=0;j<n;j++)if(j!==i){let f=M[j][i];M[j]=M[j].map((v,k)=>sub(v,mul(f,M[i][k])))}}return M.map(row=>row[n])}

function dot(a,b){return a.reduce((z,x,i)=>add(z,mul(x,b[i])),q(0))}

function signChanges(x){let s=x.map(y=>cmp(y,q(0))).filter(y=>y!==0),k=0;for(let i=1;i<s.length;i++)if(s[i]!==s[i-1])k++;return k}

function discreteBalance(N,n){let x=Array.from({length:N},(_,i)=>pow(q(2*i+1,2*N),8)),w=Array.from({length:N},(_,i)=>sub(primitive(0,q(i+1,N)),primitive(0,q(i,N))));let M=Array.from({length:n+1},(_,j)=>x.map((z,i)=>mul(w[i],pow(z,j))));let best=null,vertices=0;for(let F of choose(N,n)){let rest=Array.from({length:N},(_,i)=>i).filter(i=>!F.includes(i));for(let mask=0;mask<2**rest.length;mask++){let s=Array.from({length:N},()=>q(0));rest.forEach((i,j)=>s[i]=q((mask>>j)&1?1:-1));let A=M.slice(0,n).map(row=>F.map(i=>row[i])),b=M.slice(0,n).map(row=>neg(dot(row,s))),v=solve(A,b);if(!v||v.some(y=>cmp(abs(y),q(1))>0))continue;F.forEach((i,j)=>s[i]=v[j]);vertices++;check(M.slice(0,n).every(row=>dot(row,s)[0]===0n),"LP moment null");check(signChanges(s)>=n,"nonzero null vector sign changes");let objective=dot(M[n],s);if(!best||cmp(objective,best.objective)>0)best={s,objective}}}check(best&&best.objective[0]>0n,"positive next moment");check(best.s.filter(y=>cmp(abs(y),q(1))<0).length<=n,"fractional count");return{N,n,vertices,signChanges:signChanges(best.s),fractional:best.s.filter(y=>cmp(abs(y),q(1))<0).length,objective:fmt(best.objective),weights:"exact BBP Q cell masses",nodes:"midpoint t^8, atomic quadrature not exact continuous higher moments"}}

function viable(layers,edges,a,b,world){let L=[new Set([a])],R=Array(layers.length);for(let i=0;i<edges.length;i++)L.push(new Set(edges[i].filter(([x,y])=>world[x]===world[y]&&L[i].has(x)).map(e=>e[1])));R[R.length-1]=new Set([b]);for(let i=edges.length-1;i>=0;i--)R[i]=new Set(edges[i].filter(([x,y])=>world[x]===world[y]&&R[i+1].has(y)).map(e=>e[0]));return L.map((s,i)=>[...s].filter(x=>R[i].has(x)).sort())}

function enumeratePaths(layers,edges,a,b,world){let G=layers.map(()=>new Set());function walk(path){let i=path.length-1;if(i===layers.length-1){if(path[i]===b)path.forEach((x,j)=>G[j].add(x));return}for(let [x,y] of edges[i])if(x===path[i]&&world[x]===world[y])walk([...path,y])}walk([a]);return G.map(x=>[...x].sort())}

function det(A){let n=A.length;if(!n)return q(1);if(n===1)return A[0][0];let z=q(0);for(let j=0;j<n;j++)z=add(z,mul(mul(q(j%2?-1:1),A[0][j]),det(A.slice(1).map(row=>row.filter((_,i)=>i!==j)))));return z}

function matmul(A,B){return A.map(row=>B[0].map((_,j)=>dot(row,B.map(r=>r[j]))))}

function gram(A){return A[0].map((_,i)=>A[0].map((_,j)=>dot(A.map(r=>r[i]),A.map(r=>r[j]))))}

function primePower(p,e){return e>=0?q(BigInt(p)**BigInt(e)):q(1,BigInt(p)**BigInt(-e))}

function heightCost(a,ys,ps){let v=abs(a);for(let p of ps){v=mul(v,primePower(p,-val(mul(a,ys[p]||q(1)),p)))}return v}

function run(){
 let counts={sourceMoments:0,oddChartPartitions:0,parityObservations:0,positiveNegativeControls:0,graphOracles:0,volumeOracles:0,heightOracles:0},median=[],lp=[];
 for(let k=0;k<32;k++){check(cmp(sourceMoment(k),primitive(k,q(1)))===0,"four-pole identity");check(cmp(sourceMoment(k),primitiveFactored(k,q(1)))===0,"factor identity");check(val(sourceMoment(k),2)>=0,"source 2-integrality");check((val(sourceMoment(k),2)===0)===(k%2===0),"source parity");counts.sourceMoments++}
 for(let B of [3,5,7,9,11])for(let n=0;n<=Math.min(B-1,4);n++)for(let I of choose(B-1,n)){let cuts=I.map(i=>q(i+1,B));counts.oddChartPartitions++;for(let k=0;k<=6;k++)for(let first of [-1,1]){let D=signedMoment(k,cuts,first),O=signedOracle(k,cuts,first);check(cmp(D,O)===0,"direct integration vs factored alternating oracle");check(D[1]%2n===1n,"odd denominator");check((D[0]%2n!==0n)===(k%2===0),"partition parity");if(k===0)check(cmp(abs(D),q(1,15n*BigInt(B)**6n))>=0,"rational seam lower bound");counts.parityObservations++}}
 for(let B of [3,9,27,81,243,729,2187,6561,19683,59049]){let m=medianGrid(B);check(val(m.D,2)===0,"median residual 2-adic unit");check(cmp(abs(m.D),q(8,B))<=0,"median real convergence bound");median.push({denominator:B,numerator:m.a,residual:fmt(m.D),v2:val(m.D,2)})}
 check(cmp(signedMoment(0,[q(1,5)]),q(0))!==0,"only interior candidate rational root");counts.positiveNegativeControls++;
 let uni=(k,cuts)=>{let z=q(0),last=q(0),s=1;for(let t of [...cuts,q(1)]){z=add(z,mul(q(s,k+1),sub(pow(t,k+1),pow(last,k+1))));last=t;s=-s}return z};
 check([0,1].every(k=>uni(k,[q(1,4),q(3,4)])[0]===0n)&&cmp(uni(2,[q(1,4),q(3,4)]),q(1,16))===0,"uniform two-null control");counts.positiveNegativeControls++;
 check([0,1,2].every(i=>[["a","b"],["b","c"],["a","c"]][i].some(x=>[["a","b"],["b","c"],["a","c"]][(i+1)%3].includes(x)))&&!["a","b","c"].some(x=>[["a","b"],["b","c"],["a","c"]].every(y=>y.includes(x))),"pairwise source overlap no global world");counts.positiveNegativeControls++;
 for(let [N,n] of [[4,1],[5,2],[6,3],[7,2],[7,3]])lp.push(discreteBalance(N,n));
 let seed=20261126;const rand=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed};
 for(let z=0;z<250;z++){let layers=Array.from({length:2+rand()%4},(_,i)=>Array.from({length:3},(_,j)=>i+":"+j)),world={};for(let l of layers)for(let x of l)world[x]=rand()%2;let edges=layers.slice(0,-1).map((l,i)=>l.flatMap(x=>layers[i+1].filter(()=>rand()%5<3).map(y=>[x,y])));let a=layers[0][0],b=layers.at(-1)[2];check(JSON.stringify(viable(layers,edges,a,b,world))===JSON.stringify(enumeratePaths(layers,edges,a,b,world)),"graph oracle");counts.graphOracles++}
 for(let z=1;z<=25;z++){let B0=[[q(1),q(0)],[q(0),q(1)]],A=[[q(z),q(1)],[q(0),q(2)],[q(1),q(0)]],C=[[q(2),q(0),q(0)],[q(0),q(3),q(0)],[q(0),q(0),q(5)],[q(1),q(1),q(0)]],B1=matmul(A,B0),B2=matmul(C,B1),g0=det(gram(B0)),g1=det(gram(B1)),g2=det(gram(B2));check(g1[0]>0n&&g2[0]>0n,"injective chain");check(cmp(mul(div(g1,g0),div(g2,g1)),div(g2,g0))===0,"same image volume telescope");counts.volumeOracles++}
 for(let i=1;i<=6;i++)for(let j=1;j<=6;j++){let a=q(2n**BigInt(i)*3n**BigInt(j),5n**BigInt(i)),ps=[2,3,5],ys={2:q(3,4),3:q(9,5),5:q(5,2)},inv=Object.fromEntries(ps.map(p=>[p,div(q(1),ys[p])]));check(cmp(heightCost(a,{},ps),q(1))===0,"product formula");check(cmp(mul(heightCost(a,ys,ps),heightCost(q(7,3),inv,[2,3,5,7])),q(1))===0,"reciprocal family height cancellation");counts.heightOracles++}
 check(cmp(mul(q(1),q(1,2)),q(1))<0,"fake independent normalization budget");counts.positiveNegativeControls++;
 let d=q(10),n=q(9),h=q(20),m=q(2),R=q(4),L=q(1),I=q(30),w=add(sub(h,mul(m,R)),L),V=mul(n,w),H=q(20),delta=q(1,10);check(cmp(mul(d,sub(h,mul(q(3),L))),add(V,mul(q(2),I)))<=0,"synthetic common budget antecedent");check(cmp(mul(m,R),add(add(mul(q(4),L),mul(delta,H)),div(mul(q(2),I),d)))<=0,"budget conclusion");counts.positiveNegativeControls++;
 return{scope:"Exact BigInt rational finite controls; not universal proof or Lean verification",counts,medianGrid:median,atomicLP:lp};
}

console.log(JSON.stringify(run(),null,2));
