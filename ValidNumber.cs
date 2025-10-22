public class Solution {
    public bool IsNumber(string s) {
        s = s.Trim();
        bool numSeen = false;
        bool dotSeen = false;
        bool eSeen = false;

        for (int i = 0; i < s.Length; i++) {
            char c = s[i];

            if (char.IsDigit(c)) {
                numSeen = true;
            } 
            else if (c == '.') {
                if (dotSeen || eSeen) return false;
                dotSeen = true;
            } 
            else if (c == 'e' || c == 'E') {
                if (eSeen || !numSeen) return false;
                eSeen = true;
                numSeen = false; 
            } 
            else if (c == '+' || c == '-') {
                if (i != 0 && s[i - 1] != 'e' && s[i - 1] != 'E') return false;
            } 
            else {
                return false;
            }
        }

        return numSeen;
    }
}
