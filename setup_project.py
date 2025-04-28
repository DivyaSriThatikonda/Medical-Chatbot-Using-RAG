import os

# Define project directory
PROJECT_DIR = r"C:\Users\hp\PycharmProjects\Medical Chatbot"

# Define directories and files
DIRECTORIES = [
    "data",
    "src",
    "src/components"
]
FILES = [
    "src/__init__.py",
    "src/components/__init__.py",
    ".env",
    "requirements.txt",
    ".gitignore",
    "README.md",
    "src/components/data_ingestion.py",
    "src/components/embedding.py",
    "src/components/model_api.py",
    "app.py"
]


def create_project_structure():
    # Create project directory
    os.makedirs(PROJECT_DIR, exist_ok=True)

    # Create directories
    for directory in DIRECTORIES:
        os.makedirs(os.path.join(PROJECT_DIR, directory), exist_ok=True)

    # Create empty files
    for file_path in FILES:
        full_path = os.path.join(PROJECT_DIR, file_path)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write("")

    print(f"Project structure created at {PROJECT_DIR}")


if __name__ == "__main__":
    if os.path.exists(PROJECT_DIR) and any(os.listdir(PROJECT_DIR)):
        print(f"Directory {PROJECT_DIR} already exists with files. Delete it or choose a new directory.")
    else:
        create_project_structure()
