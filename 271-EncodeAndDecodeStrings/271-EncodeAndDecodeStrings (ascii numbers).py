from typing import List

class Solution:

    """
    waste of oxygen solution part two that i failed miserably on because im so incredibly retarded
    """

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""

        """
        just turn each string into its ascii #?
        then if i separate letters by |, and strings by # (delimiters)
        """

        encoded_string = []

        for string in strs:
            encoded = []
            for char in string:
                encoded.append(str(ord(char)))
            encoded_string.append("|".join(encoded) + "#")

        return "".join(encoded_string)
        

    def decode(self, s: str) -> List[str]:

        words = s.split("#")[:-1]
        decoded_strs = []

        for word in words:
            if not word:
                decoded_strs.append("")
                continue

            chars = word.split("|")
            string = []
            for char in chars:
                string.append(chr(int(char)))
            decoded_strs.append("".join(string))

        return decoded_strs
