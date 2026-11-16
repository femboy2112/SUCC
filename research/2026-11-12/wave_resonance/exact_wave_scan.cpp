// Exact frozen-cube-root signed prime/semiprime wave convolution.
// All coefficients <=X<998244353, so modular NTT outputs exact integer counts.
// Finite data cannot establish universal Goldbach or the stronger signed conjecture.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;
static constexpr int MOD=998244353, ROOT=3;
int pmod(int x,int64_t e){
    int64_t a=x,y=1;
    while(e){if(e&1)y=y*a%MOD;a=a*a%MOD;e>>=1;}
    return int(y);
}
void ntt(vector<int>&a,bool inv){
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
                int sum=u+v;if(sum>=MOD)sum-=MOD;
                int diff=u-v;if(diff<0)diff+=MOD;
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
vector<int> square_convolution(const vector<uint8_t>&mask,int X,int nfft){
    vector<int> v(nfft);
    for(int k=0;k<=X;k++)v[k]=mask[k];
    ntt(v,false);
    for(int &x:v)x=int(int64_t(x)*x%MOD);
    ntt(v,true);
    v.resize(2*X+1);
    return v;
}
int icbrt(int n){
    int z=0;
    while(int64_t(z+1)*(z+1)*(z+1)<=n)z++;
    return z;
}
int main(int argc,char**argv){
    int X=argc>=2?atoi(argv[1]):120000;
    if(X<16||X>500000){cerr<<"X outside calibrated range\n";return 2;}
    int nfft=1;while(nfft<2*(X+1))nfft*=2;
    if(nfft>=(1<<23)){cerr<<"NTT unsupported\n";return 3;}
    vector<uint8_t> p(X+1,1), c(X+1,1);
    p[0]=p[1]=c[0]=c[1]=0;
    for(int d=2;int64_t(d)*d<=X;d++)if(p[d])
        for(int64_t k=int64_t(d)*d;k<=X;k+=d)p[(int)k]=0;
    for(int k=2;k<=X;k++)if(p[k])c[k]=0;
    int z=icbrt(X);
    for(int ell=2;ell<=z;ell++)if(p[ell])
        for(int k=2*ell;k<=X;k+=ell)c[k]=0;
    auto pp=square_convolution(p,X,nfft);
    auto cc=square_convolution(c,X,nfft);
    for(int j=0;j<64;j++){
        int N=4+int((int64_t(2*X-4)*j)/63),r=0,s=0;
        for(int a=max(2,N-X);a<=min(X,N-2);a++){
            r+=p[a]&&p[N-a];s+=c[a]&&c[N-a];
        }
        if(r!=pp[N]||s!=cc[N]){cerr<<"direct mismatch at "<<N<<"\n";return 5;}
    }
    int Ps=0,Cs=0;
    for(int k=2;k<=X;k++){Ps+=p[k];Cs+=c[k];}
    auto count=[&](int lo,int hi,int m,int residue){
        int64_t s=0;int negative=0,zeros=0;
        for(int N=max(4,lo);N<=min(2*X,hi);N++)
            if(N%m==residue){
                int value=pp[N]-cc[N];
                s+=value;if(value<0)negative++;if(value==0)zeros++;
            }
        return tuple<int64_t,int,int>(s,negative,zeros);
    };
    vector<pair<int,int>> windows={{X/2,X},{X,3*X/2},{3*X/2,2*X}};
    cout<<"{\"X\":"<<X<<",\"z\":"<<z<<",\"prime_count\":"<<Ps
        <<",\"rough_semiprime_count\":"<<Cs<<",\"windows\":[";
    for(size_t i=0;i<windows.size();i++){
        int lo=windows[i].first,hi=windows[i].second;
        auto [total,neg,zeros]=count(lo,hi,2,0);
        if(i)cout<<",";
        cout<<"{\"lo\":"<<lo<<",\"hi\":"<<hi
            <<",\"even_signed_sum\":"<<total<<",\"negative_targets\":"<<neg
            <<",\"zero_targets\":"<<zeros<<",\"classes\":[";
        for(int j=0;j<6;j++){
            int r=2*j;
            auto [s,ng,zr]=count(lo,hi,12,r);
            if(j)cout<<",";
            cout<<"{\"r_mod_12\":"<<r<<",\"signed_sum\":"<<s
                <<",\"negative_targets\":"<<ng<<",\"zeros\":"<<zr<<"}";
        }
        cout<<"]}";
    }
    cout<<"]}\n";
    return 0;
}
