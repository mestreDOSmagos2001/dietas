# Generated by Django 4.2.3 on 2023-07-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "criados",
                    models.DateField(auto_now_add=True, verbose_name="Criação"),
                ),
                (
                    "modificado",
                    models.DateField(auto_now=True, verbose_name="Atualização"),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                ("nome", models.CharField(max_length=100, verbose_name="nome")),
                ("telefone", models.CharField(max_length=20, verbose_name="Telefone")),
                ("email", models.EmailField(max_length=254, verbose_name="E-mail")),
            ],
            options={"abstract": False,},
        ),
    ]
