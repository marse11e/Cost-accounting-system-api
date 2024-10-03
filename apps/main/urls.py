from django.urls import path
from apps.main.views import (
    IncomeListCreateView,
    IncomeRetrieveUpdateDestroyView,
    ExpenseListCreateView,
    ExpenseRetrieveUpdateDestroyView,
    StatisticsView,
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView
)


urlpatterns = [
    path('incomes/', IncomeListCreateView.as_view(), name='income-list-create'),
    path('incomes/<int:pk>/', IncomeRetrieveUpdateDestroyView.as_view(), name='income-detail'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDestroyView.as_view(), name='expense-detail'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
]
