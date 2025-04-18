## Вопросы для самопроверки по графикам в matplotlib

1. **Что такое полотно (figure)?**  
   Полотно (figure) — это весь графический холст, на котором размещаются одна или несколько осей (графиков). Создаётся с помощью `plt.figure()` или `plt.subplots()`.

2. **Что такое оси (axis)?**  
   Оси (axis) — это область внутри полотна, где непосредственно строятся графики. Они создаются через `figure.add_subplot()` или `plt.subplots()` и позволяют задавать масштаб, подписи и т.д.

3. **Сколько осей может быть на одном полотне?**  
   Неограниченное количество, в зависимости от нужд и компоновки. Обычно используется от 1 до 4, но можно и больше.

4. **Чем отличаются оси и полотно?**  
   Полотно — это контейнер для всего графического содержимого. Оси — это конкретные области на полотне, где строятся графики.

5. **Как построить график, который внутри графической оболочки?**  
   Использовать `plt.plot()` внутри `plt.figure()` или `plt.subplots()` и завершить командой `plt.show()`.

6. **Как построить несколько линий на одном графике?**  
   Вызвать `plt.plot(x1, y1)`, затем `plt.plot(x2, y2)` и т.д. перед `plt.show()`.

7. **Как изменить тип линии графика?**  
   Указать параметр стиля линии, например `'--'` или `':'` в функции `plot`, например `plt.plot(x, y, linestyle='--')`.

8. **Как изменить цвет линии графика?**  
   Через параметр `color`, например: `plt.plot(x, y, color='red')` или `plt.plot(x, y, 'g')`.

9. **Что такое легенда?**  
   Легенда — это пояснение к графику, указывающее, какие линии что означают. Создаётся через `plt.legend()` после присвоения меток (`label='...'`).

10. **Какие типы графиков вы строили в этой лабораторной? Чем они отличаются?**  
    Линейные графики, 3D-графики (`plot_surface`), контурные (`contour`), динамические (`pause` и анимация). Отличаются размерностью, способами представления данных и интерактивностью.

11. **Какие шаги нужно проделать, чтобы сделать трёхмерный график?**  
    - Импортировать `from mpl_toolkits.mplot3d import Axes3D`  
    - Создать `fig = plt.figure()`  
    - Добавить оси `ax = fig.add_subplot(111, projection='3d')`  
    - Использовать `ax.plot_surface(...)` или другие методы.

12. **Как поскомбинировать несколько графиков на одном полотне?**  
    Использовать `plt.subplots()` с несколькими подграфиками (`ax1`, `ax2`, ...), либо `fig.add_subplot(1, 2, 1)` и т.д.

13. **Что такое генератор? Чему он служил в этой лабораторной?**  
    Генератор — это объект, который порождает значения по мере необходимости. В лабораторной он использовался для динамического обновления данных во времени.

14. **Что делает функция `pause()`? Что будет, если ее не использовать?**  
    `plt.pause(t)` приостанавливает выполнение и позволяет обновить график. Без неё в интерактивных циклах график не будет отображаться обновлённым.
