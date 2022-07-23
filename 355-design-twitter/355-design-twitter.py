class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.feeds = defaultdict(deque)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if len(self.feeds[userId]) == 10:
            self.feeds[userId].popleft()
        self.time += 1
        self.feeds[userId].append((self.time,tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        tweetsCollection = []
        feedsFrom = list(self.following[userId]) + [userId]
        
        maxHeap = []
        for userId in feedsFrom:
            fetchtweets = self.feeds[userId]
            lastIndex = len(fetchtweets) - 1
            if lastIndex < 0:
                continue
            timeStamp = fetchtweets[lastIndex][0] 
            heappush(maxHeap, (-timeStamp, lastIndex, fetchtweets))
        
        while maxHeap:
            _, lastIndex, tweets = heappop(maxHeap)
            
            tweetsCollection.append(tweets[lastIndex][1])
            
            if len(tweetsCollection) == 10:
                return tweetsCollection
            
            #Check if anymore tweets from the same user
            if lastIndex > 0:
                lastIndex -= 1
                heappush(maxHeap, (-tweets[lastIndex][0], lastIndex, tweets))
        
        return tweetsCollection
                
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)