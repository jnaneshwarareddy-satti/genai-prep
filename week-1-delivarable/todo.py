# modules
import sys, json, os


def list_tasks(lst):
    if not lst:
        print("todo list is empty")
    else:
        print(lst)


def add_tasks(tasks, lst):
    id = len(lst)
    status = "incomplete"
    for task in tasks:
        id = id + 1
        lst[id] = []
        lst[id].append(task)
        lst[id].append(status)

    print("task(s) added successfully")


def remove_tasks(id, lst):
    for i in id:
        lst.pop(i, None)
    print(f"popped {id} successfully")


def change_status(id, lst):
    for i in id:
        lst[i][1] = "completed"
        print(f"{i} task status is changed")


def main():
    if os.path.isfile("list.json"):
        with open("list.json", "r") as f:
            lst = json.load(f)
    else:
        print("The json file does not exist.")
        return None
    tasks = []
    if len(sys.argv) > 1:
        funct = sys.argv[1]
        if len(sys.argv) >= 2:
            for i in range(2, len(sys.argv)):
                tasks.append(sys.argv[i])
        match funct:
            case "list_tasks":
                list_tasks(tasks, lst)
            case "add_tasks":
                add_tasks(tasks, lst)
            case "list_tasks":
                list_tasks(tasks, lst)
            case "change_status":
                change_status(tasks, lst)
            case "remove_tasks":
                remove_tasks(lst)

        if os.path.isfile("list.json"):
            with open("list.json", "w") as f:
                lst = json.dump(lst, f)


if __name__ == "__main__":
    main()
