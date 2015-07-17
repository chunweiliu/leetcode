#include <iostream>
#include <unordered_map>
#include <vector>


class Solution {
public:
  bool containsDuplicate(std::vector<int>& nums) {
    std::unordered_map<int, int> occurrences;
    for (int i = 0; i < nums.size(); ++i) {
      if (occurrences.find(nums[i]) != occurrences.end()) {
        return true;
      }
      occurrences.insert({nums[i], 1});
    }
    return false;
  }
};

int main(int argc, char** argv) {
  std::vector<int> nums = {0, 1, 2};
  Solution solution = Solution();
  if (solution.containsDuplicate(nums)) {
    std::cout << "Contains duplicate" << std::endl;
  } else {
    std::cout << "Not contains duplicate" << std::endl;
  }
  return 0;
}