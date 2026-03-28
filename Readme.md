# CSV Reports CLI

Скрипт для агрегации данных о студентах из CSV-файлов и формирования отчетов.

## Поддерживаемые отчеты

- `median-coffee` — медианная сумма трат на кофе по каждому студенту (по всем переданным файлам)

## Пример запуска

```bash
python main.py --files math.csv physics.csv programming.csv --report median-coffee