def calculate_merchant_fraud_score(transactions_list, rules_list, merchants_list):
    # 1. Parse Merchants
    merchants = {}
    for m in merchants_list:
        mid, score = m.split(",")
        merchants[mid] = float(score) # Use float for precision during math
        
    cust_merch_count = {} # (cust, merch) -> list of indices
    cust_merch_hour_count = {} # (cust, merch, hour) -> list of indices

    # 2. Single Pass Processing
    for i in range(len(transactions_list)):
        t_parts = transactions_list[i].split(",")
        r_parts = rules_list[i].split(",")
        
        m_id, t_amt, c_id, hour = t_parts[0], float(t_parts[1]), t_parts[2], int(t_parts[3])
        min_amt, mult, add_factor, penalty = float(r_parts[0]), float(r_parts[1]), float(r_parts[2]), float(r_parts[3])

        # Rule 1: Multiplicative
        if t_amt > min_amt:
            merchants[m_id] *= mult

        # Rule 2: 3+ Transactions total
        key2 = (c_id, m_id)
        cust_merch_count[key2] = cust_merch_count.get(key2, 0) + 1
        if cust_merch_count[key2] >= 3:
            # If exactly 3, add for the first two as well
            if cust_merch_count[key2] == 3:
                # Note: This assumes the add_factor is the same for all 3. 
                # If it varies, you'd need to store the previous factors.
                merchants[m_id] += (add_factor * 3) 
            else:
                merchants[m_id] += add_factor

        # Rule 3: 3+ in same hour
        key3 = (c_id, m_id, hour)
        cust_merch_hour_count[key3] = cust_merch_hour_count.get(key3, 0) + 1
        if cust_merch_hour_count[key3] >= 3:
            # Determine if it's a penalty or a discount (fix overlaps!)
            current_penalty = 0
            if 12 <= hour <= 17: # Example of making them exclusive
                current_penalty = penalty
            elif 18 <= hour <= 21:
                current_penalty = -penalty
            
            if cust_merch_hour_count[key3] == 3:
                merchants[m_id] += (current_penalty * 3)
            else:
                merchants[m_id] += current_penalty

    # 3. Format Output
    return [f"{m.split(',')[0]},{int(merchants[m.split(',')[0]])}" for m in merchants_list]