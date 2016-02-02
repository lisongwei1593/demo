# -*- coding: utf-8 -*-s
import datetime
import md5
import random
import string
import traceback
import django
from django.contrib.auth.models import User
from django.db.models import Max
from oscar.core.loading import get_model
from django.db.models.lookups import IsNull
from django.db.models import Min, Sum, Max
from django.db.models.query_utils import Q
from django.db.models import F
django.setup()
 
Product = get_model('catalogue', 'product')
Category = get_model('catalogue', 'Category')
pro = Product.objects.get(id=1)
print pro.primary_image()



