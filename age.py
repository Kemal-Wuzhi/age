drive = input("請問你是否有開過車？:")
if drive != "有" and drive != "沒有":
    print("只能輸入有或沒有")
    raise SystemExit
age = input("請問你幾歲?:")
age = int(age)


if drive == "有":
    if age >= 18:   
        print("恭喜你，請享受你的旅程")
    else:
        print("請不要無照駕駛")
elif drive == "沒有":
    if age >= 18:
        print("廢物趕快去考駕照")
    else:
        print("等毛長齊記得要考駕照，不要連車都不會開")
else:
    print("只能輸入有或沒有")