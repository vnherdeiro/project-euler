#include <boost/random.hpp>
#include <iostream>
#include <random>
#include <iomanip>
using namespace std;

typedef boost::mt19937 RNGType;

int main(){
	int64_t sum = 0;
	int64_t card = 0;
	cout.precision(8);
	random_device rd;
	RNGType rng;
	rng.seed(rd());
	auto peterS = new boost::random::uniform_int_distribution<> (1,4);
	auto peterDice = new boost::variate_generator<RNGType,boost::random::uniform_int_distribution<> >(rng,*peterS) ;
	rng.seed(rd());
	auto colinS = new boost::random::uniform_int_distribution<> (1,6);
	auto colinDice = new boost::variate_generator<RNGType,boost::random::uniform_int_distribution<> >(rng,*colinS) ;
	while (true) {
		int peterSum = (*peterDice)() + (*peterDice)() + (*peterDice)() + (*peterDice)() + (*peterDice)()+ (*peterDice)()+ (*peterDice)()+ (*peterDice)()+ (*peterDice)();
		int colinSum = (*colinDice)() + (*colinDice)() + (*colinDice)() + (*colinDice)() + (*colinDice)() + (*colinDice)();
		sum += peterSum > colinSum;
		card++;
		if (card % 1000000 ==0)
			cout << (double) sum/card << endl;
		}

	return 0;
}
		
