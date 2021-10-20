import random

if __name__ == '__main__':
    score = random.randint(0, 100);
    if score >= 60:
        print(score, "pass")
    else:
        print(score, "fail")

    print(score, "Pass" if score >= 60 else "Fail")
