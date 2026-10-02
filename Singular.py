class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # A complete string uses all n pairs
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # Can add '(' as long as we haven't used all n
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()

            # Can add ')' only if it won't close more than we've opened
            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        backtrack([], 0, 0)
        return result

if __name__ == "__main__":
    solution = Solution()
    print(f"n = 3: {solution.generateParenthesis(3)}")