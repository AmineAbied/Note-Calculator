def get_float(prompt, history):
    while True:
        value = input(prompt)
        if value.lower() == "r":
            if history:
                return "RETURN"
            else:
                print("No previous input.")
                continue
        try:
            value = float(value)
            history.append(value)
            return value
        except ValueError:
            print("Invalid input, enter a number or r")


RED = "\033[1;31m"
GREEN = "\033[1;32m"
RESET = "\033[0m"
BLUE = "\033[1;34m"

print("|---------------------|")
print("\033[1m|---NOTE CALCULATOR---|\033[0m")
print("\033[1;31m|-------------By ABIED|\033[0m")
print("|---------------------|")
print("")
print(BLUE + ">Welcome," + RESET)
print(BLUE + ">This process will take a while, please make sure you are ready before starting." + RESET)
print(BLUE + ">At any moment, you can press 'r' to return to the previous input and edit it." + RESET)
go= input(BLUE + ">When you are ready, PRESS ENTER to start : " + RESET)
print(BLUE + "-------------------------------------------" + RESET)
print("")



subjects = [
    ("\033[1mARABE (3 CONTROLES)\033[0m", [
        "Please enter ARABE note (first control): ",
        "Please enter ARABE note (second control): ",
        "Please enter ARABE note (third control): "
    ]),
    ("\033[1mFRANCAIS (4 CONTROLES)\033[0m", [
        "Please enter FRANCAIS note (first control): ",
        "Please enter FRANCAIS note (second control): ",
        "Please enter FRANCAIS note (third control): ",
        "Please enter FRANCAIS note (fourth control): "
    ]),
    ("\033[1mISLAMIQUE (3 CONTROLES)\033[0m", [
        "Please enter EDUCATION ISLAMIQUE note (first control): ",
        "Please enter EDUCATION ISLAMIQUE note (second control): ",
        "Please enter EDUCATION ISLAMIQUE note (third control): "
    ]),
    ("\033[1mMATHEMATICS (3 CONTROLES)\033[0m", [
        "Please enter MATHEMATICS note (first control): ",
        "Please enter MATHEMATICS note (second control): ",
        "Please enter MATHEMATICS note (third control): "
    ]),
    ("\033[1mPHYSICS & CHEMISTRY  (4 CONTROLES)\033[0m", [
        "Please enter PHYSICS & CHEMISTRY note (first control): ",
        "Please enter PHYSICS & CHEMISTRY note (second control): ",
        "Please enter PHYSICS & CHEMISTRY note (third control): ",
        "Please enter PHYSICS & CHEMISTRY note (fourth control): "
    ]),
    ("\033[1mATC (3 CONTROLES)\033[0m", [
        "Please enter ATC note (first control): ",
        "Please enter ATC note (second control): ",
        "Please enter ATC note (third control): "
    ]),
    ("\033[1mADC (3 CONTROLES)\033[0m", [
        "Please enter ADC note (first control): ",
        "Please enter ADC note (second control): ",
        "Please enter ADC note (third control): "
    ]),
    ("\033[1mT (3 CONTROLES)\033[0m", [
        "Please enter T note (first control): ",
        "Please enter T note (second control): ",
        "Please enter T note (third control): "
    ]),
    ("\033[1mPE (3 CONTROLES)\033[0m", [
        "Please enter PE note (first control): ",
        "Please enter PE note (second control): ",
        "Please enter PE note (third control): "
    ]),
    ("\033[1mPHILOSOPHY (3 CONTROLES)\033[0m", [
        "Please enter PHILOSOPHY note (first control): ",
        "Please enter PHILOSOPHY note (second control): ",
        "Please enter PHILOSOPHY note (third control): "
    ]),
    ("\033[1mENGLISH (3 CONTROLES)\033[0m", [
        "Please enter ENGLISH note (first control): ",
        "Please enter ENGLISH note (second control): ",
        "Please enter ENGLISH note (third control): "
    ]),
    ("\033[1mSPORT (3 CONTROLES)\033[0m", [
        "Please enter SPORT note (first control): ",
        "Please enter SPORT note (second control): ",
        "Please enter SPORT note (third control): "
    ])
]

results = {}

for title, prompts in subjects:
    print(title)
    values = []
    history = []
    i = 0
    while i < len(prompts):
        value = get_float(prompts[i], history)
        if value == "RETURN":
            i -= 1
            if i < 0:
                i = 0
            values.pop()
            history.pop()
        else:
            values.append(value)
            i += 1
    results[title] = sum(values) / len(values)

print("\033[1mDISCIPLINE (1 CONTROLE)\033[0m")
activity = float(input("Please enter DISCIPLINE note: "))

print("Procecing...")

arabe, fr, islamq, maths, pc, atc, adc, t, pe, philo, anglais, sport = results.values()

si = atc*0.3 + adc*0.3 + t*0.2 + pe*0.2
notemult = arabe*2 + fr*4 + islamq*2 + maths*6 + pc*6 + si*8 + philo*2 + anglais*2 + sport*1 + activity*1
note = notemult / 34

print("Your note is : ", note)


if note >= 15:
    print(GREEN + "Well done! Your note is excellent." + RESET)
elif note >= 10:
    print(GREEN + "It's enough. You passed." + RESET)
else:
    print(RED + "Unfortunately, your note is not enough. Keep trying!" + RESET)


print(BLUE + "\033[1mBy A B I E D\033[0m" + RESET)