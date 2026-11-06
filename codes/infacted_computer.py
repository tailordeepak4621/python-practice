# def infected(days):
#     total = 0
#     for i in range(1,days+1):
#          total=total*2
#          if i%3==0:
#               patched = int(total*(0.2))
#               total = total-patched

#     return total
# print(infected(4))

# # import math

# # def infected(days):
# #     total = 1

# #     for i in range(1, days + 1):
# #         # Step 1: Double infected computers
# #         total = total * 2

# #         # Step 2: Apply patch every 3rd day
# #         if i % 3 == 0:
# #             patched = math.ceil(total * 0.20)
# #             total = total - patched

# #     return total


# # print(infected(3))  # 6
# # print(infected(6))  # 38
# # print(infected(9))  # 243

def infected(days):
    total = 1

    for i in range(1, days + 1):
        total *= 2

        if i % 3 == 0:
            patched = int(total * 0.20)

            if total * 0.20 > patched:
                patched += 1

            total -= patched

    return total


print(infected(3))  # 6
print(infected(6))  # 38
print(infected(9))  # 243
