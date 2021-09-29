
import random
import time

class Sort:

  arr = list()
  tm = None

  def __init__(self, cnt = None, min = None, max = None):
    if cnt == None:
      return None
    for i in range(cnt):
      n = random.randrange(min, max)
      self.arr.append(n)

  def __iter__(self):
    return iter(self.arr)

  def time_out(self):
    return self.tm

  def rem(self):
    self.arr.clear()

  def SelectionSort(self):
    self.tm = 0 
    data = list(self.arr)
    start = time.time()
  
    for i in range(len(data)):
      min_ind = i
      for j in range(i+1, len(data)):
        if data[min_ind] > data[j]:
          min_ind = j
      data[i], data[min_ind] = data[min_ind], data[i]

    self.tm = time.time()-start
    return data


  def BubbleSort(self):
    self.tm = 0
    data = list(self.arr)
    start = time.time()

    for i in range(len(data)):
      flag = True
      for j in range(0, len(data)-i-1):
          if data[j] > data[j+1] :
              data[j], data[j+1] = data[j+1], data[j]
              flag = False
      if flag:
        break
        
    self.tm = time.time()-start
    return data

  def InsertionSort(self):
    self.tm = 0
    data = list(self.arr)
    start = time.time()

    for i in range(len(data)):
      ind = i - 1
      ob = data[i]
      while ind >= 0 and data[ind] > ob:
        data[ind + 1] = data[ind]
        ind -= 1
      data[ind + 1] = ob
      
    self.tm = time.time()-start
    return data

def save(arr):
    filename = "test"
    f = open(filename + ".txt", "a", encoding='utf-8')
    for i in range(len(arr)):
      f.write(str(arr[i]))
      f.write(" ")
    f.write("\n")
    f.close()

def choise(ind):
  if ind == 1:
    global bull
    bull.rem()
    print("введите количество значений:")
    num=int(input())
    print("начало диапазона:")
    start=int(input())
    print("конец диапазона:")
    end = int(input())

    bull = Sort(num, start, end)

  elif ind == 2:
    print(' '.join(map(str,bull)), "\n")
  elif ind == 3: 
    arr0 = list(bull.BubbleSort())
    # print(" ".join(map(str, bull.BubbleSort())), "\n")
    print(bull.time_out(), " sec \n")
  elif ind == 4:
    arr0 = list(bull.SelectionSort())
    # print(" ".join(map(str, bull.SelectionSort())), "\n")
    print(bull.time_out(), " sec \n")
  elif ind == 5:
    arr0 = list(bull.InsertionSort())
    # print(" ".join(map(str, bull.InsertionSort())), "\n")
    print(bull.time_out(), " sec \n" )
  
  if ind != 2 and ind != 1:
    save(arr0)
  
  
def menu():

  ind = -1
  while True:
    print("1. Input")
    print("2. Output")
    print("3. BubbleSort")
    print("4. SeletionSort")
    print("5. InsertionSort")
    print("0. exit")
    ind = int(input())
    if ind == 0:
      break
    print("")
    choise(ind)


bull = Sort()


menu()



