#include <iostream>
#include <vector>
using namespace std;

int64_t rightRotate( int64_t number){
	vector<int> digits;
	while (number){
		digits.emplace_back( number%10);
		number /= 10;
		}
	int64_t rotated = digits[0];
	for(auto it = digits.rbegin(); it != digits.rend() - 1; it++){
		rotated = 10*rotated + (*it);
		}
	return rotated;
}

#define DIGIT_CHECKED 9

int main(){
	int nDigits = 2;
	while( true){
		int64_t i = 1;
		for( int j = 0; j < nDigits; j++)
			i *= 10;
		const int64_t max = i*10/DIGIT_CHECKED + 1;
		for(int64_t n = i; n <= max; ++n){
			int64_t r = rightRotate( n);
			if ( r % n == 0 and r != n)
				cout << n << " " << r/n << endl;
			}
		cout << "\t\t" << nDigits << endl;
		nDigits++;
		}
	return 1;
}

