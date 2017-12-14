#include <cmath>
#include <iostream>
#include <vector>
#include <set>
using namespace std;

bool isPrime (int64_t num)
{

        bool prime = true;
        int64_t divisor = 3;
        //double num_d = static_cast<double>(num);
        int64_t upperLimit = static_cast<int64_t>(sqrt(num) +1);

        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                return false;
            divisor +=2;
        }
        return true;
}

int64_t divisorSum(int64_t n){
	int64_t theSum = 1+n;
	for(int64_t i = 2; i < n/2+1; ++i)
		if (n%i == 0)
			theSum += i;
	return theSum;
}

int main(){
	int64_t temp = 2017*2;
	int64_t MAX = 1e11;
	auto thePrimes = new vector<int64_t>;
	while( temp <= MAX){
		if (isPrime(temp-1)){
			thePrimes->push_back(temp-1);
			if (thePrimes->size() % 10000 == 0)
				cout << thePrimes->size() << endl;
		}
		temp += 2*2017;
	}
	cout << thePrimes->size() << endl;

	int64_t theSum = 0;
	auto addedNumbers = new set<int64_t>;
	for(auto it = thePrimes->begin(); it != thePrimes->end(); ++it){
		uint64_t i = 1;
		uint64_t temp= *it;
		uint64_t Nmul = MAX/(*it);
		while(temp <= MAX){
			//if (i%prime!=0)
			//if (i != *nextPrime)
			if (addedNumbers->find(temp) == addedNumbers->end()){
				theSum += temp;
				addedNumbers->insert(temp);
			}
			//}
			//else if (divisorSum(temp) % 2017 == 0){
			//	theSum += temp;
			//	cout << "contributed\n";
			//	}
			temp += *it;
			i++;
		}
	}
	// cout << theSum << endl;
	// for(auto it1 = thePrimes->begin(); it1 != thePrimes->end(); ++it1){
	// 	for(auto it2 = it1+1; it2 != thePrimes->end(); ++it2){
	// 		int64_t temp = (*it1) * (*it2);
	// 		while(temp <= MAX){
	// 			theSum -= temp;
	// 			temp += (*it1) + (*it2);
	// 		}
	// 	}
	// }
	cout << theSum << endl;
	return 0;
}
