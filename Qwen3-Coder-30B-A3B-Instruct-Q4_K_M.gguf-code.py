def parse_csv_line(line: str) -> list[str]:
    fields = []
    current_field = ""
    in_quotes = False
    
    i = 0
    while i < len(line):
        char = line[i]
        
        if char == '"':
            if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                # Escaped quote
                current_field += '"'
                i += 2
                continue
            else:
                # Toggle quote state
                in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            # End of field
            fields.append(current_field)
            current_field = ""
        else:
            current_field += char
            
        i += 1
    
    # Add the last field
    fields.append(current_field)
    
    return fields

# Test cases
assert parse_csv_line('a,b,c') == ['a', 'b', 'c']
assert parse_csv_line('"hello, world",foo,"bar"') == ['hello, world', 'foo', 'bar']
assert parse_csv_line('""""""') == ['""']
assert parse_csv_line('a,"b,c",d') == ['a', 'b,c', 'd']
assert parse_csv_line('x,"y""z",w') == ['x', 'y"z', 'w']
assert parse_csv_line(',a,,b,') == ['', 'a', '', 'b', '']
