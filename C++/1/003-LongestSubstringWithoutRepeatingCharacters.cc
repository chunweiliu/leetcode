#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    int max_length = 0;
    int p = 0;  // The start of the candidate string.
    int q = 0;  // The end of the candidate string.
    unordered_map<char, bool> exist;
    while (q < s.length()) {
      if (exist[s[q]]) {
        max_length = max(max_length, q - p);
        while (s[p] != s[q]) {  // Find the repeat character.
          exist[s[p]] = false;
          p++;
        }
        p++;
        q++;
      } else {
        exist[s[q]] = true;
        q++;
      }
    }
    max_length = max(max_length, q - p);
    return max_length;
  }
};

int main(int argc, char** argv) {
  Solution solution;
  cout << solution.lengthOfLongestSubstring("c") << endl;
  return 0;
}