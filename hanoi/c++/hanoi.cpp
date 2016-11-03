#include <iostream>

using namespace std;


void move(int no,int x,int y)
{
  if(no>1)
  move(no-1,x,6-x-y);
  cout << no << "を"<< x << "軸から、"<< y << "軸へ移動"<<endl;
  if(no>1)
  move(no-1,6-x-y,y);
}

int main()
{
  int N;
  cin >> N;

  move(N, 1, 3);
  return 0;
}
