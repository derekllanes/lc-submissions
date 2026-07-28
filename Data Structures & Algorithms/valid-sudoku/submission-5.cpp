class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, set<int>> colCheck;
        unordered_map<int, set<int>> rowCheck;
        unordered_map<int, set<int>> boxCheck;

        for(int row = 0; row < board.size(); ++row){
            for(int col = 0; col < board[row].size(); ++col){
                if(board[row][col] == ('.')){
                    continue;
                }

                if(colCheck[col].contains(board[row][col])){
                    return false;
                }

                if(rowCheck[row].contains(board[row][col])){
                    return false;
                }

                int curBox = (row / 3) * 3 + (col / 3);

                if(boxCheck[curBox].contains(board[row][col])){
                    return false;
                }

                colCheck[col].insert(board[row][col]);
                rowCheck[row].insert(board[row][col]);
                boxCheck[curBox].insert(board[row][col]);
            }
        }

        return true;
    }
};
