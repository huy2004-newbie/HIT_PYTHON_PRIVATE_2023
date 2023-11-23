dic = {
    'Yasuo' : {'price' : 6300, 'Ulti' : "Trăn Trối"},
    'Lee Sin' : {'price' : 4800, 'Ulti' : "Nộ Long Cước"},
    'Zed' : {'price' : 4800, 'Ulti' : "Dấu Ấn Tử Thần"},
    'Master Yi' : {'price' : 450, 'Ulti' : "Chiến Binh Sơn Cước"},
    'Garen' : {'price' : 450, 'Ulti' : "Công Lý Demacia"},
    'Tryndamere' : {'price' : 1350, 'Ulti' : "Từ Chối Tử Thần"}
}
name = str(input("nhập tên champion muốn mua: "))
name = name.title()
name_key = dic.get(name)
if(name_key != None):
    print("Price:", name_key.get('price'))
else:
    print("Không tồn tại champion!")