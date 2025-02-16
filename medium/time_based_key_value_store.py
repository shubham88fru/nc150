
# @link - https://neetcode.io/problems/time-based-key-value-store
class TimeMap:

    def __init__(self):
        self.tmMap = {}
        self.tmList = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmMap:
            self.tmMap[key] = []
            self.tmList[key] = []

        self.tmMap[key].append(value)
        self.tmList[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmMap:
            return ""

        res = self.bs(key, len(self.tmMap[key]), timestamp)
        if res == -1:
            return ""

        return self.tmMap[key][res]

    def bs(self, key, n, timestamp):
        l = 0
        r = n - 1

        best = -1
        while l <= r:
            mid = l + (r - l) // 2
            if self.tmList[key][mid] > timestamp:
                r = mid - 1
            else:
                best = mid
                l = mid + 1

        return best

