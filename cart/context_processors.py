from .views import Cart, ProductCartUser

def cart(request):
    if request.user.id:
        return{'cart': ProductCartUser(request)}

    return {'cart': Cart(request)}