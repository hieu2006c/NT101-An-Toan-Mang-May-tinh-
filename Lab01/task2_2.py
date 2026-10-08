from collections import Counter

def thong_ke_tan_suat(text):
    dem = Counter()

    for ky_tu in text:
        if ky_tu.isalpha():
            dem[ky_tu.lower()] += 1

    return dem

def thay_the(text, bang_ma):
    ket_qua = ""

    for ky_tu in text:
        if ky_tu.lower() in bang_ma:
            ky_tu_moi = bang_ma[ky_tu.lower()]

            if ky_tu.isupper():
                ket_qua += ky_tu_moi.upper()
            else:
                ket_qua += ky_tu_moi
        else:
            ket_qua += ky_tu

    return ket_qua

with open("2.2_cipher_text.txt", "r", encoding="utf-8") as file:
    van_ban_ma = file.read()


tan_suat = thong_ke_tan_suat(van_ban_ma)

print("Tan suat xuat hien cac ky tu ")
for ky_tu, so_lan in tan_suat.most_common():
    print(ky_tu, ":", so_lan)

bang_ma = {
    "a": "x",
    "b": "y",
    "c": "z",
    "d": "f",
    "e": "v",
    "f": "u",
    "g": "t",
    "h": "h",
    "i": "r",
    "j": "q",
    "k": "p",
    "l": "a",
    "m": "n",
    "n": "m",
    "o": "l",
    "p": "k",
    "q": "j",
    "r": "i",
    "s": "s",
    "t": "g",
    "u": "w",
    "v": "e",
    "w": "d",
    "x": "c",
    "y": "b",
    "z": "o"
}

ket_qua = thay_the(van_ban_ma, bang_ma)


print("\nKet qua sau khi giai ma:")
print(ket_qua)