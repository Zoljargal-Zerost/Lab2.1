# MADLIB 1
course_id = input("Хичээлийн код: ")
course_name = input("Хичээлийн нэр: ")
credit = input("Хичээлийн кредит: ")

mablib = "Энэ хичээлийн код нь {}".format(course_id).upper() + \
    ", хичээлийн нэр нь {}".format(course_name).title() + \
        " бөгөөд уг хичээл нь {}".format(credit) + " кредитийн хичээл юм."

print(madlib)