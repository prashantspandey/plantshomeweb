from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Plant(models.Model):
    ornamental = 'Ornamental'
    herb = 'Herbs'
    shrub = 'Shrubs'
    fs = 'Flowering and Seasonal'
    tree = 'Trees'
    palm = 'Palm'
    fruit = 'Fruits'
    grass = 'Grass'
    bonsai = 'Bonsai'


    category_choice = ((ornamental,'Ornamental'),(herb,'Herbs'),(shrub,'Shrubs'),(fs,'Flowering and Seasonal'),
                       (tree,'Tree'),(palm,'Palm'),(fruit,'Fruits'),(grass,'Grass'),(bonsai,'Bonsai'))
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=category_choice, default=shrub, )
    description = models.TextField()
    image1 = models.ImageField(upload_to=upload_location, max_length=500, null=True, blank=True)
    image2 = models.ImageField(max_length=500, null=True, blank=True)
    image3 = models.ImageField(max_length=500, null=True, blank=True)
    image4 = models.ImageField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('firstone:detail', kwargs={'pk': self.pk})


class RatingPlant(models.Model):
    onestar = 'One Star'
    twostar = 'Two Star'
    threestar = 'Three Star'
    fourstar = 'Four Star'
    fivestar = 'Five Star'
    rating_choice = ((onestar, 'One Star'), (twostar, 'Two Star'), (threestar, 'Three Star'),
                     (fourstar, 'Four Star'), (fivestar, 'Five Star'))

    forplant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    foruser = models.ForeignKey(User, null=True, blank=True)
    rating = models.IntegerField(choices=rating_choice, null=True, blank=True)
    reviewtime = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
    number_rating = models.IntegerField(default=0)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.review


class PlantSize(models.Model):
    thick = 'Thick'
    thin = 'Thin'
    leaves = 'Leaves'
    ztfeet = '0-2 feet'
    tffeet = '2-4 feet'
    fsfeet = '4-6 feet'
    sefeet = '6-8 feet'
    etfeet = '8-10 feet'
    seed = 'Seedling'

    size_choice = ((thick, 'Thick'), (thin, 'Thin'), (ztfeet, '0-2 feet'),
                   (tffeet, '2-4 feet'), (fsfeet, '4-6 feet'), (sefeet, '6-8 feet'),
                   (etfeet, '8-10 feet'),(seed,'Seedling'))

    psize = models.ForeignKey(Plant, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, choices=size_choice)
    price = models.IntegerField()


class Cart(models.Model):
    carter = models.ForeignKey(User, on_delete=models.CASCADE)
    plantid = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=120)
    price = models.IntegerField()
    total = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.carter)


class UserProfile(models.Model):
    us = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    address = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.address

class Order(models.Model):
    new = 'new'
    confirmed = 'confirmed'
    delivered = 'delivered'
    cancelled = 'cancelled'
    status_choice = ((confirmed,'confirmed'), (delivered,'delivered'),(cancelled,'cancelled'),(new,'new'))
    user = models.ForeignKey(User)
    phone = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    address = models.CharField(max_length=400,)
    username = models.CharField(max_length=100,)
    plnames = models.CharField(max_length=100,)
    plantsizes = models.CharField(max_length=400,)
    total = models.IntegerField()
    ordertime = models.DateTimeField(auto_now=False, auto_now_add=True,null=True,blank=True)
    status = models.CharField(max_length=50, choices= status_choice,null=True,blank=True)

    def __str__(self):
        return self.username
