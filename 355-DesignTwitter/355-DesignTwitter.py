import heapq 

class Twitter:

    """
    honestly had a little bit of a hard time doing this design problem
    
    challenges:
    1. kept using the wrong input var names since i was changing the flow as i was coding 
    2. needed to be more considerate of edge cases while coding
    3. some syntaxes needed brush up
    
    other than that, pretty proud that i was able to do a heap solution since i havent been using heaps. i did see topics to see that they were using heaps tho.

    1-10 ms runtime beats 78 - 99%
    """

    def __init__(self):

        # need to store: all users, who the user is following, all posts

        self.following = {}   # key: userId, value: set of followeeId
        self.posts = {}  # key: userId, value: array of posts
        self.id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append([-self.id, tweetId])
        
        self.id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        accepted = [userId]

        if userId in self.following:
            accepted.extend(list(self.following[userId]))

        news, feed = [], []

        for person in accepted:
            if person in self.posts:
                for post in self.posts[person]:
                    heappush(news, post)

        for i in range(10):
            if not news:
                break
            feed.append(heappop(news)[1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
