class Solution:

    """
    im genuinely retarded and a waste of oxygen on this planet for being this dumb
    """

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for string in strs:
            n = len(string)
            encoded.append(f"{n}#{string}")
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:

        decoded = []
        i = 0

        while i < len(s):
            n = ""
            while s[i] != "#":
                n += s[i]
                i += 1

            i += 1
            
            decoded.append(s[i:i+int(n)])
            i += int(n)
                
        return decoded
