#include <iostream>
#include <vector>

using namespace std;

class Solution {
 public:
  int Partition(vector<int>& nums, int left, int right) {
    int i = left;
    int j = left;
    int n = right;
    const int pivot = nums[n];
    while (j <= n) {
      cout << i << " " << j << " " << n << endl;
      if (nums[j] == pivot) j++;
      else if (nums[j] < pivot) {
        swap(nums[i++], nums[j++]);
      } else {
        swap(nums[j], nums[n--]);
      }
    }
    return i;
  }

  int findKthLargest(vector<int> nums, int k) {
    int left = 0, right = nums.size() - 1;
    while (true) {
      int p = Partition(nums, left, right);
      if (p == k - 1) return nums[p];
      if (p < k - 1) {
        left = p + 1;
      } else {
        right = p - 1;
      }
    }
  }


  // int findKthLargest(std::vector<int>& nums, int k) {
  //   std::make_heap(nums.begin(), nums.end());  // This is a max heap.
  //   int kth_element;
  //   for (int i = 0; i < k; ++i) {
  //     kth_element = nums.front();
  //     std::pop_heap(nums.begin(), nums.end());  // The largest swap to the end.
  //     nums.pop_back();
  //   }
  //   return kth_element;
  // }
};

int main(int argc, char** argv) {
  Solution solution;
  std::vector<int> nums = {1, 2, 3, 4, 5, 6};
  std::cout << solution.findKthLargest(nums, 1) << std::endl;
  return 0;
}