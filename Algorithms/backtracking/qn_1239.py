from queue import Queue
class Solution:
    def backtracker(self, i, d, arr):
        if i == len(arr):
            return 0
        x = 0
        x = self.backtracker(i + 1, d, arr)
        f = True
        temp = set(d)
        for k in arr[i]:
            if k in temp:
                f = False
                break
            else:
                temp.add(k)
        y = 0
        if f:
            y = len(arr[i]) + self.backtracker(i + 1, d + arr[i], arr)
        return max(x, y)

    def maxLength(self, arr) -> int:
        return self.backtracker(0, "", arr)
