# avgArea = [1]
# sumArea = [0, 2, 3, 4]
# avgField = [1, 3, 5]
# sumField = [0, 2, 4]
avgSummary = [5, 6, 7, 9]
sumSummary = [2, 3, 4]
nowSummary = [0, 1, 8]

# avgType = [1]
# sumType = [0, 2, 3]
# avgETF = [3, 4, 5, 15, 16, 19]
# sumETF = [0, 2, 6, 9, 10, 17, 18, 20, 21, 22]
# nowETF = [1, 7, 8, 11Fst, 12Fst, 13MAX, 14MIN]

def mergeState(statewindow, state, Option):
    if Option == 'Area':
        pass
    elif Option == 'Field':
        pass
    elif Option == 'Summary':
        sumcols = statewindow.columns[sumSummary]
        avgcols = statewindow.columns[avgSummary]
        statewindow[sumcols + avgcols] += state[sumcols + avgcols]
        statewindow[avgcols] /= WindowPoint['Days']
        nowcols = statewindow.columns[nowSummary]
        statewindow[nowcols] = state[nowcols]
        if WindowPoint['Days']==0:
            statewindow[Fst] = state[Fst]
        statewindow[Max] = max(state[Max], statewindow[Max])
        statewindow[Min] = min(state[Min], statewindow[Min])
    elif Option == 'Type':
        pass
    elif Option == 'ETF':
        pass
