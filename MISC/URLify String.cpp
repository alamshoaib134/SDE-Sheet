#include<bits/stdc++.h>
using namespace std;
int main()
{
   string input;
   getline(cin,input);
   //cout<<input;
  string rep = "%20";
    for(int i=0 ; i<input.length() ; i++)
    {
        if(input[i] == ' ')
            input.replace(i,1,rep);
    }
    cout<<input;
}