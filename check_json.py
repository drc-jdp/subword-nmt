import json


def checkjson():
    infile = open("encoder.json")
    dict_check = json.loads(infile)
    inverse_dict = {v:k for k,v in dict_check}
    for i in range(50257):
        if i not in inverse_dict:
            print('error', i)


if __name__ == "__main__":
    checkjson()