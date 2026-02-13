# Java Concurrency Cheatsheet

## Locks and Synchronization

### ReentrantLock
Used when you need more control than `synchronized` blocks, such as fairness or timed lock attempts.

```java
private final ReentrantLock lock = new ReentrantLock(); // java.util.concurrent.locks

lock.lock();
try {
    // Critical Section: Access shared state
} finally {
    lock.unlock(); // Always unlock in finally block
}
```

**Synchronized vs. ReentrantLock:**
- **`synchronized`**: Simpler, automatic unlocking, but lacks fairness and advanced features.
- **`ReentrantLock(true)`**: Enables **Fairness** (FIFO). Use when order of thread entry matters. If fairness isn't required, `synchronized` or default `ReentrantLock` is usually faster.

---

## ConcurrentHashMap
Thread-safe map that allows high concurrency by not locking the entire map for reads/writes.

### Atomic Update Patterns
Critical for avoiding "check-then-act" race conditions.

| Method | Purpose | Use Case |
| :--- | :--- | :--- |
| `putIfAbsent(K, V)` | Insert only if key is missing | "Adding a unique order ID" |
| `computeIfAbsent(K, func)` | Create and insert if missing | "Initializing a list/set for a key" |
| `computeIfPresent(K, func)` | Update if key exists | "Updating an existing order's state" |
| `compute(K, func)` | Update regardless of existence | "General purpose updates (e.g., counters)" |

**Example: Counter Update**
```java
// ❌ BAD: Race condition (check-then-act)
int old = map.get("AAPL");
map.put("AAPL", old + 10); // Two threads might both see 100 and write 110

// ✅ GOOD: Atomic update
map.compute("AAPL", (key, oldVal) -> (oldVal == null ? 10 : oldVal + 10));
```

---

## Condition Objects (Wait/Notify)
Used for inter-thread communication within a `Lock` context.

```java
private final ReentrantLock lock = new ReentrantLock();
private final Condition notEmpty = lock.newCondition(); // "Wait signal"

public void consume() throws InterruptedException {
    lock.lock();
    try {
        while (queue.isEmpty()) {
            notEmpty.await(); // Releases lock and sleeps until signaled
        }
        process(queue.pop());
    } finally {
        lock.unlock();
    }
}

public void produce(Item item) {
    lock.lock();
    try {
        queue.push(item);
        notEmpty.signal(); // Wakes up exactly one sleeping consumer
        // Use notEmpty.signalAll() to wake all threads
    } finally {
        lock.unlock();
    }
}
```
