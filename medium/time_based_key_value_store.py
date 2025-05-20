
""""""""""""""""""""""""""""
----------------------
OPTIMAL: Binary search 
----------------------
TC: O(log(max(len)); where max(len) is the max length of values for a key.
SC: O(1)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

--------------------------------
BRUTE: Linear search of each key
--------------------------------
TC: O(max(len)); where max(len) is the max length of values for a key.
SC: O(1)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/time-based-key-value-store
class TimeMap:

    # /*
    # * UPDATE 05/20: If using python, we don't really need
    # * two map. We can take a single Map of string v/s type.
    # * In Java however, since we can't have tuple or list
    # * with two different types in it, we need to use two maps.
    # * */
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

