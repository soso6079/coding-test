import time
import psutil


def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2**20  # Bytes to MB

    return rss
    # print(f"[{message}] memory usage: {rss: 10.5f} MB")


def my_solution(value):
    answer = ""

    return answer


def optimal_solution(value):
    answer = 0

    return answer


if __name__ == '__main__':
    print()
    use_before = memory_usage()
    start_time = time.time()
    ########################################################
    s = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
    # k = [[7,3,1,8],[3,3,3,4]]
    # print(my_solution(s))
    # print(my_solution(k))
    print(optimal_solution(s))
    # print(optimal_solution(k))
    ########################################################
    end_time = time.time()
    use_after = memory_usage()
    print(f"[after_work] memory usage: {use_after-use_before: 10.5f} MB")
    print('[running time]:', end_time - start_time)
    print()
