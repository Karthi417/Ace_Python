class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapping={')':'(','}':'{',']':'['}
        for char in s:
            if char in mapping.values():
                st.append(char)
            elif char in mapping.keys():
                if not st or mapping[char]!=st.pop():
                    return False
        return not st