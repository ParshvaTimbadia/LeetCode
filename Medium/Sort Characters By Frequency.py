***

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

***



#Here I have implemented the code using Heap

class Solution:
    def frequencySort(self, s: str) -> str:
        
            dict={}
            max_heap=[]
            result=""
            
            for i in s:
                if i not in dict:
                    dict[i]=0
                dict[i]+=1


            for key, value in dict.items():
                heappush(max_heap, (-value, key))
            
            while max_heap:
                x = heappop(max_heap)
                result+=(-x[0]*x[1])

            return result

