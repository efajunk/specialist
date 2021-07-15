import sys

# """ First version"""
# if __name__ == "__main__":
#     print("Hello, world")
#     print(sys.argv[0])
# 
# 
# """ Second version"""
# if __name__ == "__main__":
#     for param in sys.argv:
#         print(param)

# """ Third version"""
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         print ("Hello, {}!".format(sys.argv[1]))
#     else:
#         print ("Hello, world!")
        
# """ Fourth version --name; -n"""
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print ("Hello, world!")
    else:
        if len (sys.argv) < 3:
            print ("Error. Not enough arguments")
            sys.exit(1)

        if len(sys.argv) > 3:
            print ("Error. Too many arguments.")
            sys.exit(1)

        param_name = sys.argv[1]
        param_value = sys.argv[2]

        if param_name == "--name" or param_name == "-n":
            print ("Hello, {}!".format(param_value))
        else:
            print ("Error. Unknown argument: '{}'".format(param_name))
            sys.exit(1)
