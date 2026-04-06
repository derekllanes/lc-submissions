class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size()-1;

        while(l < r){
            if(!std::isalnum(static_cast<unsigned char>(s[l]))){
                ++l;
            }else if(!std::isalnum(static_cast<unsigned char>(s[r]))){
                --r;
            }else if(std::tolower(s[l]) == std::tolower(s[r])){
                ++l;
                --r;
            }else{
                return false;
            }
        }
        return true;
    }
};
