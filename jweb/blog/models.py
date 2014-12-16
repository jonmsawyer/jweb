from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.CharField(max_length=75)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    tags = models.CharField(max_length=256)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify("%s-%s-%s-%s" % (self.created_at.year,
                                                 self.created_at.month,
                                                 self.created_at.day,
                                                 self.title))
        super(Blog, self).save(*args, **kwargs)

