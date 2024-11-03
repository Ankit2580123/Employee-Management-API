from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.authtoken.models import Token

class EmployeeTests(APITestCase):
    def setUp(self):
        # Create a test user and generate a token for authentication
        self.user = User.objects.create_user(username='rajat', password='rajat@123')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create a sample employee for testing purposes
        self.employee = Employee.objects.create(
                name= "Ankit Kumar",
                email="ankitkumar2580123@gmail.com",
                department="Engineering",
                role= "Developer"

        )
        self.employee_url = reverse('employees')
    
    def test_get_employee_list(self):
        response = self.client.get(self.employee_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.data['results'])

    def test_get_employee_by_id(self):
        response = self.client.get(self.employee_url, {'id': self.employee.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], self.employee.name)


    # def test_create_employee_with_existing_email(self):
    #     data = {
    #         'name': 'Another John',
    #         'email': 'raj3@gmail.com',  # existing email
    #         'department': 'Engineering',
    #         'role': 'Analyst'
    #     }
    #     response = self.client.post(self.employee_url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn('email', response.data['message'])
    
    def test_update_employee(self):
        data = {
            'name': 'John Doe Updated',
            'email': 'john.doe@example.com',
            'department': 'Engineering',
            'role': 'Lead Developer'
        }
        response = self.client.put(self.employee_url + f"?id={self.employee.id}", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], data['name'])
    
 
    
    # def test_delete_employee(self):
    #     response = self.client.delete(self.employee_url + f"?id={self.employee.id}")
    #     print(response.status_code)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_delete_nonexistent_employee(self):
#         response = self.client.delete(self.employee_url + "?id=999")
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#         self.assertEqual(response.data['message'], "Employee with the given id does not exist.")

