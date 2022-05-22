from django.shortcuts import render , get_object_or_404,redirect
from .models import AlbumM,mkSelectM
from .forms import CreateForm,mkSelectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.
# ************************************************************************************
@login_required
def top(request):
    params={}
    return render(request,'album/top.html',params)
# ************************************************************************************
def album(request):
    posts = AlbumM.objects.filter(category=1)
    params={
        'posts':posts
    }
    return render(request,'album/album.html',params)
# ************************************************************************************
def mkarticle(request):
    posts = AlbumM.objects.filter(category=2)
    pot = mkSelectM()
    if request.method == 'GET':
        form = mkSelectForm(instance=pot)
        # return render(request, 'album/mkarticle.html', {'form': form})
    if request.method=='POST':
        form=mkSelectForm(request.POST,instance=pot)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            # return redirect(to='album:album')
    params={
        'posts':posts,
        'form':form,
    }
    return render(request,'album/mkarticle.html',params)
# ************************************************************************************
def detail(request, album_id):
    album_text = get_object_or_404(AlbumM, id=album_id)
    return render(request, 'album/detail.html', {'album_text': album_text })
# ************************************************************************************
def create(request):
    post = AlbumM()
    if request.method == 'GET':
        form = CreateForm(instance=post)
        return render(request, 'album/create.html', {'form': form})
    if request.method=='POST':
        form=CreateForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect(to='accounts:home')
# ************************************************************************************
class UpdateView(LoginRequiredMixin,UpdateView):
    template_name='album/update.html'
    model= AlbumM
    fields= ['title','category','name', 'age','explanation']
    def get_success_url(selfself):
        # return reverse('album/detail.html',kwargs={'pk':self.object.pk})
        return reverse('album:album')
    def get_form(self):
        form=super(UpdateView,self).get_form()
        form.fields['name'].label = '名前'
        return form
# ************************************************************************************
class AlbumDeleteView(LoginRequiredMixin,DeleteView):
    template_name='album/delete.html'
    model=AlbumM
    success_url=reverse_lazy('accounts:home')

# ************************************************************************************
def mkmake1(request, album_id,memo_id,ko_id):
    album_text = get_object_or_404(AlbumM, id=album_id)
    memo_id=get_object_or_404(AlbumM, id=memo_id)
    ko_id=get_object_or_404(AlbumM, id=ko_id)
    params={
        'album_text': album_text,
        'memo_id': memo_id ,
        'ko_id': ko_id ,
    }
    return render(request, 'album/mkmake1.html', params)