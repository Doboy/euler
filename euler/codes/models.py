from django.db import models

class problem( models.model ):
    description = models.CharField(max_length=1000)
    solution = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
