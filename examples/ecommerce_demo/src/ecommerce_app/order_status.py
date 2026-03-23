"""
Order status management module.
Handles order state transitions and validation.
"""
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Order


class OrderStatus(Enum):
    """Sipariş durumları"""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class InvalidTransitionError(Exception):
    """Geçersiz durum geçişi hatası"""
    pass


def can_transition(from_status: OrderStatus, to_status: OrderStatus) -> bool:
    """
    Durum geçişi kontrolü.
    
    Geçerli geçişler:
    - PENDING -> CONFIRMED, CANCELLED
    - CONFIRMED -> SHIPPED, CANCELLED
    - SHIPPED -> DELIVERED, CANCELLED
    - DELIVERED -> (son durum, geçiş yok)
    - CANCELLED -> (son durum, geçiş yok)
    
    Args:
        from_status: Mevcut durum
        to_status: Hedef durum
        
    Returns:
        True eğer geçiş geçerliyse, False değilse
    """
    # Aynı duruma geçiş geçersiz
    if from_status == to_status:
        return False
    
    # Son durumlardan geçiş yapılamaz
    if from_status in (OrderStatus.DELIVERED, OrderStatus.CANCELLED):
        return False
    
    # Geçerli geçiş kuralları
    valid_transitions = {
        OrderStatus.PENDING: {OrderStatus.CONFIRMED, OrderStatus.CANCELLED},
        OrderStatus.CONFIRMED: {OrderStatus.SHIPPED, OrderStatus.CANCELLED},
        OrderStatus.SHIPPED: {OrderStatus.DELIVERED, OrderStatus.CANCELLED},
    }
    
    return to_status in valid_transitions.get(from_status, set())


def transition_order(order: "Order", new_status: OrderStatus) -> "Order":
    """
    Sipariş durumu değiştirme.
    
    Args:
        order: Sipariş nesnesi
        new_status: Yeni durum
        
    Returns:
        Güncellenmiş sipariş nesnesi
        
    Raises:
        InvalidTransitionError: Geçersiz durum geçişi durumunda
        AttributeError: Order nesnesinde status attribute'u yoksa
    """
    # Order nesnesinin status attribute'una sahip olup olmadığını kontrol et
    if not hasattr(order, 'status'):
        raise AttributeError("Order object must have a 'status' attribute")
    
    current_status = order.status
    
    # Geçiş kontrolü
    if not can_transition(current_status, new_status):
        raise InvalidTransitionError(
            f"Cannot transition from {current_status.value} to {new_status.value}"
        )
    
    # Yeni durum ata
    order.status = new_status
    
    return order
