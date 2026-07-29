def parse_csv_line(line: str) -> list[str]:
    result = []
    current_field = ""
    in_quotes = False
    
    i = 0
    while i < len(line):
        char = line[i]
        
        if not in_quotes and char == '"':
            in_quotes = True
            i += 1
        elif in_quotes and char == '"':
            if i + 1 < len(line) and line[i+1] == '"':
                current_field += '"'
                i += 2
            else:
                in_quotes = False
                i += 1
        elif not in_quotes and char == ',':
            result.append(current_field)
            current_field = ""
            i += 1
        else:
            current_field += char
            i += 1
            
    result.append(current_field)
    return result

assert parse_csv_line("a,b,c") == ["a", "b", "c"]
assert parse_csv_line(",b,") == ["", "b", ""]
assert parse_csv_line('"hello, world",test') == ["hello, world", "test"]
assert parse_csv_line(' a , b ') == [" a ", " b "]
assert parse_csv_line('"say ""hi""",end') == ['say "hi"', 'end']
assert parse_csv_line('a,"b""c",d') == ['a', 'b"c', 'd']
