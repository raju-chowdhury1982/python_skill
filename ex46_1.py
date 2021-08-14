# stock_price = [('apple', 300), ('microsoft', 321), ('sun_solaries', 298), ('google', 322)]
#
# # tuple unpacking
#
# for item in stock_price:
#     print(item)
#
# print("_" * 20)
#
# for org, price in stock_price:
#     print(org)
#     # let increase price by 10%
#     print(price * 1.1)
#
# print("_" * 20)

survey_report = [('nitisha', 4), ('lalit', 8), ('niru', 7), ('vijay', 10)]


def max_survey_done(survey_report):
    emp_name = ""
    survey_done = 0
    for name, survey in survey_report:
        if survey > survey_done:
            survey_done = survey
            emp_name = name
        else:
            pass
    return(emp_name, survey_done)

result = max_survey_done(survey_report)
x, y = max_survey_done(survey_report)
print(result)
print("-" * 20)
print(f"{x.title()} done {y} today.")
