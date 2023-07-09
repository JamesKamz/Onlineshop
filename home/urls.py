from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from home.views import CategoryViewset, ProductViewset, ArticleViewset

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:id>', views.detail, name='detail'),
    path('about/', views.AboutusView, name='about'),
    path('contact/', views.ContactusView, name='contact'),
    path('product/', views.ProductViewset, name='product'),
    path('category/', views.CategoryViewset, name='categories'),
    path('category/<str:id>', views.categorydetail, name='categorydetail'),   
    path('blog/', ArticleViewset.as_view(), name='post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
