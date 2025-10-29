import pandas as pd
L = []
n = int(input("Nhập số sinh viên: "))
f = open('SinhVien.txt','w',encoding="utf-8")
f.write('Mã sinh viên Họ tên Lớp Quê quán \n')
for i in range(n):
    a = input("Nhập mã sinh viên: ")
    b = input("Nhập họ tên: ")
    c = input("Nhập lớp: ")
    d = input("Nhập quê quán: ")
    L.append([a, b, c, d])
    f.write(' '.join([a,b,c,d])+"\n")
f = open('SinhVien.txt','r',encoding="utf-8")
print(f.read())
class_ = []
dic = {}
for i in L :
    if not i[2] in class_ :
        class_.append(i[2])
        dic[i[2]] = [i]
    else : dic[i[2]].append(i)
writer = pd.ExcelWriter("SinhVien.xlsx", engine="openpyxl")
for i in dic :
    write = {
        'Mã sinh viên': [],
        'Họ tên': [],
        'Lớp': [],
        'Quê quán': []
    }
    for j in dic[i] :
        write['Mã sinh viên'].append(j[0])
        write['Họ tên'].append(j[1])
        write['Lớp'].append(j[2])
        write['Quê quán'].append(j[3])
    a = pd.DataFrame(write)
    a.to_excel(writer,sheet_name=i,index=False)
writer.close()