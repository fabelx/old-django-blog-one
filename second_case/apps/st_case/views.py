from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View

from .forms import TagForm, PostForm
from .models import Tag, Post
from .uttils import ObjectDetaiMixin, ObjectCreateMixin


class PostDetail(ObjectDetaiMixin, View):
    model = Post
    template = 'st_case/post_detail.html'


class TagDetail(ObjectDetaiMixin, View):
    model = Tag
    template = 'st_case/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'st_case/tag_create.html'
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

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'st_case/post_create_form.html'
    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'st_case/post_create_form.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'st_case/post_create_form.html', context={'form': bound_form})

def index(request):
    posts = Post.objects.all()
    return render(request, 'st_case/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'st_case/tags_list.html', context={'tags': tags})
