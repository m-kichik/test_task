import os

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


def make_num(num):
    if num < 10:
        return '00' + str(num)
    if num >= 10 and num < 100:
        return '0' + str(num)
    if num == 100:
        return '100'
# i = 1
# for file in files('VOCdevkit/Annotations'):
#     print(make_num(i))
#     file_name = file.title()
#     os.rename('VOCdevkit/Annotations/' + file, 'VOCdevkit/Annotations/' + make_num(i) + '.xml')
#     i += 1

# for file in files('VOCdevkit/JPEGImages'):
#     file_name = file.title()
#     os.rename('raw_pics/onthewall/' + file, 'raw_pics/onthewall/' + file)

# import random
#
# test = open('VOCdevkit/ImageSets/test.txt', 'w')
# val = open('VOCdevkit/ImageSets/val.txt', 'w')
# train = open('VOCdevkit/ImageSets/train.txt', 'w')
# trainval = open('VOCdevkit/ImageSets/trainval.txt', 'w')
#
# nums = []
# while len(nums) != 20:
#     new_num = random.randint(1, 100)
#     if not new_num in nums:
#         nums.append(new_num)
#         test.write(make_num(new_num) + '\n')
#         val.write(make_num(new_num) + '\n')
#
# for i in range(1, 101):
#     trainval.write(make_num(i) + '\n')
#     if not i in nums:
#         train.write(make_num(i) + '\n')
#
# print(nums)

for file in files('VOCdevkit/VOC2012/Annotations'):
    read = open('VOCdevkit/VOC2012/Annotations/' + file, 'r')
    new_string = read.read().replace('C:\dev\\test_task\VOCdevkit\JPEGImages\\' + file[0:3] + '.jpg',
                                  '\content\YOLOX\datasets\VOCdevkit\VOC2012\JPEGImages\\' + file[0:3] + '.jpg')
    read.close()
    write = open('VOCdevkit/VOC2012/Annotations/' + file, 'w')
    write.write(new_string)


