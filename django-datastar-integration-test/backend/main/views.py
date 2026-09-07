from django.shortcuts import render
from django.core.paginator import Paginator
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.loader import render_to_string
from datastar_py.django import (
    read_signals,
    DatastarResponse, 
    ServerSentEventGenerator as SSE
)
from datastar_py import consts
from .models import Film


def index(request: HttpRequest) -> HttpResponse | DatastarResponse:
    import time
    time.sleep(0.5)
    films = Film.objects.all()
    paginator = Paginator(films, 5)
    page_number = request.GET.get('page', 1)
    signals = read_signals(request)
    if signals is None:
        page_number = 1
    else:
        page_number = signals['page'] + 1
    page_obj = paginator.get_page(page_number)
    context = {'film_page': page_obj}
    
    if 'Datastar-Request' in request.headers:
        def datastar_response():
            html = render_to_string("main/partials/table-rows.html", context)
            yield SSE.patch_elements(
                elements=html,
                mode=consts.ElementPatchMode.APPEND,
                selector="#movie-table-body"
            )
            
            yield SSE.patch_signals(signals={'page': page_number})

            if not page_obj.has_next():
                yield SSE.remove_elements(selector='#more-films-btn')
                
        return DatastarResponse(content=datastar_response())   
    return render(request, "main/index.html", context)
