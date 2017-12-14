#include <iostream>
//#include <cmath>
#include <iomanip>
using namespace std;

#define SIZE 44 //2 -> 81
long double fracTab[SIZE];
long double tol = 1e-15; //words with 14

inline long double abs(long double x){
	return x < 0 ? -x : x;
}

int sums22(long double value, int index){
	int count = 0;
	long double addedValue = value + fracTab[index];
	if (addedValue - tol > .5){
		//cout << "too large" << endl;
		if (index + 1 < SIZE)
			count += sums22(value, index+1);
		//else
		//	return 0;
		}
	else if (abs(addedValue - .5) < tol){
		cout << "found one\t" << addedValue << endl;
		count += 1;
		count += sums22(value, index+1);
		}
	else if (index + 1 < SIZE){
		//cout << "too small " << addedValue << endl;
		count += sums22(addedValue, index+1);
		count += sums22(value, index+1);
		}
	return count;
}

int main(){
	cout.precision(16);
	for(int i = 0; i < SIZE; i++){
		fracTab[i] = ((long double) 1)/ ((i+2)*(i+2));
		//cout << i+2 << " " << fracTab[i] << "\n";
		}
	cout << sums22(0,0) << endl;
	return 0;
}

//eof
