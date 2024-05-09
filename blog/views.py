from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .forms import PostSearchForm
from .models import Post


class HomeView(ListView):
    model = Post
    # template_name = 'blog/index.html'
    context_object_name = "posts" # nombre de la variable que pasara los parámetros a la vista
    paginate_by = 10

    def get_queryset(self):
        # Filtrar los posts por estado "Published" o "published"
        return Post.objects.filter(status__iexact="published")

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status__in=["published", "Published"])
    post_related = Post.objects.filter(author=post.author)[:5]  # solo 5 post
    return render(
        request, "blog/single.html", {"post": post, "post_related": post_related}
    )

# Para pasar múltiples opciones de estado en la consulta de un objeto Post, puedes utilizar el operador in en Python.


class TagListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(tags__name__in=[self.kwargs["tag"]])

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements-tags.html"
        return "blog/tags.html"

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs["tag"]
        return context


class PostSearchView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = "posts"
    form_class = PostSearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Post.objects.filter(title__icontains=form.cleaned_data["s"])
        return []

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements-search.html"
        return "blog/search.html"
