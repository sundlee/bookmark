from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from bookmark.models import Bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

class IndexPage(TemplateView):
    template_name = "index.html"

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    template_name_suffix = '_create'
    fields = ['site_name', 'url']

    def form_valid(self, form):
        if form.is_valid:
            form.instance.save()
            return redirect('/bookmark/')
        else:
            return self.render_to_response({'form': form})

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    template_name_suffix = '_update'
    fields = ['site_name', 'url']

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')

