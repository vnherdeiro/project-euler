#include <iostream>
#include <set>
#include <vector>
using namespace std;



int main(){

	//filling for set
	set<int> thePrimes = {2};
	int bound = 100000000;
	//int bound = 1000000;
	for(int i = 3; i <= bound+1; i+=2){
//	for(int i = 3; i <= 10001; i+=2){
		bool isPrime = true;
		for(auto it = thePrimes.begin(); it != thePrimes.end(); ++it )
			if (i % *it == 0){
				isPrime = false;
				break;
			}
		if (isPrime)
			thePrimes.insert(i);
		}

		//outputting the primes
	//for(auto it = thePrimes.begin(); it != thePrimes.end(); ++it )
	//	cout << *it << " ";
	//cout << "\n" << thePrimes.size() << endl;
	cout << "done calculating the primes..." << endl;

	int64_t theSum = 0;
	for(int i = 1; i <= bound; ++i){
		bool reject = false;
		for (int possibleDivisor = 1; possibleDivisor < i/2; ++possibleDivisor){
			if (i % possibleDivisor == 0){
				if (thePrimes.find( possibleDivisor + i/possibleDivisor) == thePrimes.end())
					reject = true;
					break;
			}
		}
		if (not reject)
			theSum += i;
	}
	cout << theSum << endl;
	return 0;
}
