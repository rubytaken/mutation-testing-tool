# Banking Demo

Para işlemleri etrafında küçük bir bankacılık modülü. Mutation testing'in **karşılaştırma** (`<`, `<=`, `==`) ve **aritmetik** (`+`, `-`, `*`, `/`) operatörlerini para mantığında nasıl mutate ettiğini gözlemlemek için tasarlandı.

## Beklenen davranış

- `withdraw` günlük limiti ve bakiyeyi kontrol eder.
- `transfer_fee` kademeli ücret (sabit + yüzde) hesaplar.
- `apply_daily_interest` bileşik faiz uygular.

## Beklenen survivor'lar

- `amount > daily_limit` → `amount >= daily_limit`: tam limit değeriyle test yok.
- `amount > balance` → `amount >= balance`: tam bakiye = miktar senaryosu eksik.
- `amount <= 100` → `amount < 100`: ücret eşiğinin tam sınırı test edilmiyor.
- `balance <= 0` → `balance < 0`: sıfır bakiye için faiz testi yok.

## Çalıştır

```bash
pytest -q
python -m mutation_tool run . --max-mutants 25
```
