from .models import Category

# rend disponible les liens dans tout les templates


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
