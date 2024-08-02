# Generated by Django 5.0.6 on 2024-07-24 17:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cuca', models.CharField(max_length=100)),
                ('data_atual', models.CharField(max_length=100)),
                ('periodo', models.CharField(max_length=100)),
                ('atividades_realizadas', models.TextField()),
                ('problemas_enfrentados', models.TextField()),
                ('curiosidade_aprendizado', models.TextField()),
                ('pontos_forts', models.TextField()),
                ('imagem1', models.ImageField(upload_to='images/')),
                ('txt_img1', models.TextField()),
                ('imagem2', models.ImageField(upload_to='images/')),
                ('txt_img2', models.TextField()),
                ('imagem3', models.ImageField(upload_to='images/')),
                ('txt_img3', models.TextField()),
                ('imagem4', models.ImageField(upload_to='images/')),
                ('txt_img4', models.TextField()),
                ('imagem5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('txt_img5', models.TextField(blank=True, null=True)),
                ('imagem6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('txt_img6', models.TextField(blank=True, null=True)),
                ('link_relatorio', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
