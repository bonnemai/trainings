# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    """
    Count the number of artistic photographs.
    
    An artistic photograph consists of:
    - A photographer (P), actor (A), and backdrop (B)
    - Actor must be between photographer and backdrop
    - Distance between photographer and actor must be between X and Y (inclusive)
    - Distance between actor and backdrop must be between X and Y (inclusive)
    """
    count = 0
    
    # Try all possible positions for photographer, actor, and backdrop
    for p in range(N):  # photographer position
        if C[p] != 'P':
            continue
            
        for a in range(N):  # actor position
            if C[a] != 'A':
                continue
                
            for b in range(N):  # backdrop position
                if C[b] != 'B':
                    continue
                
                # Check if actor is between photographer and backdrop
                if not (p < a < b or b < a < p):
                    continue
                
                # Calculate distances
                dist_pa = abs(p - a)
                dist_ab = abs(a - b)
                
                # Check if distances are within the required range
                if X <= dist_pa <= Y and X <= dist_ab <= Y:
                    count += 1
    
    return count

if __name__=='__main__': 
    tests=[
        (5, 'APABA', 1, 2, 1),
        (5, 'APABA', 2, 3, 0),
        (8, '.PBAAP.B', 1, 3, 3),
        (3, 'PAB', 1, 3, 1),
        (3, 'PAB', 1, 200, 1),
        (5, 'PBABB', 2, 2, 1),
        (5, 'PBABB', 3, 3, 0),
        (5, 'PPABB', 1, 3, 2),
        (5, 'PBABP', 1, 3, 2),
        (5, 'PB.BP', 1, 3, 0),
        (6, 'PABPAB', 1, 3, 2),
        (25, '......................PAB', 1, 3, 1)
    ]
    
    for N, C, X, Y, expected in tests: 
        result = getArtisticPhotographCount(N, C, X, Y)
        status = "✓" if result == expected else "✗"
        print(f'{status} N={N}, C="{C}", X={X}, Y={Y}: got {result}, expected {expected}')