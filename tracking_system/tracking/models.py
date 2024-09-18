from django.db import models

class TrackingNumber(models.Model):
    tracking_number = models.CharField(max_length=16, unique=True)
    origin_country_id = models.IntegerField()
    destination_country_id = models.IntegerField()
    weight = models.FloatField()
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    customer_slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tracking_number
