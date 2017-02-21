def fetch_data():
    pass

def process_data(data_string):
    pass

def write_data(data_string):
    pass


def main():
    # Checks if the directory already exists. If not, it creates the new directory
    if not os.path.exists('out'):
        os.mkdir('out')

    data_string = fetch_data()
    if data_string:
        write_string = process_data(data_string)
        write_data(process_data(write_string))
        print("Successful")
    else:
        print("No data found")


if __name__ == '__main__':
    main()