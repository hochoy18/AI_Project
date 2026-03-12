import json

from pydantic import *


class User(BaseModel):
    name: str # 姓名
    age: int = Field(ge=0,le=120,description="年龄")# 年龄
    email: str = Field()


def base_using():
    print( '*' * 50 , 'base_using', '*' * 50)
    user_1 = User(name='zhangsan', age=18, email='hochoy18@sina.com')
    print(user_1.model_dump())
    print(type(user_1.model_dump()))

    try:
        user_2 = User(name="lisi", age=180, email='hochoy18@sina.com')
        print(user_2)
    except ValidationError as e:
        print(e)

    try:
        user_2 = User(name="lisi", age=-1, email='hochoy18@sina.com')
        print(user_2)
    except ValidationError as e:
        print(e)


class Address(BaseModel):
    street: str
    city: str
    provence: str


class Order(BaseModel):
    id: int = Field(gt=0, le=10000)
    status: bool
    address: Address
    user: User


def base_using_nested():
    print( '*' * 50 , 'base_using_nested', '*' * 50)
    order1 = Order(id=122,status=True,
          address=Address(provence='jiangsu',city='shanghai',street='shanghai',id=1),
          user = User(name='zhangsan', age=18, email='hochoy18@sina.com'),
          )
    print(order1)
    print(order1.model_dump())
    print(json.dumps(order1.model_dump()))

    order_str = '''
{
    "id": 100,
    "status": false,
    "address":
    {
        "street": "xuanwuhu",
        "city": "nanjing",
        "provence": "jiangsu"
    },
    "user":
    {
        "name": "lisi",
        "age": 18,
        "email": "hochoy18@sina.com"
    }
}
    '''
    order2 = Order(**json.loads(order_str))
    print(order2)


class Product(BaseModel):
    name: str
    price: float
    # 模型配置：允许额外字段（输入数据有多余字段时不报错）
    model_config = ConfigDict(extra="allow")


def base_using_config():
    print( '*' * 50 , 'base_using_config', '*' * 50)

    product_data = {"name": "手机", "price": 2999.9, "category": "数码"}
    product = Product(**product_data)
    print(product.model_dump())
    print(product.category)


if __name__ == '__main__':
    base_using()
    base_using_nested()
    base_using_config()