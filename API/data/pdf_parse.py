from tika import parser
raw = parser.from_file('/Users/jacob.scheuer/Downloads/carClasses.pdf')
data = raw['content']

current_year = ' 2020'
disclaimer_length = 4
dumb_names = ["Alfa Romeo", "Aston Martin", "General Motors", "Tesla Motors"]

split_data = data.split('\n')

data_non_blank_rows = [non_blank_rows for non_blank_rows in split_data if non_blank_rows != '']
data_no_headers = [non_header_rows for non_header_rows in data_non_blank_rows if not current_year in non_header_rows]
data_no_footers = [non_footer for non_footer in data_no_headers if not "Page" in non_footer]
cleanish_data = data_no_footers[:-4]

def splitter(data_row):
    for dumb_name in dumb_names:
        data_row = data_row.replace(dumb_name, dumb_name.replace(" ","_"))
    return data_row

clean_data = [splitter(data_row) for data_row in cleanish_data]
