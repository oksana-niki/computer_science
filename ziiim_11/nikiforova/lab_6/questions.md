# Вопросы для самопроверки по системам управления версиями (СУВ)

1. **Что такое система управления версиями?**  
   Это программное обеспечение, позволяющее отслеживать и управлять изменениями в коде или документации со временем.

2. **Какие системы управления версиями вы знаете?**  
   Git, Subversion (SVN), Mercurial, CVS, Perforce.

3. **Что происходит, когда пользователь СУВ создаёт новый коммит?**  
   Создаётся снимок изменений (snapshot), который сохраняется в истории проекта вместе с метаданными: автором, временем и сообщением коммита.

4. **Что такое ветвь?**  
   Ветвь — это отдельная линия разработки, которая позволяет вносить изменения изолированно от основной (стабильной) версии проекта.

5. **Как произвести слияние ветви со стволом проекта?**  
   С помощью команды `git merge` или аналогичной. Система объединяет изменения ветки с основной линией разработки (например, `main`).

6. **Как обычно организуется работа со стволом?**  
   В ствол вносятся только проверенные и протестированные изменения. Разработка ведётся в ветках, которые затем сливаются в ствол.

7. **Где можно посмотреть revision-номер?**  
   В Git — это хеш коммита (например, `git log`). В других СУВ, таких как SVN — это числовой номер версии.

8. **Что делает хранилище?**  
   Хранилище (репозиторий) сохраняет полную историю изменений проекта и обеспечивает доступ к ним для разработчиков.

9. **Что такое бэкпорт?**  
   Это перенос исправлений или функций из новой версии проекта в старую (например, из `main` в `release-1.0`).

10. **Чем отличается рабочая копия проекта от проекта в хранилище?**  
    Рабочая копия — это локальное состояние проекта, которое может включать незакоммиченные изменения. Хранилище содержит только сохранённые коммиты.

11. **С какой СУВ вы работали в этой лабораторной? К какому виду она относится?**  
    Чаще всего используется Git. Он относится к распределённым системам управления версиями.

12. **Что произойдёт при слиянии двух разных ветвей из упражнения 2?**  
    Будет создан коммит слияния, объединяющий изменения из обеих ветвей. Если изменения конфликтуют, потребуется разрешить конфликты вручную.
