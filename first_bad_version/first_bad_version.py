


class Solution:
    BAD_VERSION = 0
    def firstBadVersion(self, n: int) -> int:
        pointer = n // 2

        if pointer == 0:
            pointer = 1

        pointer_prev = 0
        while True:
            is_bad_current = self.isBadVersion(pointer)

            if is_bad_current and (pointer == 1):  # edge case - bad is the first
                return 1

            is_bad_previous = self.isBadVersion(pointer - 1)
            if is_bad_current and not is_bad_previous:
                return pointer

            step = abs(pointer - pointer_prev) // 2
            if step == 0:
                step = 1
            pointer_prev = pointer

            if not is_bad_current:
                pointer = pointer + step

            if is_bad_current and is_bad_previous:
                pointer = pointer - step

    def isBadVersion(self, version: int) -> bool:
        return version >= self.BAD_VERSION
