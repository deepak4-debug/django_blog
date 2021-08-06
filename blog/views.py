from django.shortcuts import render,get_object_or_404

from django.views import generic
from .models import Post, Comment
from .forms import CommentForm




class Postlist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    
#class PostDetail(generic.DetailView):
   # model = Post
   # template_name = 'post_detail.html'
    
    
def post_detail(request, slug):
    template_name = 'post_detail.html'
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
    
    

    
