import csv
import os

# File to store the book records
DATA_FILE = "books.txt"

# ===================== CORE FUNCTIONS =====================")
print("✅ Book added successfully.")

def search_book_by_title(title):
    found = False
    with open(DATA_FILE, 'r') as f:
        for line in f:
            book = line.strip().split(',')
            if book[0].lower() == title.lower():
                print("📚 Book Found:", book)
                found = True
    if not found:
        print("❌ No book found with that title.")

def search_book_by_isbn(isbn):
    found = False
    with open(DATA_FILE, 'r') as f:
        for line in f:
            book = line.strip().split(',')
            if book[2] == isbn:
                print("📚 Book Found:", book)
                found = True
    if not found:
        print("❌ No book found with that ISBN.")

def delete_book(isbn):
    found = False
    lines = []
    with open(DATA_FILE, 'r') as f:
        lines = f.readlines()
    with open(DATA_FILE, 'w') as f:
        for line in lines:
            book = line.strip().split(',')
            if book[2] != isbn:
                f.write(line)
            else:
                found = True
    if found:
        print("🗑️ Book deleted successfully.")
    else:
        print("❌ Book not found.")

def generate_report():
    print("\n📋 Available Books Report:")
    with open(DATA_FILE, 'r') as f:
        count = 0
        for line in f:
            book = line.strip().split(',')
            if book[4].lower() == "available":
                print(book)
                count += 1
        if count == 0:
            print("No available books found.")

# ===================== BULK OPERATIONS =====================

def bulk_upload(source_csv, target_file=DATA_FILE):
    try:
        with open(source_csv, 'r') as src:
            reader = csv.reader(src)
            with open(target_file, 'a') as tgt:
                for row in reader:
                    tgt.write(','.join(row) + '\n')
        print("📥 Bulk upload completed.")
    except Exception as e:
        print("❌ Error during bulk upload:", e)

def bulk_download(source_file=DATA_FILE, ex)

def add_book(title, author, isbn, price, status):
    with open(DATA_FILE, 'a') as f:
        f.write(f"{title},{author},{isbn},{price},{status}\nport_file="books_export.csv"):
    try:
        with open(source_file, 'r') as src:
            data = src.readlines()
        with open(export_file, 'w') as tgt:
            tgt.writelines(data)
        print(f"📤 Data exported to {export_file}.")
    except Exception as e:
        print("❌ Error during bulk download:", e)

# ===================== MENU =====================

def menu():
    while True:
        print("\n📚 Book Inventory Manager")
        print("1. Add Book")
        print("2. Search Book by Title")
        print("3. Search Book by ISBN")
        print("4. Delete Book")
        print("5. Generate Report (Available Books)")
        print("6. Bulk Upload from CSV")
        print("7. Bulk Download to CSV")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            price = input("Enter price: ")
            status = input("Enter status (Available/Unavailable): ")
            add_book(title, author, isbn, price, status)

        elif choice == '2':
            title = input("Enter title to search: ")
            search_book_by_title(title)

        elif choice == '3':
            isbn = input("Enter ISBN to search: ")
            search_book_by_isbn(isbn)

        elif choice == '4':
            isbn = input("Enter ISBN to delete: ")
            delete_book(isbn)

        elif choice == '5':
            generate_report()

        elif choice == '6':
            filename = input("Enter CSV filename to upload: ")
            bulk_upload(filename)

        elif choice == '7':
            filename = input("Enter filename to export to (e.g., export.csv): ")
            bulk_download(export_file=filename)

        elif choice == '8':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select from 1 to 8.")

# Run the menu
if __name__ == "__main__":
    # Ensure data file exists
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, 'w').close()
    menu()
