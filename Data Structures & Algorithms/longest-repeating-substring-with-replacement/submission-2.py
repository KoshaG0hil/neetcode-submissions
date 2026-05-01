class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        max_frequency = 0
        longest_length = 0

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1        # ✅ add to dict
            max_frequency = max(max_frequency, seen[s[r]])  # ✅ update freq

            while (r - left + 1) - max_frequency > k:  # ✅ invalid window
                seen[s[left]] -= 1
                left += 1

            longest_length = max(longest_length, r - left + 1)  # ✅

        return longest_length