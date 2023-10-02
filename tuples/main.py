# lists are mutable whereas tuples are immutable
tuple1 = (1, 2, 3)
print(tuple1)
tuple2 = (1, "string", (4, 5))
print(tuple2)
tuple1.append(4)  # throws error as we are trying to mutate the tuple
