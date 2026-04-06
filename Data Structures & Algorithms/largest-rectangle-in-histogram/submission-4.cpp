class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {

        int res = 0;
        stack<vector<int>> s;
        vector<int> rect;
        int start;

        for(int i = 0; i < heights.size(); ++i){
            start = i;
            while(!s.empty() && s.top()[1] > heights[i]){
                rect = s.top();
                s.pop();
                res = max(res, (i - rect[0]) * rect[1]);
                start = rect[0];
            }
            s.push({start, heights[i]});
        }

        while(!s.empty()){
            rect = s.top();
            s.pop();
            res = max(res, ((int)heights.size() - rect[0]) * rect[1]);
            start = rect[0];
        }

        return res;
    }
};
