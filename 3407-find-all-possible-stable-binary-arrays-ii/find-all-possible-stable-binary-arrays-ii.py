class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j][0]: number of stable arrays with i zeros, j ones, ending with 0
        # dp[i][j][1]: number of stable arrays with i zeros, j ones, ending with 1
        ways0 = [[0] * (one + 1) for _ in range(zero + 1)]
        ways1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # Base cases: arrays with only zeros or only ones, up to 'limit' length.
        for k in range(1, limit + 1):
            if k <= zero:
                ways0[k][0] = 1 # e.g., [0, 0, ..., 0] (k zeros)
            if k <= one:
                ways1[0][k] = 1 # e.g., [1, 1, ..., 1] (k ones)

        # sum_ways1_col[j] stores the sum ways1[x][j] for x in [i-limit, i-1].
        # It allows O(1) calculation of ways0[i][j] for each (i,j) state.
        sum_ways1_col = [0] * (one + 1)

        # Iterate over total number of zeros 'i'
        for i in range(zero + 1):
            # sum_ways0_row stores sum ways0[i][y] for y in [j-limit, j-1].
            # This variable is reset for each new row 'i' and updated as 'j' iterates.
            sum_ways0_row = 0 
            
            # Iterate over total number of ones 'j'
            for j in range(one + 1):
                # Skip the (0,0) state as it represents an empty array, which is not stable.
                if i == 0 and j == 0:
                    continue
                
                # --- Update sum_ways1_col[j] (for ways0[i][j] calculation) ---
                # sum_ways1_col[j] is the sum of ways1[x][j] from x = i-limit to i-1.
                # When moving from row i-1 to i, we add ways1[i-1][j] and remove ways1[i-limit-1][j].
                if i > 0: # Only update if we have a previous row to reference
                    sum_ways1_col[j] = (sum_ways1_col[j] + ways1[i-1][j]) % MOD
                    if i - limit - 1 >= 0:
                        sum_ways1_col[j] = (sum_ways1_col[j] - ways1[i-limit-1][j] + MOD) % MOD
                
                # --- Calculate ways0[i][j] (arrays ending with 0) ---
                # This state is formed by appending 0s to an array ending with 1.
                # Thus, it only applies if j > 0 (there are ones to alternate with).
                # If j=0, ways0[i][0] is only determined by the base cases (an array of only 0s).
                if j > 0:
                    ways0[i][j] = sum_ways1_col[j]
                # If j=0, ways0[i][0] retains its base case value (1 if 1<=i<=limit, else 0).
                # Note: sum_ways1_col[0] would be 0 because ways1[x][0] is 0 for x > 0, so it doesn't affect ways0[i][0] anyway.

                # --- Update sum_ways0_row (for ways1[i][j] calculation) ---
                # sum_ways0_row is the sum of ways0[i][y] from y = j-limit to j-1.
                # When moving from column j-1 to j, we add ways0[i][j-1] and remove ways0[i][j-limit-1].
                if j > 0: # Only update if we have a previous column to reference
                    sum_ways0_row = (sum_ways0_row + ways0[i][j-1]) % MOD
                    if j - limit - 1 >= 0:
                        sum_ways0_row = (sum_ways0_row - ways0[i][j-limit-1] + MOD) % MOD
                
                # --- Calculate ways1[i][j] (arrays ending with 1) ---
                # This state is formed by appending 1s to an array ending with 0.
                # Thus, it only applies if i > 0 (there are zeros to alternate with).
                # If i=0, ways1[0][j] is only determined by the base cases (an array of only 1s).
                if i > 0:
                    ways1[i][j] = sum_ways0_row
                # If i=0, ways1[0][j] retains its base case value (1 if 1<=j<=limit, else 0).
                # Note: sum_ways0_row (when i=0) would be 0 because ways0[0][y] is 0 for y > 0.
        
        # The total number of stable arrays is the sum of arrays ending with 0 and ending with 1.
        return (ways0[zero][one] + ways1[zero][one]) % MOD