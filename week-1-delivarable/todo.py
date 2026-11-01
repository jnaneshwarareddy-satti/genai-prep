# modules
import sys, json, os


def list_tasks(lst):
    if not lst:
        print("todo list is empty")
    else:
        print(lst)


def add_tasks(tasks, lst):
    id = int(max(lst))
    status = "incomplete"
    for task in tasks:
        id = id + 1
        lst[id] = []
        lst[id].append(task)
        lst[id].append(status)

    print("task(s) added successfully")


def remove_tasks(id, lst):
    for i in id:
        res = lst.pop(i, None)
        if res != None:
            print(f"popped {id} successfully")
        else:
            print("task not found")


def change_status(id, lst):
    for i in id:
        lst[i][1] = "completed"
        print(f"{i} task status is changed")


def main():
    if os.path.isfile("list.json"):
        with open("list.json", "r") as file:
            lst = json.load(file)
    else:
        json_string = {}
        with open("list.json", "w") as file:
            json.dump(json_string, file)
    tasks = []
    if len(sys.argv) > 1:
        funct = sys.argv[1]
        if len(sys.argv) >= 2:
            for i in range(2, len(sys.argv)):
                tasks.append(sys.argv[i])
        match funct:
            case "list_tasks":
                list_tasks(lst)
            case "add_tasks":
                add_tasks(tasks, lst)
            case "change_status":
                task_id = tasks
                change_status(task_id, lst)
            case "remove_tasks":
                task_id = tasks
                remove_tasks(task_id, lst)

        if os.path.isfile("list.json"):
            with open("list.json", "w") as f:
                lst = json.dump(lst, f)


if __name__ == "__main__":
    main()
