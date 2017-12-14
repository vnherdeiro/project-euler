#include <iostream>
using namespace std;


inline int sumDigits(int64_t n){
	int sum = 0;
	while(n){
		sum += n%10;
		n /= 10;
		}
	return sum;
}


int main(){
	int64_t ini = 10;
	int index = 1;
	

	while(true){
		int base = sumDigits(ini);
		if (base != 1 and ini % base == 0){
			int64_t n = base;
			while (n<ini)
				n*=base;
			if (n==ini){
				cout << index << " " << ini << endl;
				index++;
				}
			}
		ini++;
		}
	
	return 0;
}

