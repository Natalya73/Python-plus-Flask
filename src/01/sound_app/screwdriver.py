import sys
import requests
import os
import mimetypes

BASE_URL = 'http://localhost:8888'


def is_sound_file(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith('audio/')

def upload_file(file_path):
    if not os.path.isfile(file_path):
        print('Invalid file path.')
        return

    if not is_sound_file(file_path):
        print('Non-sound file detected. Please choose a sound file.')
        return

    url = f'{BASE_URL}/upload'
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        print('SUCCESS!')
    else:
        print('An error occurred while uploading the file.')


def list_files():
    url = f'{BASE_URL}/list'
    response = requests.get(url)
    # print(response.content)  # for debugging
    if response.status_code == 200:
        files = response.json()
        if files:
            print('Uploaded Files:')
            for file in files:
                print(file)
        else:
            print('No files uploaded yet.')
    else:
        print('An error occurred while retrieving the file list.')


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'upload':
        upload_file(sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == 'list':
        list_files()
    else:
        print('Invalid command. Usage:')
        print('python screwdriver.py upload /path/to/file.mp3')
        print('python screwdriver.py list')

