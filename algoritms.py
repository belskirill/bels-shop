import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

from beanie import Document, Indexed, init_beanie


class Product(Document):
    name: str
    price: Indexed(float)

    class Settings:
        name = "products"


async def example():
    client = AsyncIOMotorClient("mongodb://localhost:27017/")

    await init_beanie(database=client["products-db"], document_models=[Product])

    tony_bar = Product(name="Tony Bar", price=5.0)
    await tony_bar.insert()

    data = await Product.find({}).to_list()
    print(f"{data=}")


if __name__ == "__main__":
    asyncio.run(example())
