# Generated by Django 4.2.15 on 2024-08-20 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionario', '0002_opcion_alter_cuestionario_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': 'Tag',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='dificultad',
            field=models.CharField(blank=True, choices=[('Nivel 1', (('Facil', 'Facil'),)), ('Nivel 2', (('Normal', 'Normal'),)), ('Nivel 3', (('Intermedio', 'Intermedio'),)), ('Nivel 4', (('Avanzado', 'Avanzado'),)), ('Nivel 5', (('Expertiz', 'Expertiz'),)), ('Sin nivel', 'Sin nivel')], default='Facil', max_length=300),
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='imagen',
            field=models.URLField(blank=True, default='https://via.placeholder.com/150', null=True),
        ),
        migrations.CreateModel(
            name='cuestionario_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuestionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuestionario.cuestionario')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuestionario.tags')),
            ],
            options={
                'verbose_name': 'Relacion MM - Cuestionario - Tag',
                'verbose_name_plural': 'Relaciones MM - Cuestionarios - Tags',
                'db_table': 'Relacion M-M cuestionario - tag',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='Tags', related_name='RELACION_CUESTIONARIO_TAGS', related_query_name='RELACION_MM_CUESTIONARIO_TAGS', through='cuestionario.cuestionario_tag', to='cuestionario.tags', verbose_name='Tag'),
        ),
    ]
