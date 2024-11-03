from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import *
from .serializer import EmployeeSerializer,LoginSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination


# Create your views here.

def index(request):
     pass
    # return HttpResponse("This is Home Page")


class Employees(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):

        employee_id = request.query_params.get('id')
        print(id)

        if employee_id:
            # If id is provided, fetch the specific employee
            try:
                employee = Employee.objects.get(id=employee_id)
            except Employee.DoesNotExist:
                return Response({
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "Employee with provided ID not found."
                })
            serializer = EmployeeSerializer(employee)
            return Response({
                "status": status.HTTP_200_OK,
                "data": serializer.data,
            })
        else:
            queryset = Employee.objects.all()

            #Filtering by department or role
            department = request.query_params.get('department')
            role = request.query_params.get('role')
            if department:
                queryset = queryset.filter(department=department)
            if role:
                queryset = queryset.filter(role=role)

            # Pagination 
            paginator = PageNumberPagination()
            paginator.page_size = 10  # Define page size 

            # Paginate the queryset
            paginated_queryset = paginator.paginate_queryset(queryset, request, view=self)
        
            # Serialize the paginated data
            serializer = EmployeeSerializer(paginated_queryset, many=True)
            
            return paginator.get_paginated_response({
                "status": status.HTTP_200_OK,
                "data": serializer.data,
            })
             
    def post(sef,request):

        # take data from the testing tools like Postman in this case
        data=request.data
        email = data.get('email')

        serializer=EmployeeSerializer(data=data)

        
        if Employee.objects.filter(email=email).exists():
            return Response({
                'errors': {
                    'status':status.HTTP_400_BAD_REQUEST,
                    'email': ['Employee with this email already exists.']
                }
            })
        
        if not serializer.is_valid():
            return Response({'status':status.HTTP_400_BAD_REQUEST,'errors':serializer.errors})
        
        #save the data into db if serializer is valid
        serializer.save()
        return Response({ 
                "status":status.HTTP_201_CREATED,
                'data':serializer.data,
                'message':"New Data Created"
               })
    
    def put(self,request):
         # Get id from query parameters
        emp_id = request.query_params.get('id')
        
        # Check if id is provided or not
        if not emp_id:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Employee id is required as a query parameter."
            })

        # Check if employee with given id already exists or not if exist then serialize the employee queryset
        try:
            employee = Employee.objects.get(id=emp_id)
        except Employee.DoesNotExist:
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Employee with the given id does not exist."
            })

        # Validate the provided data using the serializer
        serializer = EmployeeSerializer(employee, data=request.data)
        if not serializer.is_valid():
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Complete data is required to update the employee information.'
            })
        
        # Save updated employee data
        serializer.save()
        message = f"Data updated for employee with id {emp_id}"
        
        return Response({
            "status": status.HTTP_200_OK,
            'data': serializer.data,
            'message': message
        })

    def delete(self,request):
        emp_id = request.query_params.get('id')
        
        # Check if id is provided or not
        if not emp_id:
            return Response({
                "message": "Employee id is required as a query parameter.",
                "status": status.HTTP_400_BAD_REQUEST
            })
        
        # Validate if the employee with the given id exists
        if not Employee.objects.filter(id=emp_id).exists():
            return Response({
                "message": "Employee with the given id does not exist.",
                "status": status.HTTP_404_NOT_FOUND
            })

        # Delete the employee
        Employee.objects.get(id=emp_id).delete()
        

        #return the response after successfully deleting of employee
        return Response({
            "status": status.HTTP_204_NO_CONTENT,
            "message": "Employee data has been deleted successfully.",
            "data": {}
        })
         

class LoginApi(APIView):
     def post(self,request):
          
          #take username and password from postman 
          data=request.data
          serializer=LoginSerializer(data=data)

          if not serializer.is_valid():
               return Response({
                    'status':False,
                    "data":serializer.errors
               })
          
          username=serializer.data['username']
          password=serializer.data['password']

          # check user_obj is authenticate or not using authenticate 
          # if user is authenticated then generate unique token
          user_obj=authenticate(username=username,password=password)
          if user_obj:
               token, _ = Token.objects.get_or_create(user= user_obj)
               print(str(token))
               return Response({
               "status":True,
               "data": {"token": str(token)}
                })

          return Response({
               "status":False,
               "data":{},
               "message":"Invalid Credentials"
          })
