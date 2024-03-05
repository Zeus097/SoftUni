participant_info = {}
number_of_submission = {}

while True:
    command = input()

    if command == 'exam finished':
        break

    student_info = command.split("-")

    if len(student_info) > 2:
        name = student_info[0]
        language = student_info[1]
        score = int(student_info[2])

        if language not in participant_info:
            participant_info[language] = {name: [score]}
            number_of_submission.update({language: 1})

        else:
            if name not in participant_info[language]:
                participant_info[language].update({name: [score]})
            else:
                participant_info[language][name].append(score)

            number_of_submission[language] += 1

    else:
        name = student_info[0]
        for language, current_name in participant_info.items():
            for key in current_name:
                if name in key:
                    del participant_info[language][key]
                    break

print("Results:")
for value in participant_info.values():
    for current_name, current_points in value.items():
        points = str(max(current_points))
        result = ''.join(points)
        print(f"{current_name} | {int(result)}")

print("Submissions:")
for language, submissions in number_of_submission.items():
    print(f"{language} - {submissions}")
