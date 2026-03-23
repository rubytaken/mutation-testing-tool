"""Stok yönetimi modülü"""


class InventoryManager:
    """Stok yönetimi sınıfı"""
    
    def __init__(self):
        """Stok yöneticisini başlat"""
        self._stock: dict[str, int] = {}
        self._reserved: dict[str, int] = {}
    
    def check_stock(self, product_id: str, quantity: int) -> bool:
        """
        Stok kontrolü yapar
        
        Args:
            product_id: Ürün ID'si
            quantity: İstenen miktar
            
        Returns:
            bool: Yeterli stok varsa True, yoksa False
        """
        available = self._stock.get(product_id, 0)
        reserved = self._reserved.get(product_id, 0)
        available_stock = available - reserved
        
        return available_stock >= quantity
    
    def reserve_stock(self, product_id: str, quantity: int) -> bool:
        """
        Stok rezervasyonu yapar
        
        Args:
            product_id: Ürün ID'si
            quantity: Rezerve edilecek miktar
            
        Returns:
            bool: Rezervasyon başarılıysa True, başarısızsa False
        """
        if not self.check_stock(product_id, quantity):
            return False
        
        current_reserved = self._reserved.get(product_id, 0)
        self._reserved[product_id] = current_reserved + quantity
        
        return True
    
    def release_stock(self, product_id: str, quantity: int) -> None:
        """
        Rezerve edilmiş stoku serbest bırakır
        
        Args:
            product_id: Ürün ID'si
            quantity: Serbest bırakılacak miktar
        """
        current_reserved = self._reserved.get(product_id, 0)
        new_reserved = max(0, current_reserved - quantity)
        
        if new_reserved == 0:
            self._reserved.pop(product_id, None)
        else:
            self._reserved[product_id] = new_reserved
    
    def add_stock(self, product_id: str, quantity: int) -> None:
        """
        Stok ekler (test ve setup için yardımcı metod)
        
        Args:
            product_id: Ürün ID'si
            quantity: Eklenecek miktar
        """
        current_stock = self._stock.get(product_id, 0)
        self._stock[product_id] = current_stock + quantity
    
    def get_available_stock(self, product_id: str) -> int:
        """
        Mevcut stok miktarını döndürür (rezerve edilmemiş)
        
        Args:
            product_id: Ürün ID'si
            
        Returns:
            int: Mevcut stok miktarı
        """
        total = self._stock.get(product_id, 0)
        reserved = self._reserved.get(product_id, 0)
        return total - reserved
