from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)
  slug = models.SlugField(primary_key=True, db_index=True, default="")

  def save(self, *args, **kwargs) -> None:
    """
    Save the Post.

    This method is overridden to set the slug when the Post is saved.
    """
    self.slug = slugify(self.title)
    super().save()

  def __str__(self) -> str:
    """
    Return a string representation of the Post.

    This is a human-readable representation of the Post, showing
    its title and the date it was created.

    Returns:
      str: A string representation of the Post.
    """
    return f"{self.title}"