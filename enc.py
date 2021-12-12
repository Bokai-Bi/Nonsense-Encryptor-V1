import random


def encrypt(stringg, master_pass):
    master_pass *= 9

    list_of_letters = list(stringg)
    list_of_nums = list(str(master_pass))
    random_stuff = list('`1234567890-=\\][poiuytrewqasdfghjkl;\'/.,mnbvcxz\']`~!@#$%^&*()_+|}{POIUYTREWQASDFGHJKL:"?><MNBVCXZ"}')
    random_stuff.append('\n')

    for a in range(len(list_of_nums)):
        if list_of_nums[a] == 'e':
            del list_of_nums[a:]
            del list_of_nums[1]
            break


    for a in list_of_nums:
        list_of_nums.append((int(list_of_nums.pop(0))+1)*2)
    list_of_nums[0] += int(list_of_nums[-1]/3)
    list_of_nums[2] += int(list_of_nums [-2]/3)
    list_of_nums[1] += int(list_of_nums[-6]/3)
    list_of_nums[3] += int(list_of_nums[-5]/3)
    list_of_nums[5] += int(list_of_nums[-3]/3)
    list_of_nums[4] += int(list_of_nums[-4]/3)
    list_of_nums[0] += int(list_of_nums[4]/3)
    list_of_nums[2] += int(list_of_nums [0]/3)
    list_of_nums[1] += int(list_of_nums[2]/3)
    list_of_nums[3] += int(list_of_nums[1]/3)
    list_of_nums[5] += int(list_of_nums[3]/3)
    list_of_nums[4] += int(list_of_nums[5]/3)
    output_string = ''
    list_of_nums1 = list_of_nums[:]
    while list_of_letters != []:
        if list_of_nums == []:
            list_of_nums = list_of_nums1[:]
        temp=list_of_nums.pop(0)
        for a in range(temp):
            output_string += random.choice(random_stuff)
        output_string += list_of_letters.pop(0)
    for a in range(list_of_nums1[-1]):
        output_string += random.choice(random_stuff)

    return output_string




def decrypt(stringg, master_pass):
    master_pass *= 9

    list_of_nums = list(str(master_pass))
    list_of_letters = list(stringg)

    for a in range(len(list_of_nums)):
        if list_of_nums[a] == 'e':
            del list_of_nums[a:]
            del list_of_nums[1]
            break

    for a in list_of_nums:
        list_of_nums.append((int(list_of_nums.pop(0))+1)*2)
    list_of_nums[0] += int(list_of_nums[-1]/3)
    list_of_nums[2] += int(list_of_nums [-2]/3)
    list_of_nums[1] += int(list_of_nums[-6]/3)
    list_of_nums[3] += int(list_of_nums[-5]/3)
    list_of_nums[5] += int(list_of_nums[-3]/3)
    list_of_nums[4] += int(list_of_nums[-4]/3)
    list_of_nums[0] += int(list_of_nums[4]/3)
    list_of_nums[2] += int(list_of_nums [0]/3)
    list_of_nums[1] += int(list_of_nums[2]/3)
    list_of_nums[3] += int(list_of_nums[1]/3)
    list_of_nums[5] += int(list_of_nums[3]/3)
    list_of_nums[4] += int(list_of_nums[5]/3)
    for a in range(list_of_nums[-1]):
        list_of_letters.pop()

    output_string = ''
    while list_of_letters != []:
        for num in list_of_nums:
            if list_of_letters == []:
                break
            del list_of_letters[0:num]
            if list_of_letters == []:
                break
            output_string += list_of_letters.pop(0)


    return output_string



while True:
    a=input('What do you want to do? 1-->Encrypt 2-->Decrypt 3-->Quit >>>')
    if a == '1':
        mes = input('Input the message you\'re trying to encrypt >>>')
        pwd = input('Input the key for your message(Pure numbers) >>>')
        print('Your message is:')
        print(encrypt(mes,pwd))
    elif a == '2':
        mes = input('Input the message you\'re trying to decrypt >>>')
        pwd = input('Input the key for your message(Pure numbers) >>>')
        print('Your message is:')
        print(decrypt(mes,pwd))
    elif a == '3':
        quit(0)
    else:
        print('Unknown input')
