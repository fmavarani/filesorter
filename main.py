import os
import shutil
import datetime
import sys
import glob
from multiprocessing import Pool
from PIL import Image
office_documents = (".doc", ".docx", ".docm", ".dot", ".dotx", ".dotm", ".xls", ".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".xltm", ".ppt", ".pptx", ".pptm", ".pot", ".potx", ".potm", ".ppa", ".ppam", ".pps", ".ppsx", ".ppsm", ".sldx", ".sldm", ".accdb", ".accdt", ".accdr", ".pub", 'pdf')
images=('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')       

def sort_files_by_extension_and_date(dir_path):
    # create directories for each file extension
    sortedPath=os.path.join(dir_path, "Sorted")
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # get file extension
            file_extension = os.path.splitext(file)[1][1:].lower()
            if file.lower().endswith(images):
                file_extension="Pictures"
            if file.lower().endswith(office_documents):
                file_extension="Office Documents"
            # get year the file was created
            file_path = os.path.join(root, file)
            creation_time = os.path.getmtime(file_path)
            year = datetime.datetime.fromtimestamp(creation_time).strftime('%Y')

            
            # create directory for file extension if it doesn't exist
            extension_dir = os.path.join(sortedPath, file_extension)
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            # create directory for year if it doesn't exist
            year_dir = os.path.join(extension_dir, year)
            if not os.path.exists(year_dir):
                os.makedirs(year_dir)

            # move file to extension directory
            source_path = os.path.join(root, file)
            print(source_path)
            # move file to year directory
            destination_path = os.path.join(year_dir, file)
            shutil.move(source_path, destination_path)

def sort_pics_by_extension_and_date(files,dir_path):
    # create directories for each file extension
    sortedPath=dir_path
    for file in files:
        if file.lower().endswith(images):
            # get file extension
            file_extension="Verified pictures"
        
            # get year the file was created
            file_path = file
            creation_time = os.path.getmtime(file_path)
            year = datetime.datetime.fromtimestamp(creation_time).strftime('%Y')

            
            # create directory for file extension if it doesn't exist
            extension_dir = os.path.join(sortedPath, file_extension)
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            # create directory for year if it doesn't exist
            year_dir = os.path.join(extension_dir, year)
            if not os.path.exists(year_dir):
                os.makedirs(year_dir)

            # move file to extension directory
            source_path = file
            print(source_path)
            # move file to year directory
            destination_path = os.path.join(year_dir, os.path.basename(file))
            shutil.move(source_path, destination_path)
                
def sort_documents_by_extension_and_date(dir_path):
    # create directories for each file extension
    sortedPath=dir_path
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.lower().endswith(office_documents):
                # get file extension
                file_extension="Office Documents"
            
                # get year the file was created
                file_path = os.path.join(root, file)
                creation_time = os.path.getmtime(file_path)
                year = datetime.datetime.fromtimestamp(creation_time).strftime('%Y')

                
                # create directory for file extension if it doesn't exist
                extension_dir = os.path.join(sortedPath, file_extension)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                # create directory for year if it doesn't exist
                year_dir = os.path.join(extension_dir, year)
                if not os.path.exists(year_dir):
                    os.makedirs(year_dir)

                # move file to extension directory
                source_path = os.path.join(root, file)
                print(source_path)
                # move file to year directory
                destination_path = os.path.join(year_dir, file)
                shutil.move(source_path, destination_path)
                
def delete_empty_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            folder_path = os.path.join(root, name)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                print(f"Deleted empty folder: {folder_path}")
                
def list_of_file_extention(dir_path):
    # create directories for each file extension
    my_list = []  # create an empty list
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # get file extension
            file_extension = os.path.splitext(file)[1][1:].lower()
            my_list.append(file_extension)
    print(list(set(my_list)))
      
def CheckOne(f):
    try:
        im = Image.open(f)
        im.verify()
        im.close()
        return f
    except (IOError, OSError, Image.DecompressionBombError):
        return
    
def verifiedFiles(path):
     # Create a pool of processes to check files
    p = Pool()
    f=[]
    # Create a list of files to process
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if(CheckOne(os.path.join(root, file))):
                f.append(os.path.join(root, file))
    # Map the list of files to check onto the Pool
    return f
                    
if __name__ == '__main__':
    if len(sys.argv)>=3:
        dir_path = sys.argv[2]
        command = sys.argv[1]
        if command.lower() == "document":
            sort_documents_by_extension_and_date(dir_path)
            delete_empty_folders(dir_path)
        elif command.lower() == "all":
            sort_files_by_extension_and_date(dir_path)
            delete_empty_folders(dir_path)
        elif command.lower() == "pics":
            sort_pics_by_extension_and_date(verifiedFiles(dir_path),dir_path)
            delete_empty_folders(dir_path)
        elif command.lower() == "veripix":
            print(verifiedFiles(dir_path))
    else:    
        print("Please input proper command argument")
            
