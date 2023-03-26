from hometask_26.requests_client import ClientApi


class TestClient:
    def test_getting_all_users(self):
        api_listener = ClientApi()
        response = api_listener.get_all_users()
        assert response.status_code == 200
        
    def test_creating_user(self):
        api_listener = ClientApi()
        response = api_listener.create_new_user()
        assert response.status_code == 201
        user_id = response.json()['id']
        assert api_listener.get_one_user(user_id).status_code == 200
    
    def test_updating_new_user(self):
        api_listener = ClientApi()
        response = api_listener.create_new_user()
        assert response.status_code == 201
        user_id = response.json()['id']
        assert api_listener.get_one_user(user_id).status_code == 200
        api_listener.update_new_user(user_id)
        assert api_listener.update_new_user(user_id).status_code == 200
        assert api_listener.get_one_user(user_id).json()['name'] == api_listener.GENERATED_USER.first_name
    
    def test_delete_user(self):
        api_listener = ClientApi()
        response = api_listener.create_new_user()
        assert response.status_code == 201
        user_id = response.json()['id']
        api_listener.delete_user(user_id)
        assert api_listener.get_one_user(user_id).status_code == 404
        