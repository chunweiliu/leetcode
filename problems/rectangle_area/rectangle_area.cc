#include <iostream>

class Solution {
public:
  int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {    
    // (A, B) bottom-left; (C, D) top-right
    // (E, F) bottom-left; (G, H) top-right
    // The area is the union minus the intersection
    int S1 = (C - A) * (D - B);
    int S2 = (G - E) * (H - F);
    if (C < E /* left */ || A > G /* right */ ||
        D < F /* down */ || B > H /* up */) {  // No intersection
      return S1 + S2;
    }

    int left = std::max(A, E);
    int bottom = std::max(B, F);
    int right = std::min(C, G);
    int top = std::min(D, H);
    return S1 + S2 - (right - left) * (top - bottom);
  }
};

int main(int argc, char** argv) {
  Solution solution = Solution();
  std::cout << solution.computeArea(-2, -2, 2, 2, 3, 3, 4, 4) << std::endl;
  return 0;
}