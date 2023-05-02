from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Paga implementar a paginação
from django.views.generic import ListView

# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts' # se não especificar nada, o contexto se chamada "object_list"
    paginate_by = 3 # Quantos posts por página
    template_name = 'blog/posts/list.html'
    # Por termos criado o atributo 'paginate_by', o django irá criar um paginador, e retornará 
    # nas variavies de contexto, a variavel page_obj, contendo os dados da pagina atual
    # gerados pelo paginador.

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year = year,
                             publish__month = month,
                             publish__day = day)
    return render(request, 
                  'blog/posts/detail.html',
                  {'post': post})
