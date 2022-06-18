from django.db import models

class Category(models.Model):
    '''Класс описывает категорию объявления'''
    tank = 'TN'
    healer = 'HL'
    damage_dealer = 'DD'
    vendor = 'VN'
    guild_masters = 'GM'
    quest_givers = 'QG'
    blacksmith = 'BS'
    tanner = 'TN'
    potion_maker = 'PM'
    spell_master = 'SM'
    other = 'OR'

    CATEGORY = [
        (tank, 'Танк'),
        (healer, 'Хил'),
        (damage_dealer, 'ДД'),
        (vendor, 'Торговец'),
        (guild_masters, 'Гильдмастер'),
        (quest_givers, 'Квестгивер'),
        (blacksmith, 'Кузнец'),
        (tanner, 'Кожевенник'),
        (potion_maker, 'Зельевар'),
        (spell_master, 'Мастер заклинаний'),
        (other, 'Другое')
    ]
    name: str = models.CharField(max_length=2, choices=CATEGORY, default=other)

    def __str__(self):
        return f'{self.name}'


class Advertsement(models.Model):
    '''Класс описывает объявление'''
    title: str = models.CharField(max_length=300)
    body: str = models.TextField()
    category: Category = models.OneToOneField("Category", on_delete=models.CASCADE)

