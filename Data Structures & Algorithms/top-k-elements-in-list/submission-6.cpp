class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<int> res;

        for(int i = 0; i < nums.size(); ++i){
            ++count[nums[i]];
        }

        vector<vector<int>> freq(nums.size()+1);

        for(const auto& [num, counts] : count){
            freq[counts].push_back(num);
        }

        for(int counts = freq.size()-1; counts >= 0; --counts){
            for(int num = 0; num < freq[counts].size(); ++num){
                res.push_back(freq[counts][num]);
                if(res.size() == k){
                    return res;
                }
            }
        }

        return res;
    }
};
