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
        'Excellent!': '空气质量优，请放心工作',
        'Good!': '空气质量良，请佩戴口罩，开窗通风',
        'Mild air pollution!': '当前空气质量为轻度污染，请佩戴口罩，开窗通风并打开空调新风系统',
        'Moderate air pollution!': '当前空气质量为轻度污染，请佩戴口罩，开窗通风并打开空调新风系统',
        'Severe air pollution!': '当前空气质量为严重污染，尽量不要进入设备工坊。如需进入，请佩戴口罩，打开空气净化器',
        'Very severe air pollution!': '当前空气质量为严重污染，尽量不要进入设备工坊。如需进入，请佩戴口罩，打开空气净化器'
        'Devil':'当前空气质量极差，请关闭门窗，关闭空调新风系统，打开空气质量净化器并尽快离开设备工坊'
    }
    filename = 'action.json'
    with open(filename,'w')as f:
        json.dump(action,f)
    f.close()
    return f
