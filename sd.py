def main():
    while True:
        # print_prompt()
        input_buffer = input(':>>')
        # read_input(input_buffer)
        if input_buffer == '.exit':
            # close_input_buffer(input_buffer)
            exit('exit')
        else:
            print("Unrecognized command {} \n".format(input_buffer))


if __name__ == '__main__':
    main()
