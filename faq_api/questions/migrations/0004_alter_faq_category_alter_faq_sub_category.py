# Generated by Django 5.1.3 on 2024-11-25 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_subcategory_type_alter_faq_category_faq_sub_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.category'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='questions.subcategory'),
        ),
    ]
