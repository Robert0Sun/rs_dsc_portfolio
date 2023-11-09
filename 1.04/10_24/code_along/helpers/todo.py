
def get_todo():
    with open(r"E:/Users/rsuncin.fellow/Documents/GitHub/rs_dsc_portfolio/1.04/10_24/code_along/data/todo.txt") as f:
        lines = f.readlines()

        for row in lines:
            print(row)


print("youve ran todo.py")
