### Given a tuple (1,2,3,4,5), print all pairs of elements whose sum is even

numbers = (1,2,3,4,5)

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if (numbers[i] + numbers[j]) % 2 == 0:  # check if sum is even
            print(numbers[i], numbers[j])