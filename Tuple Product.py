print("\033c")

tuple1 = (4, 3, 2, 2, -1, 18)
tuple2 = (2, 4, 8, 8, 3, 2)

print(f"1st tuple :\n{tuple1}")
print(f"\n2nd tuple :\n{tuple2}")

product = ()

for i in range(len(tuple1)):
    product += (tuple1[i] * tuple2[i],)

print(f"\nProduct of 1st and 2nd tuple :\n{product}")