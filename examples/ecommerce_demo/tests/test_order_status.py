"""
Tests for order status management module.

Tests cover:
- Valid state transitions
- Invalid state transitions
- All state combinations
- Edge cases (same state, final states)
"""
import pytest
from ecommerce_app.order_status import (
    OrderStatus,
    can_transition,
    transition_order,
    InvalidTransitionError
)
from ecommerce_app.models import Order, OrderItem


def create_test_order(status: OrderStatus = OrderStatus.PENDING) -> Order:
    """Helper function to create a test order"""
    items = [OrderItem(product_id="PROD-001", quantity=2, unit_price=50.0)]
    order = Order(
        order_id="ORD-001",
        items=items,
        customer_type="regular",
        subtotal=100.0,
        status=status
    )
    return order


def test_valid_transition_pending_to_confirmed():
    """Test valid transition from PENDING to CONFIRMED"""
    assert can_transition(OrderStatus.PENDING, OrderStatus.CONFIRMED) is True


def test_valid_transition_pending_to_cancelled():
    """Test valid transition from PENDING to CANCELLED"""
    assert can_transition(OrderStatus.PENDING, OrderStatus.CANCELLED) is True


def test_valid_transition_confirmed_to_shipped():
    """Test valid transition from CONFIRMED to SHIPPED"""
    assert can_transition(OrderStatus.CONFIRMED, OrderStatus.SHIPPED) is True


def test_valid_transition_confirmed_to_cancelled():
    """Test valid transition from CONFIRMED to CANCELLED"""
    assert can_transition(OrderStatus.CONFIRMED, OrderStatus.CANCELLED) is True


def test_valid_transition_shipped_to_delivered():
    """Test valid transition from SHIPPED to DELIVERED"""
    assert can_transition(OrderStatus.SHIPPED, OrderStatus.DELIVERED) is True


def test_valid_transition_shipped_to_cancelled():
    """Test valid transition from SHIPPED to CANCELLED"""
    assert can_transition(OrderStatus.SHIPPED, OrderStatus.CANCELLED) is True


def test_invalid_transition_same_state():
    """Test that transitioning to the same state is invalid"""
    assert can_transition(OrderStatus.PENDING, OrderStatus.PENDING) is False
    assert can_transition(OrderStatus.CONFIRMED, OrderStatus.CONFIRMED) is False
    assert can_transition(OrderStatus.SHIPPED, OrderStatus.SHIPPED) is False


def test_invalid_transition_from_delivered():
    """Test that no transitions are allowed from DELIVERED"""
    assert can_transition(OrderStatus.DELIVERED, OrderStatus.PENDING) is False
    assert can_transition(OrderStatus.DELIVERED, OrderStatus.CONFIRMED) is False
    assert can_transition(OrderStatus.DELIVERED, OrderStatus.SHIPPED) is False
    assert can_transition(OrderStatus.DELIVERED, OrderStatus.CANCELLED) is False


def test_invalid_transition_from_cancelled():
    """Test that no transitions are allowed from CANCELLED"""
    assert can_transition(OrderStatus.CANCELLED, OrderStatus.PENDING) is False
    assert can_transition(OrderStatus.CANCELLED, OrderStatus.CONFIRMED) is False
    assert can_transition(OrderStatus.CANCELLED, OrderStatus.SHIPPED) is False
    assert can_transition(OrderStatus.CANCELLED, OrderStatus.DELIVERED) is False


def test_invalid_transition_pending_to_shipped():
    """Test invalid transition from PENDING directly to SHIPPED"""
    assert can_transition(OrderStatus.PENDING, OrderStatus.SHIPPED) is False


def test_invalid_transition_pending_to_delivered():
    """Test invalid transition from PENDING directly to DELIVERED"""
    assert can_transition(OrderStatus.PENDING, OrderStatus.DELIVERED) is False


def test_invalid_transition_confirmed_to_delivered():
    """Test invalid transition from CONFIRMED directly to DELIVERED"""
    assert can_transition(OrderStatus.CONFIRMED, OrderStatus.DELIVERED) is False


def test_invalid_transition_confirmed_to_pending():
    """Test invalid backward transition from CONFIRMED to PENDING"""
    assert can_transition(OrderStatus.CONFIRMED, OrderStatus.PENDING) is False


def test_invalid_transition_shipped_to_pending():
    """Test invalid backward transition from SHIPPED to PENDING"""
    assert can_transition(OrderStatus.SHIPPED, OrderStatus.PENDING) is False


def test_invalid_transition_shipped_to_confirmed():
    """Test invalid backward transition from SHIPPED to CONFIRMED"""
    assert can_transition(OrderStatus.SHIPPED, OrderStatus.CONFIRMED) is False


def test_transition_order_success():
    """Test successful order status transition"""
    order = create_test_order(OrderStatus.PENDING)
    
    updated_order = transition_order(order, OrderStatus.CONFIRMED)
    
    assert updated_order.status == OrderStatus.CONFIRMED
    assert updated_order.order_id == "ORD-001"


def test_transition_order_invalid_raises_error():
    """Test that invalid transition raises InvalidTransitionError"""
    order = create_test_order(OrderStatus.PENDING)
    
    with pytest.raises(InvalidTransitionError) as exc_info:
        transition_order(order, OrderStatus.SHIPPED)
    
    assert "Cannot transition" in str(exc_info.value)
    assert "pending" in str(exc_info.value)
    assert "shipped" in str(exc_info.value)


def test_transition_order_from_delivered_raises_error():
    """Test that transition from DELIVERED raises error"""
    order = create_test_order(OrderStatus.DELIVERED)
    
    with pytest.raises(InvalidTransitionError):
        transition_order(order, OrderStatus.CANCELLED)


def test_transition_order_from_cancelled_raises_error():
    """Test that transition from CANCELLED raises error"""
    order = create_test_order(OrderStatus.CANCELLED)
    
    with pytest.raises(InvalidTransitionError):
        transition_order(order, OrderStatus.CONFIRMED)


def test_transition_order_same_state_raises_error():
    """Test that transitioning to same state raises error"""
    order = create_test_order(OrderStatus.CONFIRMED)
    
    with pytest.raises(InvalidTransitionError):
        transition_order(order, OrderStatus.CONFIRMED)


def test_all_state_combinations_pending():
    """Test all possible transitions from PENDING state"""
    # Valid transitions
    assert can_transition(OrderStatus.PENDING, OrderStatus.CONFIRMED) is True
    assert can_transition(OrderStatus.PENDING, OrderStatus.CANCELLED) is True
    
    # Invalid transitions
    assert can_transition(OrderStatus.PENDING, OrderStatus.PENDING) is False
    assert can_transition(OrderStatus.PENDING, OrderStatus.SHIPPED) is False
    assert can_transition(OrderStatus.PENDING, OrderStatus.DELIVERED) is False


def test_all_state_combinations_confirmed():
    """Test all possible transitions from CONFIRMED state"""
    # Valid transitions
    assert can_transition(OrderStatus.CONFIRMED, OrderStatus.SHIPPED) is True
    assert can_transition(OrderStatus.CONFIRMED, OrderStatus.CANCELLED) is True
    
    # Invalid transitions
    assert can_transition(OrderStatus.CONFIRMED, OrderStatus.CONFIRMED) is False
    assert can_transition(OrderStatus.CONFIRMED, OrderStatus.PENDING) is False
    assert can_transition(OrderStatus.CONFIRMED, OrderStatus.DELIVERED) is False


def test_all_state_combinations_shipped():
    """Test all possible transitions from SHIPPED state"""
    # Valid transitions
    assert can_transition(OrderStatus.SHIPPED, OrderStatus.DELIVERED) is True
    assert can_transition(OrderStatus.SHIPPED, OrderStatus.CANCELLED) is True
    
    # Invalid transitions
    assert can_transition(OrderStatus.SHIPPED, OrderStatus.SHIPPED) is False
    assert can_transition(OrderStatus.SHIPPED, OrderStatus.PENDING) is False
    assert can_transition(OrderStatus.SHIPPED, OrderStatus.CONFIRMED) is False


def test_all_state_combinations_delivered():
    """Test all possible transitions from DELIVERED state (none allowed)"""
    assert can_transition(OrderStatus.DELIVERED, OrderStatus.PENDING) is False
    assert can_transition(OrderStatus.DELIVERED, OrderStatus.CONFIRMED) is False
    assert can_transition(OrderStatus.DELIVERED, OrderStatus.SHIPPED) is False
    assert can_transition(OrderStatus.DELIVERED, OrderStatus.DELIVERED) is False
    assert can_transition(OrderStatus.DELIVERED, OrderStatus.CANCELLED) is False


def test_all_state_combinations_cancelled():
    """Test all possible transitions from CANCELLED state (none allowed)"""
    assert can_transition(OrderStatus.CANCELLED, OrderStatus.PENDING) is False
    assert can_transition(OrderStatus.CANCELLED, OrderStatus.CONFIRMED) is False
    assert can_transition(OrderStatus.CANCELLED, OrderStatus.SHIPPED) is False
    assert can_transition(OrderStatus.CANCELLED, OrderStatus.DELIVERED) is False
    assert can_transition(OrderStatus.CANCELLED, OrderStatus.CANCELLED) is False


def test_transition_order_without_status_attribute():
    """Test transition_order with object missing status attribute"""
    # Create a simple object without status attribute
    class InvalidOrder:
        pass
    
    invalid_order = InvalidOrder()
    
    with pytest.raises(AttributeError) as exc_info:
        transition_order(invalid_order, OrderStatus.CONFIRMED)
    
    assert "status" in str(exc_info.value)


def test_complete_workflow_happy_path():
    """Test complete order workflow from PENDING to DELIVERED"""
    order = create_test_order(OrderStatus.PENDING)
    
    # PENDING -> CONFIRMED
    order = transition_order(order, OrderStatus.CONFIRMED)
    assert order.status == OrderStatus.CONFIRMED
    
    # CONFIRMED -> SHIPPED
    order = transition_order(order, OrderStatus.SHIPPED)
    assert order.status == OrderStatus.SHIPPED
    
    # SHIPPED -> DELIVERED
    order = transition_order(order, OrderStatus.DELIVERED)
    assert order.status == OrderStatus.DELIVERED


def test_complete_workflow_cancellation_from_pending():
    """Test order cancellation from PENDING state"""
    order = create_test_order(OrderStatus.PENDING)
    
    # PENDING -> CANCELLED
    order = transition_order(order, OrderStatus.CANCELLED)
    assert order.status == OrderStatus.CANCELLED
    
    # Cannot transition from CANCELLED
    with pytest.raises(InvalidTransitionError):
        transition_order(order, OrderStatus.CONFIRMED)


def test_complete_workflow_cancellation_from_confirmed():
    """Test order cancellation from CONFIRMED state"""
    order = create_test_order(OrderStatus.PENDING)
    order = transition_order(order, OrderStatus.CONFIRMED)
    
    # CONFIRMED -> CANCELLED
    order = transition_order(order, OrderStatus.CANCELLED)
    assert order.status == OrderStatus.CANCELLED


def test_complete_workflow_cancellation_from_shipped():
    """Test order cancellation from SHIPPED state"""
    order = create_test_order(OrderStatus.PENDING)
    order = transition_order(order, OrderStatus.CONFIRMED)
    order = transition_order(order, OrderStatus.SHIPPED)
    
    # SHIPPED -> CANCELLED
    order = transition_order(order, OrderStatus.CANCELLED)
    assert order.status == OrderStatus.CANCELLED
