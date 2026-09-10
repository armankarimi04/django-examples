from typing import Generator
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.loader import render_to_string
from django.middleware.csrf import get_token
from datastar_py.django import (
    read_signals,
    DatastarResponse,
    ServerSentEventGenerator as SSE
)
from datastar_py import consts
from datastar_py.sse import DatastarEvent
from .models import Film
from .forms import FilmForm


def index(request: HttpRequest) -> HttpResponse | DatastarResponse:
    # provide artificial latency with time.sleep() to test the loading indicator
    films = Film.objects.all()
    paginator = Paginator(films, 5)
    page_number = request.GET.get('page', 1)
    signals = read_signals(request)
    print("index view ->", signals)
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


def provide_new_film_form(request: HttpRequest) -> HttpResponse | DatastarResponse:
    csrf_token_value = get_token(request)
    signals = read_signals(request)
    print("provide form view ->", signals)
    context = {}
    context['csrf_token'] = csrf_token_value
    if 'Datastar-Request' in request.headers:
        def datastar_response():
            html = render_to_string("main/partials/new-film-form.html", context)
            yield SSE.patch_elements(
                elements=html,
                mode=consts.ElementPatchMode.INNER,
                selector="#modal-box-body"
            )
            
        return DatastarResponse(content=datastar_response())
    return render(request, "main/partials/new-film-form.html")


def new_film(request: HttpRequest) -> HttpResponse | DatastarResponse | Generator[DatastarEvent]:
    if request.method == "POST":
        form = FilmForm(request.POST)
        signals = read_signals(request)
        print("new film submit ->", signals)
        if form.is_valid():
            form.save()
            if 'Datastar-Request' in request.headers:
                def datastar_response():
                    html = render_to_string("main/partials/message.html", {'message': "success"})
                    yield SSE.patch_elements(
                        elements=html,
                        mode=consts.ElementPatchMode.INNER,
                        selector="#modal-box-body"
                    )
                    
                return DatastarResponse(content=datastar_response())
        else:
            for error in form.errors:
                print("\n", error, "\n")
            return HttpResponse("Form Error")
    return HttpResponse("OK")


# not fixed yet
def provide_films(request: HttpRequest) -> Generator[DatastarEvent]:
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
                mode=consts.ElementPatchMode.REPLACE,
                selector="#movie-table-body"
            )
            yield SSE.patch_signals(signals={'page': page_number})
        return DatastarResponse(content=datastar_response())
        