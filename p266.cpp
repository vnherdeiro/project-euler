#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include <iomanip>
using namespace std;
using namespace boost::multiprecision;

//typedef uint1024_t bInt;
typedef uint256_t bInt;

vector<int> primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53};
//vector<int> primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181};
const int SIZE = 42;

bInt theMax = 0;
char c[256] = "75556";
//char c[256] = "2323218950681478446587180516177954549";
const bInt MAX = bInt(c);
const bInt theMOD = 10000000000000000;

void calcProds( bInt val, int index){
	if (val > MAX)
		return ;
	bInt newVal = val * primes[index];
	if (newVal <= MAX){
		if (newVal > theMax){
			theMax = newVal;
			cout << theMax << "\t\t" << theMax % theMOD << endl;
			}
		if (index + 1 < SIZE){
			calcProds(newVal, index+1);
			}
		}
	if (index + 1 < SIZE){
		calcProds(val, index+1);
		}
}

int main(){
	//cout << MAX << endl;
	calcProds( (bInt) 1, 0, 0);
	return 1;
}

//eof
