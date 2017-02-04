'''day5.py'''
'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

Your puzzle answer was 258.

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?

Your puzzle answer was 53.
'''

def is_string_is_nice_firstrules(input_string):
    vovels = ["a", "e", "i", "o", "u"]
    illicits = ["ab", "cd", "pq", "xy"]

    vovel_count = 0

    for item in illicits:
        if input_string.count(item) > 0:
            return False

    for letter in input_string:
        if letter in vovels:
            vovel_count += 1

    exist_letter_twice = False
    for i in range(0, len(input_string) - 2):
        if input_string[i] == input_string[i + 1]:
            exist_letter_twice = True

    if vovel_count >= 3 and exist_letter_twice:
        return True
    else:
        return False


def is_string_is_nice_secondrules(input_string):
    exist_letter_twice = False
    len_of_input_strings = len(input_string)
    if len_of_input_strings < 4:
        return False
    else:
        for i in range(0, len_of_input_strings - 2):
            if input_string.count(input_string[i] + input_string[i+1]) >= 2:
                exist_letter_twice = True
                break
        if exist_letter_twice:
            for i in range(0, len_of_input_strings - 3):
                if input_string[i] == input_string[i + 2] != input_string[i + 1]:
                    return True

        return False


input_file = open("input.txt", "r")
input_strings = input_file.readlines()
input_file.close()

num_of_nice_strings = 0
num_of_nice_strings_newrules = 0
for item in input_strings:
    if is_string_is_nice_firstrules(item):
        num_of_nice_strings += 1
    if is_string_is_nice_secondrules(item):
        num_of_nice_strings_newrules += 1

print(num_of_nice_strings)
print(num_of_nice_strings_newrules)






