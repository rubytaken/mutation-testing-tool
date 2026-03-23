"""
Inventory management module.
Handles stock checking, reservation, and release operations.
"""
from typing import Dict


class InsufficientStockError(Exception):
    """Yetersiz stok hatası"""
    pass


class InventoryManager:
    """Stok yönetimi sınıfı"""
    
    def __init__(self):
        """Initialize inventory with stock levels"""
        self._stock: Dict[str, int] = {}
        self._reserved: Dict[str, int] = {}
    
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
