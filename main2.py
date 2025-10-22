import asyncio

async def task(name, delay):
    print(f"задача {name} запустилась")
    await asyncio.sleep(delay)
    print(f"задача {name} выполнена")

async def main():
    # await task("a", 1)
    tasks = [
        task("a", 3),
        task("b", 2),
        task("c", 3),
        task("d", 5),
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

# asyncio.run(main())