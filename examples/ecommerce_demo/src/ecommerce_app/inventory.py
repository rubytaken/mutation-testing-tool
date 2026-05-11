"""
Inventory management module.
Handles stock checking, reservation, and release operations.
"""
from typing import Dict


# Raised when trying to reserve more stock than available
class InsufficientStockError(Exception):
    """Yetersiz stok hatası"""
    pass


# Manages stock levels and reservations for products
class InventoryManager:
    """Stok yönetimi sınıfı"""
    
    def __init__(self):
        """Initialize inventory with stock levels"""
        self._stock: Dict[str, int] = {}
        self._reserved: Dict[str, int] = {}
    
    # Set total stock level for a product
    def set_stock(self, product_id: str, quantity: int) -> None:
        """
        Ürün stoğunu ayarla
        
        Args:
            product_id: Ürün ID
            quantity: Stok miktarı
        """
        if quantity < 0:
            raise ValueError(f"Stock quantity cannot be negative: {quantity}")
        self._stock[product_id] = quantity
        if product_id not in self._reserved:
            self._reserved[product_id] = 0
    
    # Calculate stock that's actually available (total minus reserved)
    def get_available_stock(self, product_id: str) -> int:
        """
        Mevcut stok miktarını getir (rezerve edilmemiş)
        
        Args:
            product_id: Ürün ID
            
        Returns:
            Mevcut stok miktarı
        """
        total = self._stock.get(product_id, 0)
        reserved = self._reserved.get(product_id, 0)
        return total - reserved
    
    # Check if enough stock is available for a request
    def check_stock(self, product_id: str, quantity: int) -> bool:
        """
        Stok kontrolü
        
        Args:
            product_id: Ürün ID
            quantity: İstenen miktar
            
        Returns:
            True eğer yeterli stok varsa, False değilse
        """
        if quantity <= 0:
            return False
        
        available = self.get_available_stock(product_id)
        return available >= quantity
    
    # Reserve stock for an order (reduces available stock)
    def reserve_stock(self, product_id: str, quantity: int) -> bool:
        """
        Stok rezervasyonu
        
        Args:
            product_id: Ürün ID
            quantity: Rezerve edilecek miktar
            
        Returns:
            True eğer rezervasyon başarılıysa, False değilse
            
        Raises:
            InsufficientStockError: Yetersiz stok durumunda
        """
        if quantity <= 0:
            raise ValueError(f"Reservation quantity must be positive: {quantity}")
        
        if not self.check_stock(product_id, quantity):
            raise InsufficientStockError(
                f"Insufficient stock for product {product_id}. "
                f"Requested: {quantity}, Available: {self.get_available_stock(product_id)}"
            )
        
        # Rezerve et
        if product_id not in self._reserved:
            self._reserved[product_id] = 0
        self._reserved[product_id] += quantity
        
        return True
    
    # Release reserved stock back to available pool
    def release_stock(self, product_id: str, quantity: int) -> None:
        """
        Stok serbest bırakma (rezervasyonu iptal et)
        
        Args:
            product_id: Ürün ID
            quantity: Serbest bırakılacak miktar
        """
        if quantity <= 0:
            raise ValueError(f"Release quantity must be positive: {quantity}")
        
        if product_id not in self._reserved:
            return
        
        # Rezervasyonu azalt
        self._reserved[product_id] = max(0, self._reserved[product_id] - quantity)
