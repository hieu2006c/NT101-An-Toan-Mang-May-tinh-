
def tao_ma_tran(khoa):
    khoa = khoa.upper()
    chu_cai = ""

    for ky_tu in khoa:
        if ky_tu.isalpha():
            if ky_tu == "J":
                ky_tu = "I"
            if ky_tu not in chu_cai:
                chu_cai += ky_tu

    bang_chu_cai = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for ky_tu in bang_chu_cai:
        if ky_tu not in chu_cai:
            chu_cai += ky_tu

    ma_tran = []
    for i in range(0, 25, 5):
        ma_tran.append(list(chu_cai[i:i + 5]))

    return ma_tran


def hien_thi_ma_tran(ma_tran):
    print("\nMa Tran Playfair:")
    for hang in ma_tran:
        print(" ".join(hang))


def chuan_hoa(van_ban):
    ket_qua = ""

    for ky_tu in van_ban.upper():
        if ky_tu.isalpha():
            if ky_tu == "J":
                ky_tu = "I"
            ket_qua += ky_tu

    return ket_qua


def chia_cap(van_ban):
    van_ban = chuan_hoa(van_ban)
    ket_qua = ""
    i = 0

    while i < len(van_ban):
        ky_tu_1 = van_ban[i]

        if i + 1 >= len(van_ban):
            ky_tu_2 = "X"
            i += 1
        elif van_ban[i] == van_ban[i + 1]:
            ky_tu_2 = "X"
            i += 1
        else:
            ky_tu_2 = van_ban[i + 1]
            i += 2

        ket_qua += ky_tu_1 + ky_tu_2

    return ket_qua


def tim_vi_tri(ma_tran, ky_tu):
    if ky_tu == "J":
        ky_tu = "I"

    for i in range(5):
        for j in range(5):
            if ma_tran[i][j] == ky_tu:
                return i, j

    return -1, -1


def xu_ly_cap(ma_tran, a, b, che_do):
    hang_1, cot_1 = tim_vi_tri(ma_tran, a)
    hang_2, cot_2 = tim_vi_tri(ma_tran, b)

    if hang_1 == hang_2:
        cot_1 = (cot_1 + che_do) % 5
        cot_2 = (cot_2 + che_do) % 5
    elif cot_1 == cot_2:
        hang_1 = (hang_1 + che_do) % 5
        hang_2 = (hang_2 + che_do) % 5
    else:
        cot_1, cot_2 = cot_2, cot_1

    return ma_tran[hang_1][cot_1] + ma_tran[hang_2][cot_2]


def ma_hoa(van_ban_ro, ma_tran):
    van_ban_ro = chia_cap(van_ban_ro)
    ket_qua = ""

    for i in range(0, len(van_ban_ro), 2):
        a = van_ban_ro[i]
        b = van_ban_ro[i + 1]
        ket_qua += xu_ly_cap(ma_tran, a, b, 1)

    return ket_qua


def giai_ma(van_ban_ma, ma_tran):
    van_ban_ma = chuan_hoa(van_ban_ma)

    if len(van_ban_ma) % 2 != 0:
        raise ValueError("Ciphertext phai co so ky tu chan.")

    ket_qua = ""

    for i in range(0, len(van_ban_ma), 2):
        a = van_ban_ma[i]
        b = van_ban_ma[i + 1]
        ket_qua += xu_ly_cap(ma_tran, a, b, -1)

    return ket_qua

khoa = input("Nhap khoa: ")
ma_tran = tao_ma_tran(khoa)

hien_thi_ma_tran(ma_tran)

print("\n1. Ma hoa")
print("2. Giai ma")

lua_chon = input("Chon 1 hoac 2: ")

if lua_chon == "1":
    van_ban_ro = input("Nhap ban ro: ")

    print("\nBan ro sau khi chia cap:")
    print(chia_cap(van_ban_ro))

    print("\nCiphertext:")
    print(ma_hoa(van_ban_ro, ma_tran))

elif lua_chon == "2":
    van_ban_ma = input("Nhap ciphertext: ")

    try:
        print("\nPlaintext:")
        print(giai_ma(van_ban_ma, ma_tran))
    except ValueError as loi:
        print("Loi:", loi)

else:
    print("Lua chon khong hop le.")
