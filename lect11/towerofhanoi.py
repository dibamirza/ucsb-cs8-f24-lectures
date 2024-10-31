# Lecture 11: Recursion zybook 6.1 - 6.3
def towerofhanoi(n, source, target, auxilliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move the first n - 1 disks from source to aux
    towerofhanoi(n - 1, source, auxilliary, target)

    # Move the largest disk (n) from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move the n - 1 disks from aux to target
    towerofhanoi(n - 1, auxilliary, target , source )

    return

n = 6
towerofhanoi(n, 'A', 'C', 'B')

