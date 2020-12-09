import pyperclip

# split lines by character count at whitespace
def split_count(input, char_count):
    output = []

    output.append("".ljust(char_count))

    for line in input:
        index = 1
        this_line = line.split()
        one_line = " "
        line_index = 0

        while line_index < len(this_line):
            if index + len(this_line[line_index]) + 1 >= char_count:
                output.append(one_line.ljust(char_count))
                one_line = " "
                index = 1

            one_line += this_line[line_index] + " "
            index += len(this_line[line_index]) + 1
            line_index += 1

        if index > 1:
            output.append(one_line.ljust(char_count))

        output.append("".ljust(char_count))

    return output

if __name__ == "__main__":
    rep = ["      .~~~~`\\~~\\",
"     ;       ~~ \\",
"     |           ;",
" ,--------,______|---.",
"/          \\-----`    \\",
"`.__________`-_______-'"]

    # max length of the lines in the ascii art
    border_len = len(max(rep, key=len))

    # the number of ascii art repetitions that'll fit in 100 char
    length = (int) (100 / border_len)

    # create the top/bottom border of the box
    border_line = ""
    fence = 0
    for line in rep:
        if fence != 0:
            border_line += '\n'
        full_line = line.ljust(border_len)
        for num in range(0, length):
            border_line += full_line
        fence = 1

    while True:
        exit = False
        messages = []

        # take in input for comments
        # TODO: worry about tabbing for -1?
        while exit != True:
            print("Enter your stuff, type STOP to stop: ")
            str = input()
            exit = str == 'STOP'

            if exit != True:
                messages.append(str)

        # calculate the width inside the box, split accordingly
        message_len = (length * border_len) - (2 * border_len) - 1
        lines = split_count(messages, message_len)

        final = []
        final.append(border_line)

        # add individual lines w/ border to a list
        for index in range(0, len(lines)):
            bord_index = index % len(rep)

            temp = rep[bord_index].ljust(border_len) + " "
            temp += lines[index]
            temp += rep[bord_index].ljust(border_len)

            final.append(temp)

        leftover = len(lines) % len(rep)

        # finish ascii art on sides
        while leftover % len(rep) != 0:
            temp = rep[leftover].ljust(border_len) + " "
            temp += "".ljust(message_len)
            temp += rep[leftover].ljust(border_len)

            leftover += 1
            final.append(temp)

        # add on bottom border
        final.append(border_line)

        to_copy = ""
        print()
        for line in final:
            print(line)
            to_copy += line + "\n"

        pyperclip.copy(to_copy)

        print("The above text has been copied to your clipboard! ^C to exit\n")
