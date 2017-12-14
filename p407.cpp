#include <iostream>
using namespace std;

int main(){
	int64_t sum = 0;
	const uint64_t MAX = 10000000;
	for(int64_t a = MAX; a >=1; --a){
		int64_t n = a-1;
		while (true){
			if ((n* (n-1)) % a == 0){
				sum += n;
				break;
				}
			n--;
			}
		if (a%10000 == 0)
			cout << a << endl;
		}
	cout << sum << endl;
	return 1;
}

//eof
