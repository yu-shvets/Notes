from django.shortcuts import render
from django.forms import ModelForm
from .models import Notes
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import DetailView

# Create your views here.


class NoteForm(ModelForm):

    class Meta:
        model = Notes
        fields = ['note']


class CommentCreate(CreateView):
    model = Notes
    form_class = NoteForm
    template_name = 'index.html'

    def get_success_url(self):
            return reverse('link')


class LinkView(TemplateView):
    template_name = 'link.html'

    def get_context_data(self, **kwargs):
        context = super(LinkView, self).get_context_data(**kwargs)
        context['link'] = Notes.objects.latest('datetime')
        return context


class NoteDetail(DetailView):
    model = Notes
    template_name = 'note.html'
    slug_field = 'ekey'


class NoteDelete(DeleteView):
    model = Notes
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('home')
