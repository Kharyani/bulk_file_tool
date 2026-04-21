import os
import shutil
import datetime
import csv

LOG_FILE = "file_operations_log.csv"

# ------------------ Utility Functions ------------------

def get_files(folder):
    try:
        return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    except Exception as e:
        print(f"Error: {e}")
        return []

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def log_operation(old_name, new_name):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Old Name", "New Name", "Timestamp"])
        writer.writerow([old_name, new_name, datetime.datetime.now()])

# ------------------ Rename Functions ------------------

def rename_files(folder, prefix="", suffix="", replace_from="", replace_to="", auto_number=False):
    files = get_files(folder)
    preview = []

    for i, file in enumerate(files, start=1):
        name, ext = os.path.splitext(file)
        new_name = name

        if replace_from:
            new_name = new_name.replace(replace_from, replace_to)

        if prefix:
            new_name = prefix + new_name

        if suffix:
            new_name = new_name + suffix

        if auto_number:
            new_name = f"{new_name}_{i}"

        new_name += ext
        preview.append((file, new_name))

    return preview

def apply_rename(folder, preview_list):
    for old, new in preview_list:
        old_path = os.path.join(folder, old)
        new_path = os.path.join(folder, new)

        if os.path.exists(new_path):
            print(f"Skipping (already exists): {new}")
            continue

        try:
            os.rename(old_path, new_path)
            log_operation(old, new)
        except Exception as e:
            print(f"Error renaming {old}: {e}")

# ------------------ Organize Functions ------------------

def organize_by_type(folder):
    files = get_files(folder)

    for file in files:
        ext = file.split('.')[-1].lower()
        target_folder = os.path.join(folder, ext.upper() + "_Files")
        create_folder(target_folder)

        src = os.path.join(folder, file)
        dest = os.path.join(target_folder, file)

        if not os.path.exists(dest):
            shutil.move(src, dest)
            log_operation(file, dest)

def organize_by_date(folder):
    files = get_files(folder)

    for file in files:
        path = os.path.join(folder, file)
        timestamp = os.path.getmtime(path)
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

        target_folder = os.path.join(folder, date)
        create_folder(target_folder)

        dest = os.path.join(target_folder, file)

        if not os.path.exists(dest):
            shutil.move(path, dest)
            log_operation(file, dest)

# ------------------ Menu System ------------------

def menu():
    folder = ""

    while True:
        print("\n===== BULK FILE RENAMER & ORGANIZER =====")
        print("1. Select Folder")
        print("2. Rename Files")
        print("3. Organize by File Type")
        print("4. Organize by Date")
        print("5. View Logs")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            folder = input("Enter folder path: ")
            if os.path.isdir(folder):
                print("Folder selected successfully!")
            else:
                print("Invalid folder path!")
                folder = ""

        elif choice == '2':
            if not folder:
                print("Select folder first!")
                continue

            prefix = input("Prefix (optional): ")
            suffix = input("Suffix (optional): ")
            replace_from = input("Replace this word (optional): ")
            replace_to = input("Replace with (optional): ")
            auto_number = input("Auto number? (y/n): ").lower() == 'y'

            preview = rename_files(folder, prefix, suffix, replace_from, replace_to, auto_number)

            print("\nPreview Changes:")
            for old, new in preview:
                print(f"{old} --> {new}")

            confirm = input("Apply changes? (y/n): ").lower()
            if confirm == 'y':
                apply_rename(folder, preview)
                print("Renaming completed!")

        elif choice == '3':
            if folder:
                organize_by_type(folder)
                print("Files organized by type!")
            else:
                print("Select folder first!")

        elif choice == '4':
            if folder:
                organize_by_date(folder)
                print("Files organized by date!")
            else:
                print("Select folder first!")

        elif choice == '5':
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, 'r') as file:
                    print(file.read())
            else:
                print("No logs found!")

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")

# ------------------ Run Program ------------------

if __name__ == "__main__":
    menu()