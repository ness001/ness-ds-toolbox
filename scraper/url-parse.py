from urllib.parse import parse_qs
my_values = parse_qs('process-name=test&type-id=test.Task&_a=states',keep_blank_values=True)
print(my_values)