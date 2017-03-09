
#include <iostream>
#include <cassert>
#include <string>
#include <vector>

using namespace std;

void init_prefix_table(string pattern, int*& table) {
    int prefix_count = 0;

    //cout << "initializing prefix table: ";
    for (int i = 1; i < pattern.size(); i++) {
        if (pattern[i] == pattern[prefix_count]) {
            prefix_count++;
        } else {
            prefix_count = 0;
        }
        table[i] = prefix_count;
    }
    //cout << endl;
}

int kmp_match(string text, string pattern) {
    int *prefix_table = new int[pattern.size()];
    init_prefix_table(pattern, prefix_table);

    // check the prefix table
    cout << "pattern: " << pattern << " size: " << pattern.size() << " len:" << pattern.length() << endl;
    for (int i = 0; i < pattern.size(); i++) {
        cout << prefix_table[i] ;
    }
    cout << endl;

    int pattern_index = 0;

    for (int i = 0; i < text.size(); i++) {
        while (pattern_index > 0 and text[i] != pattern[pattern_index]) {
            pattern_index = prefix_table[pattern_index-1];
            //cout << "pattern_index: " << pattern_index << endl;
        }

        // At this point we should be in a valid state
        // check if we have a match at the new pointer position
        if (text[i] == pattern[pattern_index]) {
            if (pattern_index == pattern.size()-1) {
                return i-pattern_index;
                // alternatively the below would work also:
                //return i-pattern.size()+1;
            }
            pattern_index++;
        }
    }
    
    delete[] prefix_table;

    return -1;
}

int main(void) {
    cout << "Knuth Morris Pratt (KMP) string search algorithm" << endl;

    vector<string> v = { 
        "y ababaca siifjae", "ababaca",
        "y ababac siifjae", "ababac",
        "abababacsiifjae", "ababac",
        "adfbec dsfoeifj asdfjww abyyabcdefg siifjae", "aba",
        "adfbec dsfoeifj asdfjww sifmyy abcdefg siifjae", "ab", 
        "adfbec dsfoeifj asdfjww sifmyy abcdefg siifjae", "a", 
        "adfbec dsfoeifj asdfjww sifmyy abcdefg siifjae", "aa",
        "ababac", "ababac",
    };

    int i = 0;
    while (i+1 < v.size()) {
        string text = v[i++];
        string pattern = v[i++];

        int res = kmp_match(text, pattern);
        cout << "search '"<< pattern << "' in '" << text << "'."<< endl;
        cout << "found at pos: " << res << endl;
        assert (res == text.find(pattern));
        cout << "complete iteration : " << i << endl;
    }

    return 0;
}
