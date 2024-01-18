
<h3 id="exercise-01-screwdriver-song">Exercise 01: Screwdriver Song</h3>

 Enclosed is a simple WSGI+HTTP client-server application for managing sound files.

To launch it, do as follows:
- Go to sound_app folder and start the server with a command: python3 server.py
- open a web browser and enter 127.0.0.1:8888 in the address line
- use the "Choose File" button to pick the required file from your computer
- use the "Upload" button to upload the selected file to the server

To see how the command-line application screwdriver.py works you can try two possible actions:

- `python screwdriver.py upload ./soundSource/metalthrash.ogg` - this will upload your local audio file  to the server
- `python screwdriver.py list` this will  retrieve and print out the names of all the files currently  present on the server.
