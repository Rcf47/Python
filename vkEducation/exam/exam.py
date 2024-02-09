from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def post_tweet(self, user_id, tweet_id):
        self.tweets[user_id].append(tweet_id)

    def get_news_feed(self, user_id) -> List[int]:
        news_feed = []
        for followee in self.followers[user_id] | {user_id}:
            news_feed.extend(self.tweets[followee])
        return news_feed[::-1][:10]

    def follow(self, follower_id, followee_id):
        self.followers[follower_id].add(followee_id)

    def unfollow(self, follower_id, followee_id):
        if followee_id in self.followers[follower_id]:
            self.followers[follower_id].remove(followee_id)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# twitter = Twitter()
# twitter.follow(1, 2)
# twitter.follow(1, 3)
# twitter.post_tweet(2, 4)
# twitter.post_tweet(2, 6)
# twitter.post_tweet(3, 2)
# twitter.post_tweet(3, 7)
# twitter.post_tweet(3, 3)
# twitter.post_tweet(3, 8)
# twitter.post_tweet(2, 1)
# twitter.post_tweet(2, 9)
# twitter.follow(1, 4)
# twitter.post_tweet(4, 5)
# twitter.post_tweet(4, 10)
# twitter.unfollow(1, 2)
# twitter.post_tweet(5, 11)
# twitter.post_tweet(5, 12)
# twitter.post_tweet(5, 13)
# twitter.post_tweet(6, 14)
# twitter.follow(1, 5)
# twitter.post_tweet(7, 15)
# twitter.post_tweet(7, 16)
# twitter.post_tweet(7, 17)
# twitter.post_tweet(7, 18)
# twitter.follow(1, 7)
# print(twitter.get_news_feed(1))
