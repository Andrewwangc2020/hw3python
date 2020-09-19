#Author: Andrew Wang aqw5628@psu.edu

def digit_sum(n:int):
  if(n>0):
    print(f"{n}");
    return n%10 + digit_sum(n//10);
  else:
    return 0;

def run():
  init_num = int(input("Enter an int: "));
  fin_sum = digit_sum(init_num);
  print(f"sum of digits of {init_num} is {fin_sum}.");

if __name__ == "__main__":
  run();