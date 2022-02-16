# Group Anagrams

# Given an array of strings, return a list of groups of anagrams.
# The groups of anagrams don't need to be ordered in any particular way.
'''
Explanation:

Anagrams are strings made up of exactly the same letters.
where order doesn't matter.
(A word, phrase, or name formed by rearranging the letters)
For example, "Brush" and "shrub" are anagrams.
"cat" = "act", "doo" = "odo" etc.

# Time and Space Complexity:

# Sorting one word takes O(nlog(n)) time.
There are 'w' no. of words so, overall O(w * n * log(n)) time.

# While sorting "indices", we have 'w' no. of index values and
sorting them will take O(wlog(w)) time. But we are sorting them
in a way that words in the 'sortedWords' would be sorted.
It take almost 'n' comparisons, so overall O(n * wlog(w)) time.

# We are storing 'w' words and each of them are atmost 'n' length
so, O(w * n) space.

here, 'n' is the length of the longest word.
'''

# Solution 1 : By sorting each word alphabetically
# O(w * nlog(n) + n * wlog(w)) time , O(w * n) space
# where 'w' is the no. of words and 'n' is the length of the longest word
'''
def groupAnagrams(words):

    if len(words) == 0:
        return []

    # sortedWords = ["".join(sorted(w)) for w in words] # O(w * nlog(n)) time
    sortedWords = []
    for word in words: # O(w)
        sortedWords.append("".join(sorted(word))) # O(nlog(n)) time 
    
    indices = [i for i in range(len(words))]
    indices.sort(key = lambda x: sortedWords[x]) # O(n * wlog(w)) time 

    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for idx in indices:
        word = words[idx]
        sortedWord = sortedWords[idx]

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue

        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord

    result.append(currentAnagramGroup)

    return result
'''

# Solution 2 : By using Hashtable
# O(w * nlog(n)) time , O(w * n) space
# where 'w' is no. of words and 'n' is the length of longest word

def groupAnagrams(words):
    anagrams = {}
    for word in words:  # O(w)
        sortedWord = "".join(sorted(word)) # O(nlog(n)) time 
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())
            

# Input
words = ["do","act","flop","tac","cat","od","olfp"]
print(words)
print(groupAnagrams(words))
#output = [['do', 'od'], ['act', 'tac', 'cat'], ['flop', 'olfp']]
