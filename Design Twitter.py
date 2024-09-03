class Twitter:

    def __init__(self):
        self.user_posts = collections.defaultdict(list)
        self.user_followers = collections.defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append([self.time,tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_followers[userId] : 
            self.user_followers[userId].add(userId)
            
        result,carry = [],[]
        
        for follower in self.user_followers[userId]:
            if self.user_posts[follower]:
                time,post = self.user_posts[follower][-1]
                length = len(self.user_posts[follower])-1
                heapq.heappush(carry,(-time,post,follower,length))

        i = 0
        while i < 10 and carry:
            time,post,follower,length = heapq.heappop(carry)
            time = -time
            result.append(post)
            if length:
                time,post = self.user_posts[follower][length-1]
                heapq.heappush(carry,(-time,post,follower,length-1))
            i += 1
        
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.user_followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_followers[followerId]:
            self.user_followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)