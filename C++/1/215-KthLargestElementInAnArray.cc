#include <iostream>
#include <vector>

class Solution {
 public:
  int findKthLargest(std::vector<int>& nums, int k) {
    std::make_heap(nums.begin(), nums.end());  // This is a max heap.
    int kth_element;
    for (int i = 0; i < k; ++i) {
      kth_element = nums.front();
      std::pop_heap(nums.begin(), nums.end());  // The largest swap to the end.
      nums.pop_back();
    }
    return kth_element;
  }
};

int main(int argc, char** argv) {
  Solution solution;
  std::vector<int> nums = {3, 2, 1, 5, 6, 4};
  std::cout << solution.findKthLargest(nums, 4) << std::endl;
  return 0;
}