#libraries
import json

# store json object in a variable
json_object = """
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
"""

# function to store JSON object keys into a list 
# function should return list of keys
def get_keys():
    json_array = json.loads(json_object)
    key = list(json_array.keys())
    return key

# function to store JSON object values into a list
# function should return list of values
def get_values():
    json_array = json.loads(json_object)
    value = list(json_array.values())
    return value

# function to generate regression title from JSON object keys
# function should call function to store JSON object keys into a list twice 
# on the second call, the function should add an underscore to the end of each key
# function should return the regression title
def get_regression_title():
    key = get_keys()
    key_headings = ""
    value_headings = ""
    for items in key:
        key_headings += "| " + str(items) + " "
    for items in key:
        value_headings += "| " + str(items + "_") + " "
    headings = key_headings + value_headings + "|"
    return headings

# function to generate regular values and return a list
def null_use_case():
    value = get_values()
    # replace values with null
    null_values = []
    for items in value:
        null_values.append("null")
    return null_values

def symbols_use_case():
    value = get_values()
    # replace values with null
    null_values = []
    for items in value:
        null_values.append("$#@%")
    return null_values

def missing_value_use_case():
    values = get_values()
    keys = get_keys()

    for x in range(len(values)):
        formatted_row = []

        for item in keys:
            element = f'| "{item}": '
            formatted_row.append(element)

        for index, item in enumerate(values):
            if index == len(values) - 1 and index == x:
                value = f'|  |'
                formatted_row.append(value)
            elif index == len(values) - 1:
                value = f'| {item} |'
                formatted_row.append(value)
            else:
                if index == x:
                    value = f'|  , '
                    formatted_row.append(value)
                else:
                    value = f'| {item}, '
                    formatted_row.append(value)
        print(formatted_row)
        with open("regression_table.txt", "a") as f:
            for items in formatted_row:
                f.write(items)
            f.write("\n")

def missing_value_pairs_use_case():
    values = get_values()
    keys = get_keys()

    for x in range(len(values)):
        formatted_row = []

        for i, item in enumerate(keys):
            if i == x:
                element = f'|  '
                formatted_row.append(element)
            else:
                element = f'| "{item}": '
                formatted_row.append(element)

        for index, item in enumerate(values):
            if index == len(values) - 1 and index == x:
                value = f'|  |'
                formatted_row.append(value)
            elif index == len(values) - 1:
                value = f'| {item} |'
                formatted_row.append(value)
            else:
                if index == x:
                    value = f'|   '
                    formatted_row.append(value)
                else:
                    value = f'| {item}, '
                    formatted_row.append(value)
        print(formatted_row)
        with open("regression_table.txt", "a") as f:
            for items in formatted_row:
                f.write(items)
            f.write("\n")

    

# function to switch data types of values
def incorrect_data_type():
    value = get_values()
    # replace values with incorrect data type
    incorrect_values = []
    for items in value:
        if type(items) == int:
            incorrect_values.append("string")
        elif type(items) == bool:
            incorrect_values.append(str(123))
        else:
            incorrect_values.append(True)
    return incorrect_values

#Generate Table Rows
def generate_table_rows():
    index = 0
    use_cases = [incorrect_data_type(), null_use_case(), symbols_use_case()]
    # define formatted_keys_values as a 2D list
    formatted_keys_values = []

    raw_keys = get_keys()
    
    for function in use_cases:
        formatted_keys = []
        formatted_values = []

        for item in raw_keys:
            value = f'| "{item}": '
            formatted_keys.append(value)

        raw_values = list(function)

        for index, item in enumerate(raw_values):
            if index == len(raw_values) - 1:
                value = f'| {item} |'
                formatted_values.append(value)
            else:
                value = f'| {item}, '
                formatted_values.append(value)
        row = list(formatted_keys + formatted_values)
        formatted_keys_values.append(row)
        index += 1
    
    # print(formatted_keys_values)
    return formatted_keys_values

# function should use the keys from a call to place JSON keys into quotation marks and add a colon
# function should use the values from a call to place JSON values into quotation marks and add a comma
# function should return the regression table
def export_regression_table():
    headings = get_regression_title()
    table_rows = generate_table_rows()

    with open("regression_table.txt", "w") as file:
        file.write(headings)
        file.write("\n")

    with open("regression_table.txt", "a") as f:
        for rows in table_rows:
            for items in rows:
                f.write(items)
            f.write("\n")
                

#define main function
def main():
    export_regression_table()
    missing_value_use_case()
    missing_value_pairs_use_case()

if __name__ == "__main__":
    main()
