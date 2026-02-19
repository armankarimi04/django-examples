from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def provide_user_info_partial(request):
    user_id = request.GET.get('user_id')
    author1 = {
        'username': 'a1',
        'name': 'AuthorName1',
        'bio': "First author."
    }
    author2 = {
        'username': 'a2',
        'name': 'AuthorName2',
        'bio': "Second author."
    }
    author3 = {
        'username': 'a3',
        'name': 'AuthorName3',
        'bio': "Third author."
    }
    
    authors = {
        '1': author1,
        '2': author2,
        '3': author3
    }
    
    user = authors.get(user_id)
    return render(request, 'main/partials/authors.html#user-info', {'user': user})