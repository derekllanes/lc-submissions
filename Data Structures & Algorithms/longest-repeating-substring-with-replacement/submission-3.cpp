class Solution {
public:
    int characterReplacement(string s, int k) {
        int res = 0;
        int l = 0;
        unordered_map<char, int> letMap;
        int maxl = 0;

        for (int r = 0; r < s.size(); r++){
            letMap[s[r]]++;

            if(maxl < letMap[s[r]]){
                maxl = letMap[s[r]];
            }else if(maxl < letMap[s[l]]){
                maxl = letMap[s[l]];
            }

            while ((r-l+1) - maxl > k){
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
