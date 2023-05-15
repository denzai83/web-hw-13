from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import AuthorForm, QuoteForm, TagForm
from .models import Author, Quote, Tag
# from .utils import get_mongodb


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.user = request.user
            new_author.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_author.html', context={'form': form})
    return render(request, 'quotes/add_author.html', context={'form': AuthorForm()})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.save()
            return redirect(to='quotes:root')
        else:
            return render(request,'quotes/add_quote.html', context={'form': form})
    return render(request, 'quotes/add_quote.html', context={'form': QuoteForm()})

@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_tag.html', context={'form': form})
    return render(request, 'quotes/add_tag.html', context={'form': TagForm()})

def author_about(request, id):
    author = Author.objects.get(pk=id)
    return render(request, 'quotes/author.html', context={'author': author})

def main(request, page=1):
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})
