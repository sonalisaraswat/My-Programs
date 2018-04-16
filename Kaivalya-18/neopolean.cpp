#include<iostream>
using namespace std;
int main()
{
    int s;
    cin>>s;
    while(s>0)
    {
        int n,r,fir,nex,c=1,j;
        s--;
        cin>>n>>r;
        cin>>fir;
        for(j=0;j<n-1;j++)
        {
            cin>>nex;
            if(nex>fir)
            {
                fir=nex;
                c++;
            }
        }
        cout<<(c*r)<<endl;
    }
}
