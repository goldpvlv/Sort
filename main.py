
import random
import time


class Sort:

  arr = list()
  tm = None

  def __init__(self, cnt=None, min=None, max=None):
      if cnt == None:
          return None
      for i in range(cnt):
          n = random.randrange(min, max+1)
          self.arr.append(n)

  def __iter__(self):
      return iter(self.arr)

  def time_out(self):
      return self.tm

  def rem(self):
      self.arr.clear()
  
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

  def CocktailSort(self):
      self.tm = 0
      data = list(self.arr)
      start = time.time()

      left = 0
      right = len(data) - 1

      while left < right:

        temp = right + 1 

        for i in range(right, left, -1):
            if data[i-1] > data[i]:
              temp = i
              data[i], data[i - 1] = data[i - 1], data[i]

        left = temp
        temp = left - 1

        for i in range(left, right):
            if data[i] > data[i + 1]:
                temp = i
                data[i], data[i + 1] = data[i + 1], data[i]

        right = temp

      self.tm = time.time() - start
      return data


  def heap (self, arr, n, i):

      largest = i
      left = 2 * i + 1
      right = 2 * i + 2

      if left < n and arr[i] < arr[left]:
          largest = left

      if right < n and arr[largest] < arr[right]:
          largest = right

      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          self.heap(arr, n, largest)

  def HeapSort(self):
      self.tm = 0
      data = list(self.arr)
      start = time.time()

      for i in range(len(data), -1, -1):
          self.heap(data, len(data), i)

      for i in range(len(data)-1, 0, -1):
          data[i], data[0] = data[0], data[i]
          self.heap(data, i, 0)

      self.tm = time.time() - start
      return data

  def supporting(self, arr, value):

    cntArr = [0] * 10
    for i in range(len(arr)):
        place = (arr[i] // value) % 10
        cntArr[place] += 1

    for i in range(1, len(cntArr)):
        cntArr[i] += cntArr[i-1]

    outArr = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        current = arr[i]
        place = (arr[i] // value) % 10
        cntArr[place] -= 1
        newPos = cntArr[place]
        outArr[newPos] = current
        i -= 1

    return outArr

  def RadixSort(self):
    self.tm = 0
    data = list(self.arr)
    start = time.time()

    maxValue = max(data)

    number_digit = 0
    while int(maxValue) > 0:
        maxValue /= 10.0
        number_digit += 1

    digit = 1
    outData = data
    for i in range (number_digit):
      outData = self.supporting(outData, digit)
      digit *= 10

    self.tm = time.time() - start
    return outData

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
        num = int(input())
        print("начало диапазона:")
        start = int(input())
        print("конец диапазона:")
        end = int(input())

        bull = Sort(num, start, end)

    elif ind == 2:
      print(' '.join(map(str, bull)), "\n")
    elif ind == 3:
      arr0 = list(bull.InsertSort())
      print(bull.time_out(), " sec \n")
    elif ind == 4:
      arr0 = list(bull.CocktailSort())
      print(bull.time_out(), " sec \n")
    elif ind == 5:
      arr0 = list(bull.HeapSort())
      print(bull.time_out(), " sec \n")
    elif ind == 6:
      arr0 = list(bull.RadixSort())
      print(bull.time_out(), " sec \n")

    if ind != 2 and ind != 1:
        save(arr0)


def menu():
    ind = -1
    while True:
        print("1. Input")
        print("2. Output")
        print("3. InsertSort")
        print("4. CocktailSort")
        print("5. HeapSort")
        print("6. RadixSort")
        print("0. exit")
        ind = int(input())
        if ind == 0:
            break
        print("")
        choise(ind)


bull = Sort()

menu()







