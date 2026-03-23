"""
Property-based tests for order processor module.

Uses hypothesis for property-based testing with 100+ examples.

**Validates: Requirements 1.4**
"""
import pytest
from hypothesis import given, settings, strategies as st
from ecommerce_app.models import Order, OrderItem


class TestInvalidInputExceptionHandling:
    """
    Property 1: Invalid Input Exception Handling
    
    **Validates: Requirements 1.4**
    
    For any invalid order data (negative prices, missing required fields, 
    invalid customer types), the order processing system should raise 
    appropriate exceptions with descriptive messages rather than silently 
    failing or returning incorrect results.
    """
    
    @settings(max_examples=100)
    @given(st.floats(max_value=-0.01))
    def test_negative_unit_price_raises_exception(self, negative_price):
        """
        Property: Any negative unit price should raise ValueError.
        
        **Validates: Requirements 1.4**
        """
        with pytest.raises(ValueError, match="Unit price cannot be negative"):
            OrderItem("P001", 1, negative_price)
    
    @settings(max_examples=100)
    @given(st.integers(max_value=0))
    def test_non_positive_quantity_raises_exception(self, quantity):
        """
        Property: Any non-positive quantity should raise ValueError.
        
        **Validates: Requirements 1.4**
        """
        with pytest.raises(ValueError, match="Quantity must be positive"):
            OrderItem("P001", quantity, 50.0)
    
    @settings(max_examples=100)
    @given(st.text().filter(lambda x: x not in {"regular", "premium", "vip"}))
    def test_invalid_customer_type_raises_exception(self, invalid_type):
        """
        Property: Any customer type other than regular/premium/vip should raise ValueError.
        
        **Validates: Requirements 1.4**
        """
        items = [OrderItem("P001", 1, 50.0)]
        with pytest.raises(ValueError, match="Invalid customer type"):
            Order("ORD001", items, invalid_type, 100.0)
    
    @settings(max_examples=100)
    @given(st.floats(max_value=-0.01))
    def test_negative_subtotal_raises_exception(self, negative_subtotal):
        """
        Property: Any negative subtotal should raise ValueError.
        
        **Validates: Requirements 1.4**
        """
        items = [OrderItem("P001", 1, 50.0)]
        with pytest.raises(ValueError, match="Subtotal cannot be negative"):
            Order("ORD001", items, "regular", negative_subtotal)
    
    @settings(max_examples=100)
    @given(
        st.floats(min_value=-1000.0, max_value=-0.01),
        st.integers(min_value=-100, max_value=0)
    )
    def test_combined_invalid_inputs_raise_exceptions(self, negative_price, non_positive_qty):
        """
        Property: Multiple invalid inputs should each raise appropriate exceptions.
        
        **Validates: Requirements 1.4**
        """
        # Test negative price
        with pytest.raises(ValueError, match="Unit price cannot be negative"):
            OrderItem("P001", 1, negative_price)
        
        # Test non-positive quantity
        with pytest.raises(ValueError, match="Quantity must be positive"):
            OrderItem("P001", non_positive_qty, 50.0)
