from celery.schedules import crontab


# Celery的配置, 修改配置需要重启celery 和celery beat


broker_url = 'redis://localhost:6379/1' # 消息代理器配置, redis 用例: redis://:password@hostname:port/db_number
result_backend = 'redis://localhost:6379/2' # 结果储存
result_expires=2000
broker_transport_options = {'visibility_timeout': 3600}  # 1 hour
task_serializer = 'json'  # 序列形式
enable_utc = True         # 默认为True,当前时间-8=utc时间
# task_annotations = {'celery.add': {'rate_limit': '10/m'}}  # 限制任务的频率,10/m代表这个任务在一分钟内最多只能有10个被执行
# task_routes = {'celery.add': 'low-priority',}  # 指定任务队列

# 定时任务文档 http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules
# 使用前在 http://tool.lu/crontab/ 测试一遍
beat_schedule = {
    'test_celery_beat': {  # 测试celery 定时任务
        'task': 'Tiktok.celery.todo',
        #'schedule': crontab(hour=7, minute=30, day_of_week=1),  Executes every Monday morning at 7:30 a.m.
        'schedule': 10,
        'args': (3,5),
    },
}