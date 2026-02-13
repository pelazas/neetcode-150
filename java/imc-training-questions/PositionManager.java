import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.locks.ReentrantLock;

public class PositionManager {
    // track how many shares of a company I own

    // thread safe map for storage
    private final ConcurrentHashMap<String,Integer> positions = new ConcurrentHashMap<>();
    // lock to protect critical math
    private final ReentrantLock tradeLock = new ReentrantLock();

    public int getPosition(String symbol){
        return positions.getOrDefault(symbol, 0);
    }

    public boolean sellShares(String symbol, int qtyToSell){
        tradeLock.lock();
        try{
            int current = positions.getOrDefault(symbol, 0);
            if (current < qtyToSell){
                return false; // not enough shares
            }
            positions.put(symbol, current-qtyToSell);
            return true;
        } finally{
            tradeLock.unlock();
        }
    }
}
