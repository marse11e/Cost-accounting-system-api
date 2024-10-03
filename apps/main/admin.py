from django.contrib import admin
from .models import Category, Income, Expense


class IncomeInline(admin.TabularInline):
    """Вложенное представление для доходов в категории."""
    model = Income
    extra = 1
    verbose_name_plural = 'Доходы'


class ExpenseInline(admin.TabularInline):
    """Вложенное представление для расходов в категории."""
    model = Expense
    extra = 1
    verbose_name_plural = 'Расходы'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админский интерфейс для категорий."""
    list_display = ('name', 'user', 'get_income_count', 'get_expense_count')
    list_filter = ('user',)
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [IncomeInline, ExpenseInline]

    def get_income_count(self, obj):
        return obj.incomes.count()
    get_income_count.short_description = 'Количество доходов'

    def get_expense_count(self, obj):
        return obj.expenses.count()
    get_expense_count.short_description = 'Количество расходов'


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    """Админский интерфейс для доходов."""
    list_display = ('amount', 'category', 'date', 'user', 'description')
    list_filter = ('category', 'date', 'user')
    search_fields = ('description', 'category__name')
    ordering = ('-date',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """Админский интерфейс для расходов."""
    list_display = ('amount', 'category', 'date', 'user', 'description')
    list_filter = ('category', 'date', 'user')
    search_fields = ('description', 'category__name')
    ordering = ('-date',)
