"""
Tests for inventory management module.

Tests cover:
- Stock checking with sufficient and insufficient stock
- Stock reservation success and failure scenarios
- Stock release operations
"""
import pytest
from ecommerce_app.inventory import InventoryManager, InsufficientStockError


def test_stock_check_sufficient():
    """Test stock check when sufficient stock is available"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 100)
    
    assert inventory.check_stock("PROD-001", 50) is True
    assert inventory.check_stock("PROD-001", 100) is True


def test_stock_check_insufficient():
    """Test stock check when insufficient stock is available"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 50)
    
    assert inventory.check_stock("PROD-001", 51) is False
    assert inventory.check_stock("PROD-001", 100) is False


def test_stock_check_zero_quantity():
    """Test stock check with zero or negative quantity"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 100)
    
    assert inventory.check_stock("PROD-001", 0) is False
    assert inventory.check_stock("PROD-001", -5) is False


def test_stock_check_nonexistent_product():
    """Test stock check for product that doesn't exist"""
    inventory = InventoryManager()
    
    assert inventory.check_stock("NONEXISTENT", 10) is False


def test_reserve_stock_success():
    """Test successful stock reservation"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 100)
    
    result = inventory.reserve_stock("PROD-001", 30)
    
    assert result is True
    assert inventory.get_available_stock("PROD-001") == 70


def test_reserve_stock_multiple_times():
    """Test multiple stock reservations"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 100)
    
    inventory.reserve_stock("PROD-001", 30)
    inventory.reserve_stock("PROD-001", 20)
    
    assert inventory.get_available_stock("PROD-001") == 50


def test_reserve_stock_failure():
    """Test stock reservation failure when insufficient stock"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 50)
    
    with pytest.raises(InsufficientStockError) as exc_info:
        inventory.reserve_stock("PROD-001", 51)
    
    assert "Insufficient stock" in str(exc_info.value)
    assert "PROD-001" in str(exc_info.value)


def test_reserve_stock_exact_amount():
    """Test reserving exact available stock"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 50)
    
    result = inventory.reserve_stock("PROD-001", 50)
    
    assert result is True
    assert inventory.get_available_stock("PROD-001") == 0


def test_reserve_stock_invalid_quantity():
    """Test stock reservation with invalid quantity"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 100)
    
    with pytest.raises(ValueError):
        inventory.reserve_stock("PROD-001", 0)
    
    with pytest.raises(ValueError):
        inventory.reserve_stock("PROD-001", -10)


def test_release_stock():
    """Test stock release after reservation"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 100)
    
    inventory.reserve_stock("PROD-001", 30)
    assert inventory.get_available_stock("PROD-001") == 70
    
    inventory.release_stock("PROD-001", 30)
    assert inventory.get_available_stock("PROD-001") == 100


def test_release_stock_partial():
    """Test partial stock release"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 100)
    
    inventory.reserve_stock("PROD-001", 50)
    assert inventory.get_available_stock("PROD-001") == 50
    
    inventory.release_stock("PROD-001", 20)
    assert inventory.get_available_stock("PROD-001") == 70


def test_release_stock_nonexistent_reservation():
    """Test releasing stock when no reservation exists"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 100)
    
    # Should not raise error
    inventory.release_stock("PROD-001", 10)
    assert inventory.get_available_stock("PROD-001") == 100


def test_release_stock_invalid_quantity():
    """Test stock release with invalid quantity"""
    inventory = InventoryManager()
    inventory.set_stock("PROD-001", 100)
    
    with pytest.raises(ValueError):
        inventory.release_stock("PROD-001", 0)
    
    with pytest.raises(ValueError):
        inventory.release_stock("PROD-001", -10)


def test_set_stock_negative_quantity():
    """Test setting negative stock quantity"""
    inventory = InventoryManager()
    
    with pytest.raises(ValueError) as exc_info:
        inventory.set_stock("PROD-001", -10)
    
    assert "cannot be negative" in str(exc_info.value)
