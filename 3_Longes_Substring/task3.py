class Solution:
    def _powerSet(s: str) -> list:
        result = []
        tmp = []
        lenPot = 1 << len(s)  # 2 ** len(s)
        for i in range(lenPot):
            for j in range(lenPot):
                if i & (1 << j):
                    tmp.append(s[j])
            if "".join(tmp) in s:
                result.append(tmp)
            tmp = []
        return result

    def _hasReapeatingCharacter(s:list) -> bool:
        return len(set(s)) != len(s)

    def lengthOfLongestSubstring(self, s: str) -> list:
        result = ""
        for i in Solution._powerSet(s):
            if len(i) > len(result) and not Solution._hasReapeatingCharacter(i):
                result = "".join(i)

        return [result, len(result)]


def main():
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew"))

if __name__ == "__main__":
    main()
