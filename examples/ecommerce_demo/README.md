# E-Commerce Order Processing Demo

Bu demo, mutation testing'in gerçek dünya senaryolarında nasıl kullanılacağını gösteren orta seviye bir örnektir. E-ticaret sipariş işleme mantığı üzerinden karmaşık iş kurallarının test edilmesini öğreneceksiniz.

## Öğrenme Hedefleri

Bu demo ile şunları öğreneceksiniz:

- **Karmaşık iş mantığının test edilmesi**: İndirim hesaplama, vergi, kargo ücreti gibi çok katmanlı hesaplamaların doğru test edilmesi
- **Comparison operatörlerinin önemi**: `>=`, `<=`, `==` gibi operatörlerdeki küçük değişikliklerin büyük etkileri
- **Logical operatörlerin testi**: `and`, `or` gibi mantıksal operatörlerin tüm kombinasyonlarının test edilmesi
- **Arithmetic operatörlerin doğruluğu**: `+`, `-`, `*`, `/` gibi aritmetik işlemlerdeki hataların yakalanması
- **Boundary value testing**: Eşik değerlerin (100 TL, 200 TL gibi) doğru test edilmesi
- **Exception handling**: Geçersiz girdilerde uygun hataların fırlatılması

## Klasör Yapısı

```text
examples/ecommerce_demo/
  pyproject.toml
  README.md
  src/ecommerce/
    __init__.py
    order_processor.py    # Sipariş işleme ve fiyat hesaplamaları
    inventory.py          # Stok yönetimi
    order_status.py       # Sipariş durum geçişleri
  tests/
    test_order_processor.py
    test_inventory.py
    test_order_status.py
```

## İş Mantığı Özeti

### Müşteri Tipleri ve İndirimler

- **Regular**: 100 TL üzeri siparişlerde %5 indirim
- **Premium**: 100 TL üzeri siparişlerde %10 indirim
- **VIP**: 50 TL üzeri siparişlerde %15 indirim

### Kargo Ücreti

- 200 TL üzeri siparişler: Ücretsiz kargo
- Premium/VIP müşteriler: 150 TL üzeri ücretsiz kargo
- Diğer durumlar: 30 TL kargo ücreti

### Vergi

- Tüm siparişlere %20 KDV uygulanır

## Çalıştırma Talimatları

### 1. Normal Testleri Çalıştır

Ana proje klasöründeyken:

```bash
python -m pytest examples/ecommerce_demo/tests -v
```

Tüm testlerin geçmesi beklenir. Bu demo'da 15+ test case bulunmaktadır.

### 2. Mutation Testing Çalıştır (CLI)

Ana proje klasöründeyken:

```bash
python -m mutation_tool run examples/ecommerce_demo --max-mutants 30
```

Bu komut:
- Maksimum 30 mutant oluşturur
- Her mutant için testleri çalıştırır
- Sonuçları terminalde gösterir
- JSON raporu oluşturur

### 3. UI ile Çalıştır

```bash
python -m mutation_tool ui
```

UI açıldığında:

1. Demo seçicisinden **E-Commerce Order Processing** seçin
2. **Load Selected Demo** butonuna tıklayın (form otomatik doldurulur)
3. **Run Selected Demo** butonuna tıklayın (tek tıkla çalıştırma)
4. Alternatif: Ayarları değiştirip **Start Mutation Run** kullanabilirsiniz
5. Koşu bitince JSON ve PDF raporlarını indirebilirsiniz

## Beklenen Sonuçlar

### Mutation Score

**Hedef: %85-90**

Bu demo'da kasıtlı olarak bazı zayıf noktalar bırakılmıştır. Gerçek dünya projelerinde de %100 mutation score her zaman mümkün veya gerekli olmayabilir.

### Survivor Sayısı

**Beklenen: 2-3 survivor**

Bu survivor'lar eğitim amaçlı bırakılmıştır. Hangi tür testlerin eksik olduğunu görmek için survivor'ları inceleyebilirsiniz.

Örnek zayıf noktalar:
- Tam eşik değerlerinde (örn: tam 100 TL) test eksikliği
- Müşteri tipi kombinasyonlarında eksik test
- Sıfır miktarlı sipariş gibi edge case'ler

## Gösterilen Mutation Operatörleri

Bu demo şu mutation operatörlerini gösterir:

### 1. Comparison Operators (Karşılaştırma)

- `>=` → `>` : İndirim eşiklerinde kritik
- `<=` → `<` : Maksimum limit kontrollerinde
- `==` → `!=` : Müşteri tipi kontrollerinde

**Örnek:**
```python
# Original
if subtotal >= 100:
    discount = 0.05

# Mutant
if subtotal > 100:  # 100 TL tam değeri artık indirim almaz!
    discount = 0.05
```

### 2. Logical Operators (Mantıksal)

- `and` → `or` : Bileşik koşullarda
- `or` → `and` : Alternatif koşullarda

**Örnek:**
```python
# Original
if customer_type == "premium" or customer_type == "vip":
    free_shipping_threshold = 150

# Mutant
if customer_type == "premium" and customer_type == "vip":  # Hiçbir zaman True olmaz!
    free_shipping_threshold = 150
```

### 3. Arithmetic Operators (Aritmetik)

- `+` → `-` : Toplam hesaplamalarında
- `*` → `/` : Çarpma işlemlerinde
- `-` → `+` : Çıkarma işlemlerinde

**Örnek:**
```python
# Original
total = subtotal - discount + tax + shipping

# Mutant
total = subtotal + discount + tax + shipping  # İndirim ekleniyor!
```

## Survivor Gördüğünüzde Ne Yapmalısınız?

### 1. Survivor'ı İnceleyin

Raporda survivor'ın hangi satırda olduğunu ve ne değiştiğini görün:

```
Line 45: subtotal >= 100 → subtotal > 100
Status: SURVIVED
```

### 2. Eksik Testi Belirleyin

Bu mutant neden yaşadı? Hangi test case eksik?

- Eşik değer testi eksik mi? (tam 100 TL)
- Sınır değer testi eksik mi? (99 TL, 101 TL)
- Kombinasyon testi eksik mi? (premium + 100 TL)

### 3. Yeni Test Ekleyin

```python
def test_discount_exact_threshold_regular():
    """100 TL tam değerinde regular müşteri %5 indirim almalı"""
    order = Order(
        order_id="TEST-001",
        items=[OrderItem("PROD-1", 1, 100.0)],
        customer_type="regular",
        subtotal=100.0
    )
    result = process_order(order)
    assert result.discount == 5.0  # %5 indirim
```

### 4. Tekrar Çalıştırın

```bash
python -m mutation_tool run examples/ecommerce_demo --max-mutants 30
```

Yeni test eklendikten sonra mutation score artmalı ve survivor sayısı azalmalıdır.

## İleri Seviye İpuçları

### Boundary Value Testing

Eşik değerlerin hemen altı, tam değeri ve hemen üstü test edilmelidir:

```python
# 100 TL eşiği için
test_discount_at_99()   # Eşiğin altı
test_discount_at_100()  # Tam eşik
test_discount_at_101()  # Eşiğin üstü
```

### Kombinasyon Testleri

Farklı müşteri tipleri ve sipariş tutarlarının tüm kombinasyonları test edilmelidir:

```python
@pytest.mark.parametrize("customer_type,subtotal,expected_discount", [
    ("regular", 99, 0),
    ("regular", 100, 5),
    ("premium", 100, 10),
    ("vip", 50, 7.5),
])
def test_discount_combinations(customer_type, subtotal, expected_discount):
    # Test implementation
```

### Exception Testing

Geçersiz girdilerde uygun hatalar fırlatılmalıdır:

```python
def test_negative_price_raises_error():
    with pytest.raises(InvalidOrderError, match="negative"):
        order = Order(items=[OrderItem("PROD-1", 1, -10.0)])
        process_order(order)
```

## Gerçek Dünya Bağlantısı

Bu demo, gerçek e-ticaret sistemlerinde karşılaşabileceğiniz durumları yansıtır:

- **Promosyon kuralları**: İndirim eşikleri ve müşteri segmentasyonu
- **Fiyatlandırma mantığı**: Vergi, kargo, indirim hesaplamaları
- **İş kuralları**: Karmaşık koşullar ve öncelikler
- **Edge case'ler**: Sıfır tutarlar, maksimum limitler, geçersiz girdiler

Mutation testing, bu tür kritik iş mantığının doğru test edildiğinden emin olmanızı sağlar.

## Sonraki Adımlar

Bu demo'yu tamamladıktan sonra:

1. **Data Structures Demo**: Veri yapısı manipülasyonlarını öğrenin
2. **Auth Demo**: Güvenlik kritik kodun test edilmesini öğrenin
3. **Parser Demo**: Round-trip testing konseptini öğrenin
4. **Retry Logic Demo**: Karmaşık retry stratejilerini öğrenin

## Sorular ve Sorunlar

Mutation testing hakkında sorularınız varsa veya beklenmedik sonuçlar görürseniz:

1. Önce raporları dikkatlice inceleyin
2. Survivor'ların hangi operatörleri içerdiğine bakın
3. Eksik test case'leri belirleyin
4. Yeni testler ekleyip tekrar deneyin

Mutation testing, test kalitenizi artırmanın en etkili yollarından biridir!
