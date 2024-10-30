from django.shortcuts import render, get_object_or_404, redirect
from decimal import Decimal
from board.models import Post
from my_billboard.settings import FAVOURITES_SESSION_ID


class Favourites:
    def __init__(self, request):
        # получаем текущую сессию
        self.session = request.session
        # получаем текущего пользователя
        self.user = request.user
        # получаем корзину из сессии или создаем новую
        favourites = self.session.get(FAVOURITES_SESSION_ID)
        # создаем новую корзину
        if not favourites:
            favourites = self.session[FAVOURITES_SESSION_ID] = {}
        self.favourites = favourites

    # сохранение изменений в сессию
    def save(self):
        self.session.modified = True

    # метод помещения товара в корзину
    def add(self, post):
        # получаем id товара из ОБЪЕКТА товара
        post_id = str(post.id)
        # проверка есть-ли этот пост в избранном ????
        if post_id not in self.favourites:
            self.favourites[post_id] = {
                'post': str(post.title)
            }

        self.save()

    # удаление товара из корзины
    # def remove(self, product):
    #     product_id = str(product.id)
    #     if product_id in self.cart:
    #         del self.cart[product_id]
    #         self.save()

    # метод подсчета общего количества элементов в корзине
    # def __len__(self):
    #     return sum(item['quantity'] for item in self.cart.values())
        # return len(self.cart) - количество товаров в корзине

    # def get_total_price(self):
    #     return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    # def clear(self):
    #     self.cart.clear()
    #     # del self.session[CART_SESSION_ID]
    #     self.save()

    # def prod_id_str(self):
    #     return self.cart[]

    def __iter__(self):
        post_ids = self.favourites.keys()
        posts = Post.objects.filter(id__in=post_ids)
        favourites = self.favourites.copy()

        for post in posts:
            favourites[str(post.id)]['post'] = post

        # for item in favourites.values():
        #     item['price'] = Decimal(item['price'])
        #     item['total_price'] = item['price'] * item['quantity']
        #     yield item


def favourites_add(request, slug):
    # создаем корзину (получаем из сессии)
    favourites = Favourites(request)

    post = get_object_or_404(Post, slug=slug)
    favourites.add(post=post)

    return redirect('index')


def favourites_detail(request):
    favourites = Favourites(request)
    return render(request, template_name='favourites/favourites_detail.html', context={'favourites': favourites})
