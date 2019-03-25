from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserTests(APITestCase):
    users_url = '/api/v1/users/'
    login_url = '/api/v1/auth/signin/'
    register_url = '/api/v1/auth/register/'

    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="edna", email="edna@gmail.com",  password="password")
        admin_credentials = { "username":"edna", "password":"password"}
        admin_login_response = self.client.post(
            self.login_url, admin_credentials, format='json')
        admin_test_token = admin_login_response.data.get("token")
        self.admin_auth_header = 'JWT {}'.format(admin_test_token)
        
        user_data = {'username': 'lauren', 'email': 'lauren@bolon.com',
                     'password': 'password#1', 'first_name': 'Laura', 'last_name': 'Moon'}
        user_data2 = {'username': 'test0', 'email': 'test0@bolon.com',
                      'password': 'password#1', 'first_name': 'Test', 'last_name': 'Zero'}
        self.client.post(self.register_url, user_data, format='json')
        self.client.post(self.register_url, user_data2, format='json')
        login_credentials = {'username': 'lauren', 'password': 'password#1'}
        login_response = self.client.post(
            self.login_url, login_credentials, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.test_token = login_response.data.get("token")
        self.auth_header = 'JWT + {}'.format(self.test_token)

    def test_login_user(self):
        """
        Test if a user logs in successifully
        """
        test_credentials = {'username': 'lauren', 'password': 'password#1'}
        test_response = self.client.post(
            self.login_url, test_credentials, format='json')
        self.assertEqual(test_response.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in test_response.data)

    def test_login_user_wrong_username(self):
        """
        Test if a user logs in with wrong username
        """
        test_credentials = {'username': 'laurey', 'password': 'password#1'}
        test_response = self.client.post(
            self.login_url, test_credentials, format='json')
        self.assertEqual(test_response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertFalse("token" in test_response.data)

    def test_login_user_wrong_password(self):
        """
        Test if a user logs in with wrong password
        """
        test_credentials = {'username': 'lauren', 'password': 'password#'}
        test_response = self.client.post(
            self.login_url, test_credentials, format='json')
        self.assertEqual(test_response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertFalse("token" in test_response.data)

    def test_register_user_success(self):
        """
        Test if a user a user registers successifully
        """
        data = {'username': 'test1', 'email': 'test1@bolon.com',
                'password': 'password#1', 'first_name': 'Test', 'last_name': 'One'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_username_exists(self):
        """
        Test if a user a user registers with existing username
        """
        data = {'username': 'test0', 'email': 'test0@bolon.com',
                'password': 'password#1', 'first_name': 'Test', 'last_name': 'Zero'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_email_exists(self):
        """
        Test if a user a user registers with existing email
        """
        data = {'username': 'test1', 'email': 'test0@bolon.com',
                'password': 'password#1', 'first_name': 'Test', 'last_name': 'One'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_no_username(self):
        """
        Test if a user a user registers without username
        """
        data = {'email': 'test1@bolon.com', 'password': 'password#1',
                'first_name': 'Test', 'last_name': 'One'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_no_email(self):
        """
        Test if a user a user registers without email
        """
        data = {'username': 'test1', 'password': 'password#1',
                'first_name': 'Test', 'last_name': 'One'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_no_password(self):
        """
        Test if a user a user registers without password
        """
        data = {'username': 'test1', 'email': 'test1@bolon.com',
                'first_name': 'Test', 'last_name': 'One'}
        response = self.client.post(
            self.register_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_no_firstname(self):
        """
        Test if a user a user registers successifully
        """
        data = {'username': 'test2', 'email': 'test2@bolon.com',
                'password': 'password#1', 'last_name': 'Two'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_no_lastname(self):
        """
        Test if a user a user registers successifully
        """
        data = {'username': 'test2', 'email': 'test2@bolon.com',
                'password': 'password#1', 'first_name': 'Test'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user(self):
        """
        Test delete a user by id  successfully
        """
        user_url = self.users_url + '2/'
        response = self.client.delete(
            user_url, HTTP_AUTHORIZATION=self.admin_auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user_not_exist(self):
        """
        Test delete a user by id  who doesnt exist
        """
        user_url = self.users_url + '300/'
        response = self.client.delete(
            user_url, HTTP_AUTHORIZATION=self.admin_auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_users(self):
        """
        Test get users
        """
        response = self.client.get(
            self.users_url, HTTP_AUTHORIZATION=self.admin_auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("results" in response.data)

    def test_get_users_unauthorised(self):
        """
        Test get users
        """
        req_response = self.client.get(self.users_url, format='json')
        self.assertEqual(req_response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse("results" in response.data)

    def test_get_user(self):
        """
        Test get a user by id successfully
        """
        user_url = self.users_url + '2/'
        response = self.client.get(
            user_url, HTTP_AUTHORIZATION=self.admin_auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_not_exist(self):
        """
        Test get a user by id  who doesnt exist
        """
        user_url = self.users_url + '300/'
        response = self.client.get(
            user_url, HTTP_AUTHORIZATION=self.admin_auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
