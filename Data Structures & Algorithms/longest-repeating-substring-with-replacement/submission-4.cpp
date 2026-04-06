class Solution {
public:
    int characterReplacement(string s, int k) {
        int res = 0;
        int l = 0;
        unordered_map<char, int> letMap;
        int maxletter = 0;

        for (int r = 0; r < s.size(); r++){
            letMap[s[r]]++;

            maxletter = max(maxletter, letMap[s[r]]);

            while ((r-l+1) - maxletter > k){
                letMap[s[l]]--;
                l++;
            }

            if ((r-l+1) > res){
                res = r-l+1;
            }
        }

        return res;
    }
};
