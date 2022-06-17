from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cities, Profile
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, AbstractUser


def index(request):
    if request.method == "POST":
        today = datetime.now()
        today = today.strftime('%Y-%m-%d')
        today = datetime.strptime(today, '%Y-%m-%d')
        # extracts user choices from the form
        travelmode = request.POST.get("travelmode")
        source = request.POST.get("source")
        km = request.POST.get("destination")
        start_date = request.POST.get("start_date")
        return_date = request.POST.get("return_date")
        start_date = datetime(int(start_date[:4]), int(
            start_date[5:7]), int(start_date[8:]))
        if return_date:
            return_date = datetime(int(return_date[:4]), int(
                return_date[5:7]), int(return_date[8:]))
        else:
            return_date = start_date

        request.session['travelmode'] = travelmode

        # check if dates are correct
        if start_date < today or return_date < start_date:
            msg = "Error: Please enter correct dates"
            cities = Cities.objects.all()
            context = {'cities': cities, 'msg': msg}
            return render(request, 'index.html', context)

        if travelmode == "roundtrip":
            delta = return_date-start_date
            days = delta.days+1
            request.session['km'] = km
            request.session['days'] = days
        return redirect('carsearch')

    else:
        cities = Cities.objects.all()
        context = {'cities': cities}
        return render(request, 'index.html', context)


def carsearch(request):
    if request.method == "POST":
        driverrate = int(request.POST.get("driverrate"))
        language = request.POST.get("language")
        manufacturer = request.POST.get("manufacturer")
        if request.session['travelmode'] == 'roundtrip':
            try:
                km = int(request.session['km'])
                days = int(request.session['days'])
            except:
                return redirect('index')

            if km < 5:
                km = 5
            # calculates cost of travel
            price = (km*driverrate*2)+(days*25)
            request.session['price'] = str(price)
            try:
                del request.session['km']
                del request.session['days']
                request.session.modified = True
            except:
                pass
            return redirect('info')

        if request.session['travelmode'] == 'airport':
            request.session['price'] = "15"
            return redirect('info')
    else:
        return render(request, "carsearch.html")


@login_required
def info(request):
    if request.method == "POST":
        name = request.POST.get("name")
        pickup = request.POST.get("pickup")
        time = request.POST.get("time")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        price = request.session['price']
        context = {'name': name, 'pickup': pickup,
                   'phone': phone, 'email': email, 'price': price}
        return render(request, "invoice.html", context)

    else:
        try:
            price = request.session['price']
        except:
            return redirect('index')
        # retrieves saved user info
        username = request.user.username
        user = User.objects.get(username=username)
        fullname = user.first_name+' '+user.last_name
        email = user.email
        phone = user.profile.phone
        context = {'name': fullname, 'email': email, 'phone': phone}
        return render(request, "info.html", context)


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() or Profile.objects.filter(phone=phone).exists():
            context = {'msg': "User exists, Please Login"}
            return render(request, 'signup.html', context)
        else:
            u = User(username=username, first_name=first_name,
                     last_name=last_name, email=email)
            u.set_password(password)
            u.save()
            p = Profile(user=u, phone=phone)
            p.save()
            user = authenticate(username=username, password=password)
            login(request, user)

        if 'price' in request.session:
            return redirect('info')
        elif 'km' in request.session:
            return redirect('carsearch')
        else:
            return redirect('index')

    else:
        return render(request, 'signup.html')
