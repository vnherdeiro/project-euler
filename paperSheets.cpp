#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <random>
#include <cassert>
using namespace std;

#define NSTEPS 1000000


int main(){
	int64_t count = 0, countTrue = 0;
	auto engine = default_random_engine{};
	while(true){
		for(int stepIndex = 0; stepIndex < NSTEPS; ++stepIndex){
			vector<int> envlp = {8,4,2,1};
			count++;
			for(int i = 0; i < 14; ++i){
				if( envlp.size() == 1)
					countTrue++;
				shuffle(envlp.begin(), envlp.end(), engine);
				auto pick = envlp.back();
				envlp.pop_back();
				switch (pick){
					case 1:
						break;
					case 2:
						envlp.push_back(1);
						break;
					case 4:
						envlp.push_back(2);
						envlp.push_back(1);
						break;
					case 8:
						envlp.push_back(4);
						envlp.push_back(2);
						envlp.push_back(1);
						break;
					default:
						assert(false);
					}
				}
			}
		double p = (double) countTrue/count;
		cout << p << "\t" << sqrt(p*(1-p)/count) << endl;
		}
	}
