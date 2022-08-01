# DeepPavlov_Dream-ROS1

Используется отдельная версия Dream, в которой обучен IntentCatcherTransformers (пингуется http://0.0.0.0:8014/detect)  на 4 класса (tracking, moving forward, moving backward, turning around).

Для запуска Dream необходимо:

- создать папку `.deeppavlov/models/classifiers/` рядом с папкой dream и в нее распаковать [архив](https://drive.google.com/file/d/1Hbb54iePhfYihfiTqWOfUrvMed9zGWxZ/view?usp=sharing) с обученной моделью

- выполнить команду  `docker-compose -f docker-compose.yml -f assistant_dists/dream_robot/docker-compose.override.yml -f assistant_dists/dream_robot/dev.yml -f assistant_dists/dream_robot/proxy.yml up`
(с флагом --build в первый раз)

Для запуска текстового планировщика необходимо выполнить сборку ROS workspace. Для этого в корне проекта в отдельном терминале выполняются команды:

`catkin_make`

`source devel/setup.bash`

`roslaunch basic_text_mover basic_text_mover.launch`  

Для запуска перемещения в отдельном терминале выполняется команда:

`python3 src/communication/src/main.py <любое количество текста>`

Переданные аргументы будут сформированы в предложение и отправлены Dream на обработку. В случае учпешного ответа выполнется одна из команд перемещения. В текущей версии используется дополнительное сопоставление для преобразования moving forward, moving backward, turning around к командам:

moving forward -> forward_1

moving backward -> backward_1

turning around -> turn_360_clockwise
