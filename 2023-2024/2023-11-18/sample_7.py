def hello(message, message2):
    # print(message, message2)
    print(f"{message}, {message2}")
    return 0
    # return None

status = hello(message='hello', message2='HELLO')
status2 = hello(message='hello2', message2='HELLO2')
print(f"The status value is {status}")
print(f"The status2 value is {status2}")
