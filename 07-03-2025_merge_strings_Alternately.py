# Problem: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy


# Time: O(n)
# Space: O(n)


class Solution(object):
    def mergeAlternately(self, word1, word2):
        string=""
        while word1!="" or word2!="":
            if(word1==""):
                string=string+word2
                break
            if(word2==""):
                string=string+word1
                break
            string=string+word1[0]+word2[0]
            word1=word1[1:]
            word2=word2[1:]
        return string