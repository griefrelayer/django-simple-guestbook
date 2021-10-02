from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from .models import Messages
from .utils import replace, sanitize, replace_image_with_smiles
from django.core.exceptions import PermissionDenied
from django import forms


class MyForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = ['name', 'email', 'comment', 'rating']

    def clean(self):
        if not self.cleaned_data.get('rating', False):
            self.cleaned_data['rating'] = '0'
        print(super().clean())


class IndexView(CreateView, ListView):
    template_name = 'index4.html'
    model = Messages
    paginate_by = '10'
    form_class = MyForm

    def get_success_url(self):
        return reverse('index_page')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user

        self.object = form.save(commit=False)
        self.object.comment = replace_image_with_smiles(self.object.comment)
        self.object.comment = sanitize(self.object.comment)
        self.object.comment = replace(self.object.comment)

        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def __init__(self):
        self.object_list = Messages.objects.all()
        super(CreateView, self).__init__()
        super(IndexView, self).__init__()


class DeleteMessageView(DeleteView):
    model = Messages

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.id == Messages.objects.get(id=kwargs['pk']).user_id:
            return super().post(*args, **kwargs)
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse('index_page')



