# DZ 22
## Проверка кода на запахи
Проверял [работу Вадима Бенденко](https://github.com/bendenko-v/SkyPro-Homework-21 "Ссылка на работу")

### Функционал в Абстрактном классе
В файле *class_abc.py* описана функциональность инициализации в строке 6 \
Следует описать данную функциональность в классе ***BaseStorage*** в файле *class_base_storage.py*

### Во всех файлах хранилища используется переменная с названием ***qty***
Например, в файле *class_base_storage.py* в строке 13 описана переменная ***qty*** \
Я бы назвал ее более понятным именем, например ***quantity***

### В классе ***Shop*** в файле *class_shop.py* повторение кода
В функции ***add*** повторяется тот же самый код, что и в классе ***BaseStorage*** в функции ***add*** \
Следует вызывать функционал ***add*** из класса ***BaseStorage*** через ***super()***, 
оставив в функции только проверку на количество уникальных товаров

### В классах ***Shop*** и ***Storage*** в файлах *class_shop.py* и *class_storage.py* повторение кода
Функции ***__repr\__*** представляют одинаковый функционал, который можно вынести в базовый класс
***BaseStorage*** в файле *class_base_storage.py*

# В целом, работа выполнена отлично :)