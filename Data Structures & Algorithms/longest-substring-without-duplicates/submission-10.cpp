class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int res = 0;
        set<int> seen;

        for(int r = 0; r < s.size(); r++){
            while(seen.find(s[r]) != seen.end()){
                seen.erase(s[l]);
                l++;         
            }
            res = max(res, r-l+1);
            seen.insert(s[r]);
        }
        return res;
    }
};
