import random
import string

cum_tu_tieng_anh = {
    "the": 5,
    "and": 5,
    "ing": 4,
    "ion": 3,
    "ent": 3,
    "her": 3,
    "ere": 2,
    "for": 3,
    "tha": 3,
    "wit": 3,
    "his": 2,
    "hat": 2,
    "was": 2,
    "are": 2,
    "you": 2,
    "all": 2,
    "not": 2,
    "but": 2,
    "with": 4,
    "that": 4,
    "this": 4,
    "have": 4,
    "from": 3,
    "they": 3,
    "were": 3,
    "been": 3,
    "said": 3
}

def tao_khoa():
    chu_cai = list(string.ascii_lowercase)

    random.shuffle(chu_cai)

    return "".join(chu_cai)

def giai_ma(van_ban_ma, khoa):
    bang_ma = {}

    for i in range(26):
        bang_ma[khoa[i]] = chr(ord("a") + i)

    ket_qua = ""

    for ky_tu in van_ban_ma:

        if ky_tu.lower() in bang_ma:

            ky_tu_moi = bang_ma[ky_tu.lower()]

            if ky_tu.isupper():
                ket_qua += ky_tu_moi.upper()
            else:
                ket_qua += ky_tu_moi

        else:
            ket_qua += ky_tu

    return ket_qua

def tinh_diem(van_ban):
    van_ban = van_ban.lower()

    diem = 0

    for cum_tu, gia_tri in cum_tu_tieng_anh.items():

        vi_tri = 0

        while True:

            vi_tri = van_ban.find(cum_tu, vi_tri)

            if vi_tri == -1:
                break

            diem += gia_tri

            vi_tri += 1

    return diem

def doi_khoa(khoa):
    khoa_moi = list(khoa)

    vi_tri_1 = random.randint(0, 25)
    vi_tri_2 = random.randint(0, 25)

    khoa_moi[vi_tri_1], khoa_moi[vi_tri_2] = \
        khoa_moi[vi_tri_2], khoa_moi[vi_tri_1]

    return "".join(khoa_moi)

def hill_climbing(van_ban_ma, so_lan):
    khoa = tao_khoa()

    van_ban = giai_ma(van_ban_ma, khoa)

    diem = tinh_diem(van_ban)

    for i in range(so_lan):

        khoa_moi = doi_khoa(khoa)

        van_ban_moi = giai_ma(van_ban_ma, khoa_moi)

        diem_moi = tinh_diem(van_ban_moi)

        if diem_moi > diem:

            khoa = khoa_moi
            diem = diem_moi

    return khoa, diem

def random_restart(van_ban_ma, so_lan_khoi_dong):

    khoa_tot_nhat = ""
    diem_tot_nhat = -1
    van_ban_tot_nhat = ""

    for i in range(so_lan_khoi_dong):

        khoa, diem = hill_climbing(
            van_ban_ma,
            5000
        )

        van_ban = giai_ma(
            van_ban_ma,
            khoa
        )

        print(
            "Lan",
            i + 1,
            "- Diem:",
            diem
        )

        if diem > diem_tot_nhat:

            diem_tot_nhat = diem
            khoa_tot_nhat = khoa
            van_ban_tot_nhat = van_ban

    return (
        khoa_tot_nhat,
        diem_tot_nhat,
        van_ban_tot_nhat
    )

with open(
    "2.2_cipher_text.txt",
    "r",
    encoding="utf-8"
) as file:

    van_ban_ma = file.read()


khoa, diem, ket_qua = random_restart(
    van_ban_ma,
    20
)

print("Khoa tim duoc:")
print(khoa)

print("\Diem:")
print(diem)

print("\nPlaintext tot nhat:")


print(ket_qua)