from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Dog, Cat
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import DogSerializer, CatSerializer


# Create your views here.


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'dogs_cats/signup.html'


class ProfilePage(TemplateView):
    template_name = 'dogs_cats/profile.html'


class ThanksPage(TemplateView):
    template_name = 'dogs_cats/thanks.html'


class CreateDog(CreateView):
    template_name = 'dogs_cats/create_dog.html'
    model = Dog
    fields = ('name', 'bday')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateDog, self).form_valid(form)


class CreateCat(CreateView):
    template_name = 'dogs_cats/create_cat.html'
    model = Cat
    fields = ('name', 'bday')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateCat, self).form_valid(form)


class ListDog(ListView):
    template_name = 'dogs_cats/list_dog.html'
    model = Dog
    queryset = Dog.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class DetailDog(DetailView):
    template_name = 'dogs_cats/detail_dog.html'
    model = Dog
    context_object_name = 'dogs'


class ListCat(ListView):
    template_name = 'dogs_cats/list_cat.html'
    model = Cat
    queryset = Cat.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class DetailCat(DetailView):
    template_name = 'dogs_cats/detail_cat.html'
    model = Cat
    context_object_name = 'cats'


class UpdateDog(UpdateView):
    template_name = 'dogs_cats/update_dog.html'
    model = Dog
    fields = ('name', 'bday')


class UpdateCat(UpdateView):
    template_name = 'dogs_cats/update_cat.html'
    model = Cat
    fields = ('name', 'bday')


class DeleteDog(DeleteView):
    template_name = 'dogs_cats/delete_dog.html'
    model = Dog
    success_url = reverse_lazy('dogs_cats:list_dog')


class DeleteCat(DeleteView):
    template_name = 'dogs_cats/delete_cat.html'
    model = Cat
    success_url = reverse_lazy('dogs_cats:list_cat')


# DRF
class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def get_queryset(self):
        dog_owner = self.queryset.filter(owner=self.request.user)
        return dog_owner


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def get_queryset(self):
        cat_owner = self.queryset.filter(owner=self.request.user)
        return cat_owner
