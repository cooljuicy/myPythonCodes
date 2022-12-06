def EgyptianFraction(fzi, fmu):
    def divanre(a, b):
        a1 = a // b
        a2 = a - a1 * b
        return a1, a2

    def gcd(a, b):
        x1 = max(a, b)
        x2 = min(a, b)
        while x2:
            x1, x2 = x2, divanre(x1, x2)[1]
        return x1

    out = []
    while True:
        w, r = divanre(fmu, fzi)
        out.append((1, w + 1))
        g = gcd(fzi - r, (w + 1) * fmu)
        a = int((fzi - r) // g)
        b = int((w + 1) * fmu // g)
        if a == 1:
            out.append((1, b))
            return out
        else:
            fzi = a
            fmu = b


def main():
    fz = int(input("分子为"))
    fm = int(input("分母为"))
    answer = EgyptianFraction(fz, fm)
    out = ""
    for a, b in answer:
        out += str(a) + "/" + str(b) + "\n+"
    out = out[: len(out) - 2]
    print("{}/{}=\n{}".format(fz, fm, out))


if __name__ == "__main__":
    while True:
        try:
            main()
        except:
            print("ERROR!")