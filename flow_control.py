def if_statement():
    """
    if ~ elif ~ else
    """

    """
    금액을 입력받고
        금액이 10,000원 이상이면 by taxi
        금액이 2,000원 이상이면 by bus
        그 미만이면 on foot
    """
    money = int(input("얼마 가지고 있어? "))

    message = ""
    if money >= 10000:
        message += "by taxi"
    elif money >= 2000:
        message += "by bus"
    else:
        message += "on foot"

    print(message)


if __name__ == "__main__":
    if_statement()