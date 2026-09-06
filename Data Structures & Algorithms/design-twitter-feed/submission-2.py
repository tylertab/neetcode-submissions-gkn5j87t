class Twitter:

    def __init__(self):
        self.userfollowing = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId,tweetId))        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.tweets
        userfollowing = self.userfollowing.get(userId,[])
      
        res = []
        i = len(tweets) - 1
        while len(res) < 10 and i in range(len(tweets)):
            user, tweet = tweets[i]
            if user in userfollowing or user == userId:
                res.append(tweet)
            i -= 1
        print(res)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        userfollowing = self.userfollowing

        if followerId not in userfollowing:
            userfollowing[followerId] = set()
        userfollowing[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        userfollowing = self.userfollowing

        if followerId in userfollowing:
            following =userfollowing[followerId]
            if followeeId in following:
                following.remove(followeeId)
