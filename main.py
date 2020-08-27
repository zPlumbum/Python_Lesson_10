import requests

class User:
    def __init__(self, token):
        self.token = token
        self.id = self.get_id()

    def get_id(self):
        response = requests.get(
            'https://api.vk.com/method/account.getProfileInfo',
            params={
                'access_token': self.token,
                'v': 5.122
            }
        )
        return response.json()['response']['id']

    def __and__(self, other):
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params={
                'access_token': self.token,
                'source_uid': self.id,
                'target_uid': other.id,
                'v': 5.122
            }
        )
        return response.json()['response']

    def __str__(self):
        response = requests.get(
            'https://api.vk.com/method/account.getProfileInfo',
            params={
                'access_token': self.token,
                'v': 5.122
            }
        )
        screen_name = response.json()['response']['screen_name']
        return 'https://vk.com/' + screen_name

user1 = User(input('Введите токен: '))
user2 = User(input('Введите токен: '))

print(user1 & user2)

print(user1)
print(user2)