from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.forms import ImgForm
from django.views.generic import DetailView
from django.views.generic import TemplateView
class Image(TemplateView):
    form = ImgForm
    template_name = 'blog/image.html'

    def post(self,reguest,*args, **kwargs):
        form = ImgForm(reguest.POST, reguest.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('image_display', kwargs={'pk' :obj.id}))

        context = self.get_contaxt_data(form=form)
        return self.render_to_response(context)
    def get(self,reguest, *args, **kwargs):
        return self.post(reguest, *args, **kwargs)

class ImageDisplay(DetailView):
    model = Post
    template_name = 'blog/image_display.html'
    context_object_name =  'image'



def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post'}: post)


def error_404_view(reguest,exception):
    data = {"name": 'Blog dla programistów'}
    return render(request, 'blok/404.html', data)