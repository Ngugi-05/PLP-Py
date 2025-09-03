def main():
    filename = input("Enter the file name: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()

            modified_content = content.lower()

            new_filename = "modified_" + filename
            with open(new_filename, 'w') as new_file:
                new_file.write(modified_content)
            print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("File not found, Please check the filename.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
