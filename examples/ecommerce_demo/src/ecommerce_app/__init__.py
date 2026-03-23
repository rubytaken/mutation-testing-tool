"""
E-Commerce Order Processing Demo

Bu demo, mutation testing'in gerçek dünya e-ticaret senaryolarında nasıl kullanılacağını gösterir.
Sipariş işleme, indirim hesaplama, stok yönetimi ve durum geçişleri gibi karmaşık iş mantığını içerir.
"""

from .models import Order, OrderItem, OrderResult
from .order_status import OrderStatus, can_transition, transition_order, InvalidTransitionError

__version__ = "1.0.0"

__all__ = [
    "Order",
    "OrderItem", 
    "OrderResult",
    "OrderStatus",
    "can_transition",
    "transition_order",
    "InvalidTransitionError",
]
