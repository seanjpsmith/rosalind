#Ordering Strings of Varying Length Lexographically

input = """
D N A
3
""".strip('\n').split('\n')

alphabet, n = input[0].split(), int(input[1])

def generate(n, h=""):
    print h
    if n == 0:
        return
    for c in alphabet:
        generate(n-1, h+c)

generate(n)
