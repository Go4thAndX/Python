class User:

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Jan George")
user_2 = User("002", "Gerard")

# print(user_1, user_2)
# print(user_1.user_id, user_1.user_name, user_1.followers)
# print(user_2.user_id, user_2.user_name, user_2.followers)
# Output:
# <__main__.User object at 0x0000020D1F4B13D0> <__main__.User object at 0x0000020D1F4B1510>
# 001 Jan George 0
# 002 Gerard 0

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
# Output:
# 0
# 1
# 1
# 0
