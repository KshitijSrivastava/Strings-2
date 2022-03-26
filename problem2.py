#Find All Anagrams in a String 

# (https://leetcode.com/problems/find-all-anagrams-in-a-string/)


class Solution:
    def create_string_dict(self, word):
        d = {}
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
        
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        big = s
        small = p
        
        n_b = len(big)
        n_s = len(small)
        
        if n_s > n_b:
            return []
        
        d_s = self.create_string_dict(small)
            
        sub_d = {}
        
        i = 0
        j = 0
        while j < n_s:
            sub_d = self.insert_char_dict(big[j], sub_d)
            j += 1
            
        if d_s == sub_d:
            print(d_s, sub_d)
            output.append(i)
        
        while j < n_b:
            sub_d = self.insert_char_dict(big[j], sub_d)
            sub_d = self.delete_char_dict(big[i], sub_d)
            
            j += 1
            i += 1
            
            if d_s == sub_d:
                output.append(i)
            
        return output
        
        
        
        
        