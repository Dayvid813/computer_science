

Scret_santa = [True, False, True, True, False, True, False, False, True]
participant = Scret_santa.count(True)
Scret_santa.sort(reverse = True)
print(participant)
print(Scret_santa)

Exam_score = {"David": 96, "Howard": 96, "Eric": 89, "Yujing": 98, "Mr.Amini": 99}
MrAmini_result = Exam_score.get("Mr.Amini")
print(MrAmini_result)

Students_pet_name = {"David": "dog", "Howard": "cat", "Eric": "puppy", "Yujing": "pet_1", "Mr.Amini": "pet_2"}
MrAmini_pet = Students_pet_name.get("Mr.Amini")
print(MrAmini_pet)
sdict = sorted(Students_pet_name.items())
print(Students_pet_name)