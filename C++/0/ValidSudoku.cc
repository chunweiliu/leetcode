#include <vector>
#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;

class ValidSudoku
{
public:
	bool isValidSudoku(const vector<vector<char> > &board) {
		const int sudoku_size = 9;
		bool used[sudoku_size];

		for (int i = 0; i < sudoku_size; ++i) {
			fill(used, used+sudoku_size, false);
			for (int j = 0; j < sudoku_size; ++j) {
				if (check(board[j][i], used) == false)  // row
					return false;
			}
		}
		for (int i = 0; i < sudoku_size; ++i) {
			fill(used, used+sudoku_size, false);
			for (int j = 0; j < sudoku_size; ++j) {
				if (check(board[i][j], used) == false)  // column
					return false;
			}
		}
		for (int r = 0; r < sudoku_size/3; ++r) {
			for (int c = 0; c < sudoku_size/3; ++c) {
				fill(used, used+sudoku_size, false);
				for (int i = 0; i < sudoku_size/3; ++i) {
					for (int j = 0; j < sudoku_size/3; ++j) {
						if (check(board[3*r+i][3*c+j], used) == false)
							return false;
					}
				}
			}
		}
		return true;
	}

	bool check(char element, bool used[]) {  // &used is the address of the used
		if (element == '.') return true;
		const int index = element - '1';
		if (used[index]) return false;
		return used[index] = true;  // the assignment is true
	}
};

int main()
{
	vector<vector<char> > board;
	for (int i = 0; i < 9; ++i) {
		vector<char> row;
		for (int j = 0; j < 9; ++j) {
			row.push_back('9');
		}
		board.push_back(row);
	}
	ValidSudoku valid_sudoku;
	cout << valid_sudoku.isValidSudoku(board) << endl;
}