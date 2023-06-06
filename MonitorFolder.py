import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# src_path = 'C:\\Users\\Дом\\PycharmProjects\\pythonProject\\venv\\'

observer = Observer()


class HandlerFolder(FileSystemEventHandler): # Создаем свой класс - наследник класса FileSystemEventHandler
# переопределяем под себя три функции on_created, on_modified, on_deleted

    def on_created(self, event):
        print ('Нужно запустить скрипт python')
        #print(event.src_path, event.event_type)
        #self.checkFolderSize(event.src_path)

    def on_modified(self, event): pass
        #print(event.src_path, event.event_type)
        #self.checkFolderSize(event.src_path)

    def on_deleted(self, event):
        print('Удалили какой то файл')
        #print(event.src_path, event.event_type)



event_handler = HandlerFolder # - создаем экземпляр нашего обработчика и передаем его наблюдателю,
# в коде через строку ниже

observer.schedule(event_handler(), path='C:\\Users\\Дом\\PycharmProjects\\pythonProject\\venv', recursive=True)

#  observer.schedule - по смыслу планировщик для
# наблюдателя , передавая ему параметры (Handler(), path='/path/to/smth', recursive=True) - говорим - смотри за изменениями
# в папке, определяемой путем path='/path/to/smth', параметр recursive=True -говорит - наблюдай и за вложенными папками
# и если происходят изменения , то запускай вот этот обработчик Handler()
observer.start()  # запуск наблюдателя observer
print("Monitoring started")

try:
    while (True):
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()
    observer.join()




