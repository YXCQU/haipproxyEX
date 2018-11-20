from config.settings import (TEMP_TYC_QUEUE, VALIDATED_TYC_QUEUE, TTL_TYC_QUEUE, SPEED_TYC_QUEUE)
# ValidatorRedisSpider提供了分布式父类爬虫
from ..redis_spiders import ValidatorRedisSpider
# BaseValidator提供了基本的请求错误处理，但是业务相关逻辑错误需要自己实现
from .base import BaseValidator


class TYCValidator(BaseValidator, ValidatorRedisSpider):
    # scrapy爬虫名，必须设置且不能与已知的重复
    name = 'tyc'
    # 需要验证的URL，建议选择一个稳定且有代表意义的url，数据结构是一个list
    urls = [
        'https://www.tianyancha.com/search?key=editorai'
    ]
    # 下面四个属性必须设置，并且与maps中的一致
    task_queue = TEMP_TYC_QUEUE
    score_queue = VALIDATED_TYC_QUEUE
    ttl_queue = TTL_TYC_QUEUE
    speed_queue = SPEED_TYC_QUEUE
    # 判断success_key是否在响应内容中，从而判断IP是否正常，默认为''，表示正常
    success_key = 'editorai'
