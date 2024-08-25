﻿# курс СкиллФакТори по Джанго

прохожу обучение в компании СкиллФакТори - _**Профессия Python-разработчик**_. начал тему Джанго. 

тут тренировочные проекты. в них, в процессе обучения, выполняю задания курса и отрабатываю всё, что там показывают. 
в коммитах можно увидеть сам процесс.

отдельно веду разработку контрольного проекта: 
**"[Новостной сайт](https://github.com/Archangel-Ray/SkillFactory_NewsPaper)"**. по заданиям курса.


у СкиллФакТори нет никакой последовательности и хоть какого-то обобщения. курс перепрыгивает с одного проекта на другой,
создаёт новые никак не привязываясь к предыдущим и не показывая логики для создания этого проекта. проектов получилось 
много и я уже сам не помню что в них. названия не имеют логики (взяты с потолка) как бы - "для примера". 
решил описать проекты чтоб самому понимать как их можно использовать.

1. **[first_project](first_project)**
так и есть. это был первый. в нём подключены "flatpages", статика и шаблоны. показано бар-меню и три страницы.
сделан под диктовку. то есть я всё просто скопировал и только сейчас понимаю, что тут происходило. 
больше к этому проекту не возвращались.

2. **[NewsPaper](NewsPaper)**
этот урок я проходил дважды с разрывом в полгода. так как я окончательно убедился что СкиллФакТори не даст знаний и 
заморозил курс. пошёл, изучил ООП, Джанго и только тогда вернулся обратно. в первый раз делалось под диктовку, но 
второй уже был с пониманием происходящего. это было приятное ощущение.
* в этом проекте два пустых приложения и одно приложение с моделями. 
* три таблицы с товарами, работниками и заказами.
* через "Django shell" в базе созданы записи. 
* то есть кроме базы данных в нём больше нет ничего.

3. **[Training_Views](Training_Views)**
и вот в этом СкиллФакТори. бросили предыдущий проект и теперь в новом показывают как выводить информацию на сайт 
из базы. в этом проекте одно приложение, подключены "flatpages" и две страницы. на одной выведен список из базы 
с поиском. на второй отдельный товар. подключён шаблон создания и редактирования товара. показаны:
* дженерики представлений;
* условный оператор и оператор перебора;
* фильтры и создание собственного;
* работа с тегами;
* отображение даты;
* разбивка на страницы;
* фильтрация в представлении и форма фильтра шаблоне;
* форма для запроса;
* верификация.

* это, пока, единственный проект к которому вернулись. добавляется: кеширование.
* потом на нём демонстрировалась выгрузка базы, создание команд для manage.py и работа с админ-панелью.

4. **[simple_signup](simple_signup)**
проект создан для демонстрации аутентификации. то есть тут больше ничего и нет. почему нельзя было это сделать 
в предыдущем проекте не спрашивайте. Это СкиллФакТори... здесь подключён "allauth", показана работа в админ-панели 
с пользователями и группами. аутентификация через провайдера. и отправку почты зацепили.

5. **[project](project)**
это совсем чудесный проект. дело было так: 
начинается урок в котором демонстрируется некий процесс в каком-то пространстве. было такое впечатление, что я не 
продолжаю курс, а зашёл куда-то в чужую аудиторию. где идёт на середине какой-то процесс и я вклинился посередине. 
я ничего не понимаю, что происходит. пошёл к ментору (Олегу Афанасьеву респект). он показывает что происходит в этом 
уроке. вот там чудесным образом и появляется этот проект неизвестного происхождения.
что здесь есть:
* одно приложение. в нём моделька с одной табличкой (назначение приёма у врача). на страничке сайта отображается форма 
запроса, которая делает запись в базу;
* шаблон для письма, которое отправляется по эл.почте;
* сделаны почтовые настройки и подключён Яндекс провайдер;
* созданы сигналы, которые отправляют шаблон по эл. почте;
* подключён планировщик "django-apscheduler". (с ним возникла заминка. только что запустил, а он не может библиотеку 
планировщика найти. последняя версия стояла. куда библиотека потерялась? переставил предыдущую версию пакета, 
а там она есть. как так?...) к планировщику подключены периодические задачи;
* организован запуск планировщика через manage.py

6. **[mcdonalds](mcdonalds)**
тут своя история. начинается новая тема и нам сообщают: "вернёмся к предыдущему проекту...". искал, искал - предыдущий, 
не нашёл. получился вот этот. здесь:
* модель с товарами, форма добавление заказа;
* подключается Селери и Редис;
* у Селери две задачи. одна должна отлеживать время выполнения заказа. вторая чистить базу каждую минуту. (сейчас 
проверить не смог, почему-то Селери потерялся. разбираться сейчас нет смысла)

7. **[template_for_a_new_website](template_for_a_new_website)**
это проект-шаблон на основе которого был создан 
проект **[create_project_using_template](create_project_using_template)**. в этом, созданном по шаблону проекту, создано 
приложение-шаблон и на его основе создано ещё одно приложение.

8. **[PostgreSQL_localhost](PostgreSQL_localhost)**
этот проект создавался для работы с "PostgreSQL", но никакой работы не было. по этому он совершенно пустой и здесь 
только настройка базы под "PostgreSQL"

## история процесса...
### первый этап:
создал новый проект и новый репозиторий, создал новую среду и добавил туда Джанго. теоретически это надо было делать 
в основном репозитории курса, но я тогда не знал как правильно это сделать.
### второй этап:
сделал полугодичный перерыв в курсе, чтобы завершить все незаконченные курсы и не рассеивать внимание на несколько 
курсов одновременно. 
- окончил углублённый курс для профи по Питону. ("Поколение Python" от Тимура Гуева на Степике) 
- прошёл полностью ООП. (тоже "Поколение Python") 
- не успел дойти курс по Джанго. (Инди-курс - "Django, потанцуем?" от Артема Егорова на Степике. прошёл три четверти, 
придётся заканчивать параллельно)
### третий этап:
перешёл на новый этап. для меня это действительно сложный переход. новый компьютер, новый ПайЧарм, новый Питон... 
всё совершенно новое и не знакомое. я работал на Питоне 3.7 в ПайЧарме 2018. теперь у меня всё новейшее, и программы, 
и среда разработки, и библиотеки, и приложения, и всё обновляется автоматически. очень непривычно и я слегка стрессую.
