from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog 

import time
from time import gmtime, strftime
import os
import json
from datetime import datetime

# Handle Dupicate Names and move files with respective folders
def duplicate_name_handle(src, file_name, destination):
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

class MyOrganiser(FileSystemEventHandler):
    i = 1

    # Uses File Extension to categorize files
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'Folder-Name':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    duplicate_name_handle(src,filename ,folder_destination_path)


# Enter Path where you want the script to filter through
folder_to_track = 'D:/Downloads'
# change the destination where you would like to move files to
extensions_folders = {
#No name
    'noname' : "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Uncategorized",
#Audio
    '.aif' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
    '.cda' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
    '.mid' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
    '.midi' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
    '.mp3' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
    '.mpa' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
    '.ogg' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
    '.wav' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
    '.wma' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
    '.wpl' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
    '.m3u' : "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Audio",
#Text
    '.txt' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/TextFiles",
    '.doc' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Document/Microsoft",
    '.docx' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Document/Microsoft",
    '.odt ' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Document",
    '.pdf': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Document/PDF",
    '.rtf': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Document",
    '.tex': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/TextFiles",
    '.wks ': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/TextFiles",
    '.wps': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Document",
    '.wpd': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Document",
#Video
    '.3g2': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.3gp': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.avi': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.flv': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.h264': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.m4v': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.mkv': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.mov': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.mp4': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.mpg': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.mpeg': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.rm': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.swf': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.vob': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
    '.wmv': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Video",
#Images
    '.ai': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.bmp': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.gif': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.ico': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.jpg': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.jpeg': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.png': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.ps': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.psd': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.svg': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.tif': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.tiff': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
    '.CR2': "%path-to-the-Folder-in-desktop%/Folder-Name/Media/Images",
#Internet
    '.asp': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
    '.aspx': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
    '.cer': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
    '.cfm': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
    '.cgi': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
    '.pl': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
    '.jsp': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
    '.part': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
    '.php': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
    '.rss': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
    '.xhtml': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Internet",
#Compressed
    '.7z': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Compressed",
    '.arj': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Compressed",
    '.deb': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Compressed",
    '.pkg': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Compressed",
    '.rar': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Compressed",
    '.rpm': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Compressed",
    '.tar.gz': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Compressed",
    '.z': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Compressed",
    '.zip': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Compressed",
#Disc
    '.bin': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Disc",
    '.dmg': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Disc",
    '.iso': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Disc",
    '.toast': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Disc",
    '.vcd': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Disc",
#Data
    '.csv': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database",
    '.dat': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database",
    '.db': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database",
    '.dbf': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database",
    '.log': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database",
    '.mdb': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database", 
    '.sav': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database",
    '.sql': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database",
    '.tar': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database",
    '.xml': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database",
    '.json': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Database",
#Executables
    '.apk': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Executables",
    '.bat': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Executables",
    '.com': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Executables",
    '.exe': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Executables",
    '.gadget': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Executables",
    '.jar': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Executables",
    '.wsf': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Executables",
#Fonts
    '.fnt': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Fonts",
    '.fon': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Fonts",
    '.otf': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Fonts",
    '.ttf': "%path-to-the-Folder-in-desktop%/Folder-Name/Other/Fonts",
#Presentations
    '.key': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Presentation",
    '.odp': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Presentation",
    '.pps': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Presentation/Microsoft",
    '.pptx': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Presentation/Microsoft",
    '.ppt': "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Presentation/Microsoft",
#Programming
    '.c': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/CnC++",
    '.cpp': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/CnC++",
    '.class': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Java",
    '.dart': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Dart",
    '.py': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Python",
    '.sh': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Shell",
    '.swift': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/Swift",
    '.html': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/HTML",
    '.h': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/CnC++",
    '.css': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/CSS",
    '.htm': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/HTML",
    '.js': "%path-to-the-Folder-in-desktop%/Folder-Name/Programming/JavaScript",
#Spreadsheets
    '.ods' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Spreadsheet",
    '.xlr' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Spreadsheet/Microsoft",
    '.xls' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Spreadsheet/Microsoft",
    '.xlsx' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Spreadsheet/Microsoft",
#System
    '.bak' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.cab' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.cfg' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.cpl' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.cur' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.dll' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.dmp' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.drv' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.icns' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.ico' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.ini' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.lnk' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.msi' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.sys' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
    '.tmp' : "%path-to-the-Folder-in-desktop%/Folder-Name/Text/Other/System",
}


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
