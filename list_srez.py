# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]
# new_nums[3] = 0
#
# for i_nums in range(2, 8):
#     print(nums[i_nums], end = ' ')
# print()
#
# for i_nums in range(2, 8):
#     print(new_nums[i_nums], end = ' ')
#
# print('\n', new_nums[2:8])
# nums[:3] = [1]
# print(nums)

# def is_palindrome(list_num):
#     reverse_list = list_num[::-1]
#     if list_num == reverse_list:
#         return True
#     else:
#         return False
#
# list_num = [1, 2, 3, 4, 5]
# answer = []
#
# for i_nums in range(0, len(list_num)):
#     if is_palindrome(list_num[i_nums:len(list_num)]):
#         answer = list_num[:i_nums]
#         answer[::-1]
#         break
# print('Исходный список: ', list_num)
# print('Нужно приписать чисел: ', len(answer))
# print('Сами числа: ', answer)


# import random
#
# original_prices = [random.randint(-5, 10) for i in range(8)]
# new_prices = original_prices[:]
# for i in range(len(original_prices)):
#     if new_prices[i] < 0:
#         new_prices[i] = 0
# print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))
# print(original_prices)


nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
print(nums[:5])
print(nums[:-2])
print(nums[::2])
print(nums[1::2])
print(nums[::-1])
print(nums[::-2])






