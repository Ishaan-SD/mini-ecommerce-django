from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, OrderItem, Order
from .forms import ProductForm, OrderItemForm
from django.contrib.auth.decorators import login_required


from django.core.paginator import Paginator
# Create your views here.

# list all the products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', context={'products':products}) 


# @login_required
# def add_to_cart(request, order_id):
#     order = get_object_or_404(Order, id=order_id, user=request.user)
#     if request.method == 'POST':
#         form = OrderItemForm(request.POST)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.order = order
#             item.save()
#             order.update_total()
#             order.save()
#             return redirect('product_list')
#     else:
#         form = OrderItemForm()
#     return render(request, 'store/add_to_cart.html', {'form':form, 'order':order})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product':product})