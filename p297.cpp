#include <iostream>
#include <vector>
using namespace std;

const uint64_t MAX = 1e11;
vector<uint64_t> fib = {1,2};

uint64_t z( uint64_t sumValue, uint64_t zValue, vector<uint64_t>::iterator it){
	uint64_t count = zValue;
	while (it < fib.end()){
		if (sumValue + *it < MAX){
			count += z(sumValue + *it, zValue + 1, it + 2);
		}
		else
			break;
		it++;
	}
	return count;
}

int main(){
	while (true){
		uint64_t newValue = *(fib.end()-2) + *(fib.end()-1);
		if (newValue < MAX)
			fib.push_back( newValue);
		else
			break;
	}
	cout << "done generating fib\t" << fib.size() << endl;
	cout << z(0, 0, fib.begin()) << endl;
	return 0;
}
