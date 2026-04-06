class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<int> res;

        for(int i = 0; i < nums.size(); ++i){
            ++count[nums[i]];
        }

        vector<vector<int>> freq(nums.size()+1);

        for(const auto& [key, val] : count){
            freq[val].push_back(key);
        }

        for(int i = (int)freq.size()-1; i >= 0; --i){
            for(int num = 0; num < freq[i].size(); ++num){
                res.push_back(freq[i][num]);
                if(res.size() == k){
                    return res;
                }
            }
        }
        return res;
    }
};
