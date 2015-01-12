from django.db import models

class Copyright(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return 'Copyright page'

class Home(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return 'Home page'

