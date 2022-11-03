import enum


class RabbitExchange(enum.Enum):
    Main = 'myproject.rabbit.exchange'


class RabbitExchangeType(enum.Enum):
    FanOut = 'fanout'
    Direct = 'direct'
    Topic = 'topic'


class RabbitQueue(enum.Enum):
    FirstSampleQueue = 'myproject.rabbit.queue.first.sample.queue'
    SecondSampleQueue = 'myproject.rabbit.queue.second.sample.queue'
    FirstSampleQueueResponse = 'myproject.rabbit.queue.first.sample.queue.response'
    SecondSampleQueueResponse = 'myproject.rabbit.queue.second.sample.queue.response'
    
