def main():
    while True:
        # print_prompt()
        input_buffer = input('db:>>')
        # read_input(inp`ut_buffer)
        if input_buffer.startswith('.'):
            do_meta_command(input_buffer)
        elif donothing(input_buffer):
            continue
        else:
            statement = prepare_statement(input_buffer)
            execute_statement(statement)


def prepare_statement(command):
    if True:
        return command
    else:
        print("Unrecognized command {} \n".format(command))
        return None


def execute_statement(statement):
    print('executed')


def donothing(command):
    return command.isspace() or len(command) == 0


def do_meta_command(command):
    if command == '.exit':
        exit('exit')
    else:
        print("Unrecognized command {} \n".format(command))


if __name__ == '__main__':
    main()
