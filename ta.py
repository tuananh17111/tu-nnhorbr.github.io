def khoi_tao_phim(ten_file):
    phim = {
        "P001": {"Ten": "Avengers", "Thoi_gian": "18:00", "Gia": 50000},
        "P002": {"Ten": "Inception", "Thoi_gian": "20:00", "Gia": 60000},
        "P003": {"Ten": "Interstellar", "Thoi_gian": "21:30", "Gia": 70000},
    }

    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            for sid, info in phim.items():
                f.write(f"{sid}|{info['Ten']}|{info['Thoi_gian']}|{info['Gia']}\n")
    except IOError as e:
        print("Lỗi khi tạo file phim mẫu:", e)
    else:
        print(f"Đã khởi tạo dữ liệu phim và lưu vào '{ten_file}'.")

    return phim


def doc_du_lieu_phim(ten_file):
    phim = {}
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for line in f:
                sid, ten, thoi_gian, gia = line.strip().split('|')
                phim[sid] = {
                    "Ten": ten,
                    "Thoi_gian": thoi_gian,
                    "Gia": int(gia)
                }
    except IOError as e:
        print("Lỗi khi đọc file phim:", e)

    return phim


def luu_du_lieu_phim(ten_file, phim):
    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            for sid, info in phim.items():
                f.write(f"{sid}|{info['Ten']}|{info['Thoi_gian']}|{info['Gia']}\n")
        print(f"Đã lưu dữ liệu phim vào '{ten_file}'.")
    except IOError as e:
        print("Lỗi khi lưu dữ liệu phim:", e)


def hien_thi_phim(phim):
    if not phim:
        print("Không có dữ liệu phim.")
        return
    print("\nDanh sách phim:")
    for sid, info in phim.items():
        print(f"{sid}: {info['Ten']} - {info['Thoi_gian']} - {info['Gia']} VND")


def dat_ve(phim):
    ma = input("Nhập mã phim muốn đặt vé: ").strip()
    if ma in phim:
        print(f"Bạn đã đặt vé xem '{phim[ma]['Ten']}' lúc {phim[ma]['Thoi_gian']}. Giá: {phim[ma]['Gia']} VND")
    else:
        print("Mã phim không tồn tại.")


def them_phim(phim):
    sid = input("Nhập mã phim mới: ").strip()
    if sid in phim:
        print("Mã phim đã tồn tại.")
        return
    ten = input("Nhập tên phim: ").strip()
    thoi_gian = input("Nhập thời gian chiếu (HH:MM): ").strip()
    try:
        gia = int(input("Nhập giá vé: ").strip())
    except ValueError:
        print("Giá vé phải là số nguyên.")
        return

    phim[sid] = {"Ten": ten, "Thoi_gian": thoi_gian, "Gia": gia}
    print(f"Đã thêm phim '{ten}' thành công.")


def xoa_phim(phim):
    sid = input("Nhập mã phim cần xóa: ").strip()
    if sid in phim:
        del phim[sid]
        print(f"Đã xóa phim có mã '{sid}'.")
    else:
        print("Không tìm thấy mã phim.")


def chinh_sua_phim(phim):
    sid = input("Nhập mã phim cần chỉnh sửa: ").strip()
    if sid in phim:
        print(f"Phim hiện tại: {phim[sid]}")
        ten = input("Tên mới (Enter để giữ nguyên): ").strip()
        thoi_gian = input("Thời gian mới (Enter để giữ nguyên): ").strip()
        gia = input("Giá vé mới (Enter để giữ nguyên): ").strip()

        if ten:
            phim[sid]['Ten'] = ten
        if thoi_gian:
            phim[sid]['Thoi_gian'] = thoi_gian
        if gia:
            try:
                phim[sid]['Gia'] = int(gia)
            except ValueError:
                print("Giá không hợp lệ. Giữ nguyên giá cũ.")
        print("Đã cập nhật thông tin phim.")
    else:
        print("Không tìm thấy mã phim.")


def tim_phim(phim):
    tu_khoa = input("Nhập từ khóa tìm kiếm tên phim: ").strip().lower()
    tim_thay = False
    for sid, info in phim.items():
        if tu_khoa in info['Ten'].lower():
            print(f"{sid}: {info['Ten']} - {info['Thoi_gian']} - {info['Gia']} VND")
            tim_thay = True
    if not tim_thay:
        print("Không tìm thấy phim nào phù hợp.")


def tinh_doanh_thu(phim):
    tong = sum(info['Gia'] for info in phim.values())
    print(f"Tổng doanh thu dự kiến (1 vé/phim): {tong} VND")


# === CHỨC NĂNG MỞ RỘNG ===

def sap_xep_phim_theo_ten(phim):
    if not phim:
        print("Không có dữ liệu phim.")
        return
    sap_xep = sorted(phim.items(), key=lambda x: x[1]['Ten'].lower())
    print("\nDanh sách phim theo tên:")
    for sid, info in sap_xep:
        print(f"{sid}: {info['Ten']} - {info['Thoi_gian']} - {info['Gia']} VND")


def sap_xep_phim_theo_gia(phim):
    if not phim:
        print("Không có dữ liệu phim.")
        return
    sap_xep = sorted(phim.items(), key=lambda x: x[1]['Gia'])
    print("\nDanh sách phim theo giá:")
    for sid, info in sap_xep:
        print(f"{sid}: {info['Ten']} - {info['Thoi_gian']} - {info['Gia']} VND")


def tim_phim_theo_khoang_gia(phim):
    try:
        min_gia = int(input("Nhập giá tối thiểu: "))
        max_gia = int(input("Nhập giá tối đa: "))
    except ValueError:
        print("Giá không hợp lệ.")
        return
    found = False
    for sid, info in phim.items():
        if min_gia <= info['Gia'] <= max_gia:
            print(f"{sid}: {info['Ten']} - {info['Thoi_gian']} - {info['Gia']} VND")
            found = True
    if not found:
        print("Không tìm thấy phim trong khoảng giá.")


def thong_tin_chi_tiet(phim):
    sid = input("Nhập mã phim cần xem chi tiết: ").strip()
    if sid in phim:
        info = phim[sid]
        print(f"Phim: {info['Ten']}, Chiếu lúc: {info['Thoi_gian']}, Giá vé: {info['Gia']} VND")
    else:
        print("Không tìm thấy mã phim.")


def dem_so_luong_phim(phim):
    print(f"Tổng số phim hiện có: {len(phim)}")


def phim_chieu_sau_20h(phim):
    found = False
    for sid, info in phim.items():
        gio, phut = map(int, info['Thoi_gian'].split(":"))
        if gio > 20 or (gio == 20 and phut > 0):
            print(f"{sid}: {info['Ten']} - {info['Thoi_gian']} - {info['Gia']} VND")
            found = True
    if not found:
        print("Không có phim nào chiếu sau 20:00.")


def cap_nhat_gio_chieu(phim):
    sid = input("Nhập mã phim cần cập nhật giờ chiếu: ").strip()
    if sid in phim:
        tg = input("Nhập giờ chiếu mới (HH:MM): ").strip()
        phim[sid]['Thoi_gian'] = tg
        print("Cập nhật thành công.")
    else:
        print("Không tìm thấy mã phim.")


def xuat_csv(phim, ten_file_csv="phim.csv"):
    try:
        with open(ten_file_csv, 'w', encoding='utf-8') as f:
            f.write("Ma,Ten,Thoi_gian,Gia\n")
            for sid, info in phim.items():
                f.write(f"{sid},{info['Ten']},{info['Thoi_gian']},{info['Gia']}\n")
        print(f"Đã xuất danh sách phim ra '{ten_file_csv}'.")
    except IOError as e:
        print("Lỗi khi xuất file CSV:", e)


def dat_ve_nhieu_phim(phim):
    danh_sach = input("Nhập mã phim (cách nhau bằng dấu phẩy): ").split(',')
    for ma in danh_sach:
        ma = ma.strip()
        if ma in phim:
            print(f"Đặt vé: {phim[ma]['Ten']} - {phim[ma]['Thoi_gian']} - {phim[ma]['Gia']} VND")
        else:
            print(f"Mã không tồn tại: {ma}")


# === CHƯƠNG TRÌNH CHÍNH ===
if __name__ == "__main__":
    ten_file = "phim.txt"
    phim = {}

    while True:
        print("""
=== QUẢN LÝ VÉ XEM PHIM ===
1. Khởi tạo dữ liệu phim
2. Đọc dữ liệu từ file
3. Lưu dữ liệu ra file
4. Hiển thị danh sách phim
5. Đặt vé
6. Thêm phim mới
7. Xóa phim
8. Chỉnh sửa thông tin phim
9. Tìm kiếm phim theo tên
10. Tính tổng doanh thu
11. Thoát
12. Sắp xếp phim theo tên
13. Sắp xếp phim theo giá
14. Tìm phim theo khoảng giá
15. Xem thông tin chi tiết phim
16. Đếm số lượng phim
17. Liệt kê phim chiếu sau 20h
18. Cập nhật giờ chiếu
19. Xuất danh sách phim ra CSV
20. Đặt vé nhiều phim
============================
""")
        choice = input("Nhập lựa chọn (1-20): ").strip()

        if choice == '1':
            phim = khoi_tao_phim(ten_file)
        elif choice == '2':
            phim = doc_du_lieu_phim(ten_file)
        elif choice == '3':
            luu_du_lieu_phim(ten_file, phim)
        elif choice == '4':
            hien_thi_phim(phim)
        elif choice == '5':
            dat_ve(phim)
        elif choice == '6':
            them_phim(phim)
        elif choice == '7':
            xoa_phim(phim)
        elif choice == '8':
            chinh_sua_phim(phim)
        elif choice == '9':
            tim_phim(phim)
        elif choice == '10':
            tinh_doanh_thu(phim)
        elif choice == '11':
            print("Tạm biệt!")
            break
        elif choice == '12':
            sap_xep_phim_theo_ten(phim)
        elif choice == '13':
            sap_xep_phim_theo_gia(phim)
        elif choice == '14':
            tim_phim_theo_khoang_gia(phim)
        elif choice == '15':
            thong_tin_chi_tiet(phim)
        elif choice == '16':
            dem_so_luong_phim(phim)
        elif choice == '17':
            phim_chieu_sau_20h(phim)
        elif choice == '18':
            cap_nhat_gio_chieu(phim)
        elif choice == '19':
            xuat_csv(phim)
        elif choice == '20':
            dat_ve_nhieu_phim(phim)
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
