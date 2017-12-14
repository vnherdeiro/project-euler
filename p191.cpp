#include <iostream>
using namespace std;

#define MAX 30

uint64_t countStrings( int length, bool hasL, int NLastAs){
	uint64_t count = 0;
	if (length == MAX ){
		return 1;
		}
	if (hasL){
		count += countStrings(length+1,hasL,0); //adding a O at the end
		if (NLastAs != 2)
			count += countStrings(length+1,hasL,NLastAs+1); //adding a A
		}
	else{
		count += countStrings(length+1,true,0); //adding a L
		count += countStrings(length+1,false,0); //adding a O
		if (NLastAs != 2)
			count += countStrings(length+1,false,NLastAs+1); //adding a A
		}
	return count;
}


int main(){
	cout << countStrings( 0, false, 0) << endl;
	return 0;
}
