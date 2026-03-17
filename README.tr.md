# Mutation Testing Tool - Turkce Rehber

Bu rehber, programin ne ise yaradigini, neden kullanildigini, nasil kuruldugunu, CLI ve UI ile nasil calistirildigini ve testleri nasil yazman gerektigini hic bilmeyen birine gore anlatir.

Hazir deneme projesi:

- `examples/beginner_demo/README.md`

## 1. Bu program nedir?

`mutation-tool` bir Python mutation testing aracidir.

Normal test sunu sorar:

- "Yazdigim testler kodu geciriyor mu?"

Mutation testing ise daha guclu bir soru sorar:

- "Yazdigim testler, koda sokulan kucuk hatalari fark edecek kadar guclu mu?"

Arac, kodunda kucuk degisiklikler yapar ve her degisiklikten sonra testlerini tekrar calistirir.

Ornek:

- kodunda `value > 0` var
- arac bunu `value >= 0` yapar
- testler fail olursa mutant `killed` olur
- testler hala gecerse mutant `survived` olur

Eger mutant yasiyorsa, genelde testlerinde eksik bir durum vardir.

## 2. Neden ise yarar?

Kod coverage sana satirin calistigini soyler.

Mutation testing ise testin o satirin davranisini gercekten kontrol edip etmedigini soyler.

Bu aracin faydalari:

- zayif testleri bulur
- eksik edge-case'leri bulur
- koda guveni artirir
- regresyon testlerini guclendirir

## 3. Program arkada nasil calisir?

Araci calistirdiginda su akisi izler:

1. `pyproject.toml` icinden ayarlari okur
2. `source_paths` icindeki Python dosyalarini bulur
3. Once normal testleri baseline olarak calistirir
4. Baseline fail ise hemen durur
5. Kodunu Python `ast` ile parse eder
6. Kucuk degisiklikler uretir:
   - `>` -> `>=`
   - `True` -> `False`
   - `and` -> `or`
   - `+` -> `-`
7. Projeyi gecici bir klasore kopyalar
8. Her seferinde tek bir mutant uygular
9. Test komutunu mutated kopya uzerinde calistirir
10. Sonucu kaydeder
11. `.mutation-tool/last-run.json` raporunu uretir

Onemli:

- normal bir run sirasinda gercek kaynak dosyalarini dogrudan bozmaz
- gecici kopyalar uzerinde calisir

## 4. Sonuclar ne anlama gelir?

- `killed`: testler fail oldu, yani mutant yakalandi
- `survived`: testler gecti, yani hata fark edilmedi
- `timeout`: mutant testi cok uzun surdu
- `error`: mutant syntax/import gibi bir problemi tetikledi

## 5. Yeni baslayan icin onerilen proje yapisi

En kolay baslangic icin su yapiyi kullan:

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

Test framework onerisi:

- en iyi secenek: `pytest`

Neden `pytest`?

- yeni baslayan icin kolay
- yazimi kisa
- Python ekosisteminde cok yaygin
- bu aracta varsayilan secenek zaten bu

## 6. Kurulum

### Adim 1: Virtual environment olustur

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

### Adim 2: Araci ve gelistirme bagimliliklarini kur

```bash
python -m pip install -e .[dev]
```

## 7. Temel ayarlar

Projenin `pyproject.toml` dosyasina sunu ekle:

```toml
[tool.mutation_tool]
source_paths = ["src"]
test_command = ["pytest", "-q"]
exclude = ["tests/**", "**/__pycache__/**"]
timeout_multiplier = 5.0
min_timeout = 5.0
```

Alanlarin anlami:

- `source_paths`: mutant uygulanacak kod klasorleri veya dosyalari
- `test_command`: testleri calistiracak komut
- `exclude`: mutate edilmesini istemedigin klasor/dosyalar
- `timeout_multiplier`: baseline suresine gore timeout carpani
- `min_timeout`: minimum timeout suresi

## 8. `source_paths` icine ne yazmaliyim?

Genelde:

- kodun `src/` icindeyse `src`
- belirli paketi test etmek istiyorsan `src/my_package`
- tek dosya istiyorsan `src/my_package/service.py`

Buraya genelde `tests` yazma.

Iyi ornekler:

```toml
source_paths = ["src"]
```

```toml
source_paths = ["src/my_package"]
```

```toml
source_paths = ["src/my_package/service.py"]
```

## 9. Test tarafinda ne kullanabiliriz?

### Onerilen: `pytest`

Yeni basliyorsan en dogru secenek bu:

```toml
test_command = ["pytest", "-q"]
```

Istersen sadece `tests` klasorunu kos:

```toml
test_command = ["pytest", "-q", "tests"]
```

### `unittest` da kullanilabilir

Bu arac komut calistirdigi icin, su kosullari saglayan herhangi bir test komutu kullanilabilir:

- testleri calistirmali
- testler gecerse `0` donmeli
- testler fail ise sifirdan farkli kod donmeli

Ornek:

```toml
test_command = ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
```

Ama yeni baslayan icin tavsiyem yine `pytest`.

## 10. Sifirdan kucuk bir ornek

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
- ikinci test sinir degerini kontrol ediyor
- kod `>` yerine `>=` olursa ikinci test fail olacak

Yani mutant oldurulmus olacak.

## 11. Komut satirindan nasil kullanilir?

### Temel kullanim

```bash
python -m mutation_tool run .
```

### Az sayida mutant ile deneme

```bash
python -m mutation_tool run . --max-mutants 10
```

### Sadece belli operatorlerle calisma

```bash
python -m mutation_tool run . --operator comparison --operator logical
```

### Ilk survivor'dan sonra durma

```bash
python -m mutation_tool run . --max-mutants 20 --stop-on-survivor
```

Bu secenek, ilk survivor goruldugunde daha fazla mutant kosmadan analizi durdurur.

### Mevcut operatorleri gormek

```bash
python -m mutation_tool list-operators
```

## 12. UI nasil kullanilir?

UI'yi baslat:

```bash
python -m mutation_tool ui
```

Sonra su adrese git:

```text
http://127.0.0.1:8787
```

## 13. UI alanlarini nasil dolduracagim?

Burada sanirim "UI'da neleri nasil dolduracagiz" demek istedin; hepsini tek tek anlatiyorum.

### `Project root`

Buraya ne yazilir?

- mutation test uygulamak istedigin projenin ana klasoru

Ornek:

- `.`
- `C:\Users\Emre\Desktop\my-project`

Terminal zaten proje klasorundeyse en kolayi:

- `.`

### `Config path`

Buraya ne yazilir?

- ozel bir config dosyasi yolu

Genelde bos birak.

Ne zaman doldurulur?

- config varsayilan `pyproject.toml` disindaysa
- ya da elle baska config gostermek istiyorsan

### `Source paths`

Buraya ne yazilir?

- mutate edilmesini istedigin kod yolu
- birden fazla yazacaksan virgul ile ayir

Ornek:

- `src`
- `src/my_package`
- `src/my_package/service.py`
- `src,src/my_package/utils.py`

Yeni baslayan icin en iyi secim:

- `src`

### `Operators`

Ne yapmaliyim?

- listeden mutation tiplerini sec
- ya da hic secme, tum varsayilan operatorler kullanilsin

Yeni basliyorsan ilk denemede bos birakabilirsin.

### `Max mutants`

Buraya ne yazilir?

- o run icin en fazla kac mutant calisacagi

Yeni baslayan icin onerim:

- `5`
- `10`
- en fazla `20`

Ilk denemede ideal deger:

- `10`

### `Timeout (sec)`

Buraya ne yazilir?

- her mutant icin maksimum sure

Emin degilsen:

- bos birak

Arac baseline suresine gore timeout hesaplayabilir.

### `Fail run when a survivor appears`

Bu ne ise yarar?

- en az bir survivor varsa run'i fail kabul eder

Nerede faydali?

- CI
- kalite kapisi
- otomatik kontrol surecleri

Ilk denemelerde genelde:

- isaretleme

### `Stop after the first survivor`

Bu ne ise yarar?

- ilk survivor bulundugu anda kosuyu durdurur

Nerede faydali?

- hizli geri bildirim istediginde
- once ilk problemi gormek istediginde
- buyuk projede denemeleri kisa tutmak istediginde

Ilk denemelerde genelde:

- kapali birak

## 14. Hic bilmeyen biri icin bastan sona akıs

Sifirdan su sirayla git:

1. Kucuk bir Python projesi olustur
2. Kodlari `src/` icine koy
3. Testleri `tests/` icine koy
4. `pytest` kur
5. Once normal testlerin gectiginden emin ol:

```bash
python -m pytest
```

6. `pyproject.toml` icine mutation ayarlarini ekle
7. Kucuk bir deneme kos:

```bash
python -m mutation_tool run . --max-mutants 10
```

8. Ya da UI ac:

```bash
python -m mutation_tool ui
```

9. Survivor'lara bak
10. Eksik davranislar icin yeni test yaz
11. Tekrar mutation run yap

## 15. Testleri nasil yazmaliyiz?

En kritik konu bu.

Zayif test:

- sadece tek bir normal girdiyi kontrol eder

Guclu test:

- normal durumu kontrol eder
- sinir degerini kontrol eder
- gecersiz girdiyi kontrol eder
- true ve false dallarini kontrol eder
- sonucu net sekilde assert eder

Neleri test etmelisin?

- sinir degerler: `0`, `1`, `-1`
- bos degerler: `""`, `[]`, `{}`
- `None` kabul ediliyorsa `None`
- exception davranisi
- boolean kararlar
- `if/else` dallari
- donguler ve durma kosullari
- yan etkiler: dosya yazma, veri guncelleme, logik kararlar

### `pytest` ile faydali kaliplar

#### Net assertion

```python
def test_total() -> None:
    assert calculate_total(10, 2) == 12
```

#### Sinir durumu

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

## 16. Survivor cikarsa ne yapmaliyim?

Diyelim arac su mutantin yasadigini soyledi:

- original: `value > 0`
- mutated: `value >= 0`

Bu ne demek?

- testlerin `0` ile pozitif sayiyi ayiramiyor

O zaman sunu eklersin:

```python
def test_zero_is_not_positive() -> None:
    assert is_positive(0) is False
```

Yani mantik su:

- survivor'u gor
- hangi davranisin degistigini anla
- o davranisa uygun test yaz
- tekrar calistir

## 17. Ilk asamada en iyi strateji

Buyuk projede her seyi bir anda kosma.

Sunla basla:

- tek bir modulle
- `--max-mutants 10`
- varsayilan operatorlerle

Iyi ilk komut:

```bash
python -m mutation_tool run . --max-mutants 10
```

## 18. Sık yapilan hatalar

### Baseline testler zaten fail

Sorun:

- mutation hemen durur

Cozum:

- once normal testlerini duzelt
- mutation testing ancak yesil test suite uzerinde anlamlidir

### Yanlis klasoru mutate etmek

Sorun:

- `source_paths` icine `tests` yazmak

Cozum:

- uygulama kodunu goster, genelde `src`

### Sadece happy-path test yazmak

Sorun:

- cok fazla survivor cikar

Cozum:

- edge-case test ekle
- false-path test ekle
- daha net assert yaz

### Baslangicta cok fazla mutant kosmak

Sorun:

- sure uzar ve sonuclar karmasik olur

Cozum:

- once `5` veya `10` mutant ile dene

## 19. Sonuclari nerede gorecegim?

- CLI ozetini terminalde
- UI panelini tarayicida
- JSON raporunu `.mutation-tool/last-run.json` icinde

## 20. Bu projenin kendi testleri nasil calisir?

Eger bu mutation tool projesinin kendisini gelistiriyorsan su komutlari kullan:

```bash
python -m pytest
python -m mypy src
python -m ruff check .
```

Bu projede su araclar kullaniliyor:

- `pytest` test kosmak icin
- `mypy` tip kontrolu icin
- `ruff` lint icin
- `FastAPI TestClient` UI/API testleri icin

## 21. En basit ve dogru baslangic seti

En kolayi su:

- test framework: `pytest`
- kod klasoru: `src`
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

Sadece bu akisi uygularsan bile saglam bir baslangic yapmis olursun.
