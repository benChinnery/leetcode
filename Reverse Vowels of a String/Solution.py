class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        vowelList = set('aeiouAEIOU')
        vowels = []
        size = len(s)

        for i in range(size):
            if (s[i] in vowelList):
                vowels.append(i)
        size = len(vowels)//2
        for i in range(size):
            #end = len(vowels) - 1 - i
            s[vowels[i]], s[vowels[-i-1]] = s[vowels[-i-1]], s[vowels[i]]

        s = "".join(s)
        return(s)
        
        #print(vowels)

        """
        :type s: str
        :rtype: str
        """
