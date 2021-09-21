def str_and_bytes_convertor(chardata, operation = "byte_to_str", u_encoding = "utf-8"):
    result = chardata
    if(operation == "byte_to_str"):
        if isinstance(chardata, bytes):
            result = chardata.decode(u_encoding)
    elif(operation == "str_to_byte"):
        if isinstance(chardata, str):
            result = chardata.encode(u_encoding) 
    return result

byte = b'h\x65llo'
string = 'a\u0300 propos'
out_string = str_and_bytes_convertor(byte)
out_byte = str_and_bytes_convertor(string, 'str_to_byte')
print(type(string))
print(type(out_byte))