#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
	vector<vector<int> > generate(int num_rows) {
		vector<vector<int> > pascals_triangle;
		if (num_rows == 0) return pascals_triangle;

		pascals_triangle.push_back(vector<int>(1, 1));  // first row

		for (int i = 1; i < num_rows; ++i) {  // build from the second
			const int num_columns = i+1;
			vector<int> current(num_columns, 1);
			const vector<int> &previous = pascals_triangle[i-1];

			for (int j = 1; j < num_columns-1; ++j) {  // build the middle
				current[j] = previous[j-1] + previous[j];
			}
			pascals_triangle.push_back(current);
		}
		return pascals_triangle;
	}
};

int main()
{
	const int num_rows = 5;
	Solution pascals_triangle;
	const vector<vector<int> > &solution = pascals_triangle.generate(num_rows);
	for (int i = 0; i < num_rows; ++i) {
		for (int j = 0; j <= i; ++j) {
			cout << solution[i][j] << " ";
		}
		cout << endl;
	}
}