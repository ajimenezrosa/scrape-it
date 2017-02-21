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
    '''
    :param data_string: accepts a string representing the table data
    :return: string after removing tags and processing it
    '''
    string_to_return = ''
    # Generates a list of data of all row
    rows = data_string.split("<tr>")
    rows.pop(0)  # Removes first <table> tag

    # Reads reach row of information from the rows List
    for row in rows:
        row_string = ''

        for data in row:  # Creates a full string for a row item
            row_string += data

        # Creates a list with only required information
        row_data = re.findall(r'<td>(.*?)</td>', row_string)

        row_string = ''
        # Creates a string with data to be written to the file
        for data in row_data:
            row_string += '"' + data + '"' + ", "

        # Removes the ',' at the end of the string and adds newline character
        string_to_return += row_string[:-2] + "\n"

    return string_to_return


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