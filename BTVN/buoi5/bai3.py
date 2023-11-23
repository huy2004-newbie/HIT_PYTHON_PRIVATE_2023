
text = str(input("Nhap xau:"))
words = text.lower().split()  # chuyển về chữ thường và tách các từ
word_dem = {}  
    
for word in words:
    word = word.strip('.,!?";:') # loại bỏ các dấu
        
    if word in word_dem:
        word_dem[word] += 1
    else:
        word_dem[word] = 1
    
    hienThi = sorted(word_dem.items(), key=lambda x: x[1], reverse=True)
    # chỗ này em đi tham khảo.

print(hienThi)