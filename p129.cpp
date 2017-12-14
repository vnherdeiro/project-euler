#include <iostream>
using namespace std;

#define MIN 1000000

int A(int n){
	int rest = 1;
	int lastRest = 1;
	int i = 1;
	while (rest != 0){
		lastRest *= 10;
		lastRest %= n;
		rest += lastRest;
		rest %= n;
		i++;
	}
	return i;
}


int main(){
	int a = 1;
	int i = 3;
	while( a < MIN){
		if (i % 2 != 0 and i % 5 != 0){
			a = A(i);
		}
		i++;
	}
	cout << i-1 << endl;
}
