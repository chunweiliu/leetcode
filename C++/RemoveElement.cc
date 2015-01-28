#include <iostream>
#include <utility>

class Solution {
public:
  int removeElement(int A[], int n, int elem) {
    int removed = 0;
    for (int i = 0; i < n-removed; ++i) {
      if (A[i] == elem) {
        std::swap(A[i], A[n-removed-1]);
        removed++;
        i--;
      }
    }
    return n - removed;
  }
};

int main()
{
  Solution s;
  int A[5] = {1, 2, 2, 2, 2};
  std::cout << s.removeElement(A, 5, 2) << std::endl;
}