#include <iostream>
//#include <boost/multiprecision/cpp_int.hpp>
#include <set>
#include <map>
#include <cmath>
using namespace std;
//using namespace boost::multiprecision;

//typedef uint128_t bInt;

#define MAX 1000000000

int main(){
	map<uint64_t, uint64_t> squareMap;
	uint64_t s = 0;
	uint64_t theMax = MAX/3 + 1;
	uint64_t maxSquare = 100 * sqrt(theMax);
	for(uint64_t x = 1; x < maxSquare;  ++x)
		squareMap[ x*x] = x;
	for(int64_t a = 1; a <= theMax; ++a){
		//b = a + 1
		if ( (3*a*a - 2 * a + 1 ) % (4 * (a+1)) == 0){
			uint64_t box = (3*a*a - 2 * a + 1 ) / (4 * (a+1));
			if (squareMap.find(box) != squareMap.end()){
				if ( squareMap[box] * (a+1)*(a+1) % 2 == 0)
					s += 3*a + 1;
				}
			}
		}
	cout << s << endl;
	return 0;			
}

//eof
