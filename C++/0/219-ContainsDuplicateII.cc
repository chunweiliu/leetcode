#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
public:
  bool containsNearbyDuplicate(std::vector<int>& nums, int k) {
    std::unordered_map<int, int> occurence;
    for (int i = 0; i < nums.size(); ++i) {
      auto got = occurence.find(nums[i]);
      if (got != occurence.end()) {
        if (abs(got->second - i) <= k) {
          return true;
        } else {
          got->second = i;
        }
      } else {
        occurence.insert({nums[i], i});
      }
    }
    return false;
  }
};

int main(int argc, char** argv) {
  std::vector<int> nums = {1, 0, 1, 1};
  int k = 1;
  Solution solution = Solution();
  if (solution.containsNearbyDuplicate(nums, k)) {
    std::cout << "Contains nearby duplicate" << std::endl;
  } else {
    std::cout << "Not contains near by duplicate" << std::endl;
  }
  return 0;
}