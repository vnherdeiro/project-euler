#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;


inline int ceil2(double x){
	if (x == 0)
		return 1;
	return (int) x + 1;
}

int main( int argc, char * argv[]){
	int MAX = atoi(argv[1]);
	int NTRI = 0;
	for( int x1 = 1; x1 <= MAX; ++x1){
		for( int y1 = 0; y1 <= MAX; ++y1){
			int d10 = x1*x1 + y1*y1;
			if ( d10 > 0){
				for( int x2 = 0; x2 <= MAX; ++x2){
					for( int y2 = ceil2((double) y1 / x1 * x2); y2 <= MAX; ++y2){
						int d20 = x2*x2 + y2*y2;
						if( d20 > 0){
							int d12 = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
							if ( d12 >0 and (d12 + d10 == d20 or d20 + d10 == d12 or d20 + d12 == d10))
								NTRI++;
							}
						}
					}
				}
			}
		}
	cout << NTRI << endl;
	return 0;
}

