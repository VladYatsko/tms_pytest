import requests
from hometask_26.generator.generator import generated_data


class ClientApi:
    AUTH_TOKEN = '8710ea7abd6d5803fed378c03349c2900c5290de68469dfd7dbc60d69c0706e0'
    HEADERS = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    URL = 'https://gorest.co.in'
    GENERATED_USER = next(generated_data())
    DATA = {"name": f"{GENERATED_USER.first_name} {GENERATED_USER.last_name}",
            "email": f'{GENERATED_USER.email}',
            "gender": f"{GENERATED_USER.gender}",
            "status": f'{GENERATED_USER.status}'}
        
    def get_all_users(self):
        response = requests.get(url=f'{self.URL}/public/v2/users', headers=self.HEADERS)
        return response

    def create_new_user(self):
        response = requests.post(url=f'{self.URL}/public/v2/users', headers=self.HEADERS, json=self.DATA)
        return response
    
    def get_one_user(self, user_id):
        response = requests.get(url=f'{self.URL}/public/v2/users/{user_id}', headers=self.HEADERS)
        return response
    
    def update_new_user(self, user_id):
        response = requests.patch(f'{self.URL}/public/v2/users/{user_id}',
                                  headers=self.HEADERS, json={"name": f"{self.GENERATED_USER.first_name}"})
        return response

    def delete_user(self, user_id):
        response = requests.delete(f'{self.URL}/public/v2/users/{user_id}', headers=self.HEADERS)
        return response
