from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from sign.models import MyUser


class Category(models.Model):
    '''Класс описывает категорию объявления'''
    # tank = 'TN'
    # healer = 'HL'
    # damage_dealer = 'DD'
    # vendor = 'VN'
    # guild_masters = 'GM'
    # quest_givers = 'QG'
    # blacksmith = 'BS'
    # tanner = 'TN'
    # potion_maker = 'PM'
    # spell_master = 'SM'
    # other = 'OR'
    #
    # CATEGORY = [
    #     (tank, 'Танк'),
    #     (healer, 'Хил'),
    #     (damage_dealer, 'ДД'),
    #     (vendor, 'Торговец'),
    #     (guild_masters, 'Гильдмастер'),
    #     (quest_givers, 'Квестгивер'),
    #     (blacksmith, 'Кузнец'),
    #     (tanner, 'Кожевенник'),
    #     (potion_maker, 'Зельевар'),
    #     (spell_master, 'Мастер заклинаний'),
    #     (other, 'Другое')
    # ]

    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Advertsement(models.Model):
    '''Класс описывает объявление'''

    class CategoryChoices(models.TextChoices):
        TANK = 'TN', 'Танк'
        HEALER = 'HL', 'Хил'
        DAMAGE_DEALER = 'DD', 'ДД'
        VENDOR = 'VN', 'Торговец'
        GUILD_MASTER = 'GM', 'Гильдмастер'
        QUEST_GIVERS = 'QG', 'Квестгивер'
        BLACKSMITH = 'BS', 'Кузнец'
        TANNER = 'TR', 'Кожевенник'
        POTION_MAKER = 'PM', 'Зельевар'
        SPELL_MASTER = 'SM', 'Мастер заклинаний'
        OTHER = 'OR', 'Другое'

    title: str = models.CharField(max_length=300)
    body = RichTextUploadingField()
    category = models.CharField(max_length=2, choices=CategoryChoices.choices, default=CategoryChoices.OTHER)
    user: MyUser = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/advertsement/{self.id}'


# class AdvertsementCategory(models.Model):
#     advertsement = models.ForeignKey("Advertsement", on_delete=models.CASCADE)
#     category = models.ForeignKey("Category", on_delete=models.CASCADE)


