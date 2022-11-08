#include<iostream>
#include<string>
using namespace std;

string compress(string str)
{
    if(str.length()<=2)
    return str;
    int count=1;
    string out{""};
    for(int i=1;i<str.length();i++)
    {
        if(str[i]==str[i-1])
        {
            count++;
        }
        else
        {
            out+=str[i-1];
            out+=to_string(count);
            count=1;
        }
        if (out.length() >= str.length()) 
			return str;
        
    }
    
            out+=str[str.length()-1];
            out+=to_string(count);
            if (out.length() >= str.length()) 
			return str;
			return out;
    
}

int main()
{
    string str;
    cin>>str;
    string s = compress(str);
    cout<<s;
}