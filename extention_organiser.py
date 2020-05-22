from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog
import time
import os
import json


class MyOrganiser(FileSystemEventHandler):
    i = 1
    # Handle Dupicate Names and move files with respective folders

    def duplicate_name_handle(self, src, file_name, destination):
        new_destination = destination + "/" + file_name
        file_extension = "."+file_name.split(".")[-1]
        try:
            try:
                os.rename(src, new_destination)
            except(FileNotFoundError):
                try:
                    os.mkdir(destination)
                    os.rename(src, new_destination)
                except(FileExistsError):
                    c = 1
                    while(True):
                        try:
                            if(file_name.count("(") > 0):
                                file_name = file_name.split("(")[0]
                            else:
                                file_name = "".join(file_name.split(".")[:-1])
                            file_name = file_name+"("+str(c)+")"+file_extension
                            new_destination = destination + "/" + file_name
                            os.rename(src, new_destination)
                            break
                        except:
                            c += 1
            except(FileExistsError):

                c = 1
                while(True):
                    try:
                        if(file_name.count("(") > 0):
                            file_name = file_name.split("(")[0]
                        else:
                            file_name = "".join(file_name.split(".")[:-1])
                        new_destination = destination + "/" + file_name
                        os.rename(src, new_destination)
                        break
                    except:
                        c += 1
        except:
            print(file_name)

    # Uses File Extension to categorize files
    def on_modified(self, event):
        print("deteced")
        for filename in os.listdir(folder_to_track):
            # src = folder_to_track + "/" + filename
            if filename != 'desktop.ini':  # to prevent error in the script
                if filename.lower().endswith(('.png', '.jpg', '.tiff', '.gif', '.bmp', '.ppm', '.pgm', '.pbm', '.pnm', '.jpeg', '.heif', '.bpg', '.img', '.ico')):
                    # new_destination = pictures_destination + "/" + filename
                    os.rename(folder_to_track, filename, pictures_destination)

                elif filename.lower().endswith(('.doc', '.txt', '.pdf', '.xls', '.docx', '.html', '.htm', '.odt', '.xlsx', '.ppt', '.pptx')):
                    new_destination = documents_destination + "/" + filename
                    os.rename(src, documents_destination, new_destination)

                elif filename.lower().endswith(('.mp4', '.mkv', '.webm', '.flv', '.vob', ',ogv', '.ogg', '.drc', '.gifv', '.mng', '.wmv', '.mov', '.qt', '.avi', '.yuv', '.rm', '.asf', '.amv', '.m4v', '.m4p', '.3gp')):
                    new_destination = videos_destination + "/" + filename
                    os.rename(src, videos_destination, new_destination)

                elif filename.lower().endswith(('.mp3', '.raw')):
                    new_destination = audios_destination + "/" + filename
                    os.rename(src, audios_destination, new_destination)

                elif filename.lower().endswith(('.7z', '.zip', '.rar')):
                    new_destination = zips_destination + "/" + filename
                    os.rename(src, zips_destination, new_destination)
                else:
                    new_destination = others_destination + "/" + filename
                    os.rename(src, others_destination, new_destination)

            """ 
                To add more places to move the file use the code commented out below
                 if filename.lower().endswith(('.file_extension')):
                    new_destination = new_destination_path + "/" + filename
                    os.rename(src,new_destination)
                """


# Enter Path where you want the script to filter through
folder_to_track = 'D:/Downloads'
# change the destination where you would like to move files to
pictures_destination = 'D:/Pictures'
documents_destination = 'D:/Documents'
videos_destination = 'D:/Videos'
audios_destination = 'D:/Music'
zips_destination = 'D:/Documents/Zips'
others_destination = 'D:/Documents/Others'

event_handler = MyOrganiser()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
