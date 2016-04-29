# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def move_banners_to_index_page(apps, schema_editor):
    from molo.core.models import (
        BannerPage, SiteLanguage, BannerIndexPage, Main)
    main = Main.objects.all().first()
    main_language = SiteLanguage.objects.filter(is_main_language=True).first()

    if main and main_language:
        # Move existing banners
        index_page = BannerIndexPage.objects.live().first()
        for page in BannerPage.objects.all().child_of(main):
            page.move(index_page, pos='last-child')


def move_footers_to_index_page(apps, schema_editor):
    from molo.core.models import (FooterPage, SiteLanguage,
                                  FooterIndexPage, Main)
    main = Main.objects.all().first()
    main_language = SiteLanguage.objects.filter(is_main_language=True).first()

    if main and main_language:
        # Move existing footers
        index_page = FooterIndexPage.objects.live().first()
        for page in FooterPage.objects.all().child_of(main):
            page.move(index_page, pos='last-child')


def move_sections_to_index_page(apps, schema_editor):
    from molo.core.models import (SectionPage, SiteLanguage,
                                  SectionIndexPage, Main)
    main = Main.objects.all().first()
    main_language = SiteLanguage.objects.filter(is_main_language=True).first()

    if main and main_language:
        # Move existing sections
        index_page = SectionIndexPage.objects.live().first()
        for page in SectionPage.objects.all().child_of(main):
            page.move(index_page, pos='last-child')


def move_polls_to_index_page(apps, schema_editor):
    from molo.core.models import (SiteLanguage, Main)
    from molo.polls.models import (Question, FreeTextQuestion, PollsIndexPage)
    main = Main.objects.all().first()
    main_language = SiteLanguage.objects.filter(is_main_language=True).first()

    if main and main_language:
        # Move existing questions
        index_page = PollsIndexPage.objects.live().first()
        for page in Question.objects.all().child_of(main):
            page.move(index_page, pos='last-child')
        # Move existing FreeTextQuestion
        for page in FreeTextQuestion.objects.all().child_of(main):
            page.move(index_page, pos='last-child')


class Migration(migrations.Migration):

    dependencies = [
        ('freebasics', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(move_banners_to_index_page),
        migrations.RunPython(move_footers_to_index_page),
        migrations.RunPython(move_sections_to_index_page),
        migrations.RunPython(move_polls_to_index_page),
    ]
