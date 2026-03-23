"""
Unit tests for order processor module.

Tests cover:
- Discount calculation for different customer types
- Tax calculation
- Shipping cost calculation
- Boundary value tests
- Error handling for invalid inputs

**Validates: Requirements 1.5, 1.8**
"""
import pytest
from ecommerce_app.models import Order, OrderItem, OrderResult
from ecommerce_app.order_processor import (
    calculate_discount,
    calculate_tax,
    calculate_shipping,
    process_order
)


class TestDiscountCalculation:
    """Test discount calculation for different customer types."""
    
    def test_discount_calculation_regular_customer_above_threshold(self):
        """Regular customer with 100 TL or more gets 5% discount."""
        discount = calculate_discount(100.0, "regular")
        assert discount == 5.0
        
        discount = calculate_discount(200.0, "regular")
        assert discount == 10.0
    
    def test_discount_calculation_regular_customer_below_threshold(self):
        """Regular customer below 100 TL gets no discount."""
        discount = calculate_discount(99.0, "regular")
        assert discount == 0.0
        
        discount = calculate_discount(50.0, "regular")
        assert discount == 0.0
    
    def test_discount_calculation_premium_customer_above_threshold(self):
        """Premium customer with 100 TL or more gets 10% discount."""
        discount = calculate_discount(100.0, "premium")
        assert discount == 10.0
        
        discount = calculate_discount(200.0, "premium")
        assert discount == 20.0
    
    def test_discount_calculation_premium_customer_below_threshold(self):
        """Premium customer below 100 TL gets no discount."""
        discount = calculate_discount(99.0, "premium")
        assert discount == 0.0
    
    def test_discount_calculation_vip_customer_above_threshold(self):
        """VIP customer with 50 TL or more gets 15% discount."""
        discount = calculate_discount(50.0, "vip")
        assert discount == 7.5
        
        discount = calculate_discount(100.0, "vip")
        assert discount == 15.0
        
        discount = calculate_discount(200.0, "vip")
        assert discount == 30.0
    
    def test_discount_calculation_vip_customer_below_threshold(self):
        """VIP customer below 50 TL gets no discount."""
        discount = calculate_discount(49.0, "vip")
        assert discount == 0.0
    
    def test_discount_boundary_values(self):
        """Test discount calculation at exact boundary values."""
        # Regular customer at exactly 100 TL
        assert calculate_discount(100.0, "regular") == 5.0
        assert calculate_discount(99.99, "regular") == 0.0
        
        # Premium customer at exactly 100 TL
        assert calculate_discount(100.0, "premium") == 10.0
        assert calculate_discount(99.99, "premium") == 0.0
        
        # VIP customer at exactly 50 TL
        assert calculate_discount(50.0, "vip") == 7.5
        assert calculate_discount(49.99, "vip") == 0.0
    
    def test_discount_invalid_customer_type(self):
        """Invalid customer type returns 0 discount."""
        discount = calculate_discount(100.0, "invalid")
        assert discount == 0.0
        
        discount = calculate_discount(200.0, "unknown")
        assert discount == 0.0


class TestTaxCalculation:
    """Test tax calculation (20% VAT)."""
    
    def test_tax_calculation(self):
        """Tax should be 20% of the amount."""
        assert calculate_tax(100.0) == 20.0
        assert calculate_tax(50.0) == 10.0
        assert calculate_tax(250.0) == 50.0
    
    def test_tax_calculation_zero_amount(self):
        """Tax on zero amount should be zero."""
        assert calculate_tax(0.0) == 0.0
    
    def test_tax_calculation_small_amount(self):
        """Tax calculation should work for small amounts."""
        tax = calculate_tax(1.0)
        assert abs(tax - 0.20) < 0.001


class TestShippingCost:
    """Test shipping cost calculation."""
    
    def test_shipping_cost_free_threshold_all_customers(self):
        """Orders 200 TL or more get free shipping for all customer types."""
        assert calculate_shipping(200.0, "regular") == 0.0
        assert calculate_shipping(200.0, "premium") == 0.0
        assert calculate_shipping(200.0, "vip") == 0.0
        assert calculate_shipping(300.0, "regular") == 0.0
    
    def test_shipping_cost_below_threshold_regular(self):
        """Regular customers below 200 TL pay 30 TL shipping."""
        assert calculate_shipping(199.0, "regular") == 30.0
        assert calculate_shipping(100.0, "regular") == 30.0
        assert calculate_shipping(50.0, "regular") == 30.0
    
    def test_shipping_cost_premium_vip_threshold(self):
        """Premium and VIP customers get free shipping at 150 TL."""
        assert calculate_shipping(150.0, "premium") == 0.0
        assert calculate_shipping(150.0, "vip") == 0.0
        assert calculate_shipping(175.0, "premium") == 0.0
        assert calculate_shipping(175.0, "vip") == 0.0
    
    def test_shipping_cost_premium_vip_below_threshold(self):
        """Premium and VIP customers below 150 TL pay 30 TL shipping."""
        assert calculate_shipping(149.0, "premium") == 30.0
        assert calculate_shipping(149.0, "vip") == 30.0
        assert calculate_shipping(100.0, "premium") == 30.0
    
    def test_shipping_cost_boundary_values(self):
        """Test shipping cost at exact boundary values."""
        # 200 TL threshold for all customers
        assert calculate_shipping(200.0, "regular") == 0.0
        assert calculate_shipping(199.99, "regular") == 30.0
        
        # 150 TL threshold for premium/vip
        assert calculate_shipping(150.0, "premium") == 0.0
        assert calculate_shipping(149.99, "premium") == 30.0
        assert calculate_shipping(150.0, "vip") == 0.0
        assert calculate_shipping(149.99, "vip") == 30.0


class TestOrderProcessing:
    """Test complete order processing flow."""
    
    def test_process_order_regular_customer(self):
        """Process order for regular customer."""
        items = [OrderItem("P001", 2, 50.0)]
        order = Order("ORD001", items, "regular", 100.0)
        
        result = process_order(order)
        
        assert result.success is True
        assert result.order_id == "ORD001"
        assert result.subtotal == 100.0
        assert result.discount == 5.0  # 5% of 100
        assert result.tax == 19.0  # 20% of (100 - 5)
        assert result.shipping == 30.0  # Below 200 TL
        assert result.total == 144.0  # 95 + 19 + 30
    
    def test_process_order_premium_customer(self):
        """Process order for premium customer."""
        items = [OrderItem("P001", 3, 50.0)]
        order = Order("ORD002", items, "premium", 150.0)
        
        result = process_order(order)
        
        assert result.success is True
        assert result.subtotal == 150.0
        assert result.discount == 15.0  # 10% of 150
        assert result.tax == 27.0  # 20% of (150 - 15)
        assert result.shipping == 0.0  # Free at 150 TL for premium
        assert result.total == 162.0  # 135 + 27 + 0
    
    def test_process_order_vip_customer(self):
        """Process order for VIP customer."""
        items = [OrderItem("P001", 4, 50.0)]
        order = Order("ORD003", items, "vip", 200.0)
        
        result = process_order(order)
        
        assert result.success is True
        assert result.subtotal == 200.0
        assert result.discount == 30.0  # 15% of 200
        assert result.tax == 34.0  # 20% of (200 - 30)
        assert result.shipping == 0.0  # Free at 200 TL
        assert result.total == 204.0  # 170 + 34 + 0
    
    def test_process_order_small_amount(self):
        """Process small order with no discount."""
        items = [OrderItem("P001", 1, 30.0)]
        order = Order("ORD004", items, "regular", 30.0)
        
        result = process_order(order)
        
        assert result.success is True
        assert result.subtotal == 30.0
        assert result.discount == 0.0  # Below threshold
        assert result.tax == 6.0  # 20% of 30
        assert result.shipping == 30.0
        assert result.total == 66.0  # 30 + 6 + 30


class TestInvalidInputs:
    """Test error handling for invalid inputs."""
    
    def test_invalid_price_raises_error(self):
        """
        Feature: advanced-mutation-demos, Property 1: Invalid Input Exception Handling
        
        Negative unit price should raise ValueError.
        """
        with pytest.raises(ValueError, match="Unit price cannot be negative"):
            OrderItem("P001", 1, -10.0)
    
    def test_invalid_customer_type_raises_error(self):
        """
        Feature: advanced-mutation-demos, Property 1: Invalid Input Exception Handling
        
        Invalid customer type should raise ValueError.
        """
        items = [OrderItem("P001", 1, 50.0)]
        with pytest.raises(ValueError, match="Invalid customer type"):
            Order("ORD001", items, "invalid_type", 50.0)
    
    def test_negative_quantity_raises_error(self):
        """
        Feature: advanced-mutation-demos, Property 1: Invalid Input Exception Handling
        
        Negative or zero quantity should raise ValueError.
        """
        with pytest.raises(ValueError, match="Quantity must be positive"):
            OrderItem("P001", 0, 50.0)
        
        with pytest.raises(ValueError, match="Quantity must be positive"):
            OrderItem("P001", -1, 50.0)
    
    def test_negative_subtotal_raises_error(self):
        """
        Feature: advanced-mutation-demos, Property 1: Invalid Input Exception Handling
        
        Negative subtotal should raise ValueError.
        """
        items = [OrderItem("P001", 1, 50.0)]
        with pytest.raises(ValueError, match="Subtotal cannot be negative"):
            Order("ORD001", items, "regular", -50.0)
