#include <iostream>
#include <string>
#include <vector>


class Solution {
 public:
  std::string convert(std::string s, int numRows) {
    std::vector<std::string> strings(numRows);
    int row = 0;
    int direction = 1;
    for (int i = 0; i < s.length(); ++i) {
      // 0 1 2 1 0 1 2 1 0
      if (row == (numRows - 1) && row == 0) {
        direction = 0;
      } else if (row == numRows - 1) {
        direction = -1;
      } else if (row == 0) {
        direction = 1;
      }
      strings[row] += s[i];
      row += direction;
    }

    std::string converted_string;
    for (int i = 0; i < strings.size(); ++i) {
      converted_string += strings[i];
    }
    return converted_string;
  }
};

int main(int argc, char** argv) {
  Solution solution;
  std::cout << solution.convert("AB", 1) << std::endl;
  return 0;
}