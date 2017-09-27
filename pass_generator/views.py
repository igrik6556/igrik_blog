from django.shortcuts import render
from pass_generator.forms import GeneratorForm
from pass_generator.models import Generator


def generator(request):
    if request.method == "POST":
        form = GeneratorForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            return render(request, "pass_generator/main_gen.html", {"form": form,
                                                                   "passwords": Generator.str_for_choice(c)})
    else:
        form = GeneratorForm()
    return render(request,
                  'pass_generator/main_gen.html',
                  {"form": form})
