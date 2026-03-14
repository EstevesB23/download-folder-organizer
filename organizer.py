import os
import shutil

# caminho da pasta Downloads
path = r"C:\Users\Brenda Esteves\Downloads"


def organize_files():

    # cria as pastas se não existirem
    os.makedirs(os.path.join(path, "pdf"), exist_ok=True)
    os.makedirs(os.path.join(path, "imagens"), exist_ok=True)
    os.makedirs(os.path.join(path, "excel"), exist_ok=True)
    os.makedirs(os.path.join(path, "outros"), exist_ok=True)

    files = os.listdir(path)

    for file in files:

        source = os.path.join(path, file)

        # ignora pastas
        if os.path.isdir(source):
            continue

        file_lower = file.lower()

        if file_lower.endswith(".pdf"):
            destination = os.path.join(path, "pdf", file)

        elif file_lower.endswith(".png"):
            destination = os.path.join(path, "imagens", file)

        elif file_lower.endswith(".xlsx"):
            destination = os.path.join(path, "excel", file)

        else:
            destination = os.path.join(path, "outros", file)

        # evita erro se o arquivo já existir
        if not os.path.exists(destination):
            shutil.move(source, destination)


if __name__ == "__main__":
    organize_files()