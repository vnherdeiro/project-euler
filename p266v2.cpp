#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include <iomanip>
using namespace std;
using namespace boost::multiprecision;

//typedef uint1024_t bInt;
typedef uint128_t bInt;

vector<int> primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53};
//vector<int> primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181};
const int SIZE = 42;

bInt theMax = 0;
//char c[256] = "2323218950681478446587180516177954549";
char c[256] = "75556";
const bInt MAX = bInt(c);
const bInt theMOD = 10000000000000000;


int main(){
	//cout << MAX << endl;
	bInt n0 = MAX;
	while (true){
		bInt n = n0;
		if (n%4==0 or n%9==0 or n%15==0){
			n0--;
			continue;
			}
		for( auto val : primes){
			if (n % val == 0)
				n /= val;
			}
		if (n==1){
			cout << n << "\t" << n % theMOD << endl;
			return 1;
			}
		n0--;
		}
	return 1;
}

//eof
