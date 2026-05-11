# Password Validator Demo

Şifre güçlülük kontrolü etrafında küçük ama gerçekçi bir doğrulama mantığı. Mutation testing'in **karşılaştırma** (`<`, `<=`, `>=`) ve **mantıksal** (`and`, `or`, `not`) operatörlerini nasıl mutate ettiğini gözlemlemek için tasarlandı.

## Beklenen davranış

- `is_strong_password` 8+ karakter, en az 1 büyük harf, 1 rakam, 1 özel karakter ister.
- `categorize_strength` 0–5 arası puana göre `weak / medium / strong` döner.

## Beklenen survivor'lar

Testler tüm fonksiyonelliği kapsar **ama bazı sınır değerleri eksik bırakır**:

- `len(password) < 8` → `len(password) <= 8` mutasyonu: testler tam 8 karakter için sınır kontrolü yapmıyor.
- `score <= 2` → `score < 2`: tam puan = 2 olan bir senaryo test yok.
- `score <= 4` → `score < 4`: tam puan = 4 senaryosu eksik.

## Çalıştır

```bash
pytest -q
python -m mutation_tool run . --max-mutants 20
```
