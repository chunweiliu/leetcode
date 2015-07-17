#include <iostream>

class ReverseInteger
{
public:
    int reverse(int x)
    {
        double r = 0;  // float is not enough
        int s = x > 0 ? 1 : -1;
        for (x = s * x; x; x /= 10)
        {
            r = r * 10 + x % 10;
        }
        if (s * r >= std::numeric_limits<int>::min() &&
                s * r <= std::numeric_limits<int>::max())
            return (int) s * r;
        else return 0;
    }
};

int main()
{
    int x = 15342364;
    // int x = 2234;
    ReverseInteger reverse_integer;
    std::cout << reverse_integer.reverse(x) << std::endl;
}