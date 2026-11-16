// Exact NTT scan of the *stronger-than-Goldbach* signed cube-root sieve criterion.
// No numeric floating error: convolution counts < modulus 998244353.
// No claim that a finite verification establishes any universal theorem.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <tuple>
using namespace std;
static constexpr int MOD=998244353, ROOT=3;

int pmod(int x, int64_t e) {
    int64_t a=x, y=1;
    while(e){ if(e&1) y=y*a%MOD; a=a*a%MOD; e>>=1; }
    return int(y);
}
void ntt(vector<int>&a,bool inv) {
    int n=(int)a.size();
    for(int i=1,j=0;i<n;i++){
        int b=n>>1;
        while(j&b){j^=b;b>>=1;}
        j^=b;
        if(i<j)swap(a[i],a[j]);
    }
    for(int len=2;len<=n;len<<=1){
        int wlen=pmod(ROOT,(MOD-1)/len);
        if(inv)wlen=pmod(wlen,MOD-2);
        for(int i=0;i<n;i+=len){
            int64_t w=1;
            for(int j=0;j<len/2;j++){
                int u=a[i+j],v=int(w*a[i+j+len/2]%MOD);
                int sum=u+v; if(sum>=MOD)sum-=MOD;
                int diff=u-v; if(diff<0)diff+=MOD;
                a[i+j]=sum;a[i+j+len/2]=diff;
                w=w*wlen%MOD;
            }
        }
    }
    if(inv){
        int scale=pmod(n,MOD-2);
        for(int &x:a)x=int(int64_t(x)*scale%MOD);
    }
}
vector<int> square_convolution(const vector<uint8_t>&mask,int limit,int nfft){
    vector<int> v(nfft);
    for(int i=0;i<=limit;i++)v[i]=mask[i];
    ntt(v,false);
    for(int &x:v)x=int(int64_t(x)*x%MOD);
    ntt(v,true);
    v.resize(limit+1);
    return v;
}
int cube_root(int n){
    int z=0;
    while(int64_t(z+1)*(z+1)*(z+1)<=n)z++;
    return z;
}
int main(int argc,char**argv){
    int X=argc>=2?atoi(argv[1]):100000;
    if(X<4||X>=MOD/2){cerr<<"X out of proof-safe range"<<endl;return 2;}
    int nfft=1;
    while(nfft < 2*(X+1))nfft*=2;
    if(nfft>=(1<<23)){cerr<<"NTT size unsupported"<<endl;return 3;}
    vector<uint8_t> p(X+1,1),c(X+1,0);
    p[0]=p[1]=0;
    for(int d=2;int64_t(d)*d<=X;d++)if(p[d])
        for(int64_t k=int64_t(d)*d;k<=X;k+=d)p[(int)k]=0;
    for(int i=2;i<=X;i++)c[i]=p[i]?0:1;
    auto r=square_convolution(p,X,nfft);
    vector<uint16_t> least_certifying_cutoff(X+1,0);
    vector<int> quartic_margin(X+1,INT32_MAX);
    int failures=0,lastfail=0,firstfail=0,bestN=0,best=INT32_MAX;
    int tailmin=INT32_MAX,tailN=0,tailfrom=X/2 + X%2;
    int holdoutMin=INT32_MAX,holdoutN=0,holdoutCount=0,holdoutFail=0;
    int scanned=0;
    for(int z=1;z<=cube_root(X);z++){
        if(z>=2&&p[z])for(int k=2*z;k<=X;k+=z)c[k]=0;
        auto cc=square_convolution(c,X,nfft);
        for(int N=4;N<=X;N+=2)
            if(!least_certifying_cutoff[N] && r[N] > cc[N])least_certifying_cutoff[N]=(uint16_t)z;
        int64_t fourthlo=int64_t(z)*z*z*z;
        int64_t fourthhi=int64_t(z+1)*(z+1)*(z+1)*(z+1)-1;
        if(fourthlo<=X){
            int from=max(int64_t(4),fourthlo);if(from&1)from++;
            int to=int(min(int64_t(X),fourthhi));
            for(int N=from;N<=to;N+=2)quartic_margin[N]=r[N]-cc[N];
        }
        int lo=max(4,z*z*z), hi=min(X,(z+1)*(z+1)*(z+1)-1);
        if(lo&1)lo++;
        for(int N=lo;N<=hi;N+=2){
            int L=r[N]-cc[N];scanned++;
            if(L<=0){if(!firstfail)firstfail=N;lastfail=N;failures++;}
            if(L<best){best=L;bestN=N;}
            if(N>=tailfrom&&L<tailmin){tailmin=L;tailN=N;}
            if(N>300000){holdoutCount++;if(L<holdoutMin){holdoutMin=L;holdoutN=N;}if(L<=0)holdoutFail++;}
            // Independently verify convolution on sparse samples via exact direct integer counting.
            if(N==lo || (N%1009)==0){
                int directR=0,directC=0;
                for(int a=2;a<N-1;a++){directR+=(p[a]&&p[N-a]);directC+=(c[a]&&c[N-a]);}
                if(directR!=r[N]||directC!=cc[N]){cerr<<"NTT mismatch at "<<N<<endl;return 5;}
            }
        }
    }
    int max_cut=0,max_cut_N=0,unknown=0;
    int quartic_fail=0,quartic_first_fail=0,quartic_last_fail=0;
    vector<pair<int,int>> quartic_fail_cases;
    int max_ratio_z=0,max_ratio_cube=1,max_ratio_N=0;
    for(int N=4;N<=X;N+=2){
        int zz=least_certifying_cutoff[N];
        if(!zz){unknown++;continue;}
        if(zz>max_cut){max_cut=zz;max_cut_N=N;}
        int fourth=0;while(int64_t(fourth+1)*(fourth+1)*(fourth+1)*(fourth+1)<=N)fourth++;
        if(zz>fourth){quartic_fail++;if(!quartic_first_fail)quartic_first_fail=N;quartic_last_fail=N;
            quartic_fail_cases.push_back({N,quartic_margin[N]});}
        int root=cube_root(N);
        if(zz*max_ratio_cube>max_ratio_z*root){max_ratio_z=zz;max_ratio_cube=root;max_ratio_N=N;}
    }
    // Certificate length exactly floor(X/2)-1 even targets, including 4.
    if(scanned!=X/2-1){cerr<<"unexpected count "<<scanned<<endl;return 6;}
    cout<<"{\"method\":\"integer-NTT, verified direct samples\","
        <<"\"limit\":"<<X<<",\"scanned_even\":"<<scanned
        <<",\"failures\":"<<failures<<",\"first_failure\":"<<firstfail
        <<",\"last_failure\":"<<lastfail<<",\"minimum_signed\":"<<best
        <<",\"argmin\":"<<bestN<<",\"upper_half_minimum\":"<<tailmin
        <<",\"upper_half_argmin\":"<<tailN
        <<",\"fresh_holdout_above_300000_count\":"<<holdoutCount
        <<",\"fresh_holdout_failures\":"<<holdoutFail
        <<",\"fresh_holdout_minimum\":"<<(holdoutCount?holdoutMin:0)
        <<",\"fresh_holdout_argmin\":"<<holdoutN
        <<",\"uncertified_under_global_cuberoot\":"<<unknown
        <<",\"quartic_cutoff_nonpositive_count\":"<<quartic_fail
        <<",\"quartic_first_failure\":"<<quartic_first_fail
        <<",\"quartic_last_failure\":"<<quartic_last_fail
        <<",\"max_first_certifying_cutoff\":"<<max_cut
        <<",\"max_first_certifying_cutoff_at_N\":"<<max_cut_N
        <<",\"max_cutoff_over_cuberoot_ratio_numerator\":"<<max_ratio_z
        <<",\"max_cutoff_over_cuberoot_ratio_denominator\":"<<max_ratio_cube
        <<",\"max_cutoff_over_cuberoot_ratio_at_N\":"<<max_ratio_N
        <<",\"quartic_failure_cases\":[";
    for(size_t i=0;i<quartic_fail_cases.size();i++){
        if(i)cout<<",";
        cout<<"["<<quartic_fail_cases[i].first<<","<<quartic_fail_cases[i].second<<"]";
    }
    cout<<"]}\n";
    return 0;
}
