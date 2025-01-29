import pandas as pd
import time
import random
if __name__ == "__main__":
    data = pd.read_csv("data.csv")
    data = data.iloc[:, 0].tolist()  # İlk sütunu liste olarak aldım


    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key


    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


    def bogosort(arr):
        while not is_sorted(arr):
            random.shuffle(arr)   #bu acayip uzun çalışıyor


    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            merge_sort(L)
            merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1


    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


    algoritmalar = {
        "bubble_sort": bubble_sort,
        "insertion_sort": insertion_sort,
        "selection_sort": selection_sort,
        "bogosort": bogosort,
        "merge_sort": merge_sort,
        "quick_sort": quick_sort,
    }

    for ad, func in algoritmalar.items():
        test_data = data.copy()  # Her algoritma için aynı veriyi aldım
        başlangıç = time.time()

        if ad == "quick_sort":  # Quick Sort inplace çalışmıyor
            sorted_data = func(test_data)
        else:
            func(test_data)

        bitiş = time.time()
        geçen_süre = bitiş - başlangıç
        print(f"{ad} çalıştı. Süre: {geçen_süre} saniye")
    print("Tüm sıralama işlemleri tamamlandı.")






