#include<iostream>
#include<set>
#include<vector>

using namespace std;

int
main() {
	int count = 0;
	int i;
	set<int> mem = { 0 };
	vector<int> input;
	while ( cin >> i ) input.push_back( i );
	i = 0;
	while ( true ) {
		count += input[i];
		if ( mem.count( count ) ) break;
		mem.insert( count );
		i == input.size()-1 ?  i = 0 : i++;
	}
	cout << count << endl;
}
