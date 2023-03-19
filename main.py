# python3
#Leons Dolgopolovs 221RDB432
import heapq

def parallel_processing(n, m, data):
    output = []
    threds=[(0, i) for i in range(n)]
    heapq.heapify(threds)
    for i in range(m):
        finish_time, thread_id = heapq.heappop(threds)
        output.append((thread_id, finish_time))
        finish_time = finish_time + data[i]
        heapq.heappush(threds, (finish_time, thread_id))
    return output

def main():
    n, m= map(int, input().split())
    data = list(map(int,input().split()))

    result = parallel_processing(n,m,data)

    for thread_id, start_time in result:
        print(thread_id, start_time)



if __name__ == "__main__":
    main()
