def tinh_so_chai_bia(n):
    gia_bia = 28
    # Tính số chai bia mua được ban đầu bằng tiền
    so_chai_mua_duoc = n // gia_bia
    
    tong_so_chai = so_chai_mua_duoc
    so_vo_chai = so_chai_mua_duoc
    
    # Tiếp tục đổi vỏ chai nếu có từ 3 vỏ trở lên
    while so_vo_chai >= 3:
        chai_doi_them = so_vo_chai // 3
        tong_so_chai += chai_doi_them
        # Số vỏ chai mới = số vỏ chai dư không đổi được + số vỏ của các chai vừa đổi
        so_vo_chai = (so_vo_chai % 3) + chai_doi_them
        
    return f"Số chai bia có thể mua được là: {tong_so_chai}"

print(tinh_so_chai_bia(28))
print(tinh_so_chai_bia(56))
print(tinh_so_chai_bia(84))