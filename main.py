import numpy as np
import ikuo as i

if __name__ == "__main__":
    hoge = np.array([0, 1, 2, 3, 4])
    print(hoge)
    hoge[2] = 74  # replace an element
    print(hoge)
    i.ikuoGetPrint()
