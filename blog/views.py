from django.shortcuts import render

def posts_list(request):
    return render(request, 'blog/post_list.html',{})
