print("Introduce los números del DNI uno por uno:")
nums = []
for _ in range(8):
  nums.append(int(input()))

dni = 0
for i in range(len(nums)):
  dni += 10 ** (len(nums) - i - 1) * nums[i]

print(dni)
letters = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y",
           7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N", 13: "J",
           14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C",
           21: "K", 22: "E"}

letter = letters[dni % 23]

DNI = {"numbers": nums, "letter": letter}
print(DNI)