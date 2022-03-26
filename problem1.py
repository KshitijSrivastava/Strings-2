
#Implement strStr() (https://leetcode.com/problems/implement-strstr/)


class Solution:
    def create_string_dict(self, word):
        d ={}
        for char in word:
            if char not in d:
                d[char] = 0
            d[char] += 1
        return d
    
    def insert_char_dict(self, char, d):
        if char not in d:
            d[char] = 0
        d[char] += 1
        return d
    
    def delete_char_dict(self, char, d):
        if char not in d:
            return d
        if d[char] == 1:
            del d[char]
            return d
        d[char] -= 1
        return d
        
    def compare_needle_substring(self, needle, haystack, i, j):
        
        h_idx = i
        n_idx = 0
        
        while n_idx < len(needle):
            if needle[n_idx] != haystack[h_idx]:
                return False
            n_idx += 1
            h_idx += 1
        
        return True
        
    
    def strStr(self, haystack: str, needle: str) -> int:
        n_h = len(haystack)
        n_n = len(needle)
        
        if n_n > n_h:
            return -1
        
        d_n = self.create_string_dict(needle)
            
        sub_d = {}
        
        i = 0
        j = 0
        while j < n_n:
            sub_d = self.insert_char_dict(haystack[j], sub_d)
            j += 1
            
        if d_n == sub_d and self.compare_needle_substring(needle, haystack, i, j-1):
            return i
        
        while j < n_h:
            sub_d = self.insert_char_dict(haystack[j], sub_d)
            sub_d = self.delete_char_dict(haystack[i], sub_d)
            
            j += 1
            i += 1
            
            if d_n == sub_d and self.compare_needle_substring(needle, haystack, i, j-1):
                return i
            
        return -1
            
            
        