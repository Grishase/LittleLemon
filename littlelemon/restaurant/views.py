from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request,dish):
#     items={
#         'falafel':"Falafel is a deep-fried ball or patty-shaped fritter in Middle Eastern cuisine made from ground chickpeas, broad beans, or both. "
#     }
#     description=items[dish]
#     return HttpResponse('<h2> {dish} </h2>',description)
def index(request):
    return render(request,'index.html',{})