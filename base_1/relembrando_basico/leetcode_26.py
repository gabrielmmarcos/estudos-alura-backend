nums = [2, 3, 3, 2]
nums_2 = [0, 1, 2, 2, 3, 4, 2]

remove = int(input('Digite o númeo que vc quer tirar da lista: '))

def remover_numero(nums):
    for i in range(len(nums) -1, -1, -1):
        if remove == nums[i]:
            nums.pop(i)
    return nums

print('Lista 1: ', remover_numero(nums))
print('Lista 2: ', remover_numero(nums_2))