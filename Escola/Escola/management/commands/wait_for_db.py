import time
from psycopg2 import OperationalError as Psycopg20pError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

# Comando para esperar pelo database
class Command(BaseCommand):
    
    # Entrypoint do comando
    def handle(self, *args, **options):
        self.stdout.write("-> Wainting fot database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except(Psycopg20pError, OperationalError):
                self.stdout.write("-> Database unavailable, wainting 1 second")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("-> Database ready to aceept connections"))
                
    