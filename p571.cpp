#include <set>
#include <iostream>
using namespace std;

bool isPandigital( uint64_t number, const unsigned int base){
	set<int> digits;
	while( number){
		int lastDigit = number % base;
		digits.insert( lastDigit);
		number /= base;
		if ( digits.size() == base)
			break;
		}
	return digits.size() == base;
}

int main(){
	const int MAX_BASE = 10;
	uint64_t number = 1000000000;
	while( true){
//		bool flag = true;
//		for( int base = MAX_BASE; base > 1; base--){
//			if (not isPandigital( number, base)){
//				flag = false;
//				break;
//				}
//			}
//		if (flag){
//			cout << number << endl;
//			return 0;
//			}
//
		if (isPandigital(number, 10) and not isPandigital( number, 5))
			cout <<  number << endl;
		number++;
		}
	return 0;
}
			
