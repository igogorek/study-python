__author__ = 'igogor'

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    month, balance = 0, startPriceOld - startPriceNew
    while balance < 0:
        print "month: {0}, balance: {1}".format(month, balance)
        month += 1
        balance = - reducedSum(balance, percentLossByMonth, startPriceNew - startPriceOld) + savingperMonth * month
        print "month: {0}, balance: {1}".format(month, balance)
    return [month, int(balance)]

def reducedSum(month, monthlyLoss, sum):
    loss_persent = monthlyLoss + 0.5 * (month // 2)
    return sum * (1.0 - loss_persent / 100.0)


