#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>

#define N_FINAL 1000000

using namespace std;
using namespace boost::multiprecision;

typedef uint128_t bInt;
typedef int128_t bIntns;

int main(){
	int tot = 0;
	//for( int64_t N = 1; N <= N_FINAL; ++N){
	for( int64_t N = 1; ; ++N){
		bInt N2 = ((bInt) N) * N;
		int64_t x = N;
		int64_t y = 0;
		int Nsol = 0;
		while (x > 0 and Nsol < 106){
			x -= 1;
			while ( ((bInt) x)*x + ((bInt) y + 1)*(y+1) <= N2){
				y++;
				if ( ((bInt) x)*x + ((bInt) y)*y == N2)
					Nsol++;
				}
			}
		if (Nsol == 105){
			tot++;
			cout << N << endl;
			}
		if (Nsol > 105){
			cout << "\t" << N << endl;
			}
		}
	cout << tot << endl;
	return 0;
}
