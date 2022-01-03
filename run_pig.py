def run_pig(code):
    assert type(code) is str, 'ERROR: Code must be a string.'
    assert 'PIG' in code, 'ERROR: Code must contain "PIG".'
    file_name, file_text = code.split('PIG',1)
    file = open(f'{file_name}.txt', 'w')
    file.write(file_text)
    file.close()
