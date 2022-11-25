class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lower_start = ord('a')
        upper_start = ord('A')
        lower_char_set = {i for i in range(lower_start, lower_start+26)}
        upper_char_set = {i for i in range(upper_start, upper_start+26)}

        s = list(s)
        i, j = 0, len(s)-1
        while i <= j:
            if ord(s[i]) not in lower_char_set and ord(s[i]) not in upper_char_set:
                i += 1
            elif ord(s[j]) not in lower_char_set and ord(s[j]) not in upper_char_set:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
                
        return "".join(s)