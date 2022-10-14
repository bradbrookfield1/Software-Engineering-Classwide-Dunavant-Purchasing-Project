def populate_models(sender, **kwargs):
    from django.apps import apps
    from .apps import QuoteManagementConfig
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    staff_group, created = Group.objects.get_or_create(name='IT Staff')
    manager_group, created = Group.objects.get_or_create(name='IT Manager')

    models = apps.all_models[QuoteManagementConfig.name]
    for model in models:
        content_type = ContentType.objects.get(
            app_label=QuoteManagementConfig.name,
            model=model
        )
        permissions = Permission.objects.filter(content_type=content_type)
        staff_group.permissions.add(*permissions)