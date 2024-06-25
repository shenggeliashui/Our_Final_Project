import subprocess
import os

def run_app(path, port):
    return subprocess.Popen(['python', path], env={**os.environ, 'FLASK_RUN_PORT': str(port)})

if __name__ == '__main__':
    apps = [
        ('calendar_and_dictation/api.py', 5000),
        ('recite/app.py', 5001),
        ('information/controller.py', 5002),
    ]

    processes = [run_app(app[0], app[1]) for app in apps]

    try:
        for process in processes:
            process.wait()
    except KeyboardInterrupt:
        for process in processes:
            process.terminate()

