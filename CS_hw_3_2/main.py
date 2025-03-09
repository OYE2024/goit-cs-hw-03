from pymongo import MongoClient
from pymongo.errors import PyMongoError, ConnectionFailure


# Підключення до MongoDB
try:
    client = MongoClient("mongodb://root:example@localhost:27017/")
    db = client["my_MongoDB"]
    collection = db["animals"]
    # Перевірка з'єднання
    client.admin.command('ismaster')
    print("MongoDB was connected")
except ConnectionFailure:
    print("Can't connect to MongoDB, check your connection")


def create_record():
    try:
        name = input("Enter the name of animal: ")
        age = input("Enter age of animal: ")
        features_input = input("Enter features of animal, virgule separated: ")
        features = features_input.split(",")
        record = {"name": name, "age": age, "features": features}
        collection.insert_one(record)
        print("Record created")
    except PyMongoError as e:
        print(f'MongoDB error: {e}')
    except ValueError as e:
        print(f'Input error: {e}')


def read_all_records():
    try:
        for record in collection.find():
            print(record)
    except PyMongoError as e:
        print(f'MongoDB error: {e}')


def read_record_by_name():
    try:
        name = input("Enter the name of the animal you want to search for: ")
        record = collection.find_one({"name": name})
        if record:
            print(record)
        else:
            print("Record not found.")
    except PyMongoError as e:
        print(f'MongoDB error: {e}')


def update_record_age():
    try:
        name = input("Enter the name of the animal to update age: ")
        new_age = input("Enter the new age: ")
        result = collection.update_one(
            {"name": name},
            {"$set": {"age": new_age}}
        )
        if result.matched_count > 0:
            print("Record updated")
        else:
            print("Record not found")
    except PyMongoError as e:
        print(f'MongoDB error: {e}')


def add_feature_to_record():
    try:
        name = input("Enter the name of the animal to add feature: ")
        new_feature = input("Enter the feature to add: ")
        result = collection.update_one(
            {"name": name},
            {"$addToSet": {"features": new_feature}}
        )
        if result.matched_count > 0:
            print("Feature added")
        else:
            print("Record not found")
    except PyMongoError as e:
        print(f'MongoDB error: {e}')


def delete_record():
    try:
        name = input("Enter the name of the animal to delete: ")
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print("Record deleted")
        else:
            print("Record not found")
    except PyMongoError as e:
        print(f'MongoDB error: {e}')


def delete_all_records():
    try:
        result = collection.delete_many({})
        print(f"{result.deleted_count} records deleted")
    except PyMongoError as e:
        print(f'MongoDB error: {e}')


def main():
    while True:
        print("\nДоступні дії:")
        print("1 - Створити запис про тварину")
        print("2 - Показати всі записи")
        print("3 - Показати запис про тварину")
        print("4 - Оновити вік тварини")
        print("5 - Додати особливість до тварини")
        print("6 - Видалити запис про тварину")
        print("7 - Видалити всі записи")
        print("8 - Вийти")
        choice = input("Виберіть дію:")

        if choice == "1":
            create_record()
        elif choice == "2":
            read_all_records()
        elif choice == "3":
            read_record_by_name()
        elif choice == "4":
            update_record_age()
        elif choice == "5":
            add_feature_to_record()
        elif choice == "6":
            delete_record()
        elif choice == "7":
            delete_all_records()
        elif choice == "8":
            break
        else:
            print("Wrong choice. Try again.")


if __name__ == "__main__":
    main()
