#!/usr/bin/python3

def texer(num, *args):
    count = 0
    count_word = 0
    for x in range(num):
        count += 1
        long = len(args[x])
        if count == 1:
            text = f"--{'-'*long}--"
        else:
            text += f"--{'-'*long}-"
    for y in range(num):
        count_word += 1
        if count_word == 1:
            text_word = f'| {args[y]} |'
        else:
            text_word += f' {args[y]} |'
    return f'{text}\n{text_word}\n{text}'
