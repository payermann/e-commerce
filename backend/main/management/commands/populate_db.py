from django.core.management.base import BaseCommand
from main.models import Product
import requests
from faker import Faker

fake = Faker()

class Command(BaseCommand):
  help = 'Populate the database with fake data'
  def handle(self, *args, **kwargs):

    response = requests.get('https://picsum.photos/v2/list?limit=100')
    images = response.json()

    for image in images:
      product = Product(
        title=fake.sentence(nb_words=1),
        description=fake.text(max_nb_chars=200),
        price=round(fake.random_number(digits=2), 2),
        image=image['download_url']
      )
      product.save()
