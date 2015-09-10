#include <iostream>
#include <string>

using namespace std;

class Solution {
 public:
  string longestPalindrome(string s) {
    // Dynamic Programming: Two dimensional truth table for determining if the 
    // substring(i, j) is a palindrome. T[i, j] <- T[i+1, j-1] && s[i] == s[j].
    bool T[1000][1000];
    memset(T, false, sizeof(T));

    // Initialize and check conner cases:
    int n = s.length();
    for (int i = 0; i < n; ++i) {
      T[i][i] = true;
    }
    int longest = 1;
    for (int i = 0; i < n - 1; ++i) {
      if (s[i] == s[i + 1]) {
        T[i][i + 1] = true;
        longest = 2;
      }
    }

    int start = 0;
    for (int len = 3; len <= n; ++len) {
      for (int i = 0; i < n; ++i) {
        int j = i + len - 1;
        if (s[i] == s[j] && T[i + 1][j - 1]) {
        // T[i][j] = T[i + 1][j - 1] && (s[i] == s[j]);
        // if (T[i][j] && (len > longest)) {
          T[i][j] = true;
          longest = len;
          start = i;
        }
      }
    }
    // for (int i = 0; i < n; ++i) {
    //   for (int j = 0; j < n; ++j) {
    //     cout << T[i][j] << " ";
    //   }
    //   cout << endl;
    // }
    // cout << start << endl;
    // cout << start + longest << endl;
    return s.substr(start, longest);
  }
};

int main(int argc, char** argv) {
  Solution solution;
  string input("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
  cout << solution.longestPalindrome(input) << endl;
  return 0;
}