while i < len(line):
    char = line[i]
    
    if not in_quotes:
        if char == ',':
            fields.append(current_field)
            current_field = ""
        elif char == '"':
            in_quotes = True
        else:
            current_field += char
    else:
        if char == '"' and i + 1 < len(line) and line[i+1] == '"':
            current_field += '"'
            i += 2
            continue
        elif char == '"':
            in_quotes = False
        else:
            current_field += char
    
    i += 1
    
fields.append(current_field)
return fields
