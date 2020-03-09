from django.shortcuts import render, HttpResponse, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View
from .models import Tag, Post
from .forms import TagForm
from .uttils import ObjectDetaiMixin


class PostDetail(ObjectDetaiMixin, View):
    model = Post
    template = 'st_case/post_detail.html'


class TagDetail(ObjectDetaiMixin, View):
    model = Tag
    template = 'st_case/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'st_case/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'st_case/tag_create.html', context={'form': bound_form})

def index(request):
    posts = Post.objects.all()
    return render(request, 'st_case/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'st_case/tags_list.html', context={'tags': tags})
