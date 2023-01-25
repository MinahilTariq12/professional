def rec_tower_hanoi(n, start, end, extra):
    if n == 1:
        print("Move disc 1 from pole",start,"to pole", end)
        return
    rec_tower_hanoi(n-1, start, extra, end)
    print("Move disc",n, "from pole",start,"to pole", end)
    rec_tower_hanoi(n-1, extra, end, start)
def main():
    print(0, "A", "B", "c")
    print(1, "A", "B", "c")
    print(2, "A", "B", "c")
    print(3, "A", "B", "c")
    print(9, "A", "B", "c")
    print(20, "A", "B", "c")
    print(100, "A", "B", "c")
main()

