from django.core.management.base import BaseCommand
from main.models import Action
import requests
from faker import Faker

fake = Faker()

class Command(BaseCommand):
  help = 'Populate the database with fake data'
  def handle(self, *args, **kwargs):

    Action.objects.all().delete()

    response = requests.get('https://picsum.photos/v2/list?limit=5')
    images = response.json()

    for image in images:
      action = Action(
        title=fake.sentence(nb_words=3),
        description=fake.text(max_nb_chars=200),
        image=image['download_url']
      )
      action.save()
