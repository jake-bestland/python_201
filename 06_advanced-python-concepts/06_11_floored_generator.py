# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?



nums = range(1, 1000000)


div_1111 = (x for x in nums if x % 1111 == 0)
for x in div_1111:
    print(x // 1111)

# 1-900 #    