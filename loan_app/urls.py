"""
URLs for loan_app application.
"""

from django.urls import path
from .views import (
    LoanAPIView,
    LoanDetailView, 
    PaymentAPIView,
    BalanceApiView
)

urlpatterns = [
    path('', LoanAPIView.as_view(), name='loan-create'),
    path('<str:pk>/', LoanDetailView.as_view(), name='loan-detail'),
    path('<str:loan_id>/payments', PaymentAPIView.as_view(), name='payment-create'),
    path('<str:loan_id>/balance', BalanceApiView.as_view(), name='balance-get'),
]
