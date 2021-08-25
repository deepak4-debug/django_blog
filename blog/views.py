from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q 
from django.urls import reverse_lazy
from .forms import CommentForm
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django_searchbar.mixins import SearchBarViewMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from .models import Post, Comment,UserProfile
from django.core.paginator import Paginator


#This is about me view
class AboutMe(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/about_me.html')



 
class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        
        context ={
            'query':query,
            'post_list':post_list,
            
        }
        return render(request, 'blog/search_post.html', context)
'''
class SearchView(ListView):
    Model = Post
    template_name = 'blog/search_post.html'
    

    def get_queryset(self): # new
        query = self.request.GET.get('query')
        post_list = Post.objects.filter(
            Q(title__icontains=query)  #Q(title__icontains=query) | Q(author__icontains=query)
        )
        return post_list
 '''      
    
#This is for postlist
class PostListView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        paginator = Paginator(posts, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
       
        context = {
            'page_obj': page_obj,
           
        }
        return render(request, 'blog/index.html', context)

         
    
   #This detail view and comments 
class PostDetailView(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        template_name = 'blog/post_detail.html'
        form = CommentForm()
        
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post':post,
            'form': form,
            'comments': comments,
           
        }
        
        return render(request, template_name, context)
    
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        template_name = 'blog/post_detail.html'
        form = CommentForm(request.POST)
        new_comment = None
        
        if form.is_valid:
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        
        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }
        
        return render(request, template_name, context)

#View for replying comment
class ReplyCommentView(LoginRequiredMixin,View):
    def post(self, request, pk, post_pk, *args, **kwargs):
        post = Post.objects.get(pk=post_pk)
        parent_comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST)
        
        if form.is_valid:
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.parent = parent_comment
            new_comment.save()
            
        return redirect ('post_detail', pk=post_pk )
        



#This view is for profile
class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user 
        posts = Post.objects.filter(author=user).order_by('-created_on')
        
        '''followers = profile.followers.all()
        
        if len(followers) == 0:
            is_following = False
        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False
                
        number_of_followers = len(followers)'''
        
        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
           # 'number_of_followers':number_of_followers,
            #'is_following': is_following,
        }
    
        return render(request, 'blog/profile.html', context)
    
    
         



 # this for Editing profile 
class ProfileEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = UserProfile
    fields = ['name','birth_date','bio','location','picture']
    template_name = 'blog/profile_edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
    
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
    




'''
class Postlist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    
#class PostDetail(generic.DetailView):
   # model = Post
   # template_name = 'post_detail.html'
    
    
def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on") #queryset retrives all the approved comments from the database
    new_comment = None # initializing new comments
    
    #Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST) # holds the input data from user while commenting
        if comment_form. is_valid():
            
            #Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            #Assign the current post to the comment
            new_comment.post = post
            #save the comment to the database
            new_comment.save()
            
    else:
        comment_form = CommentForm()
        
    return render(request, template_name, {"post": post, "comments": comments, 'new_comment': new_comment, 'comment_form': comment_form})
    
    '''

    
