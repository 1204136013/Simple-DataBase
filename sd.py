def main():
    while True:
        # print_prompt()
        input_buffer = input('db:>>')
        # read_input(inp`ut_buffer)
        if input_buffer == '.exit':
            # close_input_buffer(input_buffer)
            exit('exit')
        elif input_buffer.isspace() or len(input_buffer) == 0:
            continue
        else:
            print("Unrecognized command {} \n".format(input_buffer))


if __name__ == '__main__':
    main()
