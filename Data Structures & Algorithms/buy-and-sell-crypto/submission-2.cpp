class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int r = prices.size()-1;
        int res = 0;

        for(int l = 0; l < prices.size(); ++l){
            r = prices.size()-1;
            while(l < r){
                if(prices[l] <= prices[r]){
                    res = max(res, prices[r] - prices[l]);
                }

                --r;
            }
        }

        return res;
    }
};
