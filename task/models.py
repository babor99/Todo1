from django.db import models

# username: babor
# email: islambabor947@gmail.com
# password: 8872

# Create your models here.
class ToDo(models.Model):
    content = models.TextField()

