from django.core import management

def run():
    management.call_command('flush')
    management.call_command('createsuperuser')