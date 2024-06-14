import subprocess

def iniciar_servidor_django():
    try:
        subprocess.run(["python3", "Server Django-20240612T061328Z-001/Server Django/mysite/manage.py", "runserver", "8082"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error al iniciar el servidor Django:", e)