def Add_Location(my_dict,doc_name, file_type):
    if file_type in my_dict:
        my_dict[file_type].append(doc_name)
    else:
        my_dict[file_type] = [doc_name]

   
    return my_dict