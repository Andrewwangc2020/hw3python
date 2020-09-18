#Author: Andrew Wang aqw5628@psu.edu

def digit_sum(n):
  if(n>0):
    return n%10 + digit_sum(int(n/10));
  else:
    return 0;

def run():
  init_num = int(input("Enter an int: "));
  fin_sum = digit_sum(init_num);
  print(f"sum of digits of {init_num} is {fin_sum}.");

if __name__ == "__main__":
  run();