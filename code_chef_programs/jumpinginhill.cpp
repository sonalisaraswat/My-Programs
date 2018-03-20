



#include <iostream>
using namespace std;
int main()
{
    int t,n,u,d,f,s;
    cin>>t;
    while(t>0)
    {
    t--;
    cin>>n>>u>>d;
    cin>>f;
    int i=0,para=1,fin=1,hill=1;
    while(i<(n-1) && fin==1)
    {
        cin>>s;
        if(f>s)
        {
            if(f-s<=d)
                hill++;
            else if(f-s>d && para==1)
            {
                hill++;para=2;
            }
            else
                fin=2;
        }
        else
        {
            if(s-f<=u)
                hill++;
            else
                fin=2;
        }
        i++;f=s;
    }
    while(i<(n-1))
       {
           i++;
           cin>>s;
       }
    cout<<hill<<endl;
    }
    return 0;
}
