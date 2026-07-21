def phan_tich_so(n):
    so_chu_so = len(str(abs(n)))
    tong_chu_so = sum(int(chu_so) for chu_so in str(abs(n)))
    
    la_nguyen_to = True
    if n < 2:
        la_nguyen_to = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                la_nguyen_to = False
                break
                
    trang_thai_nguyen_to = "là số nguyên tố" if la_nguyen_to else "không phải là số nguyên tố"
    
    return f"Số chữ số: {so_chu_so}, Tổng chữ số: {tong_chu_so}, {n} {trang_thai_nguyen_to}."

print(phan_tich_so(54))
print(phan_tich_so(53))
print(phan_tich_so(123))
print(phan_tich_so(2))