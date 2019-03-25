from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient


class MaintainanceRequestsTests(APITestCase):
    requests_url = '/api/v1/requests/'
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
        request_data = {'request_title': 'Test case one',
                        'comment': 'testcomment', 'request_description': 'This is test case one'}

        self.status = {"status": "rejected"}
        self.client.post(self.register_url, user_data, format='json') 
        self.client.post(self.register_url, user_data2, format='json')
        login_credentials = {'username': 'lauren', 'password': 'password#1'}
        login_response = self.client.post(
            self.login_url, login_credentials, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.test_token = login_response.data.get("token")
        self.auth_header = 'JWT {}'.format(self.test_token)
        self.client.post(self.requests_url, data=request_data,
                         HTTP_AUTHORIZATION=self.auth_header, format='json')

    def test_create_maintainance_request(self):
        """
        Make sure a user adds a maintainance request successifully
        """
        post_data = {'request_title': 'test0', 'comment': 'testcomment',
                     'request_description': 'test0@bolon.com'}
        
        client = APIClient(enforce_csrf_checks=True)
        response = client.post(self.requests_url, post_data, HTTP_AUTHORIZATION=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_maintainance_request(self):
        """
        Make sure a user deletes a maintainance request by id successifully
        """
        request_url = self.requests_url + "2/"
        data = {'request_title': 'test0', 'comment': 'testcomment',
                'request_description': 'test0@bolon.com'}
        self.client.post(self.requests_url, data=data,
                         HTTP_AUTHORIZATION=self.auth_header, format='json')
        response = self.client.delete(
            request_url, HTTP_AUTHORIZATION=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_maintainance_request_not_exist(self):
        """
        Make sure a user cant delete a maintainance request by id which doesnt exist
        """
        request_url = self.requests_url + "5/"
        response = self.client.delete(
            request_url, HTTP_AUTHORIZATION=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_maintainance_requests(self):
        """
        Make sure a user gets maintainance requests successifully
        """
        response = self.client.get(
            self.requests_url, HTTP_AUTHORIZATION=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_maintainance_request(self):
        """
        Make sure a user gets a maintainance request by id successifully
        """
        request_url = self.requests_url + "1/"
        data = {'request_title': 'test0', 'comment': 'testcomment',
                'request_description': 'test0@bolon.com'}
        self.client.post(self.requests_url, data, format='json')
        response = self.client.get(
            request_url, HTTP_AUTHORIZATION=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_maintainance_request_not_exist(self):
        """
        Make sure a user cant get a maintainance request by id which doesnt exist
        """
        request_url = self.requests_url + "5/"
        response = self.client.get(
            request_url, HTTP_AUTHORIZATION=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_status(self):
        """
        superuser updates status
        """
        request_url = self.requests_url + "1/"
        post_data = {'request_title': 'test0', 'comment': 'testcomment',
                     'request_description': 'test0@bolon.com'}
        self.client.post(
            self.requests_url, data=post_data, HTTP_AUTHORIZATION=self.auth_header, format='json')
        response = self.client.patch(
            request_url, data=self.status, HTTP_AUTHORIZATION=self.admin_auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_status_doesnot_exist(self):
        """
        superuser updates status of request that doenot exist
        """
        request_url = self.requests_url + "10/"
        response = self.client.patch(
            request_url, data=self.status, HTTP_AUTHORIZATION=self.admin_auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_invalid_status(self):
        """ 
        tests update with invalid status
        """
        invalid_status = {"status":"good"}
        request_url = self.requests_url + "1/"
        post_data = {'request_title': 'test0', 'comment': 'testcomment',
                     'request_description': 'test0@bolon.com'}
        self.client.post(
            self.requests_url, data=post_data, HTTP_AUTHORIZATION=self.auth_header, format='json')
        response = self.client.patch(
            request_url, data=invalid_status, HTTP_AUTHORIZATION=self.admin_auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


