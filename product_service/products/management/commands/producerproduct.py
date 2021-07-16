import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from products.service import produce_product

logger = logging.getLogger(__name__)


class Command(BaseCommand):
  
  help = "Produce product"

  def handle(self, *args, **options):
    produce_product()