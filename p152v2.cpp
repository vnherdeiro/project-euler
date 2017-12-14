#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
//#include <cmath>
#include <iomanip>
using namespace std;
using namespace boost::multiprecision;

typedef uint1024_t bInt;


class fraction
{

public:
	bInt num;
	bInt den;
fraction(bInt, bInt);
fraction();
bool equalsAHalf();
bool biggerThanAHalf();

};


bool fraction::equalsAHalf(){
	return num * 2 == den;
}

bool fraction::biggerThanAHalf(){
	return num * 2 > den;
}

fraction::fraction(bInt theNum, bInt theDen){
	num = theNum;
	den = theDen;
}

fraction::fraction(){
	num = 0;
	den = 1;
}

fraction operator+(const fraction& lhs, const fraction& rhs){
	return fraction( lhs.num*rhs.den + lhs.den*rhs.num, lhs.den * rhs.den);
}

#define SIZE 80//44 //2 -> 81
fraction fracTab[SIZE];


int sums22(fraction value, int index){
	int count = 0;
	auto addedValue = value + fracTab[index];
	if ( addedValue.biggerThanAHalf() ){  //adding would be bigger
		//cout << "too large" << endl;
		if (index + 1 < SIZE)
			count += sums22(value, index+1);
		//else
		//	return 0;
		}
	else if ( addedValue.equalsAHalf() ){ //exactly a half
		cout << "found one" << endl;
		count += 1;
		if (index + 1 < SIZE)
			count += sums22(value, index+1);
		}
	else if (index + 1 < SIZE){
		//cout << "too small " << addedValue << endl;
		count += sums22( addedValue, index+1);
		count += sums22( value, index+1);
		}
	return count;
}

int main(){
	//cout.precision(16);
	for(int i = 0; i < SIZE; i++){
		fracTab[i] = fraction(1, (i+2)*(i+2));
		}
	cout << sums22( fraction(), 0) << endl;
	return 0;
}

//eof
