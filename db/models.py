from django.db import models
from rest_framework import serializers

PARCEL_STATUSES = {
    'created': 'Created',
    'shipped': 'Shipped',
    'delivered': 'Delivered',
    'received': 'Received',
    'unknown': 'Unknown'
}

PARCEL_LOCKER_STATUSES = {
    'free': 'Free',
    'full': 'Full',
    'unknown': 'Unknown'
}

SIZES = {
    '1': 'XS',
    '2': 'S',
    '3': 'M',
    '4': 'L',
    '5': 'XL',
}


def parcel_status_choice():
    return_list = []
    for key, value in PARCEL_STATUSES.items():
        return_list.append((key, f'{value}'))
    return return_list


def parcel_locker_status_choice():
    return_list = []
    for key, value in PARCEL_LOCKER_STATUSES.items():
        return_list.append((key, f'{value}'))
    return return_list


def size_choice():
    return_list = []
    for key, value in SIZES.items():
        return_list.append((key, f'{value}'))
    return return_list


class Parcel(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} from {self.sender}'

    def __unicode__(self):
        return self.__str__()

    # creation_date
    # receive_date
    # delivered_date

    sender = models.TextField(null=False)  # Should be object with Name, Address, ZIP etc - better, but not today
    receiver = models.TextField(null=False)  # Should be object with Name, Address, ZIP etc - better, but not today
    status = models.CharField(max_length=30, choices=parcel_status_choice(), null=False)
    size = models.CharField(max_length=10, choices=size_choice(), null=False)

    # to_delete = models.BooleanField(default=False)


class ParcelLocker(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__parcel_before_saving = self.parcel
        self.__status_before_saving = self.status

    def __str__(self):
        return f'{self.id}@{self.address}'

    def __unicode__(self):
        return self.__str__()

    def save(self, *args, **kwargs):
        if self.parcel:
            # if address - Object, can check if ZIP/AREA ZIP equals between receiver and parcel locker
            if self.__parcel_before_saving and self.parcel != self.__parcel_before_saving:
                raise serializers.ValidationError("Already have parcel")
            else:
                if int(self.parcel.size) > int(self.size):
                    raise serializers.ValidationError("Cannot put big parcel in small locker")
                self.status = 'full'
                self.parcel.status = 'delivered'
                self.parcel.save()
        else:
            self.status = 'empty'
        super().save(*args, **kwargs)

    address = models.TextField(null=False) # Should be object with Address, ZIP etc - better, but not today
    parcel = models.ForeignKey('db.Parcel', null=True, unique=True, related_name='lockers',
                               on_delete=models.SET_NULL)
    status = models.CharField(max_length=30, choices=parcel_locker_status_choice(), null=False)
    size = models.CharField(max_length=10, choices=size_choice(), null=False)

    # to_delete = models.BooleanField(default=False)
