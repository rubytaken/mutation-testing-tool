# Beginner Demo Project

Bu klasor, mutation testing aracini denemek icin hazirlanmis kucuk bir ornek projedir.

Amac:

- normal testlerin nasil calistigini gormek
- mutation run sonuclarini incelemek
- survivor cikinca nasil test eklenecegini ogrenmek

## Klasor yapisi

```text
examples/beginner_demo/
  pyproject.toml
  src/demo_app/calculator.py
  tests/test_calculator.py
```

## 1. Normal testleri calistir

Ana proje klasorundeyken:

```bash
python -m pytest examples/beginner_demo/tests -q
```

Bu adimda tum testlerin gecmesi gerekir.

## 2. Mutation testing calistir

Ana proje klasorundeyken:

```bash
python -m mutation_tool run examples/beginner_demo --max-mutants 10
```

## 3. UI ile calistir

```bash
python -m mutation_tool ui
```

Sonra tarayicida su alanlari doldur:

- `Project root`: `examples/beginner_demo`
- `Config path`: bos birak
- `Source paths`: `src`
- `Operators`: ilk denemede bos birak
- `Max mutants`: `10`
- `Timeout (sec)`: bos birak
- `Fail run when a survivor appears`: kapali birak

## 4. Bu ornekte ne beklenir?

Bu ornek projede hem iyi hem zayif testler var.

- `is_adult()` icin testler daha guclu
- `is_positive()` icin test kasitli olarak eksik

Yani ilk mutation run'da bazi mutantlar oldurulurken bazilari survivor olabilir.

Ozellikle `is_positive(0)` gibi bir sinir durumu eksik oldugu icin survivor gorme ihtimalin yuksek.

## 5. Survivor gorursen ne yapacaksin?

Ilk bakman gereken sey, mutantin hangi davranisi degistirdigidir.

Ornek:

- original: `value > 0`
- mutated: `value >= 0`

Bu durumda eksik test sunu anlatir:

- `0` degeri icin davranis kontrol edilmiyor

Eklenmesi gereken test:

```python
def test_zero_is_not_positive() -> None:
    assert is_positive(0) is False
```

Sonra tekrar calistir:

```bash
python -m mutation_tool run examples/beginner_demo --max-mutants 10
```

## 6. Ogrenme hedefi

Bu ornek proje ile su mantigi net gorursun:

1. Testler yesil olabilir
2. Ama yine de zayif olabilir
3. Mutation testing bu zayifligi ortaya cikarir
4. Survivor'a gore yeni test eklersin
5. Test kaliten artar
