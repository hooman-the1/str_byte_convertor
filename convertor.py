def str_and_bytes_convertor(chardata, operation = "byte_to_str", u_encoding = "utf-8"):
    '''
    this function check and converts string and bytes data type to each other
    also can accept encoding as argument 
    '''
    result = chardata
    if(operation == "byte_to_str"):
        if isinstance(chardata, bytes):
            result = chardata.decode(u_encoding)
    elif(operation == "str_to_byte"):
        if isinstance(chardata, str):
            result = chardata.encode(u_encoding) 
    return result

