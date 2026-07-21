def kiem_tra_cung_hoang_dao(ngay, thang):
    ngay_toi_da = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if thang < 1 or thang > 12 or ngay < 1 or ngay > ngay_toi_da[thang]:
        return "Ngày hoặc tháng không hợp lệ"
        
    if (thang == 3 and ngay >= 21) or (thang == 4 and ngay <= 19):
        return "Bạch Dương"
    elif (thang == 4 and ngay >= 20) or (thang == 5 and ngay <= 20):
        return "Kim Ngưu"
    elif (thang == 5 and ngay >= 21) or (thang == 6 and ngay <= 20):
        return "Song Tử"
    elif (thang == 6 and ngay >= 21) or (thang == 7 and ngay <= 22):
        return "Cự Giải"
    elif (thang == 7 and ngay >= 23) or (thang == 8 and ngay <= 22):
        return "Sư Tử"
    elif (thang == 8 and ngay >= 23) or (thang == 9 and ngay <= 22):
        return "Xử Nữ"
    elif (thang == 9 and ngay >= 23) or (thang == 10 and ngay <= 22):
        return "Thiên Bình"
    elif (thang == 10 and ngay >= 23) or (thang == 11 and ngay <= 21):
        return "Bọ Cạp"
    elif (thang == 11 and ngay >= 22) or (thang == 12 and ngay <= 21):
        return "Nhân Mã"
    elif (thang == 12 and ngay >= 22) or (thang == 1 and ngay <= 19):
        return "Ma Kết"
    elif (thang == 1 and ngay >= 20) or (thang == 2 and ngay <= 18):
        return "Bảo Bình"
    elif (thang == 2 and ngay >= 19) or (thang == 3 and ngay <= 20):
        return "Song Ngư"

print(kiem_tra_cung_hoang_dao(15, 8))
print(kiem_tra_cung_hoang_dao(25, 12))
print(kiem_tra_cung_hoang_dao(30, 2))