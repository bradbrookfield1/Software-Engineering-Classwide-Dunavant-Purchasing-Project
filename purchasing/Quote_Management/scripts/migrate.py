from django.core import management

def run():
    management.call_command('makemigrations')
    management.call_command('migrate')
    management.call_command('runserver')