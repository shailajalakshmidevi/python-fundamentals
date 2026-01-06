def get_pos_args(*args):
    print(args)
    for agr in args:
       if type(agr) == int:
           print(agr)
    get_pos_args()
get_pos_args(1,2,3,4,'hiii')
