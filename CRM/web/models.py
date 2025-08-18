from django.db import models

# Category Class
class Category(models.Model):
    category_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.category_name


# Client Model
class Client(models.Model):
    client_first_name = models.CharField(max_length=250)
    client_last_name = models.CharField(max_length=250)
    client_email = models.CharField(max_length=150, unique=True)
    client_phone_number = models.IntegerField()
    client_address = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    client_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self): return f'{self.client_first_name} {self.client_last_name}'

    class Meta:
        ordering = ['-created_at']
