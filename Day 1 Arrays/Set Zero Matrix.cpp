
#include <bits/stdc++.h>
using namespace std;

void disp(vector<vector<int>> &mat)
{
  for( int i=0;i<mat.size();i++)
    {
        for(int j=0;j<mat[0].size();j++)
        {
            cout<<mat[i][j]<<" ";
        }
        cout<<endl;
    }  
}

void initilization(vector<vector<int>> & v, vector<vector<int>> & matrix)
{
    for(int i=0;i<matrix.size();i++)
    {
        vector<int> dum;
        for(int k=0;k<matrix[0].size();k++)
            dum.push_back(1);
        v.push_back(dum);
    }
    
}

vector<pair<int,int>> zero(vector<vector<int>> & temp,vector<vector<int>> & matrix)
{
    vector<pair<int,int>> zero_ind;
    
    for(int i=0;i<matrix.size();i++)
    {
        for(int j=0;j<matrix[0].size();j++)
        {
            if(matrix[i][j]==0)
               { temp[i][j]=0; zero_ind.push_back({i,j});}
        }
    }
    for(auto ele: zero_ind)
        cout<<ele.first<<" "<<ele.second<<" "<<endl;
    cout<<endl;

    return zero_ind;
    
}

void final_zero(vector<pair<int,int>> &ind,vector<vector<int>> &temp)
{
    for(auto ele: ind)
    {
        for(int i=0;i<temp[0].size();i++)
        {
            temp[ele.first][i]=0;
        }
    }
    for(auto ele: ind)
    {
        for(int i=0;i<temp.size();i++)
        {
            temp[i][ele.second]=0;
        }
    }
}

int main() {
    vector<vector<int>> matrix  {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
    vector<vector<int>> temp;
    vector<pair<int,int>> ind;
    initilization(temp,matrix);
    ind= zero(temp,matrix);
    final_zero(ind,matrix);
    disp(matrix);
    
    
}