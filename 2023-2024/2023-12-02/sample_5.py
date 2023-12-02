def f2c(f_temperature):
    c_temperature = (f_temperature - 32) * 5 / 9
    print(f"{f_temperature} F equals {c_temperature} C")

def c2f(c_temperature):
    f_temperature = c_temperature * 9 / 5 + 32
    print(f"{c_temperature} C equals {f_temperature} F")

f2c(f_temperature=0)
c2f(c_temperature=42)
c2f(c_temperature=37)
