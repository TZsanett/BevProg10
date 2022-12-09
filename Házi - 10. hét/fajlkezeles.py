def main():

   f = open("string1.py", 'r')
   a = open("string1_clean", 'a')

   li = f.readlines()
   li_clean = []

   for i in li:
      if "#" not in i[0]:
         li_clean.append(i)
      if "#" not in i:
         li_clean.append(i)

   for i in li_clean:
      print(i, file = a)

if __name__ == "__main__":
    main()