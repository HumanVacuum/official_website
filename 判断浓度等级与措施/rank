from flask import json

#  从仪器那里获得了测得的数据,判断这个数据属于哪个层次
def judge(num):
    if 0 <= num < 35:
        rank = "Excellent!"
    elif 35 <= num < 75:
        rank = "Good!"
    elif 75 <= num < 115:
        rank = "Mild air pollution!"
    elif 115 <= num < 150:
        rank = "Moderate air pollution!"
    elif 150 <= num < 250:
        rank = "Severe air pollution!"
    else:
        rank = "Very severe air pollution!"
    return rank

#  应对方案的字典
def action(rank):
    action = {
        'Excellent!': '无污染',
        'Good!': '请带上口罩,并开窗通风',
        'Mild air pollution!': '请带上口罩,并开窗通风',
        'Moderate air pollution!': '请戴上口罩,开窗通风,打开空气净化器',
        'Severe air pollution!': '请戴上口罩,开窗通风,打开空气净化器',
        'Very severe air pollution!': '请戴上口罩,开窗通风,打开空气净化器'
    }
    filename = 'action.json'
    with open(filename,'w')as f:
        json.dump(action,f)
    f.close()
    return f
