from rest_framework import status
from rest_framework.test import APITestCase

class MaintainanceRequestsTests(APITestCase):
    requests_url = '/api/v1/requests/'
    login_url = '/api/v1/auth/signin/'
    register_url = '/api/v1/auth/register/'
    def setUp(self):
        user_data = {'username': 'lauren', 'email':'lauren@bolon.com', 'password':'password#1'}
        self.client.post(self.register_url, user_data, format='json')
        user_data2 = {'username': 'test0', 'email':'test0@bolon.com', 'password':'password#1'}
        self.client.post(self.register_url, user_data2, format='json')
        self.client.login(username='lauren', password='password#1')
        login_credentials = {'username': 'lauren', 'password':'password#1'}
        login_response = self.client.post(self.login_url, login_credentials, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.test_token = login_response.data.get("token")
        self.auth_header=dict(Authorization='JWT ' + self.test_token),
        request_data = {'request_title': 'Test case one', 'request_description':'This is test case one'}
        self.client.post(self.requests_url, data=request_data, headers=self.auth_header, format='json')

    def test_create_maintainance_request(self):
        """
        Make sure a user adds a maintainance request successifully
        """  
        post_data = {'request_title': 'test0', 'request_description':'test0@bolon.com'}
        response = self.client.post(self.requests_url, data=post_data, headers=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_maintainance_request(self):
        """
        Make sure a user deletes a maintainance request by id successifully
        """  
        request_url = self.requests_url + "2/"
        data = {'request_title': 'test0', 'request_description':'test0@bolon.com'}
        self.client.post(self.requests_url, data=data, headers=self.auth_header, format='json')
        response = self.client.delete(request_url, headers=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_maintainance_request_not_exist(self):
        """
        Make sure a user cant delete a maintainance request by id which doesnt exist
        """  
        request_url = self.requests_url + "5/"
        response = self.client.delete(request_url, headers=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_get_maintainance_requests(self):
        """
        Make sure a user gets maintainance requests successifully
        """  
        response = self.client.get(self.requests_url, headers=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_maintainance_request(self):
        """
        Make sure a user gets a maintainance request by id successifully
        """  
        request_url = self.requests_url + "1/"
        data = {'request_title': 'test0', 'request_description':'test0@bolon.com'}
        self.client.post(self.requests_url, data, format='json')
        response = self.client.get(request_url, headers=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_maintainance_request_not_exist(self):
        """
        Make sure a user cant get a maintainance request by id which doesnt exist
        """  
        request_url = self.requests_url + "5/"
        response = self.client.get(request_url, headers=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
