#include <iostream>

using namespace std;

int nSol(int64_t n){
	int64_t y = 2*n;
	int nSolutions = 0;
	while (y >= n+1){
		nSolutions += ((n*y) % (y-n) == 0 ? 1 : 0);
		y--;
	}
	return nSolutions;
}

int main(){
	int64_t i = 55000;
	while (nSol(i) <= 1000){
		i++;
		}
	cout << i << "\t\t" << nSol(i) << endl;
	return 0;
}
