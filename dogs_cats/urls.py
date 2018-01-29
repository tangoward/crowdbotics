
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers

app_name = 'dogs_cats'

# api router
router = routers.DefaultRouter()
router.register('dogs', views.DogViewSet)
router.register('cats', views.CatViewSet)


urlpatterns = [
    path('', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='dogs_cats/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfilePage.as_view(), name='profile'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('create_dog/', views.CreateDog.as_view(), name='create_dog'),
    path('create_cat/', views.CreateCat.as_view(), name='create_cat'),
    path('list_dog/', views.ListDog.as_view(), name='list_dog'),
    path('list_dog/<int:pk>', views.DetailDog.as_view(), name='detail_dog'),
    path('list_cat/', views.ListCat.as_view(), name='list_cat'),
    path('list_cat/<int:pk>', views.DetailCat.as_view(), name='detail_cat'),
    path('update_dog/<int:pk>', views.UpdateDog.as_view(), name='update_dog'),
    path('update_cat/<int:pk>', views.UpdateCat.as_view(), name='update_cat'),
    path('delete_dog/<int:pk>', views.DeleteDog.as_view(), name='delete_dog'),
    path('delete_cat/<int:pk>', views.DeleteCat.as_view(), name='delete_cat'),
    path('api/', include(router.urls))
]
