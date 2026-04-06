class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // dict for seen
        unordered_map<int, int> seen;

        // go through each num
        for(int i = 0; i < nums.size(); ++i){
            // if map not empty and i + j == target: return
            if(seen.find(target - nums[i]) != seen.end()){
                return {seen[target - nums[i]], i};
            }else{
                // else: add to the map and iterate
                seen[nums[i]] = i;
            }
        }
    }
};
