import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

#import -----> function
from faker import Faker
import random
from products.models import Product,Brand,Category


def seed_brand(n):
    fake = Faker()
    images = ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg']
    for _ in range(n):
        name=fake.name()
        image = f"brand/{images[random.randint(0,4)]}"
        Brand.objects.create(
            name= name,
            image = image
        )
    print(f"succesuful {n} brand")
def seed_category(n):
    fake = Faker()
    images = ['1.jpeg', '2.jpeg', '3.jpeg', '4.jpeg', '5.jpeg','6.jpeg']
    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0,5)]}"
        Category.objects.create(
            name=name,
            image=image
        )

    print(f"succesuful {n} category")
def seed_products(n):
    fake = Faker()
    images = ['1.jpeg', '2.jpeg', '3.jpeg', '4.jpeg', '5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg']
    flag_type=['New','Feature','Sale']
    for _ in range(n):
        name = fake.name()
        sku = random.randint(1, 100000)
        subtitle = fake.text(max_nb_chars=300)
        desc = fake.text(max_nb_chars=10000)
        flag = flag_type[random.randint(0, 2)]
        price = round(random.uniform(20.99, 99.99), 2)

        image = f"products/{images[random.randint(0,8)]}"
        category = Category.objects.get(id=random.randint(1, 10))
        brand = Brand.objects.get(id=random.randint(1, 10))
        
        Product.objects.create(
            name=name,
            sku = sku,
            subtitle = subtitle,
            desc = desc,
            flag = flag,
            price = price,
            image = image,
            category = category,
            brand = brand,
            video_url="https://www.youtube.com/watch?v=xrZZLgOoX3A"

            )

    print(f"succesuful {n} products")
seed_brand(5)
seed_category(5)
seed_products(800)
