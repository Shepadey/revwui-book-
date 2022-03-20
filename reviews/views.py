from reviews.forms import ReviewForm


from reviews.forms import ReviewForm
from django.shortcuts import render
from django.shortcuts import redirect
def reviews(request):
    if request.method=="GET":
        form=ReviewForm()
        return render(request,"reviews.html",{'form':form})
    elif request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            name=data.get('name')
            email=data.get('email')
            review=data.get('reveiw')
            rating=data.get('rating')
            print(data)
            with open ('data.csv','a') as file:
                file.write(f'{name}|{email}|{review}|{rating}\n')
            return redirect('reviews')
        else:
            form=ReviewForm()
            return render(request,'reviews.html',{'form':form})
    form=ReviewForm()
    name_1=request.GET.get('name')
    email_1=request.GET.get('email')
    review_1=request.GET.get('review')
    return render(request,'reviews.html',{'name_1':name_1,'email_1':email_1,'review_1':review_1,'form':form})
# Create your views here.
