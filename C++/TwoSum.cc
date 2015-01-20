#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class TwoSum
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        vector<int> two_indices;
        unordered_map<int, int> number_to_index;
        for (int i = 0; i < numbers.size(); ++i)
        {
            number_to_index[numbers[i]] = i;
        }
        for (int i = 0; i < numbers.size(); ++i)
        {
            const int the_other = target - numbers[i];
            if (number_to_index.find(the_other) != number_to_index.end() &&
                    number_to_index[the_other] > i)    // avoid duplicates
            {
                two_indices.push_back(i + 1);
                two_indices.push_back(number_to_index[the_other] + 1);
                break;
            }
        }
        return two_indices;
    }
};

int main()
{
    TwoSum two_sum;
    vector<int> numbers = {1, 2, 3};
    const int target = 3;
    vector<int> answer = two_sum.twoSum(numbers, target);
    for (auto &index : answer)
        cout << index << " ";
}