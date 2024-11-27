import webbrowser


class CommandProcessor:
    def process_command(self, command):
        command = command.lower()
        print("Исходное предложение:", command)

        if "открой гугл" in command:
            webbrowser.open("https://www.google.com")
            # print("Открываю Google...")
