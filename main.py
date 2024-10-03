import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r.set("foo", "bar")
# True
print(r.get("foo"))
# bar

r.hset(
    "user-session:123",
    mapping={"name": "John", "surname": "Smith", "company": "Redis", "age": 29},
)
r.hset(
    "user-session:1234",
    mapping={"name": "Jedão", "surname": "Luz", "company": "Sonic Coder", "age": 27},
)
# True

print(r.hgetall("user-session:123"))
# {'surname': 'Smith', 'name': 'John', 'company': 'Redis', 'age': '29'}

# Criando e recuperando dados de um hash map
r.hset("user:1000", "name", "John Doe")
r.hset("user:1000", "email", "john.doe@example.com")
print(r.hgetall("user:1000"))
