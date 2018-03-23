from django.shortcuts import render
# +++ Import Detail & List View +++
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# +++ Import Custom models +++
from app.models import Post
# +++ import Utils +++
from django.utils import timezone



# === Index View Func ===
def index(request):
    return render(request, 'index.html')

# === Resume ===
def resume(request):
    return render(request, 'resume.html')

# === Portfolio ===
def portfolio(request):
    return render(request, 'portfolio.html')


# === Post Detail View ===
class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['-now'] = timezone.now()
        return context

# === Post List View ===
class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['-now'] = timezone.now()
        return context