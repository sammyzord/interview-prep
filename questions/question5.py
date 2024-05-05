class Solution:
    def recur(self, st: int, nums: list[int], sol: list[int]):

        copy = list(set(sol))
        copy.sort()
        if sol != copy:
            return 0
        elif st == len(nums):
            return len(sol)

        num = nums[st]
        _next = st + 1

        y = self.recur(_next, nums, [*sol, num])
        n = self.recur(_next, nums, [*sol])

        z = max(y, n)

        return z

    def lengthOfLIS(self, nums: list[int]) -> int:
        self.mem = {}
        x = self.recur(0, nums, [])

        return x


def main():
    sol = Solution()
    x = sol.lengthOfLIS([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(x)


if __name__ == "__main__":
    main()
