# დავალება 1.

# დაწერეთ ორი ასინქრონული ფუნქცია, ერთ-ერთი დააყოვნეთ 2 
# წამი, მეორე 5 წამი, დაბეჭდეთ მათი დაწყება და დასრულება, 
# თასქები შექმენით ცალ-ცალკე და გაუშვით.
import asyncio

# პირველი ფუნქცია, რომელიც 2 წამით დაყოვნდება
async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

# მეორე ფუნქცია, რომელიც 5 წამით დაყოვნდება
async def task2():
    print("Task 2 started")
    await asyncio.sleep(5)
    print("Task 2 finished")

# მთავარი ფუნქცია, რომელიც ორივე თასქს გაუშვებს
async def main():
    # ცალ-ცალკე თასქების შექმნა
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    # ყველა თასქის გაშვება
    await t1
    await t2

# ასინქრონული პროგრამის გაშვება
asyncio.run(main())

# დავალება 2.

# დაწერეთ ასინქრონული ფუნქცია, რომელიც რენდომად არჩეული 
# დროით დააყოვნებს და დაბეჭდავს რიცხვებს 1-დან 10-მდე
import asyncio
import random

# ასინქრონული ფუნქცია, რომელიც რენდომად არჩეული დროით დააყოვნებს
async def print_numbers():
    for i in range(1, 11):
        delay = random.uniform(0.1, 2.0)
        await asyncio.sleep(delay)
        print(i)

# ასინქრონული ფუნქციის გაშვება
asyncio.run(print_numbers())



# დავალება 3.

# დაწერეთ ასინქრონული ფუნქცია, დააბრუნებს ატრიბუტად 
# გადაწოდებული რიცხვის კვადრატს, იმ შემთხვევაში თუ ეს
# რიცხვი არის ლუწი, ამის შესამოწმებლად დაწერეთ მეორე 
# ასინქრონული ფუნქცია. შესამოწმებლად შექმენით რამდენიმე 
# თასქი, გამოიყენეთ gather მეთოდი

import asyncio

# ასინქრონული ფუნქცია, რომელიც რიცხვის ლუწობას ამოწმებს
async def is_even(number):
    await asyncio.sleep(1)  
    return number % 2 == 0

# ასინქრონული ფუნქცია, რომელიც რიცხვის კვადრატს აბრუნებს თუ ის ლუწია
async def square_if_even(number):
    if await is_even(number):
        return number ** 2
    else:
        return f"{number} is not even"

# მთავარი ფუნქცია, რომელიც ამოწმებს რიცხვებს
async def main():
    # თასქების შექმნა და gather-ის გამოყენება
    tasks = [square_if_even(n) for n in range(1, 11)]
    results = await asyncio.gather(*tasks)
    
    
    for result in results:
        print(result)

# ასინქრონული პროგრამის გაშვება
asyncio.run(main())
