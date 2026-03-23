# Implementation Plan: Advanced Mutation Testing Demos

## Overview

Bu plan, mutation testing tool için 5 yeni gelişmiş demo projesi oluşturmayı içerir. Her demo gerçek dünya senaryolarını yansıtacak, farklı mutation operatörlerini gösterecek ve kapsamlı test coverage sağlayacak şekilde tasarlanmıştır.

## Tasks

- [ ] 1. E-Commerce Order Processing Demo - Proje yapısı ve temel modüller
  - [x] 1.1 Demo klasör yapısını oluştur ve pyproject.toml ekle
    - `examples/ecommerce_demo/` klasörünü oluştur
    - `src/ecommerce_app/` ve `tests/` alt klasörlerini oluştur
    - `pyproject.toml` dosyasını mutation tool konfigürasyonu ile oluştur
    - `src/ecommerce_app/__init__.py` dosyasını oluştur
    - _Requirements: 7.2, 7.3_

  - [x] 1.2 Order ve OrderItem veri modellerini implement et
    - `src/ecommerce_app/models.py` dosyasını oluştur
    - `Order` ve `OrderItem` dataclass'larını tanımla
    - `OrderResult` dataclass'ını tanımla
    - _Requirements: 1.1_

  - [x] 1.3 Order processor modülünü implement et
    - `src/ecommerce_app/order_processor.py` dosyasını oluştur
    - `calculate_discount()` fonksiyonunu implement et (customer type'a göre indirim)
    - `calculate_tax()` fonksiyonunu implement et (%20 KDV)
    - `calculate_shipping()` fonksiyonunu implement et (threshold'lara göre)
    - `process_order()` ana fonksiyonunu implement et
    - _Requirements: 1.1, 1.6, 1.7_

  - [x] 1.4 Order processor için unit testler yaz
    - `tests/test_order_processor.py` dosyasını oluştur
    - Discount calculation testleri (regular, premium, vip)
    - Tax calculation testleri
    - Shipping cost testleri (free threshold, below threshold)
    - Boundary value testleri
    - _Requirements: 1.5, 1.8_

  - [x] 1.5 Order processor için property test yaz
    - **Property 1: Invalid Input Exception Handling**
    - **Validates: Requirements 1.4**
    - Invalid order data için exception testleri (negative prices, invalid customer types)
    - _Requirements: 1.4_

- [ ] 2. E-Commerce Demo - Inventory ve Order Status modülleri
  - [x] 2.1 Inventory manager modülünü implement et
    - `src/ecommerce_app/inventory.py` dosyasını oluştur
    - `InventoryManager` class'ını implement et
    - `check_stock()`, `reserve_stock()`, `release_stock()` metodlarını implement et
    - _Requirements: 1.2_

  - [x] 2.2 Order status modülünü implement et
    - `src/ecommerce_app/order_status.py` dosyasını oluştur
    - `OrderStatus` enum'ını tanımla
    - `can_transition()` fonksiyonunu implement et
    - `transition_order()` fonksiyonunu implement et
    - _Requirements: 1.3_

  - [x] 2.3 Inventory ve order status için testler yaz
    - `tests/test_inventory.py` dosyasını oluştur
    - `tests/test_order_status.py` dosyasını oluştur
    - Stock check, reserve, release testleri
    - Valid/invalid transition testleri
    - All state combinations testleri
    - _Requirements: 1.5_

  - [x] 2.4 E-Commerce demo README.md dosyasını oluştur
    - Türkçe açıklama ve öğrenme hedefleri
    - Çalıştırma talimatları (CLI ve UI)
    - Beklenen mutation score ve survivor sayısı
    - Hangi mutation operatörlerinin gösterildiği
    - _Requirements: 7.1, 7.6, 7.7_

- [ ] 3. Data Structure Manipulation Demo
  - [~] 3.1 Demo klasör yapısını oluştur ve pyproject.toml ekle
    - `examples/data_structures_demo/` klasörünü oluştur
    - `src/data_structures_app/` ve `tests/` alt klasörlerini oluştur
    - `pyproject.toml` dosyasını oluştur
    - `src/data_structures_app/__init__.py` dosyasını oluştur
    - _Requirements: 7.2, 7.3_

  - [~] 3.2 List operations modülünü implement et
    - `src/data_structures_app/list_operations.py` dosyasını oluştur
    - `filter_positive()`, `sort_by_length()`, `transform_to_upper()` fonksiyonlarını implement et
    - `chunk_list()` fonksiyonunu implement et
    - _Requirements: 2.1, 2.7_

  - [~] 3.3 Dict operations modülünü implement et
    - `src/data_structures_app/dict_operations.py` dosyasını oluştur
    - `merge_dicts()`, `validate_keys()` fonksiyonlarını implement et
    - `get_nested()`, `flatten_dict()` fonksiyonlarını implement et
    - _Requirements: 2.2_

  - [~] 3.4 Set operations modülünü implement et
    - `src/data_structures_app/set_operations.py` dosyasını oluştur
    - `find_common()`, `find_unique()`, `combine_all()` fonksiyonlarını implement et
    - _Requirements: 2.3_

  - [~] 3.5 Data structures için unit testler yaz
    - `tests/test_list_operations.py` dosyasını oluştur
    - `tests/test_dict_operations.py` dosyasını oluştur
    - `tests/test_set_operations.py` dosyasını oluştur
    - Filter, sort, transform testleri
    - Merge, validate, nested access testleri
    - Set intersection, union, difference testleri
    - _Requirements: 2.8_

  - [~] 3.6 Data structures için property testler yaz
    - **Property 2: Collection Transformation Invariants**
    - **Property 3: Empty Collection Handling**
    - **Validates: Requirements 2.4, 2.5**
    - List size preservation testleri
    - Empty collection handling testleri
    - _Requirements: 2.4, 2.5_

  - [~] 3.7 Data structures demo README.md dosyasını oluştur
    - Türkçe açıklama ve öğrenme hedefleri
    - Çalıştırma talimatları
    - Beklenen mutation score ve survivor sayısı
    - _Requirements: 7.1, 7.6, 7.7_

- [ ] 4. Authentication and Authorization Demo
  - [~] 4.1 Demo klasör yapısını oluştur ve pyproject.toml ekle
    - `examples/auth_demo/` klasörünü oluştur
    - `src/auth_app/` ve `tests/` alt klasörlerini oluştur
    - `pyproject.toml` dosyasını oluştur
    - `src/auth_app/__init__.py` dosyasını oluştur
    - _Requirements: 7.2, 7.3_

  - [~] 4.2 Password validator modülünü implement et
    - `src/auth_app/password_validator.py` dosyasını oluştur
    - `validate_password()` fonksiyonunu implement et (complexity rules)
    - `password_strength()` fonksiyonunu implement et
    - _Requirements: 3.1, 3.7_

  - [~] 4.3 Permissions modülünü implement et
    - `src/auth_app/permissions.py` dosyasını oluştur
    - `Role` ve `Permission` enum'larını tanımla
    - `has_permission()` fonksiyonunu implement et
    - `can_access_resource()` fonksiyonunu implement et
    - _Requirements: 3.2, 3.8_

  - [~] 4.4 Session management modülünü implement et
    - `src/auth_app/session.py` dosyasını oluştur
    - `Session` dataclass'ını tanımla
    - `is_session_valid()`, `extend_session()` fonksiyonlarını implement et
    - `calculate_remaining_time()` fonksiyonunu implement et
    - _Requirements: 3.3, 3.7_

  - [~] 4.5 Auth demo için unit testler yaz
    - `tests/test_password_validator.py` dosyasını oluştur
    - `tests/test_permissions.py` dosyasını oluştur
    - `tests/test_session.py` dosyasını oluştur
    - Password validation testleri (length, uppercase, lowercase, digit, special char)
    - Permission testleri (admin, user, guest roles)
    - Session validity testleri
    - _Requirements: 3.6, 3.9_

  - [~] 4.6 Auth demo için property test yaz
    - **Property 4: Authentication Validation Returns Boolean**
    - **Validates: Requirements 3.4, 3.5**
    - Invalid credentials return False testleri
    - Expired sessions return False testleri
    - _Requirements: 3.4, 3.5_

  - [~] 4.7 Auth demo README.md dosyasını oluştur
    - Türkçe açıklama ve öğrenme hedefleri
    - Security-critical code testing vurgusu
    - Çalıştırma talimatları
    - Beklenen mutation score: 95-98%, survivor: 0
    - _Requirements: 7.1, 7.6, 7.7_

- [ ] 5. Parser and Serializer Demo
  - [~] 5.1 Demo klasör yapısını oluştur ve pyproject.toml ekle
    - `examples/parser_demo/` klasörünü oluştur
    - `src/parser_app/` ve `tests/` alt klasörlerini oluştur
    - `pyproject.toml` dosyasını oluştur
    - `src/parser_app/__init__.py` dosyasını oluştur
    - _Requirements: 7.2, 7.3_

  - [~] 5.2 Config parser modülünü implement et
    - `src/parser_app/config_parser.py` dosyasını oluştur
    - `parse_config()` fonksiyonunu implement et (key=value format)
    - `format_config()` fonksiyonunu implement et
    - `validate_config()` fonksiyonunu implement et
    - _Requirements: 4.1, 4.2, 4.8_

  - [~] 5.3 JSON serializer modülünü implement et
    - `src/parser_app/json_serializer.py` dosyasını oluştur
    - `User` dataclass'ını tanımla
    - `serialize_user()`, `deserialize_user()` fonksiyonlarını implement et
    - `serialize_nested()` fonksiyonunu implement et
    - _Requirements: 4.6_

  - [~] 5.4 Parser demo için unit testler yaz
    - `tests/test_config_parser.py` dosyasını oluştur
    - `tests/test_json_serializer.py` dosyasını oluştur
    - Valid/invalid config parsing testleri
    - Format config testleri
    - JSON serialization/deserialization testleri
    - Malformed input handling testleri
    - _Requirements: 4.3, 4.7, 4.9_

  - [~] 5.5 Parser demo için property testler yaz
    - **Property 5: Invalid Configuration Error Handling**
    - **Property 6: Configuration Round-Trip Identity**
    - **Validates: Requirements 4.4, 4.5**
    - Invalid config raises ValueError testleri
    - Round-trip property testleri (parse -> format -> parse)
    - _Requirements: 4.4, 4.5_

  - [~] 5.6 Parser demo README.md dosyasını oluştur
    - Türkçe açıklama ve öğrenme hedefleri
    - Round-trip testing konsepti açıklaması
    - Çalıştırma talimatları
    - Beklenen mutation score: 95-100%, survivor: 0
    - _Requirements: 7.1, 7.6, 7.7_

- [ ] 6. Retry and Timeout Logic Demo
  - [~] 6.1 Demo klasör yapısını oluştur ve pyproject.toml ekle
    - `examples/retry_logic_demo/` klasörünü oluştur
    - `src/retry_app/` ve `tests/` alt klasörlerini oluştur
    - `pyproject.toml` dosyasını oluştur
    - `src/retry_app/__init__.py` dosyasını oluştur
    - _Requirements: 7.2, 7.3_

  - [~] 6.2 Backoff calculation modülünü implement et
    - `src/retry_app/backoff.py` dosyasını oluştur
    - `calculate_backoff()` fonksiyonunu implement et (exponential backoff)
    - `add_jitter()` fonksiyonunu implement et
    - _Requirements: 5.1, 5.7_

  - [~] 6.3 Retry logic modülünü implement et
    - `src/retry_app/retry_logic.py` dosyasını oluştur
    - `RetryableError` ve `NonRetryableError` exception'larını tanımla
    - `should_retry()` fonksiyonunu implement et
    - `execute_with_retry()` fonksiyonunu implement et
    - _Requirements: 5.2, 5.8_

  - [~] 6.4 Circuit breaker modülünü implement et
    - `src/retry_app/circuit_breaker.py` dosyasını oluştur
    - `CircuitState` enum'ını tanımla
    - `CircuitBreaker` class'ını implement et
    - `can_execute()`, `record_success()`, `record_failure()` metodlarını implement et
    - `get_next_state()` metodunu implement et
    - _Requirements: 5.3, 5.6_

  - [~] 6.5 Retry logic demo için unit testler yaz
    - `tests/test_backoff.py` dosyasını oluştur
    - `tests/test_retry_logic.py` dosyasını oluştur
    - `tests/test_circuit_breaker.py` dosyasını oluştur
    - Exponential backoff testleri
    - Retry decision testleri
    - Circuit breaker state transition testleri
    - _Requirements: 5.9_

  - [~] 6.6 Retry logic demo için property testler yaz
    - **Property 7: Retry Exhaustion Behavior**
    - **Property 8: Non-Retryable Error Immediate Failure**
    - **Validates: Requirements 5.4, 5.5**
    - Max retries exceeded testleri
    - Non-retryable error testleri
    - _Requirements: 5.4, 5.5_

  - [~] 6.7 Retry logic demo README.md dosyasını oluştur
    - Türkçe açıklama ve öğrenme hedefleri
    - Exponential backoff ve circuit breaker konseptleri açıklaması
    - Çalıştırma talimatları
    - Beklenen mutation score: 85-90%, survivor: 1-2
    - _Requirements: 7.1, 7.6, 7.7_

- [~] 7. Checkpoint - İlk 5 demo tamamlandı
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 8. Tool Verification Module
  - [~] 8.1 Verification script oluştur
    - `examples/ecommerce_demo/tests/test_verification.py` dosyasını oluştur
    - `run_verification()` fonksiyonunu implement et
    - `check_survivors_detected()` fonksiyonunu implement et
    - `check_mutations_applied()` fonksiyonunu implement et
    - `check_operators_used()` fonksiyonunu implement et
    - `check_original_files_unchanged()` fonksiyonunu implement et
    - _Requirements: 6.1, 6.2, 6.3, 6.6_

  - [~] 8.2 Verification için property testler yaz
    - **Property 9: Mutation Report Structure Validation**
    - **Property 10: Source File Integrity**
    - **Validates: Requirements 6.4, 6.7**
    - JSON report structure validation testleri
    - Original files unchanged testleri
    - _Requirements: 6.4, 6.5, 6.7_

  - [~] 8.3 Verification documentation oluştur
    - E-Commerce demo README'sine verification section ekle
    - Tool'un doğru çalıştığını nasıl doğrulayacağını açıkla
    - _Requirements: 6.8_

- [ ] 9. UI Integration
  - [~] 9.1 Demo selector'a yeni demo'ları ekle
    - `src/mutation_tool/ui/demo_selector.py` dosyasını güncelle (veya ilgili UI dosyasını bul)
    - `ADVANCED_DEMOS` listesini ekle (ecommerce, data_structures, auth, parser, retry_logic)
    - Her demo için id, name, path, description, operators, expected_survivors, difficulty bilgilerini ekle
    - _Requirements: 7.3, 7.4_

  - [~] 9.2 UI integration için property test yaz
    - **Property 11: Demo Configuration Loading**
    - **Validates: Requirements 7.5**
    - Demo selection ve config loading testleri
    - _Requirements: 7.5_

- [ ] 10. Main Documentation Update
  - [~] 10.1 Ana README.md dosyasını güncelle
    - Yeni advanced demo'ları tanıt
    - Her demo'nun öğrenme hedeflerini özetle
    - Demo'ların zorluk seviyelerini belirt (intermediate, advanced)
    - _Requirements: 7.8_

  - [~] 10.2 Demo comparison table oluştur
    - Ana README'ye demo karşılaştırma tablosu ekle
    - Mutation operator coverage matrix ekle
    - Beklenen mutation score'ları ve survivor sayılarını göster
    - _Requirements: 7.8_

- [~] 11. Final Checkpoint - Tüm demo'lar ve entegrasyon tamamlandı
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties
- Unit tests validate specific examples and edge cases
- Security-critical demo (auth_demo) should have 0 survivors
- Parser demo with round-trip properties should have 0 survivors
- All demos should follow the same structure for consistency
