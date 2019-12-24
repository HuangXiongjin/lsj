from carts.models import Cart


def manage_cart(request, id):
    """添加商品和删除商品"""
    user = request.user
    goodsid = request.data['goodsid']
    user_cart = Cart.objects.filter(user=user, goods_id=goodsid).first()
    if user_cart:
        if id == 1:
            user_cart.num += 1
            user_cart.save()
        if id == 0:
            if user_cart.num == 1:
                user_cart.delete()
            else:
                user_cart.num -= 1
                user_cart.save()
    else:
        Cart.objects.create(user=user, goods_id=goodsid)
