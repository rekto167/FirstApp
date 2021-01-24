from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_name = 'index.html'
    context = {
        'judul': 'Anda Sebagai ?'
    }

    def get(self, request):
        return render(self.request, self.template_name, self.context)
