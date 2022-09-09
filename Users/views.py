from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
import datetime


######### Add (signup)  Users api  ######### 

class signup__api(APIView):
    def get(self,request):
        f1=serializers.create_user_form()
        return Response({**f1.data,
                            },status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        f1=serializers.create_user_form(data=request.POST)
        if f1.is_valid():
            
            check_list = list(models.User.objects.filter((Q(username=request.POST['username'])|Q(email=request.POST['email']))))
            if check_list != []:
                for i in check_list:
                    if i.username==request.POST['username']:
                        return Response({'success':'false',
                                        'error_msg':'This User_Name already exists',
                                        'errors':{},
                                        'response':{},
                                        },status=status.HTTP_400_BAD_REQUEST)
                    elif i.email==request.POST['email']:
                        return Response({'success':'false',
                                        'error_msg':'This email already exists',
                                        'errors':{},
                                        'response':{},
                                        },status=status.HTTP_400_BAD_REQUEST)
            
            uzr=models.User()
            uzr.username=request.POST['username']
            uzr.email=request.POST['email']
            uzr.signup_date=datetime.datetime.strptime(request.POST['signup_date'], '%Y-%m-%dT%H:%M:%S')
            uzr.save()
            return Response({'success':'True',
                            'error_msg':'',
                            'errors':{},
                            'response':'Registration sucessfully',
                            },status=status.HTTP_200_OK)
            
        else:
            return Response({'success':'false',
                                'error_msg':'',
                                'errors':'',
                                'response':{},
                                },status=status.HTTP_400_BAD_REQUEST)

class Users_profile(APIView):
    def get(self,request):
        f1=serializers.users_profile()

        return Response({**f1.data,
                            },status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        
        hello=list(models.User.objects.filter(id=request.POST['user']))
        print(hello)
        if hello==[]:
                return Response({'success':'false',
                                    'error_msg':'invalid user id',
                                    'errors':{},
                                    'response':{},
                                    },status=status.HTTP_400_BAD_REQUEST)
        check_list = list(models.User_profile.objects.filter(user=request.POST['user']))
        print(check_list)
    
        if check_list == []:  
            
            f1=serializers.users_profile(data=request.POST)
            if f1.is_valid():    
                f1.save()
                    
                return Response({'success':'True',
                                        'error_msg':'',
                                        'errors':{},
                                        'response':'User profile save sucessfully',
                                        },status=status.HTTP_200_OK)
                
            else:
                return Response({'success':'false',
                                    'error_msg':'',
                                    'errors':'',
                                    'response':{},
                                    },status=status.HTTP_400_BAD_REQUEST)
        return Response({'success':'false',
                                'error_msg':'This User already exists',
                                'errors':{},
                                'response':{},
                                },status=status.HTTP_400_BAD_REQUEST)

######### get all users Api   ######### 

class get_all_user_api(APIView):
    def get(self,request):
        S_T=list(models.User_profile.objects.all())
        return Response({'success':'true',
                    'error_msg':'',
                    'errors':{},
                    'response':{'All_users_Details':serializers.get_all_users(S_T,many=True).data},
                    },status=status.HTTP_202_ACCEPTED)