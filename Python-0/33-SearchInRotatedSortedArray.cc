#include "leetcode.h"

class Solution {
public:
  int search(const vector<int>& nums, int target) {
    int i = 0, j = nums.size() - 1;
    while (i <= j) {
      int m = (i + j) / 2;
    
      if (target == nums[m]) return m;

      if (nums[i] <= nums[m]) {  // the first half in order, "=" is important.
        if (nums[i] <= target && target < nums[m]) {
          j = m - 1;
        } else {
          i = m + 1;
        }
      } else {
        if (nums[m] < target && target <= nums[j]) {
          i = m + 1;
        } else {
          j = m - 1;
        }
      }
    }
    return -1;
  }
};