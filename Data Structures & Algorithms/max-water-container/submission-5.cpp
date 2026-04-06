class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size()-1;
        int res = 0;

        while(l < r){
            if(heights[l] < heights[r]){
                res = max(res, heights[l] * (r - l));
                l += 1;
            }else{
                res = max(res, heights[r] * (r - l));
                r -= 1;
            }
        }

        return res;
    }
};
