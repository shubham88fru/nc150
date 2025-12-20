import heapq
from typing import List

""""""""""""""""""""""""""""
-------------------------
OPTIMAL: Merge using heap
-------------------------
TC: O(10*log(k)); where k is the number of followees
SC: O(1)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

-----------------------------------
BRUTE: Standard merge k sorted list
-----------------------------------
TC: O(10*k); where k is the number of followees
SC: O(1)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/design-twitter-feed
class Twitter:

    def __init__(self):
        self.followers_map = {}
        self.tweets_map = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_map:
            self.tweets_map[userId] = []
        self.tweets_map[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []

        self.follow(userId, userId)
        for followeeId in self.followers_map[userId]:
            if followeeId in self.tweets_map:
                idx = len(self.tweets_map[followeeId]) - 1
                last_tweet = self.tweets_map[followeeId][idx]
                min_heap.append([last_tweet[0], last_tweet[1], followeeId, idx - 1])
        heapq.heapify(min_heap)

        ans = []
        while len(min_heap) > 0 and len(ans) < 10:
            data = heapq.heappop(min_heap)
            ans.append(data[1])
            # print(ans)
            if data[3] >= 0:
                next_tweet = self.tweets_map[data[2]][data[3]]
                heapq.heappush(min_heap, [next_tweet[0], next_tweet[1], data[2], data[3] - 1])

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers_map:
            self.followers_map[followerId] = set()
        self.followers_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers_map[followerId]:
            self.followers_map[followerId].remove(followeeId)