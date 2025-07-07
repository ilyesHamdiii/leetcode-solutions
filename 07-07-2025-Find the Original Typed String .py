class Solution(object):
    def possibleStringCount(self, word):
        output=0
        x=""
        y=1
        for i in range (1,len(word)):
            if word[i-1]==word[i]:
                y+=1
                
        return y



            
        
   