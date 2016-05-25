from django.views import generic

class HomeView(generic.TemplateView):
    template_name = 'salishiw/home.html'
    
class HeaderView(generic.TemplateView):
    template_name = 'salishiw/header.html'
    context_object_name = 'user'
    