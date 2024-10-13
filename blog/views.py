from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect
from django.http import HttpRequest
from django.urls import reverse

from .models import Post


def __is_post_modified(post: Post) -> bool:
  """
  Check if a Post has been modified since it was first posted.

  Since the DateTimeField is down to the microsecond, we compare the two
  timestamps after stripping out the microseconds to avoid false
  negatives from the comparison.

  Args:
    post: The Post to check for modification.

  Returns:
    True if the Post was modified, False otherwise.
  """
  return post.date_modified.replace(microsecond=0) != post.date_posted.replace(microsecond=0)


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
  """
  Show the homepage of the blog.

  This view is the homepage of the blog. It renders the blog/index.html
  template.

  Parameters:
    request (HttpRequest): The request object.

  Returns:
    HttpResponse: The rendered template.
  """
  return render(request, "blog/index.html")

def all_posts(request: HttpRequest) -> HttpResponse:
  """
  Show all the blog posts.

  This view shows all the blog posts. It renders the blog/all-posts.html
  template.

  Parameters:
    request (HttpRequest): The request object.

  Returns:
    HttpResponse: The rendered template.
  """
  posts = Post.objects.all()
  for post in posts:
    post.is_modified = __is_post_modified(post)

  return render(request, "blog/all-posts.html", {"posts": posts})


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
  """
  Show a single blog post.

  This view takes a slug as a parameter and uses it to find the Post
  object in the database. It then renders the post-detail.html template
  with that Post object.

  If the Post object with the given slug does not exist, this view will
  raise a 404 error.

  Parameters:
    request (HttpRequest): The request object.
    slug (str): The slug of the Post to show.

  Returns:
    HttpResponse: The rendered post-detail.html template.
  """
  post = get_object_or_404(Post, slug=slug)
  post.is_modified = __is_post_modified(post)
  return render(request, "blog/post-detail.html", {"post": post})

def delete_post(request, slug: str) -> HttpResponse:
  """
  Delete a blog post.

  This view takes a slug as a parameter and deletes the Post object with
  that slug from the database. It then redirects to the all_posts_page
  URL.

  Parameters:
    request (HttpRequest): The request object.
    slug (str): The slug of the Post to delete.

  Returns:
    HttpResponse: The redirect to the all_posts_page URL.
  """
  post = Post.objects.get(slug=slug)
  post.delete()
  return HttpResponseRedirect(reverse("all_posts_page"))
  