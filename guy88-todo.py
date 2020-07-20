from colorama import Fore
from colorama import Style
from textwrap import dedent

print(f"{Fore.GREEN}Welcome to guy88-todo{Style.RESET_ALL} v1.0")
print(f"{Fore.LIGHTBLUE_EX}Made in {Fore.YELLOW}Python{Style.RESET_ALL}")
print("Remember to be careful when writing a command\n")

tasks = []


class ScreenSwitch():
    def __init__(self, screen):
        self.screen = screen

    def display(self):
        self.screen.display()

    def switch_screen(self, screen):
        self.screen = screen


class Screen():
    def __init__(self):
        pass

    def display(self):
        pass


class WaitCommand(Screen):

    def __init__(self):
        pass

    def display(self):
        while True:
            cmd = input("Input command (h for help): ")

            if "q" in cmd:
                leave()

            elif "n" in cmd:
                screen_change.switch_screen(add_task)
                screen_change.display()

            elif "h" in cmd:
                screen_change.switch_screen(_help)
                screen_change.display()

            elif "s" in cmd:
                screen_change.switch_screen(show_task)
                screen_change.display()

            elif "d" in cmd:
                screen_change.switch_screen(delete_task)
                screen_change.display()

            else:
                print(f"{Fore.RED}Input a command that exists.\n{Style.RESET_ALL}")


def leave():
    print("Exiting\n")
    exit(0)


class TaskHelp(Screen):

    def __init__(self):
        pass

    def display(self):
        print(dedent(
            """
            Command list
            ------------

            h - open this list
            n - new task
            d - delete task
            s - show tasks
            q / CTRL + C - quit
            """))

        screen_change.switch_screen(await_cmd)

class AddTask(Screen):

    def __init__(self):
        pass

    def display(self):
        global tasks

        print("What is the label of this task?")
        self.label = input("> ")

        print("When should this task start? (day)")
        self.start_day = input("> ")

        print("When should this task start? (hour)")
        self.start_hour = input("> ")

        print("When is the deadline for this task? (day)")
        self.deadline_day = input("> ")

        print("When is the deadline for this task? (hour)")
        self.deadline_hour = input("> ")

        print("What is the ID for this task?")
        self.task_id = input("> ")

        print("Well done! Task made.\n")
        tasks.append(self.label)
        tasks.append(self.start_day)
        tasks.append(self.start_hour)
        tasks.append(self.deadline_day)
        tasks.append(self.deadline_hour)
        tasks.append(self.task_id)

        screen_change.switch_screen(await_cmd)


class DeleteTask(Screen):
    def __init__(self):
        pass

    def display(self):
        print(dedent(
        f"{Fore.RED}This is currently being implemented. To delete a task quit the app. However, it will delete all tasks.{Style.RESET_ALL}\n"))

        screen_change.switch_screen(await_cmd)

class ShowTasks(Screen):

    def __init__(self):
        pass

    def display(self):
        if len(tasks) > 0:
            print(f"\n{Fore.LIGHTBLUE_EX}Task data will be displayed in the following order:{Style.RESET_ALL}")
            print(f"Label, day it starts, hour it starts, deadline day, deadline hour and ID\n")
            for t in tasks:
                print(t)
            
            print("=" * 10)
            
            screen_change.switch_screen(await_cmd)

        else:
            print(f"{Fore.RED}There seems to be no task registered yet{Style.RESET_ALL}\n")
            screen_change.switch_screen(await_cmd)


await_cmd = WaitCommand()
add_task = AddTask()
delete_task = DeleteTask()
show_task = ShowTasks()
_help = TaskHelp()
screen_change = ScreenSwitch(await_cmd)
screen_change.display()
