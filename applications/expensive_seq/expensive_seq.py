# Your code here

seq = {}


def expensive_seq(x, y, z):
    # Your code here
    step_one = (x-1, y+1, z)
    step_two = (x-2, y+2, z*2)
    step_three = (x-3, y+3, z*3)
    if x <= 0:
        return y+z
    if x > 0:
        if step_one not in seq.keys():
            seq[step_one] = expensive_seq(x-1, y+1, z)
        if step_two not in seq.keys():
            seq[step_two] = expensive_seq(x-2, y+2, z*2)
        if step_three not in seq.keys():
            seq[step_three] = expensive_seq(x-3, y+3, z*3)
    return seq[step_one]+seq[step_two]+seq[step_three]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
