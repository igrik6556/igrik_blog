import json
from django.shortcuts import render
from django.http import Http404, HttpResponse
from pass_generator.forms import GeneratorForm
from pass_generator.models import Generator


def generator_main(request):
    return render(request,
                  'pass_generator/main_gen.html',
                  {"form": GeneratorForm()})


def generate(request):
    if request.method == "POST":
        form = GeneratorForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            response_data = dict(passwords=Generator.str_for_choice(c))
            return HttpResponse(json.dumps(response_data),
                                content_type='application/json')
    else:
        raise Http404
