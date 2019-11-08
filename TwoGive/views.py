from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from TwoGive.forms import RenterSignUpForm
from TwoGive.models import Item, Cart


class renterProfileView(TemplateView):
    template_name = 'renterProfile.html'


class customerProfileView(generic.ListView):
    template_name = 'profile.html'
    # initial = {'items': Item.objects.all()}
    model = Item


class myItems(generic.ListView):
    template_name = 'shop.html'
    model = Item


class cartView(generic.ListView):
    template_name = 'cart.html'
    model = Cart


class SignUp(generic.CreateView):
    form_class = RenterSignUpForm
    template_name = 'index.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.set_password(self.request.POST['password'])
        new_user.save()
        login(self.request, new_user)
        return HttpResponseRedirect(reverse('customerprofile'))


class Items(generic.DetailView):
    model = Item
    template_name = 'customerProfile.html'


class ProductDetail(generic.DetailView):
    model = Item
    template_name = 'product-details.html'

    def post(self, request, pk):
        item = self.get_object()
        if request.user.cart_set.get() is not None:
            c = request.user.cart_set.get()
            c.products.add(item)
        else:
            c = Cart.objects.create(user=request.user)
            c.products.add(item)
        return redirect('cartview')


# -------Additional sposob dlya add cart----------------------------------------------->
# def add_to_cart(request, item_id):
#     item = get_object_or_404(Item, pk=item_id)
#     c = request.user.cart_set.get()
#     c.products.add(item)
#     return redirect('cartview')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('signup')
