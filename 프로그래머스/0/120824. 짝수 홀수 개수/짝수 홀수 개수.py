def solution(num_list):
    count_a = 0
    count_b = 0
    
    for n in num_list:
        if n % 2 == 0 :
            count_a += 1
        else:
            count_b += 1
    return [count_a, count_b]