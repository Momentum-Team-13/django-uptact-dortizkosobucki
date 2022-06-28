from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USZipCodeField
from django.utils import timezone

class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USZipCodeField(null=True, blank=True)
    note = models.ForeignKey("Note", on_delete=models.CASCADE, related_name="Note_about_Contact", null=True,blank=True)

class Note(models.Model):
    content = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    

# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, releated_name="favorites")
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="favorites")
 