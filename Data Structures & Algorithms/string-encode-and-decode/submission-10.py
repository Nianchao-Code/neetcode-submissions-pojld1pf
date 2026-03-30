class Solution:

    def encode(self, strs: List[str]) -> str:
        output_str = ""
        for s in strs:
            word_length = len(s)
            output_str += (str(word_length) + "#" + s)
        return output_str

    def decode(self, s: str) -> List[str]:
        output_lst = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            
            word_length = int(s[i:j])
            word = s[j + 1:j + 1 + word_length]
            output_lst.append(word)
            i = j + 1 + word_length

        return output_lst
