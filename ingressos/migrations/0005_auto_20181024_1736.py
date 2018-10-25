# Generated by Django 2.1.2 on 2018-10-24 20:36

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ingressos', '0004_auto_20181024_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, verbose_name='Sua URL (endereço')),
                ('logo', models.ImageField(upload_to='', verbose_name='Imagem')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do organizador (anfitrião)')),
                ('mostra_nome', models.BooleanField(default=False, verbose_name='Mostrar o nome abaixo do logo')),
                ('descricao', tinymce.models.HTMLField()),
                ('eventos_passados', models.BooleanField(default=True, verbose_name='Mostrar eventos passados')),
            ],
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AddField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ingressos.Organizador'),
        ),
    ]