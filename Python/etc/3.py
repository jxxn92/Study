hex_string = "1B 7E 7C BA 78 1B 1B 1B 1B B6 1B 7E"

# Split the hex string into a list of hexadecimal values
hex_values = hex_string.split()

result = []
i = 0

while i < len(hex_values):
    if hex_values[i] == '1B':
        if i + 1 < len(hex_values) and hex_values[i + 1] == '7E':
            i += 2
        else:
            result.append(hex_values[i])
            i += 1
    else:
        result.append(hex_values[i])
        i += 1

# Join the result list into a space-separated string
result_string = ' '.join(result)

# Prepend 'D' to the result string
result_string = 'D ' + result_string

print(result_string)
