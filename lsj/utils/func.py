from carts.models import Cart


def manage_cart(request, id):
    user = request.user
    goodsid = request.data['goodsid']
    user_cart = Cart.objects.filter(user=user, goods_id=goodsid).first()
    if user_cart:
        if id == 1:
            user_cart.num += 1
        else:
            user_cart.num -= 1
        user_cart.save()
    else:
        Cart.objects.create(user=user, goods_id=goodsid)
