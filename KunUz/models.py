from django.db import models

class NewsType(models.Model):
    category = models.CharField(max_length=100)
    
    class Meta:
        db_table = "NewsType"
        
    def __str__(self):
        return self.category


class RegionalNews(models.Model):
    category = models.ForeignKey(NewsType, on_delete=models.CASCADE)
    newsTypes = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500, null=True, blank=True)
    descriptation = models.CharField(max_length=300, null=True, blank=True)
    img = models.ImageField(upload_to="images/", blank=True)
    text = models.TextField()
    dateTime = models.DateTimeField()
    
    class Meta:
        db_table = "RegionalNews"

    def __str__(self):
        return self.descriptation
