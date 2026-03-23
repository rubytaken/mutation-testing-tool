# Requirements Document

## Introduction

Bu doküman, mutation testing tool için gelişmiş demo projeleri oluşturma özelliğini tanımlar. Mevcut demo'lar (beginner_demo, ci_gate_demo, timeout_lab_demo) çok basit ve sadece 1-2 fonksiyon içeriyor. Yeni demo'lar gerçek dünya senaryolarını yansıtacak, farklı mutation operatörlerini gösterecek, edge case'leri, exception handling'i, veri yapılarını ve karmaşık iş mantığını içerecek şekilde tasarlanacak.

## Glossary

- **Demo_Project**: Mutation testing tool'un yeteneklerini göstermek için hazırlanmış örnek Python projesi
- **Mutation_Operator**: Kodda belirli değişiklikler yapan operatör (comparison, logical, arithmetic, vb.)
- **Survivor**: Testlerin yakalayamadığı mutant
- **Edge_Case**: Sınır değerleri ve özel durumları test eden senaryo
- **Real_World_Scenario**: Gerçek projelerde karşılaşılan karmaşık iş mantığı ve veri yapıları
- **Tool**: Mutation testing aracının kendisi

## Requirements

### Requirement 1: E-Commerce Order Processing Demo

**User Story:** As a developer learning mutation testing, I want to see a realistic e-commerce order processing example, so that I can understand how mutation testing works with complex business logic.

#### Acceptance Criteria

1. THE Demo_Project SHALL include an order processing module with discount calculation, tax calculation, and shipping cost logic
2. THE Demo_Project SHALL include inventory validation with stock checking and reservation logic
3. THE Demo_Project SHALL include order status transitions (pending, confirmed, shipped, delivered, cancelled)
4. WHEN invalid order data is provided, THE Demo_Project SHALL raise appropriate exceptions with descriptive messages
5. THE Demo_Project SHALL include at least 15 test cases covering normal flow, edge cases, and error conditions
6. THE Demo_Project SHALL demonstrate comparison operators (>=, <=, ==) in discount thresholds
7. THE Demo_Project SHALL demonstrate logical operators (and, or) in eligibility checks
8. THE Demo_Project SHALL include boundary value tests for minimum order amounts and maximum discount limits

### Requirement 2: Data Structure Manipulation Demo

**User Story:** As a developer, I want to see mutation testing applied to data structure operations, so that I can learn how to test list, dict, and set manipulations effectively.

#### Acceptance Criteria

1. THE Demo_Project SHALL include a module with list filtering, sorting, and transformation operations
2. THE Demo_Project SHALL include dictionary merging, key validation, and nested access operations
3. THE Demo_Project SHALL include set operations (union, intersection, difference)
4. THE Demo_Project SHALL include at least one invariant property test (e.g., list size after map operation)
5. WHEN empty collections are provided, THE Demo_Project SHALL handle them correctly without errors
6. THE Demo_Project SHALL include tests for collection membership checks using 'in' operator
7. THE Demo_Project SHALL demonstrate arithmetic operators (+, -, *, /) in collection size calculations
8. THE Demo_Project SHALL include at least 12 test cases covering various data structure scenarios

### Requirement 3: Authentication and Authorization Demo

**User Story:** As a developer, I want to see mutation testing applied to security-critical code, so that I can understand how to ensure authentication and authorization logic is thoroughly tested.

#### Acceptance Criteria

1. THE Demo_Project SHALL include password validation with complexity rules (length, special chars, numbers)
2. THE Demo_Project SHALL include role-based permission checking (admin, user, guest)
3. THE Demo_Project SHALL include session expiration logic with timeout calculations
4. WHEN invalid credentials are provided, THE Demo_Project SHALL return False without raising exceptions
5. WHEN expired sessions are checked, THE Demo_Project SHALL correctly identify them as invalid
6. THE Demo_Project SHALL include tests for all permission combinations and edge cases
7. THE Demo_Project SHALL demonstrate comparison operators in password length and session timeout checks
8. THE Demo_Project SHALL demonstrate logical operators in compound permission rules
9. THE Demo_Project SHALL include at least 18 test cases covering security scenarios

### Requirement 4: Parser and Serializer Demo

**User Story:** As a developer, I want to see mutation testing applied to parsers and serializers, so that I can learn the importance of round-trip testing.

#### Acceptance Criteria

1. THE Demo_Project SHALL include a configuration file parser that reads key-value pairs
2. THE Demo_Project SHALL include a pretty printer that formats configuration objects back to text
3. WHEN a valid configuration file is provided, THE Parser SHALL parse it into a dictionary
4. WHEN an invalid configuration file is provided, THE Parser SHALL raise a descriptive ValueError
5. FOR ALL valid configuration dictionaries, parsing then printing then parsing SHALL produce an equivalent object (round-trip property)
6. THE Demo_Project SHALL include JSON serialization and deserialization with nested objects
7. THE Demo_Project SHALL include tests for malformed input handling
8. THE Demo_Project SHALL demonstrate string operators and comparison operators in parsing logic
9. THE Demo_Project SHALL include at least 10 test cases including round-trip tests

### Requirement 5: Retry and Timeout Logic Demo

**User Story:** As a developer, I want to see a more comprehensive retry and timeout example than the current timeout_lab_demo, so that I can understand complex retry strategies.

#### Acceptance Criteria

1. THE Demo_Project SHALL include exponential backoff calculation with jitter
2. THE Demo_Project SHALL include retry decision logic based on error types (retryable vs non-retryable)
3. THE Demo_Project SHALL include circuit breaker state management (closed, open, half-open)
4. WHEN max retries are exceeded, THE Demo_Project SHALL return a failure result
5. WHEN a non-retryable error occurs, THE Demo_Project SHALL not attempt retries
6. THE Demo_Project SHALL include tests for all circuit breaker state transitions
7. THE Demo_Project SHALL demonstrate arithmetic operators in backoff calculations
8. THE Demo_Project SHALL demonstrate comparison operators in retry limit checks
9. THE Demo_Project SHALL include at least 14 test cases covering retry scenarios

### Requirement 6: Tool Verification Tests

**User Story:** As a user, I want to verify that the mutation tool actually performs real mutations and is not mocked, so that I can trust the tool's results.

#### Acceptance Criteria

1. THE Demo_Project SHALL include a verification script that runs mutation testing on a known weak test
2. THE Verification_Script SHALL confirm that at least one survivor is detected in the weak test scenario
3. THE Verification_Script SHALL confirm that mutations are actually applied by checking the mutated code snippets in the report
4. THE Verification_Script SHALL parse the JSON report and validate the structure
5. WHEN the verification script runs, THE Tool SHALL produce a report with killed, survived, and total mutant counts
6. THE Verification_Script SHALL check that different mutation operators (comparison, logical, arithmetic) are applied
7. THE Verification_Script SHALL confirm that the tool creates temporary workspaces and does not modify original source files
8. THE Demo_Project SHALL include documentation explaining how to verify the tool is working correctly

### Requirement 7: Demo Integration and Documentation

**User Story:** As a user, I want all new demos to be integrated into the UI demo selector and documented, so that I can easily discover and run them.

#### Acceptance Criteria

1. THE Demo_Project SHALL include a README.md file in Turkish explaining the demo's purpose and learning objectives
2. THE Demo_Project SHALL include a pyproject.toml with appropriate mutation_tool configuration
3. THE Demo_Project SHALL be added to the UI demo selector dropdown
4. THE Demo_Project SHALL include expected mutation scores and survivor counts in the documentation
5. WHEN a demo is selected in the UI, THE System SHALL correctly load the demo's configuration
6. THE Demo_Project SHALL include instructions for running the demo via CLI and UI
7. THE Demo_Project SHALL include a section explaining which mutation operators are demonstrated
8. THE Main_README SHALL be updated to reference the new advanced demos

