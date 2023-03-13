from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated 


from  .models import Booking,MenuItem
from .serializers import BookingSerializer,MenuItemSerializer,UserSerializer

class BookingViewSet(viewsets.ModelViewSet):
     queryset=Booking.objects.all()
     serializer_class=BookingSerializer



# def index(request):
#     return render(request,'index.html',{})


    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):  
        queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer
        permission_classes=[IsAuthenticated]
        
class MenuItem(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
    permission_classes=[IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
             queryset=User.objects.all()
             serializer_class=UserSerializer
             permission_classes=[IsAuthenticated]
        
            

        
              
              
              

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
      return Response({'message':'This view is protected '})
