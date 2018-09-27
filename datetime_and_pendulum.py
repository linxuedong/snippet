from datetime import timezone, datetime
import pendulum

# 获取当前 UTC 时间
now = datetime.now(tz=timezone.utc)
print(now)

now = datetime(2018, 9, 27, 17, tzinfo=timezone.utc)

# datetime convert to pendulum
dt = pendulum.instance(now)
print(dt)
print(dt.timezone)

# 转化时区
dt = dt.in_tz(tz='Asia/Shanghai')

dt.date()


def is_today():
    return dt.date() == pendulum.today().date()
