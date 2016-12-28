#coding:utf-8
#以正确的宽度在居中的“盒子”内打印一个句子

#注意，整数除法运算符（//）只能用在Python 2.2以及后续版本，在之前的版本中，只使用普通除法（/）

sentence = raw_input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_magin = (screen_width - box_width) // 2
 
print 
print '-' * left_magin + '+'  + '-' * (box_width-2) +  '+'
print ' ' * left_magin + '| ' + ' ' * text_width    + ' |'
print ' ' * left_magin + '| ' +       sentence      + ' |'
print ' ' * left_magin + '| ' + ' ' * text_width    + ' |'
print '-' * left_magin + '+'  + '-' * (box_width-2) +  '+'
print