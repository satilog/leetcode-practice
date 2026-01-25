from typing import List


class Solution:
    def numMatchingSubseq(self, s, words: List[str]) -> int:
        count = 0
        for word in words:
            seq = s
            isSubseq = True
            for c in word:
                matchIndex = seq.find(c)
                if matchIndex != -1:
                    seq = seq[matchIndex + 1 :]
                else:
                    isSubseq = False
                    break
            if isSubseq:
                count += 1
        return count


words = ["a", "bb", "acd", "ace"]
seq = "abcde"
solution = Solution()
print(solution.numMatchingSubseq(seq, words))
