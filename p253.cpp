#include <iostream>
#include <cmath>

using namespace std;

// Check if a number is prime.
int isPrime(int64_t n) {
	for (int i = 2; i <= sqrt(n); i ++)
		if (n % i == 0)
			return 0;

	return 1;
}
// Use Euler's product formula.
float eulerTot(int64_t n) {
	float result = n;

	// Compute prime factors and execute multiplication.
	for (int64_t i = 2; i <= n/2; i++)
		if (n % i == 0 && isPrime(i))
			result *= (1 - (1 / (float) i));

	return result;
}



double R(const int64_t n){
	return (double) eulerTot(n)/(n-1);
}

int main(){
	int64_t i = 433231119;
	double threshold = (double)15499/94744;
	while( R(i) >= threshold){
		i += 1;
	}
	cout << i << endl;
	return 0;
}
