from rest_framework import serializers
from apps.main.models import Income, Expense, Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории."""

    class Meta:
        model = Category
        fields = ['id', 'name', 'user']
        read_only_fields = ['user']


class IncomeSerializer(serializers.ModelSerializer):
    """Сериализатор для доходов."""
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Income
        fields = ['id', 'amount', 'category', 'date', 'description', 'user']
        read_only_fields = ['user']


class ExpenseSerializer(serializers.ModelSerializer):
    """Сериализатор для расходов."""
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Expense
        fields = ['id', 'amount', 'category', 'date', 'description', 'user']
        read_only_fields = ['user']
