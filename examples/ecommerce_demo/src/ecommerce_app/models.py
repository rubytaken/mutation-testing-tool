"""
Data models for e-commerce order processing.
"""
from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .order_status import OrderStatus


@dataclass
class OrderItem:
    """Sipariş kalemi"""
    product_id: str
    quantity: int
    unit_price: float
    
    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError(f"Quantity must be positive, got {self.quantity}")
        if self.unit_price < 0:
            raise ValueError(f"Unit price cannot be negative, got {self.unit_price}")


@dataclass
class Order:
    """Sipariş veri modeli"""
    order_id: str
    items: List[OrderItem]
    customer_type: str  # "regular", "premium", "vip"
    subtotal: float
    status: "OrderStatus" = None  # Sipariş durumu, default None (will be set to PENDING)
    
    def __post_init__(self):
        valid_customer_types = {"regular", "premium", "vip"}
        if self.customer_type not in valid_customer_types:
            raise ValueError(
                f"Invalid customer type: {self.customer_type}. "
                f"Must be one of {valid_customer_types}"
            )
        if self.subtotal < 0:
            raise ValueError(f"Subtotal cannot be negative, got {self.subtotal}")
        
        # Set default status to PENDING if not provided
        if self.status is None:
            from .order_status import OrderStatus
            self.status = OrderStatus.PENDING


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
