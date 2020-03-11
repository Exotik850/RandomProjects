import os
import json
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            fileString = [i for i in filename]
            extension = fileString[-3:]
            folder_destination = "/Users/KidKo/Downloads/" + extension + "_folder"
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = "/Users/KidKo/Downloads/"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()