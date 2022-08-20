# Ex using Instagram to create a User class and defining methods to increase follower count
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # lets def a method where when users follow each other, their followers total increases
    def follow(self, user):
        user.followers += 1     # user goes up by 1
        self.following += 1     # your account goes up by 1

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

# user 1 decided to follow user 2
user_1.follow(user_2)
print(user_1.followers)     # 0
print(user_1.following)     # 1
print(user_2.followers)     # 1
print(user_2.following)     # 0