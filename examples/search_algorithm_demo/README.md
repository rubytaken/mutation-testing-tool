# Search Algorithm Demo

Klasik arama ve pencere algoritmaları. Mutation testing'in **off-by-one** hatalarını ve **algoritmik sabit kayma**larını (`mid + 1` vs `mid`, `<=` vs `<`) nasıl ortaya çıkardığını gösterir.

## Beklenen davranış

- `binary_search` sıralı listede `target`'ı arar; bulamazsa `-1`.
- `count_occurrences` sıralı listede `target`'ın kaç kez geçtiğini sayar.
- `max_in_window` `window` boyutunda kayan pencerelerdeki maksimumu döner.

## Beklenen survivor'lar

- `low <= high` → `low < high`: tek elemanlı liste senaryosu eksik olabilir.
- `mid + 1` → `mid`: bazı durumlarda timeout yapar (mutation tool zaten "timeout" diye işaretler), bazılarında survivor kalır.
- `window <= 0` → `window < 0`: tam sıfır pencere boyutu testi eksik.

## Çalıştır

```bash
pytest -q
python -m mutation_tool run . --max-mutants 25
```
