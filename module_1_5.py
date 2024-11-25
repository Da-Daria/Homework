immutable_var = (1, 2, False, 'lol')
print(immutable_var)
print(immutable_var[1])
# immutable_var[1] = 5
# кортежи не подвержены изменениям для того, чтобы данные, которые они содержат, остались в неприкосновенности, а также это экономит память
mutable_list = [3, 4, 'angel']
print(mutable_list)
mutable_list[0] = 'go'
mutable_list[2] = 678
print(mutable_list)