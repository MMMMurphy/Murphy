
import datetime
import calendar

def fourth_wednesday(yymm):
    # 解析输入的 yymm 格式
    year = int(yymm[:2])
    month = int(yymm[2:])
    # 如果年份是两位数，转换为四位数
    if year < 100:
        year += 2000  # 假设年份在2000年到2099年之间
    
    # 获取该月份的第一天是星期几（0=星期一，6=星期日）
    first_day_weekday, _ = calendar.monthrange(year, month)
    # 计算第一个星期三
    first_wednesday = 2 - first_day_weekday  # 2代表星期三
    if first_wednesday < 0:
        first_wednesday += 7
    # 计算第四个星期三
    fourth_wednesday = first_wednesday + 21  # 21天后是第四个星期三
    # 创建日期对象
    result_date = datetime.date(year, month, fourth_wednesday)
    return result_date

fourth_wednesday("2501")