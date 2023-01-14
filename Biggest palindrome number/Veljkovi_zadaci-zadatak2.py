# 2.	Napisati program koji računa najveći palindrom broj koji je nastao kao proizvod dva dvocifrena broja. Primer: 9009 = 91 × 99

def najveci_palindrom(prvi_dvocifren_broj:int, drugi_dvocifren_broj:int) -> str:
    sample_dict = {}
    if prvi_dvocifren_broj == 99:
        for i in range(1, prvi_dvocifren_broj + 1):
            if drugi_dvocifren_broj == 99:
                for j in range(1, drugi_dvocifren_broj + 1):
                    sample_dict[f"{i}, {j}"] = i * j
            else:
                for j in range(1, drugi_dvocifren_broj):
                    sample_dict[f"{i}, {j}"] = i * j
    else:
        for i in range(1, prvi_dvocifren_broj):
                for j in range(1, drugi_dvocifren_broj):
                    sample_dict[f"{i}, {j}"] = i * j

        
    maks_vrednost = 0
    for i in sample_dict.items():
        if str(i[1]) == str(i[1])[::-1]:
            if i[1] > maks_vrednost:
                maks_vrednost = i[1]

    # print(maks_vrednost)
    return f"Najveci palindrom koji se dobija proizvodom {prvi_dvocifren_broj} i {drugi_dvocifren_broj} je {maks_vrednost}"

print(najveci_palindrom(98, 99))