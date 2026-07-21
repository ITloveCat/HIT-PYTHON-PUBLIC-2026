def tinh_so_ngay(thang, nam):
   
    la_nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
    
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
  
    elif thang in [4, 6, 9, 11]:
        return 30
    
    elif thang == 2:
        return 29 if la_nam_nhuan else 28
    else:
        return "Tháng không hợp lệ"


print(f"Tháng 10, Năm 2020 -> Output: {tinh_so_ngay(10, 2020)}")
print(f"Tháng 2, Năm 2024  -> Output: {tinh_so_ngay(2, 2024)}")
print(f"Tháng 2, Năm 2025  -> Output: {tinh_so_ngay(2, 2025)}")
print(f"Tháng 11, Năm 1921 -> Output: {tinh_so_ngay(11, 1921)}")