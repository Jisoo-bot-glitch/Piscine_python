def ft_count_harvest_recursive():
    recursive = int(input("Days until harvest: "))

    def ft_helper(i):
        if i <= recursive:
            print(f"Day {i}")
            ft_helper(i + 1)
        else:
            print("Harvest time!")
    ft_helper(1)
