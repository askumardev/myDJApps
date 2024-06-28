from django.db import models

# Create your models here.
class Tour(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    # This string representatio of the tours
    
    def __str__(self):
        return (f"ID:{self.id}: From {self.origin} To {self.destination}, "
                f"{self.number_of_nights} nights cost {self.price}")


# from tourmate.models import Tour
# tour1 = Tour(origin="Japan", destination="India", number_of_nights=10, price=1500)
# tour1.save
# tour2 = Tour(origin="Australia", destination="Srikanka", number_of_nights=7, price=2500)
# tour2.save