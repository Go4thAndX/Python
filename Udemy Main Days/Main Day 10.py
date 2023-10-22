# Functions with Outputs, funtions with one Output


# def format_name(first_name, last_name):
#     # De .title() methode zorgt ervoor dat alle strings beginnen met een hoofdletter
#     print(first_name.title())
#     print(last_name.title())


# format_name("jAN gEORGE", "kOOMEN")

# # Output:
# # Jan George
# # Koomen


# def format_name(first_name, last_name):
#     title_case_first_name = first_name.title()
#     title_case_last_name = last_name.title()

#     print(f"{title_case_first_name} {title_case_last_name}")


# format_name("jAN gEORGE", "kOOMEN")


# def format_name(first_name, last_name):
#     title_case_first_name = first_name.title()
#     title_case_last_name = last_name.title()
#     return f"{title_case_first_name} {title_case_last_name}"


# format_string = format_name("jAN gEORGE", "kOOMEN")
# print(format_string)


# def format_name(first_name, last_name):
#     title_case_first_name = first_name.title()
#     title_case_last_name = last_name.title()
#     return f"{title_case_first_name} {title_case_last_name}"


# print(format_name("jAN gEORGE", "kOOMEN"))

# Functions with Outputs, funtions with multiple outputs


# def format_name(first_name, last_name):
#     if first_name == "" or last_name == "":
#         return
#     title_case_first_name = first_name.title()
#     title_case_last_name = last_name.title()
#     return f"{title_case_first_name} {title_case_last_name}"


# print(
#     format_name(
#         input("What is your first name ?: "), input("What is your last name ?: ")
#     )
# )
# # Output:
# # What is your first name ?:
# # What is your last name ?:
# # None


def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs !"
    title_case_first_name = first_name.title()
    title_case_last_name = last_name.title()
    return f"{title_case_first_name} {title_case_last_name}"


print(
    format_name(
        input("What is your first name ?: "), input("What is your last name ?: ")
    )
)
# Output:
# What is your first name ?:
# What is your last name ?:
# You didn't provide valid inputs !
