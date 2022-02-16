from hashlib import sha256

text = 'Mortem'
set_text = set()

for i in range(len(text)):
    for j in range(len(text)):
        if text[i:j]:
            res = text[i:j].encode()
            set_text.add(sha256(res))

print(f"в строке '{text}' {len(set_text)} подстрок \n {set_text}")
