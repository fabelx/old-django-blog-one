from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TagForm, PostForm
from .models import Tag, Post
from .uttils import ObjectDetaiMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin


class PostDetail(ObjectDetaiMixin, View):
    model = Post
    template = 'st_case/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'st_case/post_create_form.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'st_case/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'st_case/post_delete_form.html'
    redirect_url = 'post_list_url'
    raise_exception = True


class TagDetail(ObjectDetaiMixin, View):
    model = Tag
    template = 'st_case/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'st_case/tag_create.html'
    raise_exception = True
    # def get(self, request):
    #     form = TagForm()
    #     return render(request, 'st_case/tag_create.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST)
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'st_case/tag_create.html', context={'form': bound_form})


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'st_case/tag_update_form.html'
    raise_exception = True
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'st_case/tag_update_form.html', context={'form': bound_form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'st_case/tag_update_form.html', context={'form': bound_form, 'tag': tag})


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'st_case/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'st_case/tag_delete_form.html', context={'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tags_list_url'))


def index(request):
    posts = Post.objects.all()
    return render(request, 'st_case/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'st_case/tags_list.html', context={'tags': tags})
