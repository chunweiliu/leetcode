#include <cstdio>
#include <iostream>
using namespace std;

// int main(){
//   int x = 2, y = 6, z = 6;
//   x=y==z;
//   printf("%d", x);
//   return 0;
// }


// int main() {
//   int x = 3;
//   if (x == 2);
//   x = 0;
//   if (x == 3)
//     x++;
//   else x += 2;
//   cout << x;
//   return 0;
// }

// 8
// int main() {
//   int a = 5;
//   if (a=1) {
//     printf("%d", a);
//   }
//   return 0;
// }

// 9
// int main() {
//   char *ptr;
//   char myString[] = "abcdefg";
//   ptr = myString;
//   ptr += 5;
//   cout << *ptr;
// }

// 10
// struct A{
//   int i, j;
//   A(int ii, int jj) : i(ii), j(ii){}
//   A(const A&a) {

//   }
//   A& operator =(const A& a) {
//     i = a.i;
//     j = a.j;
//     return (*this);
//   }
// };

// int main() {
//   A a(1, 2);
//   A b(2, 3);
//   A z = (a=b);
//   cout << z.i << " " << z.j << endl;
//   return 0;
// }

// 13
// int main() {
//   int z, x = 5, y = -10, a = 4, b = 2;
//   z = x++ - --y * b/a;  // 5 - -11 * 2 / 4
//   printf("%d\n", z);
//   return 0;
// }

// 15
// int main() {
//   int x = 4, *y;
//   y = &x; (*y)++;
//   printf("%d\n", *y);
//   return 0;
// }

// 16
// template <class T>
// struct sum {
//   static void foo(T op1, T op2) {
//     cout << op1 << op2;
//   }
// };

// int main() {
//   sum<int>::foo(1, 3);
// }

// 17
// int main() {
//   int i = 4;
//   switch (i) {
//     default:
//       ;
//     case 3:
//       i += 5;
//       if (i == 8) {
//         i++;
//         if (i == 9) break;
//         i *= 4;
//       }
//       i -= 4;
//       break;
//     case 8:
//       i += 5;
//       break;
//   }
//   printf("i = %d\n", i);
//   return 0;
// }

// 18
// #define VALUE 1+2
// int main() {
//   printf("%d %d\n",VALUE/VALUE,VALUE*3);
// }

// 20
int main() {
  int i = 20, k = 0;
  for (int j = 1; j--; k+=j<10?4:3);
  printf("%d", k);
  return 0;
}