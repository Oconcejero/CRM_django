from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@admin.com', '12345')

class Migration(migrations.Migration):
    # '0001_initial' debería ser el nombre de tu migración anterior
    dependencies = [('crm', '0001_initial')] 
    
    operations = [
        migrations.RunPython(create_superuser),
    ]