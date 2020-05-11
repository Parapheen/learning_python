alphabet = input()
key_to_alphabet = input()

if len(alphabet) == len(key_to_alphabet):
    snowden = {}
    snowden_inverted = {}
    for word, key in zip(alphabet, key_to_alphabet):
        snowden[word] = key
        snowden_inverted[key] = word

target_string = input()
inverted_target = input()

for i in target_string:
    print(snowden[i], end='')
print()
for p in inverted_target:
    print(snowden_inverted[p], end='')
