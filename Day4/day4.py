'''day4.py'''

'''
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

--- Part Two ---

Now find one that starts with six zeroes.

'''

import hashlib

def get_secret_key(file_name):
    input_file = open(file_name, "r", encoding='utf-8')
    key = input_file.read()
    input_file.close()

    return key

def find_specific_quested_data(input_data, start_with):
    quested_hash = ""
    quested_number = 0

    while not quested_hash.startswith(start_with):
        quested_number += 1
        data_to_hash = input_data + str(quested_number)
        quested_hash = str(hashlib.md5(data_to_hash.encode()).hexdigest())

    return quested_number


key = get_secret_key("input.txt")
first_half_answer = find_specific_quested_data(key, "00000")
print(first_half_answer)

second_half_answer = find_specific_quested_data(key, "000000")
print(second_half_answer)


