from django.db import models
from django.utils import timezone

# -- Таблица User
# CREATE TABLE User (
#     User_ID INT AUTO_INCREMENT PRIMARY KEY,
#     First_name VARCHAR(200) NOT NULL,
#     Last_name VARCHAR(200) NOT NULL,
#     Email VARCHAR(200) NOT NULL,
#     Date_of_birth DATE
# );

from django.db import models
from django.utils import timezone

# class User(models.Model):
#     first_name = models.CharField(max_length=200, db_index=True)
#     last_name = models.CharField(max_length=200, db_index=True)
#     email = models.EmailField(unique=True, default='example@example.com')
#     date_of_birth = models.DateField()
#     created_user = models.DateTimeField(auto_now_add=True)
#     updated_user = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
