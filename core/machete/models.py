from django.db import models

# Create your models here.

class ClickWhatsApp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, default='')
    from_site = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.created_at)
    
class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100)
    unsubscribed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name or "Unnamed Contact"
    

