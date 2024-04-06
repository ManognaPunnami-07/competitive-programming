class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=[]
        for i in range(len(s)-len(p)+1):
            a=s[i:i+len(p)]
            a=list(a)
            a.sort()
            p=list(p)
            p.sort()
            if a==p:
                l=l+[i]
        return l


        