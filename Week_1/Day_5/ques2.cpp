class Solution {
public:
    void reverseString(vector<char>& s) {
        char temp ;
        int a = 0 ;
        int b = s.size()-1;

        while (a<b){
            temp = s[a] ;
            s[a] = s[b] ; 
            s[b] = temp ;
            a++;b--;
        }
    }
};