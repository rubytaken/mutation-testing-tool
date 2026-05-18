"""E-Commerce veri modelleri"""
from dataclasses import dataclass


@dataclass
class OrderItem:
    """Sipariş kalemi"""
    product_id: str
    quantity: int
    unit_price: float


@dataclass
class Order:
    """Sipariş veri modeli"""
    order_id: str
    items: list[OrderItem]
    customer_type: str  # "regular", "premium", "vip"
    subtotal: float


@dataclass
class OrderResult:
    """Sipariş işleme sonucu"""
    success: bool
    order_id: str
    subtotal: float
    discount: float
    tax: float
    shipping: float
    total: float
    message: str
