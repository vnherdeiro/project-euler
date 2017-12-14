#include <fstream>
#include <iostream>
#include <vector>
//#include <cmath>
#include <boost/multiprecision/cpp_int.hpp>
#include <set>

using namespace std;
using namespace boost::multiprecision;

typedef uint128_t bInt;

bInt ipow(bInt base, bInt exp)
{
    bInt result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

int main(){
    const char * fname = "primes193.dat";
    ifstream infile(fname);
    vector<bInt> primes;
    bInt a;
    while (infile >> a ){
        primes.push_back(a*a);
        }

	//const bInt MAX = ipow((bInt)2,(bInt)50);
	const bInt MAX = (bInt)4e7;
	
	bInt count = 0;
	auto theSet = new set< bInt>;
	for (auto p : primes){
		bInt n = p;
		while( n < MAX){
			if ( theSet->find(n) == theSet->end()){
				count++;
				theSet->insert(n);
				}
			n += p;
		//count += (bInt) (MAX-1)/p;
			}
		}
	
	cout << count << endl;
//	for(auto it1 = primes.begin(); it1 != primes.end()-1; ++it1)
//		for( auto it2 = it1+1; it2 != primes.end(); ++it2){
//			bInt number = *it1 * *it2;
//			if (number > MAX - 1)
//				break;
//			count -= (MAX-1)/number;
//			}
//	cout << count << endl;
	cout << MAX -1 - count<< endl;
	return 0;
}
