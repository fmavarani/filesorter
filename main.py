import os
import shutil
import datetime

def sort_files_by_extension_and_date(dir_path):
    # create directories for each file extension
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # get file extension
            file_extension = os.path.splitext(file)[1][1:].lower()
            
            # get year the file was created
            file_path = os.path.join(root, file)
            creation_time = os.path.getctime(file_path)
            year = datetime.datetime.fromtimestamp(creation_time).strftime('%Y')

            
            # create directory for file extension if it doesn't exist
            extension_dir = os.path.join(dir_path, file_extension)
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            # create directory for year if it doesn't exist
            year_dir = os.path.join(extension_dir, year)
            if not os.path.exists(year_dir):
                os.makedirs(year_dir)

            # move file to extension directory
            source_path = os.path.join(root, file)
            
             # move file to year directory
            destination_path = os.path.join(year_dir, file)
            shutil.move(source_path, destination_path)


if __name__ == '__main__':
    dir_path = '/path/to/directory'
    sort_files_by_extension_and_date(dir_path)