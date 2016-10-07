#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    // Table look up
    unordered_map<int, int> table;
    for (int i = 0; i < nums.size(); ++i) {
      table[nums[i]] = i;
    }

    for (int i = 0; i < nums.size(); ++i) {
      unordered_map<int, int>::iterator iter = table.find(target - nums[i]);
      if (iter != table.end() && iter->second != i) {
        return {i + 1, iter->second + 1};
      }
    }
    return {};
  }

  vector<int> TwoSum_TLE(vector<int>& nums, int target) {
    // Time Limited Exceeded. O(n * O(find)) = O(n^2)
    vector<int> ans;
    for (int i = 0; i < nums.size(); ++i) {
      int the_other = target - nums[i];
      const auto& iter = std::find(  // Complexity at least O(n)
          nums.begin() + i, nums.end(), the_other);
      if (iter != nums.end()) {
        ans.push_back(i + 1);
        ans.push_back(iter - nums.begin() + 1);  // Get the position
      }
    }
    return ans;
  }
};

int main(int argc, char** argv) {
  Solution solution;
  vector<int> nums = {2, 7, 11, 15};
  int target = 9;

  vector<int> ans = solution.twoSum(nums, target);
  if (ans.size() == 2) {
    std::cout << ans[0] << ", " << ans[1] << std::endl;    
  }

}