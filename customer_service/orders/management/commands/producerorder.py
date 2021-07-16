# runapscheduler.py
import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from orders.service import produce_order, create_order

logger = logging.getLogger(__name__)


class Command(BaseCommand):
  
  help = "Produce order"

  def handle(self, *args, **options):
    produce_order()
    #create_order({})