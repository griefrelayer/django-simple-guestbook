from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from .models import Messages
from .utils import replace, sanitize, replace_image_with_smiles


class IndexView(CreateView, ListView):
    template_name = 'index3.html'
    model = Messages
    fields = ['name', 'email', 'comment', 'rating']
    paginate_by = 10

    def get_success_url(self):
        return reverse('index_page')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.comment = replace_image_with_smiles(self.object.comment)
        self.object.comment = sanitize(self.object.comment)
        self.object.comment = replace(self.object.comment)

        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def __init__(self):
        self.object_list = Messages.objects.all();
        super(CreateView, self).__init__()
        super(IndexView, self).__init__()


class DeleteMessageView(DeleteView):
    model = Messages

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse('index_page')



