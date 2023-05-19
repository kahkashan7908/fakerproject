from django.shortcuts import render,redirect
import faker
fake=faker.Faker()
from.models import employeeData

#default page
def mainPage(request):
    return render(request,'mainpage.html')

#adding data to database table
def generatingData(request):
    for i in range(50):
        employeeData(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            salary=fake.random_element(elements=(10000,20000,30000,40000)),
            company=fake.random_element(elements=('TCS','Wipro','Infosys','CTS')),
            location=fake.random_element(elements=('Hyderabad','Bangalore','Chennai','Pune')),
            mobile=fake.random_element(elements=(7896543789,8976543289,9876536786,8765498765)),
            email=fake.email(),
            address=fake.address()
        ).save()
    return redirect("fetchingData")

#fetching all employee data in a table
def fetchingData(request):
    data= employeeData.objects.all()
    return render(request,'fetchingdata.html',{'data':data})


def hyderabadData(request):
    #fetching all hyderabad employee data
    if request.method=='GET':
        hydData=employeeData.objects.filter(location='Hyderabad')
        return render(request,'hyderabad.html',{'hydData':hydData})
    else:
        #filltering company wise hyderabad employee data
        company1=request.POST['com']
        hydData=employeeData.objects.filter(location='Hyderabad') & employeeData.objects.filter(company=company1)
        return render(request,'hyderabad.html',{'hydData':hydData})
    
    
#fetching all bangalore employee data and filltering company wise
def bangaloreData(request):
    if request.method=='GET':
        bangData=employeeData.objects.filter(location='Bangalore')
        return render(request,'bangalore.html',{'bangData':bangData})
    else:
        company1=request.POST['com']
        bangData=employeeData.objects.filter(location='Bangalore') & employeeData.objects.filter(company=company1)
        return render(request,'bangalore.html',{'bangData':bangData})

#fetching all chennai employee data and filltering company wise
def chennaiData(request):
    if request.method=='GET':
        cheData=employeeData.objects.filter(location='Chennai')
        return render(request,'chennai.html',{'cheData':cheData})
    else:
        company1=request.POST['com']
        cheData=employeeData.objects.filter(location='Chennai') & employeeData.objects.filter(company=company1)
        return render(request,'chennai.html',{'cheData':cheData})

#fetching all pune employee data and filltering company wise
def puneData(request):
    if request.method=='GET':
        puneData=employeeData.objects.filter(location='Pune')
        return render(request,'pune.html',{'puneData':puneData})
    else:
         company1=request.POST['com']
         puneData=employeeData.objects.filter(location='Pune') & employeeData.objects.filter(company=company1) 
         return render(request,'pune.html',{'puneData':puneData})

    
