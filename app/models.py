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
    # __ Get Right Url ___
    def get_absolute_url(self):
        return "/posts/%s/" % self.slug


# -- Portfolio --

class Portfolio(models.Model):
    title = models.CharField(max_length=80)
    sub = models.CharField(max_length=40 , null=True,blank=True)
    body = models.TextField()
    pic = models.ImageField(upload_to='portfolio/')
    pub = models.DateTimeField(auto_now=False)
    draft = models.BooleanField(default=False)
    tags = TaggableManager()

    def __str__(self):
        return self.title


# -- Resume --

class Resume(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField(null=True,blank=True)
    pic = models.ImageField(upload_to='resume/', blank=True, null=True)
    position = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    body = models.TextField()


    def __str__(self):
        return self.title


