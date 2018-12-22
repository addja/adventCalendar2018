#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int
main() {
	int count2 = 0;
	int count3 = 0;
	string s;
	size_t n;
	int tmpCount2;
	int tmpCount3;
	while ( cin >> s ) {
		tmpCount2 = 0;
		tmpCount3 = 0;
		for ( int i = 0; i < s.size(); i++ ) {
			n = std::count(s.begin(), s.end(), s[i]);
			if ( n == 2 ) tmpCount2++;
			if ( n == 3 ) tmpCount3++;
			if ( tmpCount2 && tmpCount3 ) break;
		}
		if ( tmpCount2 ) count2++;
		if ( tmpCount3 ) count3++;
	}
	cout << count2 * count3 << endl;
}
