def fetch_data():
     '''
    Retrieves data from the given url.
    Returns a string representing the whole table data
    '''
    data_string = ''
    try:
        url_1 = "https://cdn.rawgit.com/younginnovations/"
        url_2 = "internship-challenges/master/data-analysis/scrape-it/exampledata.html"
        url = url_1 + url_2
        with urllib.request.urlopen(url) as url_link:
            for line in url_link:
                data_string += line.decode('utf-8')

    except urllib.request.URLError as e:
        print("ERROR Connecting to Web page", e)

    finally:
        return data_string


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