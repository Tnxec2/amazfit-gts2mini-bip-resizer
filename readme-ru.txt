
1. Создаем рабочую папку c:\bip3
2. Скачиваем актуальную версия парсера в рабочую папку c:\bip3
https://github.com/Tnxec2/py_amazfit_tools/raw/GTS2mini/output/gts2mini/main.exe
3. Скачиваем BIN файл в рабочую папку (amaz_nike_en_na-gts2mini.bin)
4. Распаковываем BIN парсером:
cmd
cd c:\bip3
main.exe --gts2mini --file amaz_nike_en_na-gts2mini.bin

(для BipU пишем вместо --gts2mini параметр --bipu)

в рабочей папке появится новая папка "amaz_nike_en_na-gts2mini" с файлами изображений (0000.png - 0089.png), json файл (amaz_nike_en_na.json), 
log файл (amaz_nike_en_na.log), Preview.States, и превьюшки (amaz_nike_en_na-gts2mini_animated.gif, amaz_nike_en_na-gts2mini_static.png, amaz_nike_en_na-gts2mini_static_242.png). 

5. Изменяем картинки как нам нужно. Масштабируем под нужный размер или перерисовываем. 
Для автоматического масштабирования изображений можно воспользоваться моей программой, написанной специально для этих целей.
a) Скачиваем resizer в рабочую папку c:\bip3:
https://github.com/Tnxec2/amazfit-gts2mini-bip-resizer/raw/master/exe/resize.exe
б) у программы много параметров для настройки конвертации изображений, их можно посмотреть запустив программу с параметром -h

[CODE]
usage: resize.exe [-h] [-n] [-i] [-r] [-b BACKGROUNDCOLOR BACKGROUNDCOLOR BACKGROUNDCOLOR] [-x SCALEX] [-y SCALEY]
                  [-o OUTPUTDIR]
                  path [path ...]

positional arguments:
  path                  path to image or directory for scale

options:
  -h, --help            show this help message and exit
  -n, --noscale         no scale images
  -i, --invert          invert color of images
  -r, --removealpha     remove alpha channel of images
  -na, --noantialiased  not antialiased scale
  -b BACKGROUNDCOLOR BACKGROUNDCOLOR BACKGROUNDCOLOR, --backgroundcolor BACKGROUNDCOLOR BACKGROUNDCOLOR BACKGROUNDCOLOR
                        background color for replace alpha channel, format: R G B, example: -b 255 255 0)
  -x SCALEX, --scalex SCALEX
                        scale factor horizontaly, examle 0.5
  -y SCALEY, --scaley SCALEY
                        scale factor verticaly, example 0.5
  -o OUTPUTDIR, --outputdir OUTPUTDIR
                        output directory name, default = resized
[/CODE]

c) нам нужно вычислить фактор масштабирования по обеим осям X и y
у gts2mini размер часов 306х354
у bipU - 302х320
у bip3 240х280

исходя из этих данных вычисляем scale фактор:
scalex = 240 / 306 = 0.78
scaley = 280 / 354 = 0.79

в) мы просто хотим уменьшить наши картинки, поэтому задаем только фактор масштабирования:
resize.exe amaz_nike_en_na-gts2mini\ -x 0.78 -y 0.79 -o bip3

тут важно правильно указать путь к исходным картинкам: путь должен быть впереди параметров, и оканчиваться слэшем "\".

г) программа создает новую папку ("bip3") с измененными картинками. Тамже создается новый json файл с перерасчитанными координатами. Json файл можно переименовать например в amaz_nike_en_na-bip3.json

6. Проверяем и если нужно корректируем циферблат в онлайн редакторе
https://tnxec2.github.io/amazfit-gts2mini-watchface-react/

краткие инструкции можно найти здесь:
https://4pda.to/forum/index.php?showtopic=1022247&view=findpost&p=122262855

7. Запаковываем готовый циферблат назад в Bin:
cmd
cd c:\bip3
main.exe --bip3 --file amaz_nike_en_na-gts2mini\bip3\amaz_nike_en_na-bip3.json

в папке "amaz_nike_en_na\bip3" парсер создал новый BIN файл "amaz_nike_en_na-bip3_packed.bin", лог файл, и новые превьюшки.

P.S. если json или bin файл не создается, то смотрим ошибки в консоли и лог файле. Ошибки обычно идут в конце лог файла.

