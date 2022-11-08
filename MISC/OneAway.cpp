#include<bits/stdc++.h>
#include<math.h>
using namespace std;

bool oneAway(string s1, string s2)

{
    int g = s1.length()-s2.length();
   // cout<<g<<endl;
    if(abs(g)>1)
    return false;
    
    string s = s1.length()>s2.length()?s2:s1;
    string l= s1.length()>s2.length()?s1:s2;
   // cout<<"Short String :"<<s<<endl;
    //cout<<"Long String :"<<l<<endl;
    int wrong=0,i=0,j=0;
    while(i<s.length())
    {
        if(s[i]!=l[j])
        {
            wrong++;
            if(wrong>1)
                return false;
            j++;
            if(s.length()==l.length())
            i++;
        }
        else
        {
            i++;
            j++;
        }
    }
    return true;
    
}

int main()
{
    string s1,s2;
    cin>>s1>>s2;
    bool res ;
    res = oneAway(s1,s2);
    if(res) cout<<"TRUE";
    else cout<<"FALSE";
}
  