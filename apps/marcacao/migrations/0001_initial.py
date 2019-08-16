# Generated by Django 2.2.4 on 2019-08-15 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0002_auto_20190815_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('dia_semana', models.CharField(max_length=20)),
                ('hora', models.TimeField()),
                ('tipo', models.CharField(choices=[('E', 'Entrada'), ('SI', 'Saída Intervalo'), ('R', 'Retorno Intervalo'), ('S', 'Saída'), ('D', 'Desconsiderar')], default='E', max_length=2, verbose_name='tipo de marcacao')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marcacao', to='funcionarios.Funcionario', verbose_name='funcionario')),
            ],
            options={
                'verbose_name': 'marcacao',
                'verbose_name_plural': 'marcacoes',
                'db_table': 'marcacao',
                'ordering': ['data', 'hora', 'funcionario'],
            },
        ),
    ]
