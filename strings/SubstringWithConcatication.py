class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        result = []
        word_dict = {}
        
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1
        
        for i in range(len(s) - total_len + 1):
            window = {}
            j = 0
            while j < total_len:
                word = s[i + j:i + j + word_len]
                if word in word_dict:
                    window[word] = window.get(word, 0) + 1
                    if window[word] > word_dict[word]:
                        break
                else:
                    break
                j += word_len
            if j == total_len:
                result.append(i)
        
        return result
