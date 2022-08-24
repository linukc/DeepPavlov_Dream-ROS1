# DeepPavlov_Dream-ROS1

Используется отдельная версия Dream, в которой обучен IntentCatcherTransformers на 4 класса (tracking, moving forward, moving backward, turning around). Бот способен поддерживать обычное общение, если ни одна из этих команд не распознана.

Для запуска Dream необходимо:

- выполнить команду  `docker-compose -f docker-compose.yml -f assistant_dists/dream_robot/docker-compose.override.yml -f assistant_dists/dream_robot/dev.yml -f assistant_dists/dream_robot/proxy.yml up`
(с флагом --build в первый раз)

Для запуска текстового планировщика необходимо выполнить сборку ROS workspace. Для этого в корне проекта в отдельном терминале выполняются команды:

`catkin_make`

`source devel/setup.bash`

`roslaunch basic_text_mover basic_text_mover.launch`  

Для запуска перемещения в отдельном терминале выполняются команды:

- `cd src/communication/docker/`
- `./build.sh` (в первый раз)
- `./start.sh`
- `./into.sh`
- `python3 src/communication/src/main.py <любое количество текста>` (текст на английском)

Переданные аргументы будут сформированы в предложение и отправлены Dream на обработку. В случае распознавания комманды, выполнится одна из команд перемещения.
Существующий список команд перемещения:
turn_90_clockwise  
turn_180_clockwise  
turn_270_clockwise  
turn_360_clockwise  
turn_90_counterclockwise  
turn_180_counterclockwise  
turn_270_counterclockwise  
turn_360_counterclockwise  
forward_1  
forward_2  
backward_2  
backward_2  
