def ma_hoa(text, khoa):
    ket_qua = ""
    for ky_tu in text:
        if 'A' <= ky_tu <= 'Z':
            ket_qua += chr((ord(ky_tu) - ord('A') + khoa) % 26 + ord('A'))

        elif 'a' <= ky_tu <= 'z':
            ket_qua += chr((ord(ky_tu) - ord('a') + khoa) % 26 + ord('a'))

        else:
            ket_qua += ky_tu

    return ket_qua

def giai_ma(text, khoa):
    return ma_hoa(text, -khoa)

def thu_khoa(text):
    for khoa in range(1, 26):
        print("Khoa", khoa, ":", giai_ma(text, khoa))

while True:
    print("1. Ma hoa")
    print("2. Giai ma")
    print("3. Brute-force")
    print("0. Thoat")

    chon = input("Nhap lua chon: ")

    if chon == "1":
        van_ban = input("Nhap van ban: ")
        khoa = int(input("Nhap khoa: "))

        print("Ket qua:", ma_hoa(van_ban, khoa))

    elif chon == "2":
        van_ban = input("Nhap van ban: ")
        khoa = int(input("Nhap khoa: "))

        print("Ket qua:", giai_ma(van_ban, khoa))

    elif chon == "3":
        van_ban = input("Nhap ciphertext: ")
        thu_khoa(van_ban)

    elif chon == "0":
        break

    else:
        print("Lua chon khong hop le")