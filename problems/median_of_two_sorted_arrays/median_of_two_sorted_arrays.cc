#include <iostream>
#include <vector>

using namespace std;

class Solution {
 public:
  double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    // Median definition.
    int len1 = nums1.size();
    int len2 = nums2.size();
    int total = len1 + len2;
    if (total % 2 == 1) {
      return FindKthElement(nums1.begin(), len1, nums2.begin(), len2,
                            total / 2 + 1);
    }
    return 0.5 * (FindKthElement(nums1.begin(), len1, nums2.begin(), len2, 
                                 total / 2) + 
                  FindKthElement(nums1.begin(), len1, nums2.begin(), len2, 
                                 total / 2 + 1));
  }

  double FindKthElement(vector<int>::iterator iter1, int len1,
                        vector<int>::iterator iter2, int len2,
                        int kth) {
    if (len1 < len2) {  // Assume |nums1| >= |nums2|
      return FindKthElement(iter2, len2, iter1, len1, kth);  
    }
    if (len2 == 0) {
      return *(iter1 + kth - 1);
    }
    if (kth == 1) {
      return min(*iter1, *iter2);
    }
    // Binary search for the k-th element. Get the first n from num1 and the
    // first m from num2 (where n + m == k). If the n-th of num1 is smaller than
    // the m-th of num2, than the k-th wouldn't be in the first n-th of num1.
    // Same observation apply to num2. 
    // Why? Because the kth element couldn't in either n-th nor m-th elements 
    // anyway. You just want to get rid of one part and move on.
    int m = min(kth / 2, len2);
    int n = kth - m;
    if (*(iter1 + n - 1) < *(iter2 + m - 1)) {
      return FindKthElement(iter1 + n, len1 - n, iter2, len2, kth - n);
    }
    return FindKthElement(iter1, len1, iter2 + m, len2 - m, kth - m);
  }
};

int main(int argc, char** argv) {
  Solution solution;
  vector<int> nums1 = {};
  vector<int> nums2 = {1, 2};
  cout << solution.findMedianSortedArrays(nums1, nums2) << endl;
  return 0;
}