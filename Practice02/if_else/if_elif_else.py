final_grade = 38
attestation = 57
total_grade = final_grade + attestation

if total_grade >= 69.5 and final_grade >= 19.5:
    print("Congratulations on passing the course and keeping your scholarship!")
elif total_grade >= 50 and final_grade >= 19.5:
    print("Congratulations! You passed the course")
elif attestation <= 29.5:
    print("Sorry, but you didn't pass the attestation requirement")
else:
    print("You didn't pass the course and need to retake the discipline.")