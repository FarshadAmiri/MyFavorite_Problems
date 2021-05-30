# https://quera.ir/problemset/university/633/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D9%85%D8%AD%D8%A7%D8%B3%D8%A8%D9%87-%D8%B6%D8%B1%D8%A7%DB%8C%D8%A8-%DA%86%D9%86%D8%AF%D8%AC%D9%85%D9%84%D9%87%D8%A7%DB%8C
# محاسبه‌ ضرایب چندجمله‌ای


import numpy as np

_,n = map(int,input().split(' '))
coefs = np.array(list(map(int,input().split(' '))))

# n = 20
# coefs = np.random.randint(1,200,(1,21))

t1 = time.time()

def summarize_poly(array):
    coefs_dict = dict()
    for index,i in np.ndenumerate(array):
        index_sum = index[0] + index[1]
        if index_sum in coefs_dict:
            coefs_dict[index_sum] += i
        else:
            coefs_dict[index_sum] = i
    summarized_poly = np.array(list([coefs_dict[x] for x in sorted(coefs_dict)]))
    return summarized_poly

poly_mat = coefs
while n>1:
    outer_of_two = np.outer(poly_mat,coefs)
    poly_mat = summarize_poly(outer_of_two)
    n -= 1

result = [str(int(i)) for i in poly_mat]
print(' '.join(result))