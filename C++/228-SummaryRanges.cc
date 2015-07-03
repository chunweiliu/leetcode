#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

class Solution {
 public:
    vector<string> summaryRanges(vector<int>& nums) {
      vector<string> answer;
      if (nums.size() < 1) {
      } else if (nums.size() == 1) {
        answer.push_back(to_string(nums[0]));
      } else {
        pair<int, int> interval;
        interval.first = nums[0];
        interval.second = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
          if (nums[i] - nums[i - 1] == 1) {
            interval.second = nums[i];
          } else {
            Check(interval, &answer);
            interval.first = nums[i];
            interval.second = nums[i];
          }
        }
        Check(interval, &answer);
      }
      return answer;
    }

    void Check(std::pair<int, int> interval, vector<string>* answer) {
      if (interval.second - interval.first >= 1) {
        answer->push_back(to_string(interval.first) + "->" + to_string(interval.second));
      } else {
        answer->push_back(to_string(interval.first));
      }
    }

    void Print(vector<int>& nums) {
      vector<string> answer = summaryRanges(nums);
      for (int i = 0; i < answer.size(); ++i) {
        cout << answer.at(i) << endl;
      }
    }
};

int main(int argc, char** argv) {
  vector<int> nums {0, 1};
  Solution solution = Solution();
  solution.Print(nums);
}