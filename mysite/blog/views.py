#!coding:utf-8
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
from blog.models import blogdata
from django.forms import ModelForm


class blogform(ModelForm):
    class Meta:
        model = blogdata
        fields = ('title', 'text', 'date', )

def edit(request):
    blogs = blogdata()
    form = None
    if request.method == 'POST':
        pass
    else:
        form = blogform(instance=blogs)
    #return render_to_response('blog/blogedit.html', {'form': form}, context_instance=RequestContext(request))
    return render(request, 'blog/blogedit.html', {'form': form})

def show(request):
    blogs = blogdata.objects.all()
    #return render_to_response('blog/blogshow.html', {'blogs': blogs}, context_instance=RequestContext(request))
    return render(request, 'blog/blogshow.html', {'blogs': blogs})

