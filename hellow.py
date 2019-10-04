 
###########################
"""
n = int(input('請輸入月份判斷目前的季節\n'))
print()
if n >= 1 and n <= 3:
    print('春天')
elif n >= 4 and n <=6 :
    print('夏天')
elif n >= 7 and n <= 9:
    print('秋天')
elif n >= 10 and n <=12:
    print('冬天')
else:
    print('請勿亂輸入！')
"""
##############################

print('1 : 半票 , 票價：110')
print('2 : 全票 , 票價：220')
print('3 : 軍警 , 票價：180')

i = 'n'
count = int(0)
while i == 'n':
    m = int(input('請輸入票卷種類\n'))
    n = int(input('請輸入張數\n'))
    if m == 1 :
        count= count + 110*n 
    elif m == 2:
        count= count + 220*n
    elif m == 3:
        count= count + 180*n
    i = input('請問是否輸入結束,y/n\n')

print('票價總金額是',count)
