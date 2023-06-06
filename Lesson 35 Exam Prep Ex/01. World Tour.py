def is_valid_index(index, seq):
     return 0 <= index < len(seq)

text = input()
valid_index = False

while True:
     commands = input()
     if commands == "Travel":
          break

     command, argument, argument2 = commands.split(":")

     if command == "Add Stop":
          strings = argument2
          idx = int(argument)
          if is_valid_index(idx, text):
               text = text[:idx] + strings + text[idx:]

     elif command == "Remove Stop":
          start_idx = int(argument)
          end_index = int(argument2)
          if is_valid_index(start_idx, text) and is_valid_index(end_index, text):
               text = text[:start_idx] + text[end_index + 1:]

     elif command == "Switch":
          old_string = argument
          new_string = argument2
          text = text.replace(old_string, new_string)

     print(text)

print(f"Ready for world tour! Planned stops: {text}")
