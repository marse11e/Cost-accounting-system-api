from rest_framework import generics, permissions, status
from rest_framework.response import Response
from apps.main.models import Income, Expense, Category
from apps.main.serializers import IncomeSerializer, ExpenseSerializer, CategorySerializer


class IncomeListCreateView(generics.ListCreateAPIView):
    """Представление для получения и создания доходов."""
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class IncomeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для получения, обновления и удаления дохода."""
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExpenseListCreateView(generics.ListCreateAPIView):
    """Представление для получения и создания расходов."""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для получения, обновления и удаления расхода."""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatisticsView(generics.GenericAPIView):
    """Представление для получения статистики по финансам."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        incomes = Income.objects.filter(user=user)
        expenses = Expense.objects.filter(user=user)

        total_income = sum(income.amount for income in incomes)
        total_expense = sum(expense.amount for expense in expenses)

        statistics = {
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': total_income - total_expense
        }

        return Response(statistics, status=status.HTTP_200_OK)


class CategoryListCreateView(generics.ListCreateAPIView):
    """Представление для получения и создания категорий."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для получения, обновления и удаления категории."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
