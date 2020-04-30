from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) > 100:
            return self.body[:100] + "..."
        else:
            return self.body

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

