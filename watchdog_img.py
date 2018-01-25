import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import angle_detection3


class CreatedEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        file_name = event.src_path
        print("create")
        print(file_name)
        # angle_detection3.detect_img(file_name)
        angle_detection3.detect_img("%s" % file_name)

    def on_modified(self, event):
        file_name = event.src_path
        print("modified")
        print(file_name)
        # angle_detection3.detect_img("%s" % file_name)
        # angle_detection3.detect_img("images/test_1.bmp")
        # time.sleep(1)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = "G:/Code/angle_detection/images/"
    event_handler = CreatedEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
