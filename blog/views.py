from django.shortcuts import render, HttpResponse
from django.http import Http404

samplePostsData = [
  {
    "title": "Post One",
    "content": "This is my first blog post!",
    "date_posted": "August 27, 2020",
    "post_link": "post-one",
  },
  {
    "title": "Post Two: My Favorite Hobby",
    "content": "I love playing guitar in my free time. There's something about creating music that just makes me feel alive. I've been playing for years now, and I still get excited every time I pick up my instrument.",
    "date_posted": "September 1, 2020",
    "post_link": "my-favorite-hobby",
  },
  {
    "title": "Post Three: Traveling the World",
    "content": "I've always been fascinated by different cultures and ways of life. That's why I love traveling so much. Whether it's exploring the ancient ruins of Rome or trying new foods in Tokyo, I'm always up for an adventure.",
    "date_posted": "September 15, 2020",
    "post_link": "traveling-the-world",
  },
  {
    "title": "Post Four: My Favorite Books",
    "content": "I'm a big reader, and I love getting lost in a good book. Some of my favorite authors include J.K. Rowling, J.R.R. Tolkien, and George R.R. Martin. I also enjoy reading non-fiction books on history and science.",
    "date_posted": "October 1, 2020",
    "post_link": "my-favorite-books",
  },
  {
    "title": "Post Five: Learning to Code",
    "content": "I recently started learning how to code, and it's been a really rewarding experience. I've always been interested in technology, and now I'm finally able to create my own projects and bring my ideas to life.",
    "date_posted": "October 15, 2020",
    "post_link": "learning-to-code",
  },
  {
    "title": "Post Six: My Favorite Foods",
    "content": "I love trying new foods and drinks, but I also have a few favorite comfort foods that I always come back to. Some of my go-to dishes include pasta, pizza, and sushi. I also enjoy trying new craft beers and wines.",
    "date_posted": "November 1, 2020",
    "post_link": "my-favorite-foods",
  },
]


# Create your views here.
def index(request) -> HttpResponse:
  return render(request, "blog/index.html")


def all_posts(request) -> HttpResponse:
  return render(request, "blog/all-posts.html", {"posts": samplePostsData})


def post_detail(request, slug: str) -> HttpResponse:
  post = next((post for post in samplePostsData if post["post_link"] == slug), None)
  if post:
    return render(request, "blog/post-detail.html", {"post": post})
  
  raise Http404("Post not found")
