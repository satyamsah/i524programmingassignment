import cmd


class HelloWorld(cmd.Cmd):
    '''Simple command processor example.'''

    def do_mycmd(self,line):
        if line == "deploy":
            print('1.%s!' % line)
        elif line == "kill":
            print('2.%s!' % line)
        elif line == "benchmark":
            print('3.%s!' % line)
        elif line == "benchmark":
            print('4.%s!' % line)
	else:
            print("cannot recognize the command")


    def do_EOF(self, line):
        print('bye, bye')
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
