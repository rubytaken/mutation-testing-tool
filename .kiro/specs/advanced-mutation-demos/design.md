# Design Document: Advanced Mutation Testing Demos

## Overview

Bu tasarım, mutation testing tool için gelişmiş demo projeleri oluşturma özelliğini tanımlar. Mevcut demo'lar (beginner_demo, ci_gate_demo, timeout_lab_demo) temel seviyede olup sadece 1-2 fonksiyon içermektedir. Yeni demo'lar gerçek dünya senaryolarını yansıtacak, farklı mutation operatörlerini gösterecek ve karmaşık iş mantığını içerecek şekilde tasarlanacaktır.

Bu tasarım 5 yeni demo projesi içerir:
1. E-Commerce Order Processing Demo
2. Data Structure Manipulation Demo
3. Authentication and Authorization Demo
4. Parser and Serializer Demo
5. Retry and Timeout Logic Demo

Her demo, mutation testing'in gücünü farklı bir açıdan gösterecek ve geliştiricilere gerçekçi örnekler sunacaktır.

## Architecture

### High-Level Structure

```
examples/
├── beginner_demo/              (mevcut)
├── ci_gate_demo/               (mevcut)
├── timeout_lab_demo/           (mevcut)
├── ecommerce_demo/             (yeni)
├── data_structures_demo/       (yeni)
├── auth_demo/                  (yeni)
├── parser_demo/                (yeni)
└── retry_logic_demo/           (yeni)
```

Her demo projesi şu yapıyı takip edecek:

```
demo_name/
├── README.md                   # Türkçe açıklama ve öğrenme hedefleri
├── pyproject.toml              # Mutation tool konfigürasyonu
├── src/
│   └── demo_package/
│       ├── __init__.py
│       ├── module1.py          # Ana iş mantığı
│       └── module2.py          # Yardımcı modüller
└── tests/
    ├── test_module1.py         # Kapsamlı testler
    └── test_module2.py
```

### Design Principles

1. **Realistic Scenarios**: Her demo gerçek dünya problemlerini yansıtır
2. **Operator Coverage**: Her demo farklı mutation operatörlerini gösterir
3. **Progressive Complexity**: Demo'lar basit'ten karmaşık'a doğru sıralanır
4. **Educational Value**: Her demo belirli bir testing konseptini öğretir
5. **Self-Contained**: Her demo bağımsız çalışabilir

## Components and Interfaces

### 1. E-Commerce Order Processing Demo

#### Module: `order_processor.py`

```python
class Order:
    """Sipariş veri modeli"""
    order_id: str
    items: list[OrderItem]
    customer_type: str  # "regular", "premium", "vip"
    subtotal: float
    
class OrderItem:
    """Sipariş kalemi"""
    product_id: str
    quantity: int
    unit_price: float
    
def calculate_discount(subtotal: float, customer_type: str) -> float:
    """
    İndirim hesaplama
    - regular: 100 TL üzeri %5
    - premium: 100 TL üzeri %10
    - vip: 50 TL üzeri %15
    """
    
def calculate_tax(amount: float) -> float:
    """KDV hesaplama (%20)"""
    
def calculate_shipping(subtotal: float, customer_type: str) -> float:
    """
    Kargo ücreti hesaplama
    - 200 TL üzeri ücretsiz
    - premium/vip: 150 TL üzeri ücretsiz
    - altında: 30 TL
    """
    
def process_order(order: Order) -> OrderResult:
    """Sipariş işleme ana fonksiyonu"""
```

#### Module: `inventory.py`

```python
class InventoryManager:
    """Stok yönetimi"""
    
    def check_stock(self, product_id: str, quantity: int) -> bool:
        """Stok kontrolü"""
        
    def reserve_stock(self, product_id: str, quantity: int) -> bool:
        """Stok rezervasyonu"""
        
    def release_stock(self, product_id: str, quantity: int) -> None:
        """Stok serbest bırakma"""
```

#### Module: `order_status.py`

```python
class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    
def can_transition(from_status: OrderStatus, to_status: OrderStatus) -> bool:
    """Durum geçişi kontrolü"""
    
def transition_order(order: Order, new_status: OrderStatus) -> Order:
    """Sipariş durumu değiştirme"""
```

**Demonstrated Mutation Operators:**
- Comparison: `>=`, `<=`, `==` (indirim eşikleri)
- Logical: `and`, `or` (müşteri tipi kontrolleri)
- Arithmetic: `+`, `-`, `*`, `/` (fiyat hesaplamaları)

### 2. Data Structure Manipulation Demo

#### Module: `list_operations.py`

```python
def filter_positive(numbers: list[int]) -> list[int]:
    """Pozitif sayıları filtrele"""
    
def sort_by_length(strings: list[str]) -> list[str]:
    """String'leri uzunluğa göre sırala"""
    
def transform_to_upper(strings: list[str]) -> list[str]:
    """String'leri büyük harfe çevir"""
    
def chunk_list(items: list[Any], chunk_size: int) -> list[list[Any]]:
    """Listeyi parçalara böl"""
```

#### Module: `dict_operations.py`

```python
def merge_dicts(dict1: dict, dict2: dict, prefer_first: bool = True) -> dict:
    """İki dictionary'yi birleştir"""
    
def validate_keys(data: dict, required_keys: set[str]) -> bool:
    """Gerekli anahtarların varlığını kontrol et"""
    
def get_nested(data: dict, path: str, default: Any = None) -> Any:
    """İç içe dictionary'den değer al (örn: "user.address.city")"""
    
def flatten_dict(nested: dict, separator: str = ".") -> dict:
    """İç içe dictionary'yi düzleştir"""
```

#### Module: `set_operations.py`

```python
def find_common(set1: set, set2: set) -> set:
    """İki kümenin kesişimini bul"""
    
def find_unique(set1: set, set2: set) -> set:
    """İlk kümede olup ikincide olmayan elemanlar"""
    
def combine_all(sets: list[set]) -> set:
    """Tüm kümeleri birleştir"""
```

**Demonstrated Mutation Operators:**
- Comparison: `>`, `<`, `==` (uzunluk kontrolleri)
- Arithmetic: `+`, `-` (boyut hesaplamaları)
- Logical: `and`, `or` (anahtar varlık kontrolleri)
- Membership: `in`, `not in` (eleman kontrolü)

### 3. Authentication and Authorization Demo

#### Module: `password_validator.py`

```python
def validate_password(password: str) -> tuple[bool, str]:
    """
    Şifre karmaşıklık kuralları:
    - En az 8 karakter
    - En az 1 büyük harf
    - En az 1 küçük harf
    - En az 1 rakam
    - En az 1 özel karakter
    """
    
def password_strength(password: str) -> str:
    """Şifre gücü: "weak", "medium", "strong" """
```

#### Module: `permissions.py`

```python
class Role(Enum):
    GUEST = "guest"
    USER = "user"
    ADMIN = "admin"
    
class Permission(Enum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN_PANEL = "admin_panel"
    
def has_permission(role: Role, permission: Permission) -> bool:
    """Rol bazlı yetki kontrolü"""
    
def can_access_resource(role: Role, resource_owner: str, current_user: str) -> bool:
    """Kaynak erişim kontrolü"""
```

#### Module: `session.py`

```python
class Session:
    user_id: str
    created_at: datetime
    expires_at: datetime
    role: Role
    
def is_session_valid(session: Session, current_time: datetime) -> bool:
    """Oturum geçerlilik kontrolü"""
    
def extend_session(session: Session, minutes: int) -> Session:
    """Oturum süresini uzat"""
    
def calculate_remaining_time(session: Session, current_time: datetime) -> int:
    """Kalan süreyi dakika cinsinden hesapla"""
```

**Demonstrated Mutation Operators:**
- Comparison: `>=`, `<=` (şifre uzunluğu, oturum süresi)
- Logical: `and`, `or` (bileşik yetki kuralları)
- Boolean: `True`/`False` (yetki sonuçları)

### 4. Parser and Serializer Demo

#### Module: `config_parser.py`

```python
def parse_config(content: str) -> dict[str, str]:
    """
    Basit key=value formatını parse et
    
    Örnek:
    ```
    host=localhost
    port=8080
    debug=true
    ```
    """
    
def format_config(config: dict[str, str]) -> str:
    """Config dictionary'yi text formatına çevir"""
    
def validate_config(config: dict[str, str], schema: dict[str, type]) -> bool:
    """Config'i şemaya göre doğrula"""
```

#### Module: `json_serializer.py`

```python
class User:
    id: int
    name: str
    email: str
    metadata: dict[str, Any]
    
def serialize_user(user: User) -> str:
    """User nesnesini JSON'a çevir"""
    
def deserialize_user(json_str: str) -> User:
    """JSON'dan User nesnesi oluştur"""
    
def serialize_nested(data: dict) -> str:
    """İç içe yapıları JSON'a çevir"""
```

**Demonstrated Mutation Operators:**
- Comparison: `==`, `!=` (string karşılaştırma)
- String: değişiklikler (parsing logic)
- Logical: `and`, `or` (validation logic)

### 5. Retry and Timeout Logic Demo

#### Module: `backoff.py`

```python
def calculate_backoff(attempt: int, base_delay: float, max_delay: float) -> float:
    """
    Exponential backoff hesaplama
    delay = min(base_delay * (2 ** attempt), max_delay)
    """
    
def add_jitter(delay: float, jitter_factor: float = 0.1) -> float:
    """Delay'e rastgele jitter ekle"""
```

#### Module: `retry_logic.py`

```python
class RetryableError(Exception):
    """Tekrar denenebilir hata"""
    
class NonRetryableError(Exception):
    """Tekrar denenemez hata"""
    
def should_retry(error: Exception, attempt: int, max_attempts: int) -> bool:
    """Tekrar deneme kararı"""
    
def execute_with_retry(
    func: Callable,
    max_attempts: int,
    base_delay: float
) -> Any:
    """Fonksiyonu retry logic ile çalıştır"""
```

#### Module: `circuit_breaker.py`

```python
class CircuitState(Enum):
    CLOSED = "closed"      # Normal çalışma
    OPEN = "open"          # Devre açık, istekler reddediliyor
    HALF_OPEN = "half_open"  # Test aşaması
    
class CircuitBreaker:
    state: CircuitState
    failure_count: int
    failure_threshold: int
    success_count: int
    last_failure_time: datetime
    
    def can_execute(self) -> bool:
        """İstek yapılabilir mi?"""
        
    def record_success(self) -> None:
        """Başarılı istek kaydı"""
        
    def record_failure(self) -> None:
        """Başarısız istek kaydı"""
        
    def get_next_state(self) -> CircuitState:
        """Sonraki durum hesaplama"""
```

**Demonstrated Mutation Operators:**
- Arithmetic: `*`, `**`, `+` (backoff hesaplamaları)
- Comparison: `>=`, `<=` (retry limit kontrolleri)
- Logical: `and`, `or` (retry kararları)

### 6. Tool Verification Module

#### Module: `verify_tool.py`

```python
def run_verification() -> VerificationResult:
    """
    Mutation tool'un doğru çalıştığını doğrula
    1. Zayıf test senaryosu oluştur
    2. Mutation testing çalıştır
    3. Survivor'ların tespit edildiğini kontrol et
    4. JSON raporu parse et ve doğrula
    """
    
def check_survivors_detected(report: dict) -> bool:
    """En az bir survivor tespit edildi mi?"""
    
def check_mutations_applied(report: dict) -> bool:
    """Mutasyonlar gerçekten uygulandı mı?"""
    
def check_operators_used(report: dict, expected_operators: list[str]) -> bool:
    """Beklenen operatörler kullanıldı mı?"""
    
def check_original_files_unchanged(project_path: str, backup_hashes: dict) -> bool:
    """Orijinal dosyalar değişmedi mi?"""
```

### 7. UI Integration

#### Module: `ui/demo_selector.py` (mevcut dosyaya eklenecek)

```python
ADVANCED_DEMOS = [
    {
        "id": "ecommerce",
        "name": "E-Commerce Order Processing",
        "path": "examples/ecommerce_demo",
        "description": "Gerçekçi e-ticaret sipariş işleme mantığı",
        "operators": ["comparison", "logical", "arithmetic"],
        "expected_survivors": 2,
        "difficulty": "intermediate"
    },
    {
        "id": "data_structures",
        "name": "Data Structure Manipulation",
        "path": "examples/data_structures_demo",
        "description": "List, dict, set operasyonları",
        "operators": ["comparison", "arithmetic", "logical"],
        "expected_survivors": 1,
        "difficulty": "intermediate"
    },
    {
        "id": "auth",
        "name": "Authentication & Authorization",
        "path": "examples/auth_demo",
        "description": "Güvenlik kritik kod testi",
        "operators": ["comparison", "logical", "boolean"],
        "expected_survivors": 0,
        "difficulty": "advanced"
    },
    {
        "id": "parser",
        "name": "Parser & Serializer",
        "path": "examples/parser_demo",
        "description": "Round-trip testing örneği",
        "operators": ["comparison", "string", "logical"],
        "expected_survivors": 0,
        "difficulty": "advanced"
    },
    {
        "id": "retry",
        "name": "Retry & Circuit Breaker",
        "path": "examples/retry_logic_demo",
        "description": "Karmaşık retry stratejileri",
        "operators": ["arithmetic", "comparison", "logical"],
        "expected_survivors": 1,
        "difficulty": "advanced"
    }
]
```

## Data Models

### OrderResult

```python
@dataclass
class OrderResult:
    success: bool
    order_id: str
    subtotal: float
    discount: float
    tax: float
    shipping: float
    total: float
    message: str
```

### VerificationResult

```python
@dataclass
class VerificationResult:
    tool_working: bool
    survivors_detected: bool
    mutations_applied: bool
    operators_verified: list[str]
    original_files_intact: bool
    details: dict[str, Any]
```

### DemoConfig

```python
@dataclass
class DemoConfig:
    demo_id: str
    name: str
    path: str
    description: str
    operators: list[str]
    expected_survivors: int
    difficulty: str
    max_mutants: int
    timeout_multiplier: float
```


## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system-essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property Reflection

Prework analizinde tespit edilen testable property'leri gözden geçirdim:

**Identified Properties:**
1. Invalid order data raises exceptions (1.4)
2. List size invariant after map (2.4)
3. Empty collections handled without errors (2.5)
4. Invalid credentials return False (3.4)
5. Expired sessions identified as invalid (3.5)
6. Valid config parsing (4.3)
7. Invalid config raises ValueError (4.4)
8. Round-trip property for parser (4.5)
9. Max retries exceeded returns failure (5.4)
10. Non-retryable errors don't retry (5.5)
11. JSON report structure validation (6.4)
12. Original files unchanged after mutation (6.7)
13. Demo config loading (7.5)

**Redundancy Analysis:**

- Property 3 (invalid credentials) ve Property 4 (expired sessions) aslında aynı konsepti test ediyor: authentication/authorization fonksiyonlarının invalid input'larda False dönmesi. Bunlar birleştirilebilir.
- Property 6 (valid config parsing) ve Property 8 (round-trip) ilişkili: round-trip property zaten parsing'in doğru çalıştığını garanti eder. Property 6, Property 8 tarafından kapsanır.
- Property 9 (max retries) ve Property 10 (non-retryable errors) farklı senaryolar test ediyor, ayrı kalmalı.

**Consolidated Properties:**

After reflection, eliminating redundant properties:
- Property 6 removed (subsumed by Property 8 - round-trip)
- Properties 3 and 4 combined into one comprehensive authentication property

### Property 1: Invalid Input Exception Handling

*For any* invalid order data (negative prices, missing required fields, invalid customer types), the order processing system should raise appropriate exceptions with descriptive messages rather than silently failing or returning incorrect results.

**Validates: Requirements 1.4**

### Property 2: Collection Transformation Invariants

*For any* list and any transformation function (map, filter with always-true predicate, identity), applying the transformation should preserve the list length when the transformation is length-preserving by definition.

**Validates: Requirements 2.4**

### Property 3: Empty Collection Handling

*For any* data structure operation (list filtering, dict merging, set operations), when provided with empty collections as input, the system should handle them gracefully and return valid results without raising errors.

**Validates: Requirements 2.5**

### Property 4: Authentication Validation Returns Boolean

*For any* authentication or authorization check (invalid credentials, expired sessions, insufficient permissions), the validation functions should return False rather than raising exceptions, ensuring graceful handling of invalid authentication attempts.

**Validates: Requirements 3.4, 3.5**

### Property 5: Invalid Configuration Error Handling

*For any* malformed configuration input (missing equals signs, invalid syntax, empty lines in wrong places), the parser should raise a descriptive ValueError that clearly indicates what went wrong.

**Validates: Requirements 4.4**

### Property 6: Configuration Round-Trip Identity

*For any* valid configuration dictionary, the operation of formatting to text and then parsing back should produce an equivalent dictionary (parse(format(config)) == config), ensuring serialization and deserialization are true inverses.

**Validates: Requirements 4.5**

### Property 7: Retry Exhaustion Behavior

*For any* operation that exceeds the maximum retry attempts, the retry logic should return a failure result and not attempt additional retries beyond the configured limit.

**Validates: Requirements 5.4**

### Property 8: Non-Retryable Error Immediate Failure

*For any* error classified as non-retryable (e.g., authentication errors, validation errors), the retry logic should immediately return failure without attempting any retries, regardless of the retry count configuration.

**Validates: Requirements 5.5**

### Property 9: Mutation Report Structure Validation

*For any* mutation testing run that completes, the generated JSON report should contain all required fields (killed count, survived count, total mutants, mutant details) and be parseable as valid JSON with the expected schema.

**Validates: Requirements 6.4**

### Property 10: Source File Integrity

*For any* mutation testing run, after the run completes (whether successful or not), the original source files in the project should remain completely unchanged, with all mutations applied only to temporary copies.

**Validates: Requirements 6.7**

### Property 11: Demo Configuration Loading

*For any* demo selected in the UI, the system should correctly load that demo's configuration including source paths, test commands, and mutation settings without errors or missing values.

**Validates: Requirements 7.5**

## Error Handling

### Order Processing Errors

```python
class InvalidOrderError(ValueError):
    """Geçersiz sipariş verisi"""
    
class InsufficientStockError(Exception):
    """Yetersiz stok"""
    
class InvalidTransitionError(Exception):
    """Geçersiz durum geçişi"""
```

**Error Handling Strategy:**
- Validation errors: ValueError with descriptive messages
- Business logic errors: Custom exceptions
- All errors should include context (order_id, product_id, etc.)

### Parser Errors

```python
class ConfigParseError(ValueError):
    """Config parsing hatası"""
    
class InvalidFormatError(ValueError):
    """Geçersiz format"""
```

**Error Handling Strategy:**
- Include line number where error occurred
- Show the problematic line in error message
- Suggest correct format

### Retry Logic Errors

```python
class MaxRetriesExceededError(Exception):
    """Maksimum deneme sayısı aşıldı"""
    
class CircuitOpenError(Exception):
    """Devre açık, istek kabul edilmiyor"""
```

**Error Handling Strategy:**
- Distinguish between retryable and non-retryable errors
- Log all retry attempts
- Include attempt count in error messages

### General Error Handling Principles

1. **Fail Fast**: Invalid input'larda hemen hata fırlat
2. **Descriptive Messages**: Hata mesajları sorunu açıkça belirtmeli
3. **Context Preservation**: Hata mesajlarında ilgili veriyi göster
4. **Type Safety**: Uygun exception türlerini kullan
5. **No Silent Failures**: Asla sessizce başarısız olma

## Testing Strategy

### Dual Testing Approach

Bu projede hem unit testing hem de property-based testing kullanılacak:

**Unit Tests:**
- Specific examples demonstrating correct behavior
- Edge cases (boundary values, empty inputs, special characters)
- Error conditions (invalid inputs, exceptions)
- Integration points between modules
- State transitions (order status, circuit breaker states)

**Property Tests:**
- Universal properties across all inputs
- Invariants (collection size preservation)
- Round-trip properties (parse/format, serialize/deserialize)
- Metamorphic properties (relationships between operations)
- Comprehensive input coverage through randomization

### Property-Based Testing Configuration

**Framework:** `hypothesis` (Python'un en yaygın property-based testing kütüphanesi)

**Configuration:**
```python
from hypothesis import given, settings
import hypothesis.strategies as st

@settings(max_examples=100)  # Minimum 100 iteration
@given(st.integers(), st.text())
def test_property(value, text):
    # Property test implementation
    pass
```

**Test Tagging:**
Her property test, design dokümanındaki property'ye referans verecek:

```python
def test_order_invalid_input_raises():
    """
    Feature: advanced-mutation-demos, Property 1: Invalid Input Exception Handling
    
    For any invalid order data, the system should raise appropriate exceptions.
    """
```

### Test Organization

#### E-Commerce Demo Tests

```python
# tests/test_order_processor.py
- test_discount_calculation_regular_customer()
- test_discount_calculation_premium_customer()
- test_discount_calculation_vip_customer()
- test_discount_boundary_values()
- test_tax_calculation()
- test_shipping_cost_free_threshold()
- test_shipping_cost_below_threshold()
- test_invalid_price_raises_error()  # Property 1
- test_invalid_customer_type_raises_error()  # Property 1
- test_negative_quantity_raises_error()  # Property 1

# tests/test_inventory.py
- test_stock_check_sufficient()
- test_stock_check_insufficient()
- test_reserve_stock_success()
- test_reserve_stock_failure()
- test_release_stock()

# tests/test_order_status.py
- test_valid_transitions()
- test_invalid_transitions()
- test_all_state_combinations()
```

**Expected Mutation Score:** 85-90%
**Expected Survivors:** 2-3 (intentional weak spots for educational purposes)

#### Data Structures Demo Tests

```python
# tests/test_list_operations.py
- test_filter_positive_numbers()
- test_filter_empty_list()  # Property 3
- test_sort_by_length()
- test_transform_preserves_length()  # Property 2
- test_chunk_list_exact_division()
- test_chunk_list_remainder()

# tests/test_dict_operations.py
- test_merge_dicts_prefer_first()
- test_merge_dicts_prefer_second()
- test_merge_empty_dicts()  # Property 3
- test_validate_keys_all_present()
- test_validate_keys_missing()
- test_get_nested_value()
- test_flatten_dict()

# tests/test_set_operations.py
- test_find_common_elements()
- test_find_unique_elements()
- test_combine_empty_sets()  # Property 3
```

**Expected Mutation Score:** 90-95%
**Expected Survivors:** 1-2

#### Authentication Demo Tests

```python
# tests/test_password_validator.py
- test_password_length_minimum()
- test_password_requires_uppercase()
- test_password_requires_lowercase()
- test_password_requires_digit()
- test_password_requires_special_char()
- test_password_strength_weak()
- test_password_strength_medium()
- test_password_strength_strong()

# tests/test_permissions.py
- test_admin_has_all_permissions()
- test_user_has_read_write()
- test_guest_has_read_only()
- test_invalid_role_returns_false()  # Property 4
- test_resource_owner_access()
- test_non_owner_access_denied()

# tests/test_session.py
- test_valid_session()
- test_expired_session_invalid()  # Property 4
- test_extend_session()
- test_remaining_time_calculation()
```

**Expected Mutation Score:** 95-98%
**Expected Survivors:** 0 (security-critical code should have no survivors)

#### Parser Demo Tests

```python
# tests/test_config_parser.py
- test_parse_valid_config()
- test_parse_empty_config()
- test_parse_invalid_format_raises()  # Property 5
- test_format_config()
- test_round_trip_property()  # Property 6
- test_validate_config_schema()

# tests/test_json_serializer.py
- test_serialize_user()
- test_deserialize_user()
- test_serialize_deserialize_round_trip()  # Property 6
- test_nested_serialization()
- test_malformed_json_raises()  # Property 5
```

**Expected Mutation Score:** 95-100%
**Expected Survivors:** 0 (round-trip properties catch most mutations)

#### Retry Logic Demo Tests

```python
# tests/test_backoff.py
- test_exponential_backoff_calculation()
- test_backoff_max_delay_limit()
- test_jitter_adds_randomness()

# tests/test_retry_logic.py
- test_retry_on_retryable_error()
- test_no_retry_on_non_retryable_error()  # Property 8
- test_max_retries_exceeded()  # Property 7
- test_successful_retry()

# tests/test_circuit_breaker.py
- test_circuit_closed_allows_requests()
- test_circuit_opens_after_failures()
- test_circuit_half_open_after_timeout()
- test_circuit_closes_after_success()
- test_all_state_transitions()
```

**Expected Mutation Score:** 85-90%
**Expected Survivors:** 1-2

### Tool Verification Tests

```python
# tests/test_verification.py
- test_verification_detects_survivors()  # Example test
- test_verification_confirms_mutations_applied()  # Example test
- test_verification_validates_report_structure()  # Property 9
- test_verification_checks_original_files_intact()  # Property 10
- test_verification_checks_operators_used()  # Example test
```

### Mutation Operator Coverage Matrix

| Demo | Comparison | Logical | Arithmetic | Boolean | String | Membership |
|------|-----------|---------|-----------|---------|--------|-----------|
| E-Commerce | ✓ | ✓ | ✓ | - | - | - |
| Data Structures | ✓ | ✓ | ✓ | - | - | ✓ |
| Auth | ✓ | ✓ | - | ✓ | - | - |
| Parser | ✓ | ✓ | - | - | ✓ | - |
| Retry Logic | ✓ | ✓ | ✓ | - | - | - |

### Test Execution

**Running Individual Demo Tests:**
```bash
# E-Commerce demo
python -m pytest examples/ecommerce_demo/tests -v

# Data Structures demo
python -m pytest examples/data_structures_demo/tests -v

# Auth demo
python -m pytest examples/auth_demo/tests -v

# Parser demo
python -m pytest examples/parser_demo/tests -v

# Retry Logic demo
python -m pytest examples/retry_logic_demo/tests -v
```

**Running Mutation Tests:**
```bash
# E-Commerce demo
python -m mutation_tool run examples/ecommerce_demo --max-mutants 30

# All demos
for demo in ecommerce_demo data_structures_demo auth_demo parser_demo retry_logic_demo; do
    python -m mutation_tool run examples/$demo --max-mutants 30
done
```

**Running Verification:**
```bash
python -m pytest examples/ecommerce_demo/tests/test_verification.py -v
```

### Success Criteria

Her demo için başarı kriterleri:

1. **All unit tests pass**: Tüm unit testler yeşil olmalı
2. **Property tests pass**: Tüm property testler 100 iteration'da geçmeli
3. **Mutation score target met**: Hedef mutation score'a ulaşılmalı
4. **Expected survivors match**: Beklenen survivor sayısı ±1 olmalı
5. **No false positives**: Timeout veya error olarak işaretlenen mutant olmamalı
6. **Documentation complete**: README ve inline dokümantasyon eksiksiz olmalı

### CI Integration

Demo'lar CI pipeline'ında şu şekilde test edilecek:

```yaml
# .github/workflows/test-demos.yml
- name: Test E-Commerce Demo
  run: |
    pytest examples/ecommerce_demo/tests
    python -m mutation_tool run examples/ecommerce_demo --max-mutants 20 --fail-on-survivor

- name: Test Auth Demo (no survivors allowed)
  run: |
    pytest examples/auth_demo/tests
    python -m mutation_tool run examples/auth_demo --max-mutants 20 --fail-on-survivor
```

Security-critical demo'lar (auth_demo) için `--fail-on-survivor` flag'i kullanılarak hiç survivor olmaması garanti edilecek.
