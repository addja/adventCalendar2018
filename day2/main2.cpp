#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

bool keyFinder( string & s1, string & s2 ) {
	bool first = true;
	for ( int i = 0; i < s1.size(); i++ ) {
		if ( s1[i] != s2[i] && first ) first = false;
		else if ( s1[i] != s2[i]) return false;
	}
	for ( int i = 0; i < s1.size(); i++ ) {
		if ( s1[i] == s2[i]) cout << s1[i];
	}
	cout << endl;
	return true;
}

int
main() {
	vector< string > input;
	string s;
	while ( cin >> s ) input.push_back( s );
	for ( int i = 0; i < input.size(); i++ ) {
		for ( int j = i+1; j < input.size(); j++ ) {
			if ( keyFinder( input[i], input[j] ) ) return 0;
		}
	}
}
