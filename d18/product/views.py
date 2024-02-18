from django.shortcuts import render

def index(request):
    context ={

            'title': 'магааааааааз'
        }

    return render(request, 'index.html', context = context)


def products(request):
    context = {
        'products' : [
            {'image':'/static/vendor/img/products/Adidas-hoodie.png',
            'name':'ivwue',
            'price':'45692340562346582374776411326490',
            'description':'сасен'},

            {'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
            'name': 'uwfepov',
            'price':'45692340562346582374776411326490',
            'description': 'сасен'},

            {'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
            'name': 'auhcfpso',
            'price':'45692340562346582374776411326490',
            'description': 'сасен'},

            {'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
            'name': 'qufoajic',
            'price':'45692340562346582374776411326490',
            'description': 'сасен'},

            {'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
            'name': 'atydiui',
            'price':'45692340562346582374776411326490',
            'description': 'сасен'},

            {'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
            'name': 'asdyoiujio',
            'price':'45692340562346582374776411326490',
            'description': 'сасен'},
    ]
    }
    return render(request, 'products.html', context = context)
