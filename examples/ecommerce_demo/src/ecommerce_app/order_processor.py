"""
Order processing module with discount, tax, and shipping calculations.

This module demonstrates mutation testing with:
- Comparison operators (>=, <=, ==) in discount thresholds
- Logical operators (and, or) in eligibility checks
- Arithmetic operators in price calculations
"""
from .models import Order, OrderResult


def calculate_discount(subtotal: float, customer_type: str) -> float:
    """
    İndirim hesaplama
    
    Kurallar:
    - regular: 100 TL üzeri %5
    - premium: 100 TL üzeri %10
    - vip: 50 TL üzeri %15
    
    Args:
        subtotal: Ara toplam (KDV hariç)
        customer_type: Müşteri tipi ("regular", "premium", "vip")
        
    Returns:
        İndirim tutarı
    """
    if customer_type == "regular":
        if subtotal >= 100:
            return subtotal * 0.05
        return 0.0
    elif customer_type == "premium":
        if subtotal >= 100:
            return subtotal * 0.10
        return 0.0
    elif customer_type == "vip":
        if subtotal >= 50:
            return subtotal * 0.15
        return 0.0
    else:
        return 0.0


def calculate_tax(amount: float) -> float:
    """
    KDV hesaplama (%20)
    
    Args:
        amount: KDV hesaplanacak tutar
        
    Returns:
        KDV tutarı
    """
    return amount * 0.20


def calculate_shipping(subtotal: float, customer_type: str) -> float:
    """
    Kargo ücreti hesaplama
    
    Kurallar:
    - 200 TL üzeri ücretsiz
    - premium/vip: 150 TL üzeri ücretsiz
    - altında: 30 TL
    
    Args:
        subtotal: Ara toplam (KDV hariç)
        customer_type: Müşteri tipi ("regular", "premium", "vip")
        
    Returns:
        Kargo ücreti
    """
    # 200 TL üzeri tüm müşteriler için ücretsiz
    if subtotal >= 200:
        return 0.0
    
    # Premium ve VIP müşteriler için 150 TL üzeri ücretsiz
    if (customer_type == "premium" or customer_type == "vip") and subtotal >= 150:
        return 0.0
    
    # Diğer durumlarda 30 TL
    return 30.0


def process_order(order: Order) -> OrderResult:
    """
    Sipariş işleme ana fonksiyonu
    
    İşlem adımları:
    1. İndirim hesapla
    2. İndirimli tutarı hesapla
    3. KDV hesapla
    4. Kargo ücreti hesapla
    5. Toplam tutarı hesapla
    
    Args:
        order: İşlenecek sipariş
        
    Returns:
        Sipariş işleme sonucu
    """
    # İndirim hesapla
    discount = calculate_discount(order.subtotal, order.customer_type)
    
    # İndirimli tutar
    discounted_amount = order.subtotal - discount
    
    # KDV hesapla (indirimli tutar üzerinden)
    tax = calculate_tax(discounted_amount)
    
    # Kargo ücreti hesapla
    shipping = calculate_shipping(order.subtotal, order.customer_type)
    
    # Toplam tutar
    total = discounted_amount + tax + shipping
    
    return OrderResult(
        success=True,
        order_id=order.order_id,
        subtotal=order.subtotal,
        discount=discount,
        tax=tax,
        shipping=shipping,
        total=total,
        message="Sipariş başarıyla işlendi"
    )
