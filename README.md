### Проект стабильной обёртки Selenium Webdriver с явными ожиданиями

Реализован простой тест нахождения в поисковике вкладки pull requests репозитория и проверки количество реквестов на странице
* Создан модуль browser в котором 
  * Иницализируются:
    * driver
    * implicit wait
  * Хранятся методы:
    * open
    * element
    * type
    * click
    * assert_that
    * quit