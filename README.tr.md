# Mutation Testing Tool - Türkçe Rehber

Bu rehber, programın ne işe yaradığını, neden kullanıldığını, nasıl kurulduğunu, CLI ve UI ile nasıl çalıştırıldığını ve testleri nasıl yazman gerektiğini hiç bilmeyen birine göre anlatır.

Hazır deneme projesi:

- `examples/beginner_demo/README.md`

## 1. Bu program nedir?

`mutation-tool` bir Python mutation testing aracıdır.

Normal test şunu sorar:

- "Yazdığım testler kodu geçiriyor mu?"

Mutation testing ise daha güçlü bir soru sorar:

- "Yazdığım testler, koda sokulan küçük hataları fark edecek kadar güçlü mü?"

Araç, kodunda küçük değişiklikler yapar ve her değişiklikten sonra testlerini tekrar çalıştırır.

Örnek:

- kodunda `value > 0` var
- araç bunu `value >= 0` yapar
- testler fail olursa mutant `killed` olur
- testler hâlâ geçerse mutant `survived` olur

Eğer mutant yaşıyorsa, genelde testlerinde eksik bir durum vardır.

## 2. Neden işe yarar?

Kod coverage sana satırın çalıştığını söyler.

Mutation testing ise testin o satırın davranışını gerçekten kontrol edip etmediğini söyler.

Bu aracın faydaları:

- zayıf testleri bulur
- eksik edge-case'leri bulur
- koda güveni artırır
- regresyon testlerini güçlendirir

## 3. Program arkada nasıl çalışır?

Aracı çalıştırdığında şu akışı izler:

1. `pyproject.toml` içinden ayarları okur
2. `source_paths` içindeki Python dosyalarını bulur
3. Önce normal testleri baseline olarak çalıştırır
4. Baseline fail ise hemen durur
5. Kodunu Python `ast` ile parse eder
6. Küçük değişiklikler üretir:
   - `>` -> `>=`
   - `True` -> `False`
   - `and` -> `or`
   - `+` -> `-`
7. Projeyi geçici bir klasöre kopyalar
8. Her seferinde tek bir mutant uygular
9. Test komutunu mutated kopya üzerinde çalıştırır
10. Sonucu kaydeder
11. `.mutation-tool/last-run.json` raporunu üretir

Önemli:

- normal bir run sırasında gerçek kaynak dosyalarını doğrudan bozmaz
- geçici kopyalar üzerinde çalışır

## 4. Sonuçlar ne anlama gelir?

- `killed`: testler fail oldu, yani mutant yakalandı
- `survived`: testler geçti, yani hata fark edilmedi
- `timeout`: mutant testi çok uzun sürdü
- `error`: mutant syntax/import gibi bir problemi tetikledi

## 5. Yeni başlayan için önerilen proje yapısı

En kolay başlangıç için şu yapıyı kullan:

```text
proje/
  pyproject.toml
  src/
    your_package/
      __init__.py
      calculator.py
  tests/
    test_calculator.py
```

Test framework önerisi:

- en iyi seçenek: `pytest`

Neden `pytest`?

- yeni başlayan için kolay
- yazımı kısa
- Python ekosisteminde çok yaygın
- bu araçta varsayılan seçenek zaten bu

## 6. Kurulum

### Adım 1: Virtual environment oluştur

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Adım 2: Aracı ve geliştirme bağımlılıklarını kur

```bash
python -m pip install -e .[dev]
```

## 7. Temel ayarlar

Projenin `pyproject.toml` dosyasına şunu ekle:

```toml
[tool.mutation_tool]
source_paths = ["src"]
test_command = ["pytest", "-q"]
exclude = ["tests/**", "**/__pycache__/**"]
timeout_multiplier = 5.0
min_timeout = 5.0
```

Alanların anlamı:

- `source_paths`: mutant uygulanacak kod klasörleri veya dosyaları
- `test_command`: testleri çalıştıracak komut
- `exclude`: mutate edilmesini istemediğin klasör/dosyalar
- `timeout_multiplier`: baseline süresine göre timeout çarpanı
- `min_timeout`: minimum timeout süresi

## 8. `source_paths` içine ne yazmalıyım?

Genelde:

- kodun `src/` içindeyse `src`
- belirli paketi test etmek istiyorsan `src/my_package`
- tek dosya istiyorsan `src/my_package/service.py`

Buraya genelde `tests` yazma.

İyi örnekler:

```toml
source_paths = ["src"]
```

```toml
source_paths = ["src/my_package"]
```

```toml
source_paths = ["src/my_package/service.py"]
```

## 9. Test tarafında ne kullanabiliriz?

### Önerilen: `pytest`

Yeni başlıyorsan en doğru seçenek bu:

```toml
test_command = ["pytest", "-q"]
```

İstersen sadece `tests` klasörünü koş:

```toml
test_command = ["pytest", "-q", "tests"]
```

### `unittest` da kullanılabilir

Bu araç komut çalıştırdığı için, şu koşulları sağlayan herhangi bir test komutu kullanılabilir:

- testleri çalıştırmalı
- testler geçerse `0` dönmeli
- testler fail ise sıfırdan farklı kod dönmeli

Örnek:

```toml
test_command = ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
```

Ama yeni başlayan için tavsiyem yine `pytest`.

## 10. Sıfırdan küçük bir örnek

### Uygulama kodu

Dosya: `src/sample_project/calculator.py`

```python
def is_positive(value: int) -> bool:
    return value > 0
```

### Test kodu

Dosya: `tests/test_calculator.py`

```python
from sample_project.calculator import is_positive


def test_positive_number() -> None:
    assert is_positive(5) is True


def test_zero_is_not_positive() -> None:
    assert is_positive(0) is False
```

Bu neden iyi?

- ilk test normal durumu kontrol ediyor
- ikinci test sınır değerini kontrol ediyor
- kod `>` yerine `>=` olursa ikinci test fail olacak

Yani mutant öldürülmüş olacak.

## 11. Komut satırından nasıl kullanılır?

### Temel kullanım

```bash
python -m mutation_tool run .
```

### Az sayıda mutant ile deneme

```bash
python -m mutation_tool run . --max-mutants 10
```

### Sadece belli operatörlerle çalışma

```bash
python -m mutation_tool run . --operator comparison --operator logical
```

### İlk survivor'dan sonra durma

```bash
python -m mutation_tool run . --max-mutants 20 --stop-on-survivor
```

Bu seçenek, ilk survivor görüldüğünde daha fazla mutant koşmadan analizi durdurur.

### Mevcut operatörleri görmek

```bash
python -m mutation_tool list-operators
```

## 12. UI nasıl kullanılır?

UI'yı başlat:

```bash
python -m mutation_tool ui
```

Sonra şu adrese git:

```text
http://127.0.0.1:8787
```

## 13. UI alanlarını nasıl dolduracağım?

Burada sanırım "UI'da neleri nasıl dolduracağız" demek istedin; hepsini tek tek anlatıyorum.

### `Project root`

Buraya ne yazılır?

- mutation test uygulamak istediğin projenin ana klasörü

Örnek:

- `.`
- `C:\Users\Emre\Desktop\my-project`

Terminal zaten proje klasöründeyse en kolayı:

- `.`

### `Config path`

Buraya ne yazılır?

- özel bir config dosyası yolu

Genelde boş bırak.

Ne zaman doldurulur?

- config varsayılan `pyproject.toml` dışındaysa
- ya da elle başka config göstermek istiyorsan

### `Source paths`

Buraya ne yazılır?

- mutate edilmesini istediğin kod yolu
- birden fazla yazacaksan virgül ile ayır

Örnek:

- `src`
- `src/my_package`
- `src/my_package/service.py`
- `src,src/my_package/utils.py`

Yeni başlayan için en iyi seçim:

- `src`

### `Operators`

Ne yapmalıyım?

- listeden mutation tiplerini seç
- ya da hiç seçme, tüm varsayılan operatörler kullanılsın

Yeni başlıyorsan ilk denemede boş bırakabilirsin.

### `Max mutants`

Buraya ne yazılır?

- o run için en fazla kaç mutant çalışacağı

Yeni başlayan için önerim:

- `5`
- `10`
- en fazla `20`

İlk denemede ideal değer:

- `10`

### `Timeout (sec)`

Buraya ne yazılır?

- her mutant için maksimum süre

Emin değilsen:

- boş bırak

Araç baseline süresine göre timeout hesaplayabilir.

### `Fail run when a survivor appears`

Bu ne işe yarar?

- en az bir survivor varsa run'ı fail kabul eder

Nerede faydalı?

- CI
- kalite kapısı
- otomatik kontrol süreçleri

İlk denemelerde genelde:

- işaretleme

### `Stop after the first survivor`

Bu ne işe yarar?

- ilk survivor bulunduğu anda koşuyu durdurur

Nerede faydalı?

- hızlı geri bildirim istediğinde
- önce ilk problemi görmek istediğinde
- büyük projede denemeleri kısa tutmak istediğinde

İlk denemelerde genelde:

- kapalı bırak

## 14. Hiç bilmeyen biri için baştan sona akış

Sıfırdan şu sırayla git:

1. Küçük bir Python projesi oluştur
2. Kodları `src/` içine koy
3. Testleri `tests/` içine koy
4. `pytest` kur
5. Önce normal testlerin geçtiğinden emin ol:

```bash
python -m pytest
```

6. `pyproject.toml` içine mutation ayarlarını ekle
7. Küçük bir deneme koş:

```bash
python -m mutation_tool run . --max-mutants 10
```

8. Ya da UI aç:

```bash
python -m mutation_tool ui
```

9. Survivor'lara bak
10. Eksik davranışlar için yeni test yaz
11. Tekrar mutation run yap

## 15. Testleri nasıl yazmalıyız?

En kritik konu bu.

Zayıf test:

- sadece tek bir normal girdiyi kontrol eder

Güçlü test:

- normal durumu kontrol eder
- sınır değerini kontrol eder
- geçersiz girdiyi kontrol eder
- true ve false dallarını kontrol eder
- sonucu net şekilde assert eder

Neleri test etmelisin?

- sınır değerler: `0`, `1`, `-1`
- boş değerler: `""`, `[]`, `{}`
- `None` kabul ediliyorsa `None`
- exception davranışı
- boolean kararlar
- `if/else` dalları
- döngüler ve durma koşulları
- yan etkiler: dosya yazma, veri güncelleme, lojik kararlar

### `pytest` ile faydalı kalıplar

#### Net assertion

```python
def test_total() -> None:
    assert calculate_total(10, 2) == 12
```

#### Sınır durumu

```python
def test_zero_case() -> None:
    assert is_positive(0) is False
```

#### Exception testi

```python
import pytest


def test_negative_age_raises() -> None:
    with pytest.raises(ValueError):
        validate_age(-1)
```

#### Parametrize

```python
import pytest


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (5, True),
        (0, False),
        (-3, False),
    ],
)
def test_is_positive(value: int, expected: bool) -> None:
    assert is_positive(value) is expected
```

## 16. Survivor çıkarsa ne yapmalıyım?

Diyelim araç şu mutantın yaşadığını söyledi:

- original: `value > 0`
- mutated: `value >= 0`

Bu ne demek?

- testlerin `0` ile pozitif sayıyı ayıramıyor

O zaman şunu eklersin:

```python
def test_zero_is_not_positive() -> None:
    assert is_positive(0) is False
```

Yani mantık şu:

- survivor'u gör
- hangi davranışın değiştiğini anla
- o davranışa uygun test yaz
- tekrar çalıştır

## 17. İlk aşamada en iyi strateji

Büyük projede her şeyi bir anda koşma.

Şunla başla:

- tek bir modülle
- `--max-mutants 10`
- varsayılan operatörlerle

İyi ilk komut:

```bash
python -m mutation_tool run . --max-mutants 10
```

## 18. Sık yapılan hatalar

### Baseline testler zaten fail

Sorun:

- mutation hemen durur

Çözüm:

- önce normal testlerini düzelt
- mutation testing ancak yeşil test suite üzerinde anlamlıdır

### Yanlış klasörü mutate etmek

Sorun:

- `source_paths` içine `tests` yazmak

Çözüm:

- uygulama kodunu göster, genelde `src`

### Sadece happy-path test yazmak

Sorun:

- çok fazla survivor çıkar

Çözüm:

- edge-case test ekle
- false-path test ekle
- daha net assert yaz

### Başlangıçta çok fazla mutant koşmak

Sorun:

- süre uzar ve sonuçlar karmaşık olur

Çözüm:

- önce `5` veya `10` mutant ile dene

## 19. Sonuçları nerede göreceğim?

- CLI özetini terminalde
- UI panelini tarayıcıda
- JSON raporunu `.mutation-tool/last-run.json` içinde

## 20. Bu projenin kendi testleri nasıl çalışır?

Eğer bu mutation tool projesinin kendisini geliştiriyorsan şu komutları kullan:

```bash
python -m pytest
python -m mypy src
python -m ruff check .
```

Bu projede şu araçlar kullanılıyor:

- `pytest` test koşmak için
- `mypy` tip kontrolü için
- `ruff` lint için
- `FastAPI TestClient` UI/API testleri için

## 21. En basit ve doğru başlangıç seti

En kolayı şu:

- test framework: `pytest`
- kod klasörü: `src`
- ayarlar:

```toml
[tool.mutation_tool]
source_paths = ["src"]
test_command = ["pytest", "-q"]
exclude = ["tests/**", "**/__pycache__/**"]
timeout_multiplier = 5.0
min_timeout = 5.0
```

- ilk run:

```bash
python -m mutation_tool run . --max-mutants 10
```

- ilk UI run:

```bash
python -m mutation_tool ui
```

Sadece bu akışı uygularsan bile sağlam bir başlangıç yapmış olursun.
