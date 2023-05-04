

# как функция print принимает столько разных разнородных значений 

def print_them_all(*args, **kwargs):
    for i , e in enumerate(args):
        print(i,e)

    for k , v in kwargs.items():
        print(k,v)


print_them_all(1,2,'aaa', 4, 5)
# 0 1
# 1 2
# 2 aaa
# 3 4
# 4 5
#  копия от Никиты
# # Как функция print принимает столько значений!?
# # print(1, 2, False, 3 ,4 ,5, 6,' Hff', sep='\n')
 
# def print_them_all(*args, **kwargs):
#     for i, e in enumerate(args):
#         print(i, e)
 
#     for k, v in kwargs.items():
#         print(k, v)
 
# print_them_all(1, 2, 'AAA', 4, 5, a=1, b=False)