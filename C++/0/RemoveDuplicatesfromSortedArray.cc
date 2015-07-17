#include <iostream>

class Solution {
public:
  int removeDuplicates(int A[], int n) {
    if (n == 0) return 0;

    int n_nonduplicate = 0;
    for (int i = 1; i < n; ++i) {
      // if all are duplicates, what should be outputed?
      if (A[n_nonduplicate] != A[i]) {
        A[++n_nonduplicate] = A[i];
      }
    }
    return n_nonduplicate + 1;
  }
};

int main()
{
  int A[5] = {1, 1, 2, 2, 3};
  Solution s;
  std::cout << s.removeDuplicates(A, sizeof(A)/sizeof(*A)) << std::endl;
}