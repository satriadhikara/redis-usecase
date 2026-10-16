import time

def redis_mock(currency):
    # asumsi redis 60 detik ilang
    time.sleep(0.05)
    if currency == "SGD-IDR":
        return 10000
    return 0



in_memory_hit = 0
redis_hit = 0
in_memory = {}
currency_req = "SGD-IDR"
for i in range(60):
    if i % 30 == 0:
        in_memory.clear()
    for j in range(50000):
        if not bool(in_memory):
            redis_hit += 1
            in_memory[currency_req] = redis_mock(currency_req)
        elif in_memory[currency_req] == 0:
            redis_hit += 1
            in_memory[currency_req] = redis_mock(currency_req)
        in_memory_hit += 1

print("Redis Hit: ", redis_hit)
print("In Memory Hit:", in_memory_hit)