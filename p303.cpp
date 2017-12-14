
#include <iostream>
using namespace std;

#define START 9900
#define END 10000

bool correct(int64_t n){
	while (n != 0){
		int dig = n%10;
		if (dig != 0 and dig != 1 and dig != 2)
			return false;
		else
			n /= 10;
		}
	return true;
}

int64_t f2(int64_t n){
	int64_t number = n;
	while (true){
		if (correct(number))
			return number;
		else
			number += n;
	}
}


int main(){
	int64_t s = 0;
	for(int i = START; i <= END; ++i){
		s += f2(i)/i;
		cout << i << endl;
	}
	cout << s << endl;
}
