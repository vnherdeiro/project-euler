#include <iostream>
using namespace std;


int main(){
	int64_t num = 1;
	int64_t fact = 1;
	//int64_t MAX = 1000000000000;
	int64_t MAX = 100000;
	while(num <= MAX){
		fact *= num;
		num++;
		while( fact % 10 == 0){
			//cout << fact << endl;
			fact /= 10;
			}
		fact %= 100000;
		}
	cout << fact << endl;
	return 0;
}

//eof
