subj = {}
bad_chars = ["(", ")", "\n", chr(1087), chr(1088), chr(1083), chr(1072), chr(1073)]
with open('text_6.txt', 'r', encoding='utf-8') as init_f:
    for line in init_f:
        line = "".join(r for r in line if r not in bad_chars)
        subject, lecture, practice, lab = line.split()
        lecture1 = lecture.replace("-", "0")
        practice1 = practice.replace("-", "0")
        lab1 = lab.replace("-", "0")
        subj[subject] = int(lecture1) + int(practice1) + int(lab1)
    print(f'Общее количество часов по предмету - \n {subj}')

