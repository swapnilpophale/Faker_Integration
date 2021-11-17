import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Faker.settings')
import django
django.setup()

from faker import Faker
from firstapp.models import Student


fake=Faker()

def fakerfun(n):
    for i in range(n):
        rn =fake.random_int(min=1,max=100)
        fname =fake.first_name()
        lname =fake.last_name()
        dob =fake.date()
        email =fake.email()
        addr =fake.address()

        obj=Student.objects.get_or_create(rn=rn,
                                           fname=fname,
                                           lname=lname,
                                           dob=dob,
                                           email=email,
                                           addr=addr,
                                           )

fakerfun(10)

