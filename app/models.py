from django.db import models

# +++ Tag app +++
from taggit.managers import TaggableManager

# *** Model ***
# --- Post ---
class Post (models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField()
    pic = models.ImageField(upload_to='posts/')
    body = models.TextField()
    pub = models.DateTimeField(auto_now=False)
    draft = models.BooleanField(default=False)
    tags = TaggableManager()

    # __ Show in String __
    def __str__(self):
        return self.title


# -- Portfolio --

class Portfolio(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField()
    thumb = models.ImageField(upload_to='portfolio/')
    pic = models.ImageField(upload_to='portfolio/')
    pub = models.DateTimeField(auto_now=False)
    draft = models.BooleanField(default=False)
    tags = TaggableManager()

    def __str__(self):
        return self.title