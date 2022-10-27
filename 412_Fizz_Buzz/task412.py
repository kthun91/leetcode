TESTCASE = 20

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        mylist = []
        for i in range(1,n+1):
            if not ((i % 5) or (i % 3)):
                mylist.append("FizzBuzz")
            if (not (i % 5) and (i % 3)):
                mylist.append("Buzz")
            if ((i % 5) and not (i % 3)):
                mylist.append("Fizz")
            if (((i % 5) and (i % 3))):
                mylist.append(str(i))
        return mylist

res = Solution()
print(res.fizzBuzz(TESTCASE))