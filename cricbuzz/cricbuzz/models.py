from django.db import models

class BaseModel(models.Model):
    """
        base class to monitor changes in a particular record
    """
    created_at = models.DateField(auto_now_add=True, null=True, editable=False)
    updated_at = models.DateField(auto_now=True, null=True)

class Data(BaseModel):
    '''
        Data class to store all the media and metadata to display on home page
    '''
    title = models.CharField(max_length=100, null=False)
    url = models.URLField(null=False)
    description = models.TextField()
    thumbnail = models.ImageField()
    is_premium = models.BooleanField(default=False)
    is_video = models.BooleanField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

class Subscription(BaseModel):
    '''
        Subscription class to store all the subscription plans
    '''

    title = models.CharField(max_length=100, null=False)
    url = models.URLField(null=False)
    description = models.TextField(null=True)
    features = models.TextField(null=False)
    price = models.FloatField(null=False)

    def __str__(self):
        return str(self.title)