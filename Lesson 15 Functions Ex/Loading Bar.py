# Read user input
number = int(input())

# Logic
def loading_bar(a):
    a = number / 10
    # bar = list(filter(lambda x: x <= percent, range(1, 11)))
    # return f"{a}% [{'%' * len(bar)}{'.' * (10 - len(bar))}]"
    bar = "[%%%%%%%%%%]"
    bar_lenght = int(a)
    if bar_lenght == 10:
        return f"{number}% Complete!\n{bar}"
    else:
        bar = f"{number}% [" + "%" * bar_lenght + "." * (10 - bar_lenght) + "]\nStill loading..."
        return(bar)


# Output
print(loading_bar(number))