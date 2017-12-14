#include <fstream>
#include <iostream>
#include <vector>

using namespace std;


int main(){
	const char * fname = "thePrimes.dat";
	ifstream infile(fname);
	vector<int64_t> primes;
	int64_t a;
	while (infile >> a ){
		primes.push_back(a);
		}
	cout << primes.size() << endl;

	int theSum = 0;
	int64_t threshold = 100000000;
	for( auto prime1 = primes.begin(); prime1 != primes.end(); ++prime1){
		for(auto prime2 = prime1; prime2 != primes.end() and (*prime1)* (*prime2) < threshold; ++prime2)
			theSum++;
		}

	cout << theSum << endl;
	return 0;
}
