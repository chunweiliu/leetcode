#include <iostream>
#include <string>
#include <limits>

using namespace std;

class Solution {
 public:
  int myAtoi(string str) {
    int begin = 0;
    while (str.compare(begin, 1, " ") == 0) {
      begin++;
    }

    int sign = 1;
    if (str.compare(begin, 1, "-") == 0) {
      sign = -1;
      begin++;
    } else if (str.compare(begin, 1, "+") == 0) {
      begin++;
    }

    long num = 0;
    int i = begin;
    for (; i < str.length(); ++i) {
      if (!IsDigit(str[i])) {
        break;
      }
      num += str[i] - '0';
      if (i != str.length() && IsDigit(str[i + 1])) {
          num *= 10;
      }
    }
    if (sign == 1 && (num > numeric_limits<int>::max() || i - begin > 10)) {
      return numeric_limits<int>::max();
    }
    if (sign == -1 && (num > numeric_limits<int>::max() || i - begin > 10)) {
      return numeric_limits<int>::min();
    }
    return static_cast<int>(sign * num);
  }

  bool IsDigit(char c) {
    int digit = c - '0';
    if (digit < 0 || digit > 9) {
      return false;
    }
    return true;
  }
};

int main(int argc, char** argv) {
  Solution solution;
  string s("      -2147483648");
  cout << solution.myAtoi(s) << endl;
  return 0;
}