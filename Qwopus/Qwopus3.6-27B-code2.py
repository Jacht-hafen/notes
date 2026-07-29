def parse_csv_line(line: str) -> list[str]:
    result = []
    current_field = []
    in_quotes = False
    
    i = 0
    while i < len(line):
        char = line[i]
        
        if not in_quotes:
            if char == '"' and not current_field:
                in_quotes = True
            elif char == ',':
                result.append(''.join(current_field))
                current_field = []
            else:
                current_field.append(char)
        else:
            if char == '"':
                if i + 1 < len(line) and line[i+1] == '"':
                    current_field.append('"')
                    i += 2
                    continue
                else:
                    in_quotes = False
            else:
                current_field.append(char)
        
        i += 1
    
    result.append(''.join(current_field))
    
    return result

assert parse_csv_line("a,b,c") == ["a", "b", "c"]
assert parse_csv_line("a,,c") == ["a", "", "c"]
assert parse_csv_line('"hello world",foo') == ["hello world", "foo"]
assert parse_csv_line('a,"b""c",d') == ["a", 'b"c', "d"]
assert parse_csv_line('"a""b"') == ['a"b']
assert parse_csv_line(" a , b ") == [" a ", " b "]
