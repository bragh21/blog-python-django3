from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_list(request):
    object_list = Post.published.all() # Retorna um QuerySet
    paginator = Paginator(object_list, 3) # 3 postagens em cada pagina
    page = request.GET.get('page') # Informa o número da pagina atual
    try:
        posts = paginator.page(page)
        
    except PageNotAnInteger:
        # Se a página não for um inteiro, exibe a primeira página
        posts = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo, 
        # exibe a última página de resultados
        posts = paginator.page(paginator.num_pages)
    
    third_next_page = posts.number + 3 if posts.number + 3 < posts.paginator.num_pages else  posts.paginator.num_pages
    return render(request,
                  'blog/posts/list.html',
                  {'page': page, 'posts': posts, 'pages_range': range(posts.number+1, third_next_page)})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year = year,
                             publish__month = month,
                             publish__day = day)
    return render(request, 
                  'blog/posts/detail.html',
                  {'post': post})
