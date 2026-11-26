# Лабораторная 5 · Настройки линтера / форматтера учебного проекта

**Касьян А.С. · Вариант 12**

## Постановка

Конфиг ESLint/Prettier/ruff/editorconfig (на выбор). Ветка `stricter-rules` усиливает правила; ветка `team-exceptions` ослабляет или меняет те же опции. Разрешите конфликт конфига, кратко обоснуйте итог в README.

## Как возник конфликт

От исходной ветки с оглавлением создана база `editor-base` с четырьмя пробелами и пределом в 100 символов. Две рабочие ветки редактируют одну строку. Проследить изменения можно через `git log --graph --oneline --all`.

| Этап | Команда или действие |
|---|---|
| Подготовка | `git switch -c editor-base main`, добавить .editorconfig и сделать коммит |
| Строгие правила | `git switch -c stricter-rules editor-base`, установить 79 |
| Предложение команды | `git switch -c team-exceptions editor-base`, установить 120 |
| Интеграция | В lab-05 принять изменения team-exceptions и выполнить `git merge stricter-rules` |
| Проверка конфликта | `git ls-files -u` показывает базу и обе версии одного файла |

Фрагмент файла после остановки слияния

```text
<<<<<<< HEAD
max_line_length = 120
=======
max_line_length = 79
>>>>>>> stricter-rules
```

В итоговом файле предел в 88 символов сохраняет читаемость кода. Для тестовых данных в tests/*.py разрешены 120 символов, чтобы таблицы примеров читались построчно. После удаления маркеров выполнены `git add .editorconfig` и `git commit`. Оба родителя доступны через `git show --format=raw 824264b`.

## Удалённый репозиторий

```sh
git remote -v
git push -u origin lab-05 stricter-rules team-exceptions
git pull --ff-only origin lab-05
```
