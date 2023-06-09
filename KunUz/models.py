from django.db import models


class NewsType(models.Model):
    category = models.CharField(max_length=100)
    
    class Meta:
        db_table = "NewsType"
        
    def __str__(self):
        return self.category


class RegionalNews(models.Model):
    category = models.ForeignKey(NewsType, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null= True, blank=True)
    description = models.CharField(max_length=10000, null=True, blank=True)
    articels = models.TextField()
    newsTypes = models.CharField(max_length=300, null=True, blank=True)
    img = models.ImageField(upload_to="images/", blank=True)
    create_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "RegionalNews"

    def __str__(self):
        return self.title
    