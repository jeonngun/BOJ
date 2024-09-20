def solution(wallet, bill):
    result = 0
    while min(wallet) < min(bill) or max(wallet) < max(bill):
        if bill[0] > bill[1]:
            bill[0] = int(bill[0] * 0.5)
        elif bill[0] < bill[1]:
            bill[1] = int(bill[1] * 0.5)
        result += 1
    return result
        