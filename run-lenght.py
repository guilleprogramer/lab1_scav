from collections import OrderedDict
def runLengthEncoding(bits):
    dict = OrderedDict.fromkeys(bits, 0)
    for ch in bits:
        dict[ch] += 1
    output = ''
    for key, value in dict.items():
        output = output + key + str(value)
    return output
x="01000101010"
runLengthEncoding(x)