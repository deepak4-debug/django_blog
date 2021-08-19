from django.shortcuts import render,get_object_or_404,redirect
from .forms import CommentForm
from django.views import View
from .models import Post, Comment


#This is for postlist
class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
       
        context = {
            'post_list': posts,
           
        }
        return render(request, 'blog/index.html', context)
    
   #This detail view and comments 
class PostDetailView(View):
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
class ReplyCommentView(View):
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

    
