import argparse #สำหรับ รับ input จากภายนอก

def parse_input():
     parser = argparse.ArgumentParser(description='test program to learn about argparse and subprocess')
     parser.add_argument(
          'm', 
          type=int,
          help='value of M positional argument')
     parser.add_argument(
          '--x', 
          type=int,
          help='value of x')

     parser.add_argument(
         '--yval',
         type=int,
         default=3,
         help='value of y')

     args = parser.parse_args()
     return args


def print_other():
     print('something else')
     
def print_one():
     print('11111')

if __name__ == "__main__":
    x = parse_input()
    print_other()
    print_one()
    print_other()
<<<<<<< HEAD
    print(f"yval = {x.yval}")
    print(f'x = {x.x}')
=======

    print(f"yval = {x.yval}")
    print(f'xt = {(x.x)*2}')
>>>>>>> 4842d2334fd52ee9c11ec36ed5a231cc3d11af2f
