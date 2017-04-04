from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import generic
from .models import Plant, RatingPlant, PlantSize, UserProfile, Cart, Order
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from .forms import UserForm, LoginForm, ProfileForm
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import timezone
import json
from django.db.models import Q


class AllPlantsView(generic.ListView):
    model = Plant
    template_name = 'firstone/plantlist.html'
    context_object_name = 'plants'

    def get_context_data(self, **kwargs):
        atallplants = True

        context = super(AllPlantsView, self).get_context_data(**kwargs)
        context['atallplants'] = atallplants
        return context


def home(request):
    athome = True
    plants = Plant.objects.all()

    context = {'athome': athome, 'plants': plants}
    return render(request, 'firstone/home.html', context)


def search(request):
    plant = Plant.objects.all()
    query = request.GET['query']
    if query:
        plant = plant.filter(name__icontains=query)
        context = {'plant': plant}
        return render(request, 'firstone/search.html', context)
    else:
        return redirect('firstone:allPlants')


def detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    rating_of_plant = plant.plantsize_set.all()
    user = request.user

    if request.POST:
        rev = request.POST['rev']
        reviewtime = timezone.now()
        kk = plant.ratingplant_set.create(review=rev, foruser=user, reviewtime=reviewtime)
        kk.save()
        messages.add_message(request, messages.INFO, "Review Successfully Written !")
        return HttpResponseRedirect(plant.get_absolute_url())
    context = {'plant': plant, 'ratingofplant': rating_of_plant, }
    return render(request, 'firstone/detail.html', context, )


def cart(request):
    atcart = True
    user = request.user
    ca = user.cart_set.all()

    allids = []
    allplants = []

    if 'delbutt' in request.POST:
        cd = ca.get(pk=request.POST['delbutt'])

        cd.delete()
        return HttpResponseRedirect(reverse('firstone:cart'))
    elif 'plantid' in request.POST:

        plantid = request.POST['plantid']
        try:
            choice = request.POST['choice']
        except MultiValueDictKeyError:
            choice = False
            messages.add_message(request, messages.INFO, 'Please select size of plant !')
            return redirect('firstone:detail', pk=plantid)
        pl = get_object_or_404(Plant, pk=plantid)

        ps = pl.plantsize_set.get(pk=choice)

        kk = user.cart_set.create(plantid=plantid, price=ps.price, size=ps.size, photo=pl.image1)
        kk.save()

    # if request.POST:
    #     if 'delbutt'
    #
    #     if request.POST['delbutt']:
    #         cd=ca.get(pk=request.POST['delbutt'])
    #         print(cd.price)
    #         cd.delete()
    #     else:
    #         plantid = request.POST['plantid']
    #         try:
    #             choice = request.POST['choice']
    #         except MultiValueDictKeyError:
    #             choice = False
    #             messages.add_message(request, messages.INFO, 'Please select size of plant !')
    #             return redirect('firstone:detail', pk=plantid)
    #         pl = get_object_or_404(Plant, pk=plantid)
    #
    #         ps = pl.plantsize_set.get(pk=choice)
    #
    #         kk = user.cart_set.create(plantid=plantid, price=ps.price, size=ps.size, photo=pl.image1)
    #         kk.save()


    total = 0
    tot = []

    plant = Plant.objects.all()
    for indprice in ca:
        tot.append(indprice.price)

    for i in tot:
        total += i

    if total == 0:
        messages.add_message(request, messages.INFO, "Your cart is Empty !")
    # get plant objects with cart ids

    allcarts = []
    for i in ca:
        allids.append(i.plantid)
        allcarts.append(i)
        for j in plant:
            if j.pk == i.plantid:
                allplants.append(j)

    mix = zip(allcarts, allplants)
    mix = list(mix)
    ids = []
    for i in allcarts:
        ids.append(allcarts)

    cartids = []
    for i in allcarts:
        cartids.append(i.id)
    try:

        context = {'cart': ca, 'mix': mix, 'plant': pl, 'sizeprice': ps, 'atcart': atcart, 'total': total}
        return HttpResponseRedirect(reverse('firstone:cart'))
    except:
        pass
    context = {'cart': ca, 'mix': mix, 'atcart': atcart, 'total': total, 'cartids': cartids, }
    return render(request, 'firstone/cart.html', context)


class PlantCreatesizeandprice(CreateView):
    model = PlantSize
    template_name = 'firstone/plantsize_form.html'
    fields = ['size', 'price']


def user_logo(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.INFO, "Successfully Logged Out")
        return render(request, 'firstone/home.html')
    else:
        messages.add_message(request, messages.INFO, "You were not logged in.")
        return render(request, 'firstone/home.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'firstone/registration_form.html'
    atregister = True

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'atregister': self.atregister})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('firstone:allPlants')
        return render(request, self.template_name, {'form': form})


# class LoginFormView(View):
#     form_class = LoginForm
#     template_name = 'firstone/login.html'
#     atlogin = True
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form, 'atlogin': self.atlogin})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             username = request.POST['username']
#             password = request.POST['password']
#             user.set_password(password)
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 print("user there, but not active")
#                 if user.is_active:
#
#                     login(request, user)
#                     print("yes")
#                     messages.add_message(request, messages.INFO, "Logged In")
#                     return redirect('firstone:allPlants')
#                 else:
#                     print("user not active")
#             else:
#                 print("User not authenticated")
#                 messages.add_message(request, messages.INFO, "Wrong Username or Password.")
#         print("does noting")
#         return render(request, self.template_name, {'form': form})
def user_login(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}

    if request.POST:

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:

            if user.is_active:
                login(request, user)
                messages.add_message(request, messages.INFO, 'Successfully Logged in !')
                return redirect('firstone:allPlants')

    return render(request, 'firstone/login.html', context)


def ordersubmit(request):
    form = ProfileForm(request.POST or None)
    context = {'form': form}
    user = request.user
    usercart = user.cart_set.all()
    tot = 0
    for i in usercart:
        tot = tot + i.price
    delcharge = 0
    if tot <1000:
        delcharge = (0.1)*tot
    else:
        delcharge=0

    tbp = int(tot + delcharge)
    if 'cart' in request.POST:
        total = request.POST['total']

        context = {'form': form, 'total': total, 'usercart': usercart,'tbp':tbp,'delcharge':delcharge}
        return render(request, 'firstone/ordersubmit.html', context)

    return render(request, 'firstone/ordersubmit.html', {'form': form})


def confirmedorder(request):
    form = ProfileForm(request.POST or None)
    plantname = Plant.objects.all()
    context = {'form': form}
    user = request.user
    usercart = user.cart_set.all()
    plids = []
    plantn = []
    ppsize = []
    total = 0
    for i in usercart:
        plids.append(i.plantid)
        ppsize.append(i.size)
        total = total + i.price
    for i in plids:
        plantn.append(plantname.get(pk=i))

    ppname = []

    for i in plantn:
        ppname.append(i.name)
    delcharges = 0
    if total < 1000:
        delcharges = (0.1) * total
    else:
        delcharges = 0

    atbp = int(total + delcharges)

    if request.POST:
        if form.is_valid():
            address = request.POST['address']
            phonenumber = request.POST['phone']
            ot = timezone.now()
            pname = json.dumps(ppname)
            psize = json.dumps(ppsize)
            neworder = user.order_set.create(address=address, phone=phonenumber, username=user.username, plnames=pname,
                                             plantsizes=psize, total=atbp,ordertime=ot,status='new')
            neworder.save()
            usercart.delete()
            context = {'add': address, 'phone': phonenumber, 'pname': ppname, 'psize': psize,
                       'total': atbp , 'neworder':neworder}

            return render(request, 'firstone/confirmorder.html', context)

        else:
            messages.add_message(request, messages.INFO, "Wrong address or Phone Number.")
            return render(request, 'firstone/ordersubmit.html', context)
    return HttpResponseRedirect('firstone:allPlants')
def comingsoon(request):
    return render(request,'firstone/comingsoon.html')

def vendororder(request):
    orders = Order.objects.all()
    tbdorders = Order.objects.filter(Q(status='new')|Q(status='confirmed'))

    atorders = True

    if 'confirm' in request.POST:
        orderid = request.POST['orderid']
        ord = orders.get(pk=orderid)
        ord.status = 'confirmed'
        ord.save()
        return redirect('firstone:vendororder')
    if 'cancel' in request.POST:
        orderid = request.POST['orderid']
        ord = orders.get(pk=orderid)
        ord.status = 'cancelled'
        ord.save()
        return redirect('firstone:vendororder')
    if 'deliver' in request.POST:
        orderid = request.POST['orderid']
        ord = orders.get(pk=orderid)
        ord.status = 'delivered'
        ord.save()
        return redirect('firstone:vendororder')
    context={'orders':tbdorders, 'atorders':atorders}
    return render(request,'firstone/vendororder.html',context)

def previousorders(request):
    atprevorders = True
    orders = Order.objects.all()
    prevorders = Order.objects.filter(Q(status='delivered')|Q(status='cancelled'))
    context = {'orders': prevorders, 'atprevorders': atprevorders }
    return render(request,'firstone/vendorpreviousorders.html',context)

def myorders(request):
    atmyorders = True
    user = request.user
    myorder = user.order_set.all()
    context = {'orders':myorder,'atmyorders':atmyorders}
    return render(request,'firstone/myorders.html',context)