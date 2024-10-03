from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Модель для категорий доходов и расходов."""
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории',
        help_text='Введите название категории (например, "Еда", "Транспорт").'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name='Пользователь',
        help_text='Выберите пользователя, которому принадлежит данная категория.'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Income(models.Model):
    """Модель для доходов."""
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма дохода',
        help_text='Введите сумму дохода (например, 1500.00).'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='incomes',
        verbose_name='Категория',
        help_text='Выберите категорию, к которой относится этот доход.'
    )
    date = models.DateField(
        verbose_name='Дата дохода',
        help_text='Выберите дату получения дохода.'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
        help_text='Введите описание дохода (необязательное поле).'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='incomes',
        verbose_name='Пользователь',
        help_text='Выберите пользователя, которому принадлежит данный доход.'
    )

    def __str__(self):
        return f"{self.amount} - {self.category.name}"

    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'
        ordering = ['-date']


class Expense(models.Model):
    """Модель для расходов."""
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма расхода',
        help_text='Введите сумму расхода (например, 500.00).'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='expenses',
        verbose_name='Категория',
        help_text='Выберите категорию, к которой относится этот расход.'
    )
    date = models.DateField(
        verbose_name='Дата расхода',
        help_text='Выберите дату совершения расхода.'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
        help_text='Введите описание расхода (необязательное поле).'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='expenses',
        verbose_name='Пользователь',
        help_text='Выберите пользователя, которому принадлежит данный расход.'
    )

    def __str__(self):
        return f"{self.amount} - {self.category.name}"

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'
        ordering = ['-date']
