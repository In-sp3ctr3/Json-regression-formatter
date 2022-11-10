#python code to split JSON objects into individual words
import json

#Initialize global counter
counter = 0

#Set json text
json_object = """ {
            "title": "Production",
            "description": "sample description",
            "projectId": "$M{requestHelper.id}",
            "slug": "prod",
            "url": "https://url.com"
        }
        """

json_array = json.loads(json_object)

key = list(json_array.keys())
value = list(json_array.values())
pairs = list(json_array.items())

keys= []
values= []
incorrect_values = []
null_values = []
character_values = []

def sanitize_keys_value_pairs():
  for items in key:
    item = f'"{items}":'
    keys.append(item)

  for items in value:
    if type(items) == int:
      incorrect_values.append("string" + ",")
      null_values.append("null" + ",")
      character_values.append( "&^%^&%^" + ",")
      values.append(items)
    elif type(items) == bool:
      incorrect_values.append(str(123)+ " ,")
      null_values.append("null" + " ,")
      character_values.append( "&^%^&%^" + ",")
      values.append(items)
    else:
      item = f'"{items}",'
      incorrect_values.append(str(3423) + " ,")
      null_values.append("null" + " ,")
      character_values.append( "&^%^&%^" + ",")
        
      values.append(item)
  
  null = [i.replace('"', '') for i in null_values]
  characters = [i.replace('"', '') for i in character_values]

  h1 = keys + values
  h2 = keys + incorrect_values 
  h3 = keys + null
  h4 = keys + characters
  return h1, h2, h3, h4

def set_headings():
  key_headings = ""
  value_headings = ""
  for items in key:
    key_headings += "| " + str(items) + " "
  for items in key:
    value_headings += "| " + str(items + "_") + " "
  headings = key_headings + value_headings + "|"
  return headings
    
def set_no_missing_values(h1):
  no_missing_values = ""
  for items in h1:
    no_missing_values += f'| {items} '
  no_missing_values += "|"
  return no_missing_values

def set_incorrect_values(h2):
  incorrect_values = ""
  for items in h2:
    incorrect_values += f'| {items} '
  incorrect_values += "|"
  return incorrect_values

def set_null_values(h3):
  null_values = ""
  for items in h3:
    null_values += f'| {items} '
  null_values += "|"
  return null_values

def set_character_values(h4):
  character_values = ""
  for items in h4:
    character_values += f'| {items} '
  character_values += "|"
  return character_values

def set_single_missing_values(h1):
  single_missing_values = ""
  for x in range(len(h1)):
    for i in range(len(h1)):
      value = h1[i]
      if x == i and x < (len(h1)/2):
        value = " :"
      elif x == i and x >= (len(h1)/2):
        value = " ,"
      single_missing_values += "| " + str(value) + " "
    single_missing_values += "|\n"
  return single_missing_values

def set_missing_key_pair_values():
  missing_key_pair_values = ""
  counter = 0
  for i in range(len(pairs)):
    for items in pairs:
      if counter == i:
        missing_key_pair_values += "| " + " "+ " "
      else:
        missing_key_pair_values += f'| "{items[0]}": '
      counter = counter+1
    counter = 0
    for items in pairs:
      if counter == i:
        missing_key_pair_values += "| " + " "+ " "
      else:
        if type( items[1] ) == int:
          missing_key_pair_values += "| " + str(items[1]) + " "
        elif type( items[1] ) == bool:
          missing_key_pair_values += "| " + str( items[1] ) + " "
        else:
          missing_key_pair_values += f'| "{ items[1]}", '
      counter = counter + 1
    missing_key_pair_values += "|\n"
    counter = 0
  return missing_key_pair_values

def main():
  h1 = sanitize_keys_value_pairs()
  headings = set_headings()
  no_missing_values = set_no_missing_values(h1[0])
  incorrect_values = set_no_missing_values(h1[1])
  null_values = set_no_missing_values(h1[2])
  character_values = set_character_values(h1[3]) 
  single_missing_values = set_single_missing_values(h1[0])
  missing_key_pair_values = set_missing_key_pair_values()

  output = headings + "\n" + no_missing_values + "\n" + incorrect_values + "\n"+ character_values + "\n" + null_values + "\n" + single_missing_values + "\n" + missing_key_pair_values
  with open('JSONoutput.txt', 'w') as f:
    f.write(output)

if __name__ == "__main__":
    main()


  
