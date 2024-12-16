import subprocess

# URL del repositorio de GitHub
repo_url = "https://huggingface.co/coqui/XTTS-v2"

# Ejecutar el comando git clone
subprocess.run(["git", "clone", repo_url], check=True)

print(f"Repositorio clonado desde {repo_url}")
