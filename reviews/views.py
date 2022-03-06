from reviews.forms import ReviewForm


from reviews.forms import ReviewForm
from django.shortcuts import render
def reviews(request):
    form=ReviewForm()
    name_1=request.GET.get('name')
    email_1=request.GET.get('email')
    review_1=request.GET.get('review')
    return render(request,'reviews.html',{'name_1':name_1,'email_1':email_1,'review_1':review_1,'form':form})
# Create your views here.
